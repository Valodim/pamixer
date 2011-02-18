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

class SinkInput():
    def __init__(self, index, struct):

        self.index = index
        self.name = struct.name
        self.client = struct.client
        self.sink = struct.sink

        self.channels = struct.volume.channels
        self.volume = []
        for i in range(0, self.channels+1):
            self.volume.append(struct.volume.values[i])

    def draw(self, win, par):

        # gauge, one bar for each channel
        gauge = win.derwin(22, self.channels+2, 0, 8-(self.channels/2))
        for i in range(0, self.channels+1):
            barheight = int(self.volume[i] / 65535.0 * 20.0)
            gauge.vline(21-barheight, i+1, curses.ACS_BLOCK, barheight)
        gauge.border()

        win.move(23, 3)
        win.addstr(self.name)


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
