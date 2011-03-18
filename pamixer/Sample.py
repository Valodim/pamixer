import re
import time
import datetime
import curses

from xml.dom.minidom import *

from classes.SubVolume import SubVolume

class Sample(SubVolume):

    def __init__(self, index, struct, props):
        self.index = index

        self.update(struct, props)

        SubVolume.__init__(self)

    def update(self, struct, props):
        self.name = struct.name
        self.duration = struct.duration
        self.bytes = struct.bytes
        self.lazy = struct.lazy
        self.filename = struct.filename

        self.props = props

        SubVolume.update(self, struct)

    def draw_info(self, win):
        """ general information """
        win.addstr(self.name.center(40) + "\n")

        win.addstr("\nLazy:\t\t" + ("yes" if self.lazy else "no"))
        win.addstr("\nDuration:\t" + ('{:.2f}'.format(self.duration/1000.0/1000.0)) + " s")
        win.addstr("\nSize:\t\t" + str(self.bytes/1024) + " KiB")

        win.addstr("\n\n" + "Properties".center(40) + "\n\n")

        for key in self.props:
            if key:
                win.addstr(key + ":\t" + self.props[key] + "\n")

    def draw_control(self, win, active):

        if len(self.volume) == 0:
            return False

        # draw volume gauge, just an average
        gauge = win.derwin(22, 2+self.channels, 0, 11-int(self.channels/2))
        for i in range(0, self.channels):
            self.draw_gauge(gauge, self.volume[i], 1, i)
        gauge.border()

        win.move(24, 3)
        win.addstr(self.name[0:20].center(20), curses.A_BOLD if active else 0)
        win.move(25, 7)
        if par.use_dezibel:
            volume_db_avg = round(sum(self.volume_db) / len(self.volume_db), 2)
            win.addstr(('{:+3.2f}'.format(volume_db_avg) + " dB").rjust(9), curses.color_pair(2) if not self.volume_uniform() else 0)
        else:
            volume_avg = round(sum(self.volume) / len(self.volume), 2)
            win.addstr(('{:3.2f}'.format(volume_avg * 100) + " %").rjust(9), curses.color_pair(2) if not self.volume_uniform() else 0)

        return True

    def play(self, sink_index = -1):
        par.sample_play(self.name, sink_index)

from pamixer.ParCur import par

"""
    ('index', uint32_t),
    ('name', STRING),
    ('volume', pa_cvolume),
    ('sample_spec', pa_sample_spec),
    ('channel_map', pa_channel_map),
    ('duration', pa_usec_t),
    ('bytes', uint32_t),
    ('lazy', c_int),
    ('filename', STRING),
    ('proplist', POINTER(pa_proplist)),
"""
