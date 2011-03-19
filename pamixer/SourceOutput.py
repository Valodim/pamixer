import curses 
import sys

from ParCur import par
from classes.SubVolume import SubVolume

class SourceOutput():
    def __init__(self, index, struct, props):

        self.index = index

        self.wcontrols = None

        self.update(struct, props)

    def update(self, struct, props):
        self.name = struct.name
        self.client = struct.client
        self.source = struct.source

        self.driver = struct.driver

        self.props = props

    def draw_control(self, win, active):
        """ single volume control """
        pass

    def draw_info(self, win):
        """ general information """
        win.move(0, 0)
        win.addstr(self.name.center(40) + "\n")

        win.addstr("\nDriver:\t\t" + self.driver)
        win.addstr("\nClient:\t\t" + par.pa_clients[self.client].name)
        win.addstr("\nLatency:\t")
        win.addstr("\nState:\t\t")

    def kill(self):
        par.kill_source_output(self.index)

    def setVolume(self, value, hard = False, channels = None):
        volume = self.getSetVolume(value, hard, channels)
        par.set_source_output_volume(self.index, volume)

    def changeVolume(self, up, hard = False, channels = None):
        volume = self.getChangeVolume(up, hard, channels)
        par.set_source_output_volume(self.index, volume)

    def still_exists(self):
        return self.index in par.pa_source_outputs

"""
('index', c_uint32),
('name', c_char_p),
('owner_module', c_uint32),
('client', c_uint32),
('source', c_uint32),
('sample_spec', pa_sample_spec),
('channel_map', pa_channel_map),
('volume', pa_cvolume),
('buffer_usec', pa_usec_t),
('source_usec', pa_usec_t),
('resample_method', c_char_p),
('driver', c_char_p),
('mute', c_int),
("proplist",        POINTER(c_int)),
('monitor_index', c_int),
"""
