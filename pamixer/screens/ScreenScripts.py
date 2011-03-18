import curses 
import os 

from ..PulseAudio import PA_SINK_RUNNING, PA_SINK_SUSPENDED, PA_SINK_IDLE

MODE_NORMAL = 0
MODE_MOVE = 1

state_colors = { }
state_colors[PA_SINK_RUNNING] = 3
state_colors[PA_SINK_SUSPENDED] = 4
state_colors[PA_SINK_IDLE] = 1

class ScreenScripts():

    def __init__(self):

        self.active_sink = -1

        self.win = None
        self.windex = None
        self.wpreview = None

        self.drawable = False

        self.cursor = -1

        self.scripts = [ ] # os.listdir("scripts")

        return

    def layout(self, win):
        if win is None:
            self.drawable = False
            return

        self.drawable = True

        self.win = win
        maxy, maxx = win.getmaxyx()

        # window for the sink list
        win.attron(curses.color_pair(2))
        win.hline(2, 0, curses.ACS_HLINE, maxx)
        win.vline(1, 25, curses.ACS_VLINE, maxy-1)
        win.addch(2, 25, curses.ACS_PLUS)
        win.attroff(curses.color_pair(2))
        win.move(1, 2)
        win.addstr("Script Index")
        win.move(1, 28)
        win.addstr("Script Preview")

        win.move(0, 33)
        win.addstr("NOT YET IMPLEMENTED")

        self.windex = win.derwin(maxy-4, 23, 4, 1)

        # window for the active sink
        self.wpreview = win.derwin(4, 28)


        # initial redraw
        self.redraw()

    def redraw(self, recurse = False):
        if self.drawable is False:
            return

        windex = self.windex
        wpreview = self.wpreview

        windex.erase()
        windex.move(0, 0)

        self.cursorCheck()

        for i in range(0, len(self.scripts)):
            windex.addstr(self.scripts[i] + "\n", curses.A_BOLD if i == self.cursor else 0)

        wpreview.erase()
        wpreview.move(0, 1)

        if self.cursor >= 0:
            scriptfile = open("scripts/" + self.scripts[self.cursor])
            script = scriptfile.readlines()
            scriptfile.close()

            for line in script:
                wpreview.addstr(line)


        return

    def cursorCheck(self):
        """
        Moves the cursor to the left until there is a sink input,
        or it's at the sink's volume.
        """
        while self.cursor >= len(self.scripts):
            self.cursor -= 1
        if self.cursor < 0 and len(self.scripts) > 0:
            self.cursor = 0
        elif len(self.scripts) == 0:
            self.cursor = -1

    def key_event(self, event):
        self.cursorCheck()

        # change focus
        if event == ord('k') or event == ord('j'):
            self.cursor += -1 if event == ord('k') else +1
            # cursorCheck happens here, too!
            self.redraw()
            return True

        return False

    def draw_help(self, win):
        pass

from ..ParCur import par
