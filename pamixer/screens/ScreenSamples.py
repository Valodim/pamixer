import curses

class ScreenSamples():

    def __init__(self):

        self.win = None
        self.windex = None
        self.wpreview = None

        self.cursor = -1

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
        win.addstr("Samples")

        self.windex = win.derwin(maxy-4, 23, 4, 1)

        # window for the active sink
        self.wpreview = win.derwin(4, 28)


        # initial redraw
        self.redraw()

    def redraw(self, recurse = False):
        if self.win is None:
            return

        windex = self.windex
        windex.erase()
        windex.move(0,0)

        self.cursorCheck()

        samples = par.pa_samples.values()
        for i in range(0, len(samples)):
            windex.addstr(samples[i].name + "\n", curses.A_BOLD if i == self.cursor else 0)

        wpreview = self.wpreview
        wpreview.erase()

        if self.cursor >= 0:
            if samples[self.cursor].draw_control(self.wpreview, False):
                samples[self.cursor].draw_info(self.wpreview.derwin(0, 30))
            else:
                samples[self.cursor].draw_info(self.wpreview)

        return

    def cursorCheck(self):
        """
        Moves the cursor to the left until there is a sink input,
        or it's at the sink's volume.
        """
        while self.cursor >= len(par.pa_samples):
            self.cursor -= 1
        if self.cursor < 0 and len(par.pa_samples) > 0:
            self.cursor = 0
        elif len(par.pa_samples) == 0:
            self.cursor = -1

    def key_event(self, event):
        self.cursorCheck()

        # change focus
        if event == ord('k') or event == ord('j'):
            self.cursor += -1 if event == ord('k') else +1
            # cursorCheck happens here, too!
            self.redraw()
            return True

        elif event == ord('p') or event == curses.KEY_ENTER or event < 256 and chr(event) == "\n":
            par.pa_samples.values()[self.cursor].play()
            return True

        return False

    def draw_help(self, win):
        win.attron(curses.A_BOLD)
        win.addstr("  Keys - Samples\n")
        win.addstr("-----------------------------------------")
        win.attroff(curses.A_BOLD)
        win.addstr("""
       j / Up\t\t: Move Cursor up
       k / Down\t: Move Cursor down

       p / Enter\t: Play sample

""")

from ..ParCur import par
