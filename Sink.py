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

class Sink():
    def __init__(self, index, struct):

        self.index = index
        self.update(struct)

    def update(self, struct):
        self.name = struct.name
        self.channels = struct.volume.channels

        self.volume = []
        for i in range(0, self.channels+1):
            self.volume.append(int(struct.volume.values[i] / PA_VOLUME_CONVERSION_FACTOR))

    def draw(self, win, par, cursor):

        # gauge, one bar for each channel
        gauge = win.derwin(22, self.channels+2, 7, 8-(self.channels/2))
        for i in range(0, self.channels+1):
            barheight = int(self.volume[i] * 0.2)
            gauge.vline(21-barheight, i+1, curses.ACS_BLOCK, barheight)
        gauge.border()

        win.move(30, 6)
        win.addstr("Volume", curses.A_BOLD if cursor == -1 else 0)

        inputs = par.get_sink_inputs_by_sink(self.index)
        i = 0
        for input in inputs:
            input.draw(win.derwin(7, 20 + i*20), par, cursor == i)
            i += 1

    def changeVolume(self, par, cursor, up):
        if cursor == -1:
            volume = []
            for i in range(0, self.channels+1):
                volume.append(PA_VOLUME_CONVERSION_FACTOR * max(0, min(100, self.volume[i] + (+1 if up else -1) * 5)))
            par.pa.set_sink_volume(self.index, volume, self.channels)

    """
    ('name', c_char_p),
    ('index', c_uint32),
    ('description', c_char_p),
    ('sample_spec', pa_sample_spec),
    ('channel_map', pa_channel_map),
    ('owner_module', c_uint32),
    ('volume', pa_cvolume),
    ('mute', c_int),
    ('monitor_source', c_uint32),
    ('monitor_source_name', c_char_p),
    ('latency', pa_usec_t),
    ('driver', c_char_p),
    ('flags', pa_sink_flags_t),
    ("proplist",        POINTER(c_int)),
    """
