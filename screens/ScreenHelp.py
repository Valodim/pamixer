import curses 

class ScreenHelp():
    def __init__(self):
        return

    def layout(self, win):
        self.win = win

        # initial redraw
        self.redraw()

    def redraw(self, recurse = False):
        if self.win is None:
            return

        win = self.win

        win.erase()
        win.move(3, 7)

        win.addstr("Hello, World!")

        win.refresh()

        return

    def key_event(self, event):
        return False
