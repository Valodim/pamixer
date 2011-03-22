import re
import time
import datetime
import curses

from xml.dom.minidom import *

class Client():

    def __init__(self, index, struct, proplist):
        self.index = index

        self.update(index, struct, proplist)

        # -1 is volume, 0 and above are sink inputs
        self.cursor = -1

    def update(self, index, struct, proplist):
        self.name = struct.name
        self.clean_name = self.clean_client_name(struct.name)
        if 'pid' in proplist:
            self.pid = proplist['pid']

    def layout(self, win):
        # just clean up?
        if win is None:
            self.drawable = False
            return

        self.drawable = True

        maxy, maxx = win.getmaxyx()

        if maxy > 32:
            win.attron(curses.color_pair(2))
            win.hline(32, 0, curses.ACS_HLINE, maxx)
            win.vline(32, 45, curses.ACS_VLINE, maxy)
            win.addch(32, 45, curses.ACS_TTEE)
            win.attroff(curses.color_pair(2))

        self.wcontrols = win.derwin(30, maxx, 1, 0)

        self.winfol = win.derwin(15, 41, 33, 2) if maxy > 33 else None
        self.winfor = win.derwin(33, 48) if maxy > 33 else None

        self.redraw()

    def redraw(self, recurse = False):
        self.draw_controls()
        self.draw_info()

    def draw_controls(self):
        # don't proceed if it's not even our turn to draw
        if self.drawable is False:
            return

        # if we aren't active, this needn't even be considered
        self.cursorCheck()

        wcontrols = self.wcontrols
        wcontrols.erase()

        inputs = par.get_sink_inputs_by_client(self.index)
        i = 0
        for input in inputs:
            input.draw_control(wcontrols.derwin(2, 2 + i*20),  curses.A_BOLD if self.cursor == i else 0)
            i += 1

    def draw_info(self):
        if self.drawable is False:
            return

        wleft = self.winfol
        wright = self.winfor

        wleft.erase()
        wright.erase()

        wleft.move(0, 2)
        wleft.addstr(self.name.center(36) + "\n")

        # wleft.addstr("\nDriver:\t\t" + self.driver)
        # wleft.addstr("\nLatency:\t" + str(self.latency * 100))
        # wleft.addstr("\nState:\t\t" + state_names[self.state])

        # if(self.driver == "module-alsa-sink.c") and 'alsa.card_name' in self.props:
            # wright.addstr("\nCard Name:\t" + self.props['alsa.card_name'])
        # elif(self.driver == "module-tunnel.c"):
            # wright.addstr("\nServer:\t\t" + self.props['tunnel.remote.server'])
            # wright.addstr("\nRemote User:\t" + self.props['tunnel.remote.user'])
            # wright.addstr("\nRemote Sink:\t" + self.props['tunnel.remote.description'])

    def key_event(self, event):
        self.cursorCheck()

        # change focus
        if event == ord('h') or event == ord('l'):
            self.cursor += -1 if event == ord('h')  else +1
            # cursorCheck happens here, too!
            self.draw_controls()
            self.draw_info()
            return True

        elif event in [ ord('k'), ord('K'), ord('j'), ord('J') ]:
            if self.cursor >= 0:
                par.get_sink_inputs_by_client(self.index)[self.cursor].changeVolume(event == ord('k') or event == ord('K'), event == ord('K') or event == ord('J'))

            self.draw_controls()
            return True

        elif event == ord('n'):
            if self.cursor >= 0:
                par.get_sink_inputs_by_client(self.index)[self.cursor].setVolume(1.0)

            self.draw_controls()
            return True

        elif event == ord('N'):
            sink_inputs = par.get_sink_inputs_by_client(self.index)
            for sink_input in sink_inputs:
                sink_input.setVolume(1.0)

            self.draw_controls()
            return True

        elif event == ord('m'):
            if self.cursor >= 0:
                par.get_sink_inputs_by_client(self.index)[self.cursor].setVolume(0.0)

            self.draw_controls()
            return True

        elif event == ord('M'):
            sink_inputs = par.get_sink_inputs_by_client(self.index)
            for sink_input in sink_inputs:
                sink_input.setVolume(0.0)

            self.draw_controls()
            return True

        elif event == ord('X'):
            if self.cursor >= 0:
                par.get_sink_inputs_by_client(self.index)[self.cursor].kill()

            self.draw_controls()
            return True

        return False

    def clean_client_name(self, name):
        name = name.strip()
        alsa_plugin = "ALSA plug-in ["
        if name.startswith(alsa_plugin):
            name = name[len(alsa_plugin):-1]
        return name

    def getActiveVolume(self):
        self.cursorCheck()
        if self.cursor >= 0:
            return par.get_sink_inputs_by_client(self.index)[self.cursor]
        return None

    def cursorCheck(self):
        """
        Moves the cursor to the left until there is a sink input,
        or it's at the sink's volume.
        """
        client_inputs = par.get_sink_inputs_by_client(self.index)
        while self.cursor >= len(client_inputs):
            self.cursor -= 1
        if self.cursor < 0 and len(client_inputs) > 0:
            self.cursor = 0
        if len(client_inputs) == 0:
            self.cursor = -1

from ParCur import par
