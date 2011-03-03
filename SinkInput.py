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
from pulseaudio.PulseAudio import PA_VOLUME_CONVERSION_FACTOR

from CursesHelpers import *

class SinkInput():
    def __init__(self, index, struct):

        self.index = index
        self.update(struct)

    def update(self, struct):
        self.name = struct.name
        self.client = struct.client
        self.sink = struct.sink

        self.channels = struct.volume.channels
        self.volume = []
        for i in range(0, self.channels+1):
            self.volume.append(int(struct.volume.values[i] / PA_VOLUME_CONVERSION_FACTOR))

    def draw(self, win, active):

        # gauge, one bar for each channel
        gauge = win.derwin(22, self.channels+2, 0, 8-(self.channels/2))
        for i in range(0, self.channels+1):
            barheight = int(self.volume[i] * 0.2)
            gauge.vline(21-barheight, i+1, curses.ACS_BLOCK, barheight)
        gauge.border()

        win.move(23, 4)
        win.addstr(center(par.pa_clients[self.client].clean_name, 12), curses.color_pair(2) if par.pa_clients[self.client].clean_name != par.pa_clients[self.client].name else 0)
        win.move(24, 3)
        win.addstr(center(self.name, 12), curses.A_BOLD if active else 0)

from ParCur import par

"""
('index', c_uint32),
('name', c_char_p),
('owner_module', c_uint32),
('client', c_uint32),
('sink', c_uint32),
('sample_spec', pa_sample_spec),
('channel_map', pa_channel_map),
('volume', pa_cvolume),
('buffer_usec', pa_usec_t),
('sink_usec', pa_usec_t),
('resample_method', c_char_p),
('driver', c_char_p),
('mute', c_int),
("proplist",        POINTER(c_int)),
('monitor_index', c_int),
"""
