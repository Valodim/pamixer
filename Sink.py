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

from pulseaudio.PulseAudio import PA_VOLUME_CONVERSION_FACTOR, PA_SINK_RUNNING, PA_SINK_SUSPENDED, PA_SINK_IDLE
from CursesHelpers import *

state_names = { }
state_names[PA_SINK_RUNNING] = "running"
state_names[PA_SINK_SUSPENDED] = "suspended"
state_names[PA_SINK_IDLE] = "idle"

class Sink():
    def __init__(self, index, struct, props):

        self.index = index
        self.update(struct, props)

    def update(self, struct, props):
        self.name = struct.name
        self.channels = struct.volume.channels
        self.driver = struct.driver
        self.latency = struct.latency
        self.mute = struct.mute
        self.state = struct.state
        self.props = props

        self.volume = []
        for i in range(0, self.channels+1):
            self.volume.append(int(struct.volume.values[i] / PA_VOLUME_CONVERSION_FACTOR))

    def draw_controls(self, win, cursor):

        # gauge, one bar for each channel
        gauge = win.derwin(22, self.channels+2, 7, 8-(self.channels/2))
        for i in range(0, self.channels+1):
            barheight = int(self.volume[i] * 0.2)
            gauge.vline(21-barheight, i+1, curses.ACS_BLOCK, barheight)
        gauge.border()

        win.move(29, 6)
        win.addstr("Volume", curses.A_BOLD if cursor == -1 else 0)

        inputs = par.get_sink_inputs_by_sink(self.index)
        i = 0
        for input in inputs:
            input.draw(win.derwin(7, 20 + i*20), cursor == i)
            i += 1

    def draw_info(self, win):
        maxy, maxx = win.getmaxyx()
        win.attron(curses.color_pair(2))
        win.hline(0, 0, curses.ACS_HLINE, maxx)
        win.vline(0, 45, curses.ACS_VLINE, maxy)
        win.addch(0, 45, curses.ACS_TTEE)
        win.attroff(curses.color_pair(2))

        wleft = win.derwin(10, 42, 1, 2)

        wleft.move(0, 2)
        wleft.addstr(center(self.name, 36) + "\n")

        wleft.addstr("\nDriver:\t\t" + self.driver)
        wleft.addstr("\nLatency:\t" + str(self.latency * 100))
        wleft.addstr("\nState:\t\t" + state_names[self.state])

        wright = win.derwin(1, 48)
        if(self.driver == "module-alsa-sink.c") and 'alsa.card_name' in self.props:
            wright.addstr("\nCard Name:\t" + self.props['alsa.card_name'])
        elif(self.driver == "module-tunnel.c"):
            wright.addstr("\nServer:\t\t" + self.props['tunnel.remote.server'])
            wright.addstr("\nRemote User:\t" + self.props['tunnel.remote.user'])
            wright.addstr("\nRemote Sink:\t" + self.props['tunnel.remote.description'])

    def changeVolume(self, cursor, up):
        if cursor == -1:
            volume = []
            for i in range(0, self.channels+1):
                volume.append(PA_VOLUME_CONVERSION_FACTOR * max(0, min(100, self.volume[i] + (+1 if up else -1) * 5)))
            par.pa.set_sink_volume(self.index, volume, self.channels)

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
