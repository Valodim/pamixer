import curses 

class ScreenVolume():

    def __init__(self):

        self.active_volume = None
        self.sinkchars = "wertyuiopWERTYUIOP"

        self.win = None
        self.wcontrols = None

        self.drawable = False

        return

    def layout(self, win):
        if win is None:
            if self.active_volume is not None:
                # draw some stuff
                self.active_volume.layout_volume(None)
            self.drawable = False
            return

        self.drawable = True

        self.win = win
        maxy, maxx = win.getmaxyx()

        # window for the sink list
        self.wcontrols = win.derwin(maxy-1, maxx, 1, 0)

        # if the active index is valid
        if self.active_volume is not None:
            # draw some stuff
            self.active_volume.layout_volume(self.wcontrols)
        else:
            self.wcontrols.addstr("No such volume control!")

    def redraw(self, recurse = False):
        if self.drawable is False:
            return

        self.check_volume()
        if self.active_volume is not None:
            self.active_volume.redraw_volume()
        else:
            self.wcontrols.erase()
            self.wcontrols.addstr("No such volume control!")

    def key_event(self, event):
        self.check_volume()
        if self.active_volume is not None:
            return self.active_volume.key_event_volume(event)

    def check_volume(self):
        if self.active_volume is not None:
            if not self.active_volume.still_exists():
                self.active_volume = None

    def setActiveVolume(self, volume):
        """ Set a new active sink input (will not redraw itself!) """
        self.active_volume = volume

    def draw_help(self, win):
        win.attron(curses.A_BOLD)
        win.addstr("  Keys - Sink Inputs\n")
        win.addstr("-----------------------------------------")
        win.attroff(curses.A_BOLD)
        win.addstr("""
       h / Left\t\t: Move Cursor left
       l / Right\t: Move Cursor right

       enter\t\t: Previous screen

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

