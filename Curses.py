import curses 
import time
import sys

class Curses():

    def __init__(self):
        self.counter = 0
        self.screen = None

        self.modes = [ CursesHelp(), CursesSink() ]

        self.active_mode = 1

    def update(self):
        # don't do anything if we aren't active
        if not self.subscreen:
            return

        self.subscreen.attrset(0)
        self.subscreen.clear()

        self.modes[self.active_mode].draw(self.subscreen)

        self.refresh()

        return

    def refresh(self):
        self.subscreen.refresh()

    def keyevent(self, event):

        # nothing here? ok, allow active mode to parse
        return self.modes[self.active_mode].key_event(event)

    def run(self):

        self.screen = curses.initscr()
        curses.start_color()
        curses.use_default_colors()

        curses.noecho()
        curses.curs_set(0)
        self.screen.keypad(1)

        maxy, maxx = self.screen.getmaxyx()

        curses.init_pair(1, -1, -1);
        curses.init_pair(2, curses.COLOR_YELLOW, -1);
        curses.init_pair(3, curses.COLOR_GREEN, -1);
        curses.init_pair(4, curses.COLOR_CYAN, -1);
        curses.init_pair(5, curses.COLOR_MAGENTA, -1);

        self.screen.move(0, 1)
        self.screen.addstr("1", curses.A_BOLD) # | (curses.COLOR_GREEN if self.active_mode == 1 else 0))
        self.screen.addstr(":Help  ")
        self.screen.addstr("2", curses.A_BOLD)
        self.screen.addstr(":Sinks")
        self.screen.attron(curses.color_pair(2))
        self.screen.hline(1, 0, curses.ACS_HLINE, maxx)
        self.screen.attroff(curses.color_pair(2))

        self.subscreen = self.screen.subwin(2, 0)
        self.screen.refresh()

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

