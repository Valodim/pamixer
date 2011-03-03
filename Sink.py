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

import curses 

from pulseaudio.PulseAudio import PA_SINK_RUNNING, PA_SINK_SUSPENDED, PA_SINK_IDLE
from CursesHelpers import *

state_names = { }
state_names[PA_SINK_RUNNING] = "running"
state_names[PA_SINK_SUSPENDED] = "suspended"
state_names[PA_SINK_IDLE] = "idle"

class Sink():
    def __init__(self, index, struct, props):

        self.wcontrols = None
        self.winfol = None
        self.winfor = None

        self.index = index
        self.update(struct, props)

        # -1 is volume, 0 and above are sink inputs
        self.cursor = -1

    def update(self, struct, props):
        self.name = struct.name
        self.channels = struct.volume.channels
        self.driver = struct.driver
        self.latency = struct.latency
        self.mute = struct.mute
        self.state = struct.state
        self.props = props

        self.volume = par.volume_to_linear(struct.volume)
        self.volume_db = par.volume_to_dB(struct.volume)

        self.redraw()

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

        # gauge, one bar for each channel
        gauge = wcontrols.derwin(22, self.channels+2, 2, 8-(self.channels/2))
        for i in range(0, self.channels):
            barheight = min(22, int(self.volume[i] * 18))
            # lowest nine
            if barheight > 0:
                gauge.attron(curses.color_pair(3))
                gauge.vline(21-min(9, barheight), i+1, curses.ACS_BLOCK, min(9, barheight))
                gauge.attroff(curses.color_pair(3))
            # mid eight
            if barheight > 9:
                gauge.vline(12-min(8, barheight-9), i+1, curses.ACS_BLOCK, min(8, barheight-9))
            # top three (clipping!)
            if barheight > 17:
                gauge.attron(curses.color_pair(6))
                gauge.vline(4-min(3, barheight-17), i+1, curses.ACS_BLOCK, min(3, barheight-17))
                gauge.attroff(curses.color_pair(6))
        gauge.border()

        wcontrols.move(26, 4)
        wcontrols.addstr("Sink Volume", curses.A_BOLD if self.cursor == -1 else 0)
        wcontrols.move(27, 5)
        volume_db_avg = round(sum(self.volume_db) / len(self.volume_db), 2)
        wcontrols.addstr(right('{:+03.2f}'.format(volume_db_avg) + " dB", 9))

        inputs = par.get_sink_inputs_by_sink(self.index)
        i = 0
        for input in inputs:
            input.draw_control(wcontrols.derwin(2, 20 + i*20), self.cursor == i)
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

        wleft.addstr("\nDriver:\t\t" + self.driver)
        wleft.addstr("\nLatency:\t" + str(self.latency * 100))
        wleft.addstr("\nState:\t\t" + state_names[self.state])

        if self.cursor == -1:
            if(self.driver == "module-alsa-sink.c") and 'alsa.card_name' in self.props:
                wright.addstr("\nCard Name:\t" + self.props['alsa.card_name'])
            elif(self.driver == "module-tunnel.c"):
                wright.addstr("\nServer:\t\t" + self.props['tunnel.remote.server'])
                wright.addstr("\nRemote User:\t" + self.props['tunnel.remote.user'])
                wright.addstr("\nRemote Sink:\t" + self.props['tunnel.remote.description'])
        else:
            par.get_sink_inputs_by_sink(self.index)[self.cursor].draw_info(wright)

        wright.refresh()
        wleft.refresh()

    def cursorCheck(self):
        """
        Moves the cursor to the left until there is a sink input,
        or it's at the sink's volume.
        """
        sink_inputs = par.get_sink_inputs_by_sink(self.index)
        while self.cursor >= len(sink_inputs):
            self.cursor -= 1
        if self.cursor < -1:
            self.cursor = -1

    def key_event(self, event):

        # change focus
        if event == curses.KEY_LEFT or event == curses.KEY_RIGHT:
            self.cursor += -1 if event == curses.KEY_LEFT else +1
            # cursorCheck happens here, too!
            self.draw_controls()
            self.draw_info()
            return True

        elif event == curses.KEY_UP or event == curses.KEY_DOWN:
            if self.cursor == -1:
                self.changeVolume(event == curses.KEY_UP)
            else:
                par.get_sink_inputs_by_sink(self.index)[self.cursor].changeVolume(event == curses.KEY_UP)

            self.draw_controls()
            return True

        elif event == ord('n'):
            if self.cursor == -1:
                self.setVolume(1.0)
            else:
                par.get_sink_inputs_by_sink(self.index)[self.cursor].setVolume(1.0)

            self.draw_controls()
            return True

        elif event == ord('m'):
            if self.cursor == -1:
                self.setVolume(0.0)
            else:
                par.get_sink_inputs_by_sink(self.index)[self.cursor].setVolume(0.0)

            self.draw_controls()
            return True

    def setVolume(self, value):
        volume = []
        for i in range(0, len(self.volume)):
            volume.append(value)
        par.set_sink_volume(self.index, volume)

    def changeVolume(self, up):
        volume = []
        for i in range(0, len(self.volume)):
            volume.append(max(0.0, min(1.2, self.volume[i] + (+0.075 if up else -0.075))))
        par.set_sink_volume(self.index, volume)

    def moveInput(self, index):
        # get the sink inputs of current sink
        sink_inputs = par.get_sink_inputs_by_sink(self.index)
        # move the selected sink input to the new sink
        par.move_sink_input(sink_inputs[self.cursor].index, index)

    """
    ('name', STRING),
    ('index', uint32_t),
    ('description', STRING),
    ('sample_spec', pa_sample_spec),
    ('channel_map', pa_channel_map),
    ('owner_module', uint32_t),
    ('volume', pa_cvolume),
    ('mute', c_int),
    ('monitor_source', uint32_t),
    ('monitor_source_name', STRING),
    ('latency', pa_usec_t),
    ('driver', STRING),
    ('flags', pa_sink_flags_t),
    ('proplist', POINTER(pa_proplist)),
    ('configured_latency', pa_usec_t),
    ('base_volume', pa_volume_t),
    ('state', pa_sink_state_t),
    ('n_volume_steps', uint32_t),
    ('card', uint32_t),
    ('n_ports', uint32_t),
    ('ports', POINTER(POINTER(pa_sink_port_info))),
    ('active_port', POINTER(pa_sink_port_info)),
    """

from ParCur import par
