import curses 

class ScreenSinkInput():

    def __init__(self):

        self.active_sink_input = -1
        self.sinkchars = "werty"

        self.win = None
        self.wcontrols = None

        return

    def layout(self, win):
        self.win = win

        maxy, maxx = win.getmaxyx()

        # window for the sink list
        self.wcontrols = win.derwin(maxy-1, maxx, 1, 0)

        # if the active index is valid
        if self.active_sink_input in par.pa_sink_inputs:
            # draw some stuff
            par.pa_sink_inputs[self.active_sink_input].layout(self.wcontrols)
        else:
            self.wcontrols.addstr("No such sink input!")

    def redraw(self, recurse = False):
        if recurse:
            par.pa_sink_inputs[self.active_sink_input].redraw()

    def key_event(self, event):
        return par.pa_sink_inputs[self.active_sink_input].key_event(event)

    def setActiveSinkInput(self, sink_input):
        """ Set a new active sink input (will not redraw itself!) """
        self.active_sink_input = sink_input

    def draw_help(self, win):
        win.attron(curses.A_BOLD)
        win.addstr("  Keys - Sinks\n")
        win.addstr("-----------------------------------------")
        win.attroff(curses.A_BOLD)
        win.addstr("""
       h / Left\t\t: Move Cursor left
       l / Right\t: Move Cursor right

       k / Up\t\t: Volume Up
       j / Down\t\t: Volume Down
       K\t\t: Volume Up, ignore soft limit
       J\t\t: Volume Down, ignore soft limit
       n\t\t: Set selected volume to 1.0
       m\t\t: Set selected volume to 0.0 (Mute)
       N\t\t: Set all volumes to 1.0

       X\t\t: Kill Sink Input
       M [werty]\t: Move Sink Input to Sink by char


""")

from ParCur import par

