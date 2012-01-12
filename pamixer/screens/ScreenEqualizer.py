import curses 
import sys

from ..pulse.PulseAudio import PA_SINK_RUNNING, PA_SINK_SUSPENDED, PA_SINK_IDLE

MODE_NORMAL = 0
MODE_MOVE = 1

state_colors = { }
state_colors[PA_SINK_RUNNING] = 3
state_colors[PA_SINK_SUSPENDED] = 4
state_colors[PA_SINK_IDLE] = 1

class ScreenEqualizer():

    def __init__(self):

        self.active_sink = -1
        self.sinkchars = "wertyuiopWERTYUIOP"

        self.show_data = True

        self.wsinklist = None

        self.drawable = False

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
        if len(eq.eq_sinks) > 0:
            # reset if invalid
            if self.active_sink == -1 or self.active_sink >= len(eq.eq_sinks):
                self.active_sink = 0
            # show some controls
            eq.eq_sinks.values()[self.active_sink].layout(self.wactivesink)

    def redraw(self, recurse = False):
        if self.drawable is False:
            return

        if self.active_sink == -1 and len(eq.eq_sinks) > 0:
            self.active_sink = 0
            eq.eq_sinks.values()[self.active_sink].layout(self.wactivesink)

        wsinklist = self.wsinklist

        wsinklist.erase()
        wsinklist.move(0, 1)

        i = 0
        # print the available sinks
        for key in eq.eq_sinks:
            sink = eq.eq_sinks[key]

            if i > 0:
                wsinklist.addstr(" | ")
            wsinklist.addstr(self.sinkchars[i] + ": ")

            wsinklist.addstr(sink.name, (curses.A_BOLD if i == self.active_sink else 0))

            i += 1

        if recurse and self.active_sink >= 0 and self.active_sink < len(eq.eq_sinks):
            eq.eq_sinks.values()[self.active_sink].redraw(True, False)

        return

    def key_event(self, event):

        # sink range
        for i in range(0, min(len(self.sinkchars), len(eq.eq_sinks))):
            if event == ord(self.sinkchars[i]):
                if self.active_sink == i:
                    return True
                eq.eq_sinks.values()[self.active_sink].layout(None)
                self.active_sink = i
                eq.eq_sinks.values()[self.active_sink].layout(self.wactivesink)
                self.redraw(True)
                return True

        return eq.eq_sinks.values()[self.active_sink].key_event(event)

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

from ..pulse.ParCur import par
from ..dbus.Equalizer import eq
