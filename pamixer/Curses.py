import curses 
import time
import sys
import threading

class Curses():

    def __init__(self, verbose = False):
        self.counter = 0
        self.screen = None
        self.subpad = None

        self.verbose = verbose

        # initialize modes
        self.modes = [ ScreenHelp(), ScreenSinks(), ScreenClients(), ScreenSources(), ScreenSamples(), ScreenVolume() ]

        # append help messages from modes. ScreenHelp has global help, too!
        for i in range(0, len(self.modes)):
            self.modes[0].helps.append(self.modes[i].draw_help)

        # start at the  sink screen
        self.active_mode = 1
        self.last_mode = 1
        self.switch_mode = None

        self.lock_update = threading.Lock()

    def update(self):
        # don't do anything if we aren't active
        if not self.subpad:
            return

        self.lock_update.acquire(True)

        # shall we switch?
        if self.switch_mode is not None:
            # to something else, actually?
            if self.switch_mode != self.active_mode:
                self.last_mode = self.active_mode
                self.modes[self.active_mode].layout(None)
                self.active_mode = self.switch_mode

            # don't do it again.
            self.switch_mode = None

        self.subpad.attrset(0)
        self.subpad.erase()

        self.modes[self.active_mode].layout(self.subpad)
        self.redraw()

        self.lock_update.release()

        return

    def redraw(self):

        self.screen.move(0, 1)
        self.screen.addstr("1", curses.A_BOLD) # | (curses.COLOR_GREEN if self.active_mode == 1 else 0))
        self.screen.addstr(":Help  ", curses.A_BOLD if self.active_mode == 0 else 0)
        self.screen.addstr("2", curses.A_BOLD)
        self.screen.addstr(":Sinks  ", curses.A_BOLD if self.active_mode == 1 else 0)
        self.screen.addstr("3", curses.A_BOLD)
        self.screen.addstr(":Clients  ", curses.A_BOLD if self.active_mode == 2 else 0)
        self.screen.addstr("4", curses.A_BOLD)
        self.screen.addstr(":Sources  ", curses.A_BOLD if self.active_mode == 3 else 0)
        self.screen.addstr("5", curses.A_BOLD)
        self.screen.addstr(":Samples", curses.A_BOLD if self.active_mode == 4 else 0)

        self.modes[self.active_mode].redraw(True)

        maxy, maxx = self.screen.getmaxyx()

        self.screen.hline(1, 0, curses.ACS_HLINE, maxx)

        self.screen.refresh()
        if 'scrollStatus' in self.modes[self.active_mode].__class__.__dict__:
            scrolly = self.modes[self.active_mode].scrollStatus()
            self.subpad.refresh(scrolly, 0, 2, 0, maxy-1, maxx)
        else:
            self.subpad.refresh(0, 0, 2, 0, maxy-1, maxx)

    def keyevent(self, event):

        # ^R request update of info from pulseaudio
        if event == 18: # ctrl-r
            par.request_update()
            self.screen.clear()
            self.update()

        # ^L redraw screen (clear for the flash, looks good!)
        elif event == 12: # ctrl-l
            self.screen.clear()
            self.update()

        # go to a different screen
        # right side is < because the last screen, ScreenSinkInput, cannot be chosen this way!
        elif ord('1') <= event < ord(str(len(self.modes))):
            self.switch_mode = event - ord('1')
            return False

        # return to last mode
        elif event == curses.KEY_BACKSPACE:
            self.switch_mode = self.last_mode
            return False

        elif event == curses.KEY_CLEAR:
            return False

        # switch between dezibel and percent
        elif event == ord("u"):
            par.use_dezibel = not par.use_dezibel
            return False

        # enter key is unreliable
        # dynamically check if the active screen has any active associated sink input
        elif event == curses.KEY_ENTER or event < 256 and chr(event) == "\n":
            if 'getActiveVolume' in self.modes[self.active_mode].__class__.__dict__:
                # if we can get one, go to the sink input screen
                input = self.modes[self.active_mode].getActiveVolume()
                if input is not None:
                    self.modes[5].setActiveVolume(input)
                    self.switch_mode = 5
                    return False

            elif self.active_mode == 5:
                self.switch_mode = self.last_mode
                return False

        # fix for vim keybindings
        elif event == curses.KEY_LEFT:
            event = ord('h')
        elif event == curses.KEY_DOWN:
            event = ord('j')
        elif event == curses.KEY_UP:
            event = ord('k')
        elif event == curses.KEY_RIGHT:
            event = ord('l')

        # nothing here? ok, allow active mode to parse
        return self.modes[self.active_mode].key_event(event)

    def run(self):

        # wrap it up, so that errors don't screw up the terminal
        curses.wrapper(self.run2)

    def run2(self, stdscr):

        self.screen = stdscr

        curses.use_default_colors()
        curses.curs_set(0)

        curses.init_pair(1, -1, -1);
        curses.init_pair(2, curses.COLOR_YELLOW, -1);
        curses.init_pair(3, curses.COLOR_GREEN, -1);
        curses.init_pair(4, curses.COLOR_CYAN, -1);
        curses.init_pair(5, curses.COLOR_MAGENTA, -1);
        curses.init_pair(6, curses.COLOR_RED, -1);

        maxy, maxx = self.screen.getmaxyx()

        self.subpad = curses.newpad(200, maxx)
        self.update()

        while True:
            # anything happen?
            event = self.screen.getch()

            # maybe it's an event on the lower layers?
            if self.keyevent(event):
                self.redraw()
                continue

            # end of program, just break out
            if event == ord("q"):
                break

            # no char hit? well, at least redraw..
            self.update()

from screens.ScreenHelp import ScreenHelp
from screens.ScreenSinks import ScreenSinks
from screens.ScreenClients import ScreenClients
from screens.ScreenSources import ScreenSources
from screens.ScreenSamples import ScreenSamples
from screens.ScreenVolume import ScreenVolume

from ParCur import par
