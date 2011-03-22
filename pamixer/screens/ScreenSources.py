import curses 

from ..PulseAudio import PA_SINK_RUNNING, PA_SINK_SUSPENDED, PA_SINK_IDLE

class ScreenSources():

    def __init__(self):

        # 0 = regular, 1 = monitors, 2 = both
        self.active_type = 0
        self.typechars = "wer"
        self.typenames = [ "Regular", "Monitors", "Both" ]

        self.show_data = True

        self.wsourcelist = None

        self.drawable = False

        return

    def layout(self, win):
        if win is None:
            self.drawable = False
            return

        self.drawable = True

        maxy, maxx = win.getmaxyx()

        if maxy > 32:
            win.attron(curses.color_pair(2))
            win.hline(32, 0, curses.ACS_HLINE, maxx)
            win.vline(32, 49, curses.ACS_VLINE, maxy)
            win.addch(32, 49, curses.ACS_TTEE)
            win.attroff(curses.color_pair(2))

        # window for the source list
        self.wsourcelist = win.derwin(1, maxx, 0, 0)

        # window for the active source
        self.wactivesource = win.derwin(2, 0)

        self.winfol = win.derwin(15, 45, 33, 2) if maxy > 33 else None
        self.winfor = win.derwin(33, 52) if maxy > 33 else None

    def redraw(self, recurse = False):
        if self.drawable is False:
            return

        outputcount = { 0: 0, 1: 0, 2: 0 }
        for output in par.pa_source_outputs.values():
            type = 1 if par.pa_sources[output.source].is_monitor else 0
            outputcount[type] = 1

        wsourcelist = self.wsourcelist

        wsourcelist.erase()
        wsourcelist.move(0, 1)

        i = 0
        # print the available sources
        for type in range(0, len(self.typenames)):
            if i > 0:
                wsourcelist.addstr(" | ")
            wsourcelist.addstr(self.typechars[type] + ": ")
            wsourcelist.addstr(self.typenames[type], curses.color_pair(3 if outputcount[type] > 0 else 1) | (curses.A_BOLD if i == self.active_type else 0))

            if outputcount[type] > 0:
                wsourcelist.addstr(" [" + str(outputcount[type]) + "]")

            i += 1

        self.wactivesource.erase()
        self.wactivesource.move(0, 0)

        i = 0
        for source in par.pa_sources:
            if self.active_type == 2 or par.pa_sources[source].is_monitor == (self.active_type == 1):
                par.pa_sources[source].draw_control(self.wactivesource.derwin(1, i))

                i += 23

        return

    def key_event(self, event):
        # source range
        for i in range(0, len(self.typechars)):
            if event == ord(self.typechars[i]):
                if self.active_type == i:
                    return True
                self.active_type = i
                self.redraw(True)
                return True

        return False
        # return par.pa_sources.values()[self.active_source].key_event(event)

    def getActiveVolume(self):
        return None # par.pa_sources.values()[self.active_source].getActiveVolume()

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
