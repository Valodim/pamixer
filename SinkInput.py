import curses 

import sys

from PulseAudio import PA_CHANNEL_POSITION_FRONT_LEFT, PA_CHANNEL_POSITION_FRONT_RIGHT, PA_CHANNEL_POSITION_FRONT_CENTER, PA_CHANNEL_POSITION_REAR_CENTER, PA_CHANNEL_POSITION_REAR_LEFT, PA_CHANNEL_POSITION_REAR_RIGHT, PA_CHANNEL_POSITION_LFE, PA_CHANNEL_POSITION_FRONT_LEFT_OF_CENTER, PA_CHANNEL_POSITION_FRONT_RIGHT_OF_CENTER, PA_CHANNEL_POSITION_SIDE_LEFT, PA_CHANNEL_POSITION_SIDE_RIGHT

channel_names = { }
channel_names[PA_CHANNEL_POSITION_FRONT_LEFT] = 'front left';
channel_names[PA_CHANNEL_POSITION_FRONT_RIGHT] = 'front right';
channel_names[PA_CHANNEL_POSITION_FRONT_CENTER] = 'front center';
channel_names[PA_CHANNEL_POSITION_REAR_CENTER] = 'rear center';
channel_names[PA_CHANNEL_POSITION_REAR_LEFT] = 'rear left';
channel_names[PA_CHANNEL_POSITION_REAR_RIGHT] = 'rear right';
channel_names[PA_CHANNEL_POSITION_LFE] = 'sub';
channel_names[PA_CHANNEL_POSITION_FRONT_LEFT_OF_CENTER] = 'front left';
channel_names[PA_CHANNEL_POSITION_FRONT_RIGHT_OF_CENTER] = 'front right';
channel_names[PA_CHANNEL_POSITION_SIDE_LEFT] = 'side left';
channel_names[PA_CHANNEL_POSITION_SIDE_LEFT] = 'side right';


class SinkInput():
    def __init__(self, index, struct):

        self.index = index

        self.cursor = 0

        self.wcontrols = None

        self.update(struct)

    def update(self, struct):
        self.name = struct.name
        self.client = struct.client
        self.sink = struct.sink

        self.driver = struct.driver

        self.channels = struct.channel_map.channels
        self.channel_map = [ ]
        for i in range(0, struct.channel_map.channels):
            self.channel_map.append(struct.channel_map.map[i])

        self.volume = par.volume_to_linear(struct.volume)
        self.volume_db = par.volume_to_dB(struct.volume)

    def layout(self, win):
        """ fullscreen layout """
        # just clean up?
        if win is None:
            self.wcontrols = None
            return

        self.wcontrols = win.derwin(4, 6)
        self.redraw()

    def redraw(self, recurse = False):
        self.draw_all_controls()

    def draw_all_controls(self):
        # don't proceed if it's not even our turn to draw
        if self.wcontrols is None:
            return

        # if we aren't active, this needn't even be considered
        self.cursorCheck()

        wcontrols = self.wcontrols
        wcontrols.erase()

        # draw volume gauge, just an average
        for i in range(0, self.channels):
            gauge = wcontrols.derwin(22, 4, 0, 3 + i*23)
            self.draw_gauge(gauge, self.volume[i])
            gauge.border()

            wcontrols.move(24, i*23)
            wcontrols.addstr(channel_names[self.channel_map[i]], curses.A_BOLD if self.cursor == i else 0)

            # text info, too
            wcontrols.move(25, i*23)
            if par.use_dezibel:
                wcontrols.addstr(('{:+3.2f}'.format(self.volume_db[i]) + " dB").rjust(9))
            else:
                wcontrols.addstr(('{:3.2f}'.format(self.volume[i] * 100) + " %").rjust(9))

        self.wcontrols.refresh()

    def cursorCheck(self):
        while self.cursor >= self.channels:
            self.cursor -= 1
        if self.cursor < 0:
            self.cursor = 0

    def key_event(self, event):

        # change focus
        if event == ord('h') or event == ord('l'):
            self.cursor += -1 if event == ord('h') else +1
            # cursorCheck happens here, too!
            self.draw_all_controls()
            return True

        elif event in [ ord('k'), ord('K'), ord('j'), ord('J') ]:
            self.cursorCheck()
            self.changeVolume(event == ord('k') or event == ord('K'), event == ord('K') or event == ord('J'), [ self.cursor ])

            self.draw_all_controls()
            return True

        elif event == ord('n'):
            self.cursorCheck()
            self.setVolume(1.0, False, [ self.cursor ])

            self.draw_all_controls()
            return True

        elif event == ord('N'):
            self.setVolume(1.0)

            self.draw_all_controls()
            return True

        elif event == ord('m'):
            self.setVolume(0.0)

            self.draw_all_controls()
            return True


    def draw_gauge(self, win, volume, width = 2, offset = 0):
        for i in range(1, width+1):
            barheight = min(22, int(volume * 18))
            # lowest eight
            if barheight > 0:
                win.attron(curses.color_pair(3))
                win.vline(21-min(8, barheight), offset +i, curses.ACS_BLOCK, min(8, barheight))
                win.attroff(curses.color_pair(3))
            # mid seven
            if barheight > 8:
                win.vline(13-min(7, barheight-8), offset +i, curses.ACS_BLOCK, min(7, barheight-8))
            # top three
            if barheight > 15:
                win.attron(curses.color_pair(6))
                win.vline(6-min(3, barheight-15), offset +i, curses.ACS_BLOCK, min(3, barheight-15))
                win.attroff(curses.color_pair(6))
            # over the top (clipping and stuff)
            if barheight > 18:
                win.attron(curses.color_pair(2))
                win.vline(3-min(3, barheight-18), offset +i, curses.ACS_BLOCK, min(3, barheight-18))
                win.attroff(curses.color_pair(2))

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
        par.kill_sink_input(self.index)

    def setVolume(self, value, hard = False, channels = None):
        volume = []
        value = max(0.0, min(par.volume_max_hard if hard else par.volume_max_soft, value))

        # create a list of channels
        for i in range(0, len(self.volume)):
            # apply new value?
            if channels is None or i in channels:
                volume.append(value)
            else:
                volume.append(self.volume[i])

        par.set_sink_input_volume(self.index, volume)

    def changeVolume(self, up, hard = False, channels = None):
        volume = []

        # create a list of volumes
        for i in range(0, len(self.volume)):
            # apply new value?
            if channels is None or i in channels:
                volume.append(max(0.0, min(par.volume_max_hard if hard else par.volume_max_soft, self.volume[i] + (par.volume_step if up else -par.volume_step))))
            else:
                volume.append(self.volume[i])

        par.set_sink_input_volume(self.index, volume)

    def volume_uniform(self):
        if self.channels == 0:
            return True
        for i in range(1, self.channels):
            if self.volume[i] != self.volume[0]:
                return False
        return True


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
