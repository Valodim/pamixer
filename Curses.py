import curses 
import time

class Curses():

    def __init__(self):
        self.counter = 0
        self.screen = None

        self.modes = [ CursesHelp(), CursesSink() ]

        self.active_mode = 1

    def update(self):
        # don't do anything if we aren't active
        if not self.screen:
            return

        maxy, maxx = self.screen.getmaxyx()

        self.screen.attrset(0)

        self.screen.clear()
        self.screen.move(0, 1)
        self.screen.addstr("1", curses.A_BOLD)# | (curses.COLOR_GREEN if self.active_mode == 1 else 0))
        self.screen.addstr(":Help  ")
        self.screen.addstr("2", curses.A_BOLD)
        self.screen.addstr(":Sinks")
        self.screen.hline(1, 0, curses.ACS_HLINE, maxx)

        self.modes[self.active_mode].draw(self.screen.subwin(2,0))

        return

    def keyevent(self, event):

        # nothing here? ok, allow active mode to parse
        return self.modes[self.active_mode].key_event(event)

    def run(self):

        self.screen = curses.initscr()
        # curses.start_color()

        curses.noecho()
        curses.curs_set(0)
        self.screen.keypad(1)

        self.update()
        while True:
            event = self.screen.getch()
            if event == -1:
                self.update()
                continue

            if self.keyevent(event):
                continue

            self.update()
            # end of program, just break out
            if event == ord("q"):
                break

        curses.endwin()

from CursesSink import CursesSink
from CursesHelp import CursesHelp

