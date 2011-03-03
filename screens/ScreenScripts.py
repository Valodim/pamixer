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

        self.windex = None
        self.wpreview = None

        self.show_preview = True

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

        for script in self.scripts:
            windex.addstr(script + "\n")

        wpreview.erase()
        wpreview.move(0, 1)

        scriptfile = open("scripts/" + self.scripts[0])
        script = scriptfile.readlines()
        scriptfile.close()

        for line in script:
            wpreview.addstr(line)

        # if recurse and self.active_sink in par.pa_sinks:
            # par.pa_sinks[self.active_sink].redraw(True)

        windex.refresh()
        wpreview.refresh()

        return

    def key_event(self, event):
        return False

from ParCur import par
