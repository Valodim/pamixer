import curses 

import sys

class ScreenHelp():
    def __init__(self):

        self.drawable = False

        self.helps = []

        return

    def layout(self, win):
        if win is None:
            self.drawable = False
            return

        self.drawable = True

        self.win = win
        self.whelp = win.derwin(1, 1)

        maxy, maxx = self.whelp.getmaxyx()

        # enable scrolling
        self.whelp.scrollok(1)
        self.whelp.setscrreg(0, maxy-1)

        # initial redraw
        self.redraw()

    def redraw(self, recurse = False):
        if self.drawable is False:
            return

        whelp = self.whelp

        whelp.erase()
        whelp.move(0, 0)

        whelp.attron(curses.color_pair(2))

        for help in self.helps:
            help(whelp)

        whelp.attroff(curses.color_pair(2))

        whelp.refresh()

        return

    def key_event(self, event):
        return False

    def draw_help(self, win):
        win.attron(curses.A_BOLD)
        win.addstr("  Keys - Global\n")
        win.addstr("-----------------------------------------")
        win.attroff(curses.A_BOLD)
        win.addstr("""
       q\t\t: Quit

       1\t\t: Show Help
       2\t\t: Show Sinks
       3\t\t: Show Clients
       4\t\t: Show Scripts
       5\t\t: Show Samples

       u\t\t: Switch volume unit dB / Percent


""")
