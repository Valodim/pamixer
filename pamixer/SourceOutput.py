import curses 
import sys

from ParCur import par
from classes.SubVolume import SubVolume

class SourceOutput(SubVolume):
    def __init__(self, index, struct):

        self.index = index

        SubVolume.__init__(self)

        self.wcontrols = None

        self.update(struct)

    def update(self, struct):
        self.name = struct.name
        self.client = struct.client
        self.source = struct.source

        self.driver = struct.driver

        SubVolume.update(self, struct)

    def draw_control(self, win, active):
        """ single volume control """

        # draw volume gauge, just an average
        gauge = win.derwin(22, 2+self.channels, 0, 11-int(self.channels/2))
        for i in range(0, self.channels):
            self.draw_gauge(gauge, self.volume[i], 1, i)
        gauge.border()

        win.move(23, 3)
        win.addstr(par.pa_clients[self.client].clean_name[0:20].center(20), curses.color_pair(2) if par.pa_clients[self.client].clean_name != par.pa_clients[self.client].name else 0)
        win.move(24, 3)
        win.addstr(self.name[0:20].center(20), curses.A_BOLD if active else 0)
        win.move(25, 7)
        if par.use_dezibel:
            volume_db_avg = round(sum(self.volume_db) / len(self.volume_db), 2)
            win.addstr(('{:+3.2f}'.format(volume_db_avg) + " dB").rjust(9), curses.color_pair(2) if not self.volume_uniform() else 0)
        else:
            volume_avg = round(sum(self.volume) / len(self.volume), 2)
            win.addstr(('{:3.2f}'.format(volume_avg * 100) + " %").rjust(9), curses.color_pair(2) if not self.volume_uniform() else 0)

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