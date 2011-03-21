import curses 

from ..PulseAudio import PA_SINK_RUNNING, PA_SINK_SUSPENDED, PA_SINK_IDLE

MODE_NORMAL = 0
MODE_MOVE = 1

state_colors = { }
state_colors[PA_SINK_RUNNING] = 3
state_colors[PA_SINK_SUSPENDED] = 4
state_colors[PA_SINK_IDLE] = 1

class ScreenSinks():

    def __init__(self):

        self.active_sink = -1
        self.sinkchars = "wertyuiopWERTYUIOP"

        self.show_data = True

        self.wsinklist = None

        self.drawable = False

        # 0 = 
        self.mode = MODE_NORMAL
        return

    def layout(self, win):
        if win is None:
            self.drawable = False
            if self.active_sink >= 0 and self.active_sink < len(par.pa_sinks.values()):
                par.pa_sinks.values()[self.active_sink].layout(None)
            return

        self.drawable = True

        maxy, maxx = win.getmaxyx()

        # window for the sink list
        self.wsinklist = win.derwin(1, maxx, 0, 0)

        # window for the active sink
        self.wactivesink = win.derwin(2, 0)

        # print the active sink
        if len(par.pa_sinks) > 0:
            # reset if invalid
            if self.active_sink == -1 or self.active_sink >= len(par.pa_sinks):
                self.active_sink = 0
            # show some controls
            par.pa_sinks.values()[self.active_sink].layout(self.wactivesink)

    def redraw(self, recurse = False):
        if self.drawable is False:
            return

        if self.active_sink == -1 and len(par.pa_sinks) > 0:
            self.active_sink = 0
            par.pa_sinks.values()[self.active_sink].layout(self.wactivesink)

        i = 0
        inputcount = { }
        for input in par.pa_sink_inputs.values():
            if input.sink in inputcount:
                inputcount[input.sink] += 1
            else:
                inputcount[input.sink] = 1

        wsinklist = self.wsinklist

        wsinklist.erase()
        wsinklist.move(0, 1)

        # print the available sinks
        for sink in par.pa_sinks.values():
            if i > 0:
                wsinklist.addstr(" | ")
            wsinklist.addstr(self.sinkchars[i] + ": ")

            wsinklist.addstr(sink.short_name, curses.color_pair(state_colors[sink.state]) | (curses.A_BOLD if i == self.active_sink else 0))

            if sink.index in inputcount and inputcount[sink.index] > 0:
                wsinklist.addstr(" [" + str(inputcount[sink.index]) + "]")

            i += 1

        if recurse and self.active_sink >= 0 and self.active_sink < len(par.pa_sinks):
            par.pa_sinks.values()[self.active_sink].redraw(True, self.mode == MODE_MOVE)

        return

    def key_event(self, event):
        if self.mode == MODE_NORMAL:

            # cheating a little here, don't allow move on the own volume
            if event == ord("C") and par.pa_sinks.values()[self.active_sink].cursor >= 0:
                self.mode = MODE_MOVE
                self.redraw(True)
                return False

            # sink range
            for i in range(0, min(len(self.sinkchars), len(par.pa_sinks))):
                if event == ord(self.sinkchars[i]):
                    if self.active_sink == i:
                        return True
                    par.pa_sinks.values()[self.active_sink].layout(None)
                    self.active_sink = i
                    par.pa_sinks.values()[self.active_sink].layout(self.wactivesink)
                    self.redraw(True)
                    return True

            return par.pa_sinks.values()[self.active_sink].key_event(event)

        elif self.mode == MODE_MOVE:

            # sink range
            for i in range(0, min(len(self.sinkchars), len(par.pa_sinks))):
                if event == ord(self.sinkchars[i]):
                    # tell the sink to move this thing around
                    par.pa_sinks.values()[self.active_sink].moveInput(par.pa_sinks.values()[i].index)
                    # return to normal mode
                    self.mode = MODE_NORMAL
                    return False

            self.mode = MODE_NORMAL

        return False

    def getActiveVolume(self):
        return par.pa_sinks.values()[self.active_sink].getActiveVolume()

    def draw_help(self, win):
        win.attron(curses.A_BOLD)
        win.addstr("  Keys - Sinks\n")
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

       X\t\t: Kill Sink Input
       C [sinkchar]\t: Move Sink Input to Sink by char


""")

from ..ParCur import par
