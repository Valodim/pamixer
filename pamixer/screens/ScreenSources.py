import curses 

from ..PulseAudio import PA_SINK_RUNNING, PA_SINK_SUSPENDED, PA_SINK_IDLE

state_colors = { }
state_colors[PA_SINK_RUNNING] = 3
state_colors[PA_SINK_SUSPENDED] = 4
state_colors[PA_SINK_IDLE] = 1

class ScreenSources():

    def __init__(self):

        self.active_source = -1
        self.sourcechars = "wertyuiopWERTYUIOP"

        self.show_data = True

        self.wsourcelist = None

        self.drawable = False

        return

    def layout(self, win):
        if win is None:
            self.drawable = False
            if self.active_source >= 0 and self.active_source < len(par.pa_sources.values()):
                par.pa_sources.values()[self.active_source].layout(None)
            return

        self.drawable = True

        maxy, maxx = win.getmaxyx()

        # window for the source list
        self.wsourcelist = win.derwin(1, maxx, 0, 0)

        # window for the active source
        self.wactivesource = win.derwin(2, 0)

        # print the active source
        if len(par.pa_sources) > 0:
            # reset if invalid
            if self.active_source == -1 or self.active_source >= len(par.pa_sources):
                self.active_source = 0
            # show some controls
            par.pa_sources.values()[self.active_source].layout(self.wactivesource)

    def redraw(self, recurse = False):
        if self.drawable is False:
            return

        if self.active_source == -1 and len(par.pa_sources) > 0:
            self.active_source = 0
            par.pa_sources.values()[self.active_source].layout(self.wactivesource)

        i = 0
        outputcount = { }
        for output in par.pa_source_outputs.values():
            if output.source in outputcount:
                outputcount[output.source] += 1
            else:
                outputcount[output.source] = 1

        wsourcelist = self.wsourcelist

        wsourcelist.erase()
        wsourcelist.move(0, 1)

        # print the available sources
        for source in par.pa_sources.values():
            if i > 0:
                wsourcelist.addstr(" | ")
            wsourcelist.addstr(self.sourcechars[i] + ": ")

            wsourcelist.addstr(source.short_name, curses.color_pair(state_colors[source.state]) | (curses.A_BOLD if i == self.active_source else 0))

            if source.index in outputcount and outputcount[source.index] > 0:
                wsourcelist.addstr(" [" + str(outputcount[source.index]) + "]")

            i += 1

        if recurse and self.active_source >= 0 and self.active_source < len(par.pa_sources):
            par.pa_sources.values()[self.active_source].redraw(True)

        return

    def key_event(self, event):
        # source range
        for i in range(0, min(len(self.sourcechars), len(par.pa_sources))):
            if event == ord(self.sourcechars[i]):
                if self.active_source == i:
                    return True
                par.pa_sources.values()[self.active_source].layout(None)
                self.active_source = i
                par.pa_sources.values()[self.active_source].layout(self.wactivesource)
                self.redraw(True)
                return True

        return par.pa_sources.values()[self.active_source].key_event(event)

    def getActiveVolume(self):
        return par.pa_sources.values()[self.active_source].getActiveVolume()

    def draw_help(self, win):
        win.attron(curses.A_BOLD)
        win.addstr("  Keys - Sources\n")
        win.addstr("-----------------------------------------")
        win.attroff(curses.A_BOLD)
        win.addstr("""
       h / Left\t\t: Move Cursor left
       l / Right\t: Move Cursor right

       enter\t\t: Detailed volume control

       k / Up\t\t: Volume Up
       j / Down\t\t: Volume Down
       K\t\t: Volume Up, ignore soft limit
       J\t\t: Volume Down, ignore soft limit
       n\t\t: Set selected volume to 1.0
       m\t\t: Set selected volume to 0.0 (Mute)
       N\t\t: Set all volumes to 1.0
       M\t\t: Set all volumes to 0.0

""")

from ..ParCur import par
