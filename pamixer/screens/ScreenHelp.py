import curses 

import sys

class ScreenHelp():
    def __init__(self):

        self.drawable = False

        self.helps = []

        self.scrolly = 0

        return

    def layout(self, win):
        if win is None:
            self.drawable = False
            return

        self.drawable = True

        self.whelp = win

        maxy, maxx = self.whelp.getmaxyx()

        # initial redraw
        self.redraw()

    def redraw(self, recurse = False):
        if self.drawable is False:
            return

        whelp = self.whelp

        whelp.erase()
        whelp.move(1, 0)

        whelp.attron(curses.color_pair(2))

        for help in self.helps:
            help(whelp)

        whelp.attroff(curses.color_pair(2))

        maxy, maxx = self.whelp.getmaxyx()
        whelp.move(self.scrolly, maxx-15)
        whelp.addstr(('+' + str(self.scrolly)).rjust(15))

    def scrollStatus(self):
        return self.scrolly

    def key_event(self, event):
        if event == ord('j'):
            self.scrolly += 1
            if self.scrolly > 150:
                self.scrolly = 150
            return True
        elif event == curses.KEY_NPAGE:
            self.scrolly += 10
            if self.scrolly > 150:
                self.scrolly = 150
            return True
        elif event == ord('k'):
            self.scrolly -= 1
            if self.scrolly < 0:
                self.scrolly = 0
            return True
        elif event == curses.KEY_PPAGE:
            self.scrolly -= 10
            if self.scrolly < 0:
                self.scrolly = 0
            return True

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

       backspace\t: Previous screen

       ^R\t\t: Force PA info update
       ^L\t\t: Redraw screen

       u\t\t: Switch volume unit dB / percent
""")

        win.attron(curses.A_BOLD)
        win.addstr("  Keys - Help\n")
        win.addstr("-----------------------------------------")
        win.attroff(curses.A_BOLD)
        win.addstr("""

       h\t\t: Scroll up
       j\t\t: Scroll down
       Page up\t\t: Scroll farther up
       Page down\t: Scroll farther down

""")
