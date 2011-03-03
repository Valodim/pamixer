import curses 
import os 

from pulseaudio.PulseAudio import PA_SINK_RUNNING, PA_SINK_SUSPENDED, PA_SINK_IDLE

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

        self.cursor = -1

        self.scripts = os.listdir("scripts")

        return

    def layout(self, win):
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

        self.windex = win.derwin(maxy-4, 23, 4, 1)

        # window for the active sink
        self.wpreview = win.derwin(4, 28)

        win.refresh()

        # initial redraw
        self.redraw()

    def redraw(self, recurse = False):
        if self.windex is None:
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

        windex.refresh()
        wpreview.refresh()
        self.win.refresh()

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
        if event == curses.KEY_UP or event == curses.KEY_DOWN:
            self.cursor += -1 if event == curses.KEY_UP else +1
            # cursorCheck happens here, too!
            self.redraw()
            return True

        # change focus
        if event == ord('X'):
            return True

        return False

from ParCur import par
