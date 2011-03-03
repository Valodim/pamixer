# Ear Candy - Pulseaduio sound managment tool
# Copyright (C) 2008 Jason Taylor
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import re
import time
import datetime
import curses

from xml.dom.minidom import *
from CursesHelpers import *

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
            self.wcontrols = None
            self.winfol = None
            self.winfor = None
            return

        maxy, maxx = win.getmaxyx()

        win.attron(curses.color_pair(2))
        win.hline(32, 0, curses.ACS_HLINE, maxx)
        win.vline(32, 45, curses.ACS_VLINE, maxy)
        win.addch(32, 45, curses.ACS_TTEE)
        win.attroff(curses.color_pair(2))

        win.refresh()

        self.wcontrols = win.derwin(30, maxx, 1, 0)

        self.winfol = win.derwin(15, 41, 33, 2)
        self.winfor = win.derwin(33, 48)

        self.redraw()

    def redraw(self, recurse = False):
        self.draw_controls()
        self.draw_info()

    def draw_controls(self):
        # don't proceed if it's not even our turn to draw
        if self.wcontrols is None:
            return

        # if we aren't active, this needn't even be considered
        self.cursorCheck()

        wcontrols = self.wcontrols
        wcontrols.erase()

        inputs = par.get_sink_inputs_by_client(self.index)
        i = 0
        for input in inputs:
            input.draw_control(wcontrols.derwin(2, 2 + i*20), self.cursor == i)
            i += 1

        wcontrols.refresh()

    def draw_info(self):
        if self.winfol is None or self.winfor is None:
            return

        wleft = self.winfol
        wright = self.winfor

        wleft.erase()
        wright.erase()

        wleft.move(0, 2)
        wleft.addstr(center(self.name, 36) + "\n")

        # wleft.addstr("\nDriver:\t\t" + self.driver)
        # wleft.addstr("\nLatency:\t" + str(self.latency * 100))
        # wleft.addstr("\nState:\t\t" + state_names[self.state])

        # if(self.driver == "module-alsa-sink.c") and 'alsa.card_name' in self.props:
            # wright.addstr("\nCard Name:\t" + self.props['alsa.card_name'])
        # elif(self.driver == "module-tunnel.c"):
            # wright.addstr("\nServer:\t\t" + self.props['tunnel.remote.server'])
            # wright.addstr("\nRemote User:\t" + self.props['tunnel.remote.user'])
            # wright.addstr("\nRemote Sink:\t" + self.props['tunnel.remote.description'])

        wleft.refresh()
        wright.refresh()

    def key_event(self, event):
        return False

    def is_active(self):

        # If ear candy did pause then consider active
        if self.__pause_status > 0: return True

        # no sinks then not active
        if len(self.sinks.values()) == 0: return False

        timestamp = time.mktime(datetime.datetime.now().timetuple())

        # check meter levels on others
        if self.apply_volume_meter_hack:
            for sink in self.sinks.values():

                if sink.volume_meter > 0:
                    self.__pause_status = 0
                    return True

                # HACK: Check how long its been inactive... and if more than a second count as expired
                if timestamp - sink.volume_meter_last_non_zero < 1:
                    self.__pause_status = 0
                    return True

            return False

        self.__pause_status = 0
        return True

    def set_primary(self, value):
        if value or self.category == "default":
            self.__fade_in()
            if self.__pause_status > 0:
                for plugin in self.plugins:
                    if plugin.enabled and not plugin.is_playing():
                        if plugin.set_pause(False): 
                            self.__pause_status = 0
        else:
            self.__fade_mute()
            if self.is_active() and self.__pause_status == 0:                 
                self.__pause_status = 1

    # called by sink, check if all sinks are at correct volume
    def check_volume(self):
        result = True
        for sink in self.sinks.values():
            result = result and sink.volume_check

        if result and self.__pause_status == 1:
           for plugin in self.plugins:
                if plugin.enabled and plugin.is_playing():
                    plugin.set_pause(True)
           self.__pause_status = 2

    def move_to_output(self, output):
        if not self.output == output:
            self.output = output
            self.core.move_client(self)

    def clean_client_name(self, name):
        name = name.strip()
        alsa_plugin = "ALSA plug-in ["
        if name.startswith(alsa_plugin):
            name = name[len(alsa_plugin):-1]
        return name

    def cursorCheck(self):
        """
        Moves the cursor to the left until there is a sink input,
        or it's at the sink's volume.
        """
        client_inputs = par.get_sink_inputs_by_client(self.index)
        while self.cursor >= len(client_inputs):
            self.cursor -= 1
        if self.cursor < -1:
            self.cursor = -1

from ParCur import par
