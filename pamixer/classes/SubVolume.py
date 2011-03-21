import curses 

from ..PulseAudio import PA_CHANNEL_POSITION_FRONT_LEFT, PA_CHANNEL_POSITION_FRONT_RIGHT, PA_CHANNEL_POSITION_FRONT_CENTER, PA_CHANNEL_POSITION_REAR_CENTER, PA_CHANNEL_POSITION_REAR_LEFT, PA_CHANNEL_POSITION_REAR_RIGHT, PA_CHANNEL_POSITION_LFE, PA_CHANNEL_POSITION_FRONT_LEFT_OF_CENTER, PA_CHANNEL_POSITION_FRONT_RIGHT_OF_CENTER, PA_CHANNEL_POSITION_SIDE_LEFT, PA_CHANNEL_POSITION_SIDE_RIGHT
from ..ParCur import par

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

channel_picto = {
        PA_CHANNEL_POSITION_FRONT_LEFT: [ 'FL', 0, 0 ],
        PA_CHANNEL_POSITION_FRONT_RIGHT: [ 'FR', 0, 7 ],
        PA_CHANNEL_POSITION_FRONT_CENTER: [ 'C', 1, 4 ],
        PA_CHANNEL_POSITION_REAR_CENTER: [ 'c', 3, 4 ],
        PA_CHANNEL_POSITION_REAR_LEFT: [ 'RL', 4, 0 ],
        PA_CHANNEL_POSITION_REAR_RIGHT: [ 'RR', 4, 7 ],
        PA_CHANNEL_POSITION_LFE: [ 'S', 2, 5 ],
        PA_CHANNEL_POSITION_FRONT_LEFT_OF_CENTER: [ 'CL', 1, 1 ],
        PA_CHANNEL_POSITION_FRONT_RIGHT_OF_CENTER: [ 'CR', 1, 6 ],
        PA_CHANNEL_POSITION_SIDE_LEFT: [ 'L', 2, 0 ],
        PA_CHANNEL_POSITION_SIDE_LEFT: [ 'R', 2, 7 ],
}

class SubVolume(object):
    """ This is a superclass for anything that has a volume """

    def __init__(self):
        self.volume = [ ]
        self.volume_db = [ ]

        self.drawable_volume = False

        self.wcontrols = None
        self.win = None

        self.cursor_volume = 0

    def update(self, struct):
        self.channels = struct.channel_map.channels
        self.channel_map = [ ]
        for i in range(0, struct.channel_map.channels):
            self.channel_map.append(struct.channel_map.map[i])

        self.volume = par.volume_to_linear(struct.volume)
        self.volume_db = par.volume_to_dB(struct.volume)

    def layout_volume(self, win):
        """ fullscreen layout """
        # just clean up?
        if win is None:
            self.drawable_volume = False
            return

        self.drawable_volume = True

        self.win = win
        self.wcontrols = win.derwin(4, 6)

    def redraw_volume(self, recurse = False):
        self.draw_controls_volume()

    def draw_controls_volume(self):
        # don't proceed if it's not even our turn to draw
        if self.drawable_volume is False:
            return

        # if we aren't active, this needn't even be considered
        self.cursorCheck_volume()

        wcontrols = self.wcontrols
        wcontrols.erase()

        self.win.move(0, 3)
        self.win.addstr(self.name)

        self.draw_picto(wcontrols.derwin(30, 5), self.cursor_volume)

        # draw volume gauge, just an average
        for i in range(0, self.channels):
            gauge = wcontrols.derwin(22, 4, 0, 3 + i*23)
            self.draw_gauge(gauge, self.volume[i])
            gauge.border()

            wcontrols.move(24, i*23)
            wcontrols.addstr(channel_names[self.channel_map[i]].center(12), curses.A_BOLD if self.cursor_volume == i else 0)

            # text info, too
            wcontrols.move(25, i*23)
            if par.use_dezibel:
                wcontrols.addstr(('{:+3.2f}'.format(self.volume_db[i]) + " dB").rjust(9))
            else:
                wcontrols.addstr(('{:3.2f}'.format(self.volume[i] * 100) + " %").rjust(9))

    def cursorCheck_volume(self):
        while self.cursor_volume >= self.channels:
            self.cursor_volume -= 1
        if self.cursor_volume < 0:
            self.cursor_volume = 0

    def key_event_volume(self, event):

        # change focus
        if event == ord('h') or event == ord('l'):
            self.cursor_volume += -1 if event == ord('h') else +1
            # cursorCheck_volume happens here, too!
            self.draw_controls_volume()
            return True

        elif 'changeVolume' in self.__class__.__dict__ and event in [ ord('k'), ord('K'), ord('j'), ord('J') ]:
            self.cursorCheck_volume()
            self.changeVolume(event == ord('k') or event == ord('K'), event == ord('K') or event == ord('J'), [ self.cursor_volume ])

            self.draw_controls_volume()
            return True

        elif 'setVolume' in self.__class__.__dict__:
            if event == ord('n'):
                self.cursorCheck_volume()
                self.setVolume(1.0, False, [ self.cursor_volume ])

                self.draw_controls_volume()
                return True

            elif event == ord('N'):
                self.setVolume(1.0)

                self.draw_controls_volume()
                return True

            elif event == ord('m'):
                self.cursorCheck_volume()
                self.setVolume(0.0, False, [ self.cursor_volume ])

                self.draw_controls_volume()
                return True

            elif event == ord('M'):
                self.setVolume(0.0)

                self.draw_controls_volume()
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

    def draw_picto(self, win, cursor = False):
        """ Draws a neat little pictogram of the speaker setup """
        for i in range(0, self.channels):
            picto = channel_picto[self.channel_map[i]]
            win.move(picto[1], picto[2])
            color = 0
            if self.volume[i] == 0.0:
                color = curses.color_pair(6)
            elif self.volume[i] > 1.0:
                color = curses.color_pair(2)
            win.addstr(picto[0], color | (curses.A_BOLD if cursor is not False and (i == cursor) else 0))

    def volume_uniform(self):
        if self.channels == 0:
            return True
        for i in range(1, self.channels):
            if self.volume[i] != self.volume[0]:
                return False
        return True

    def getSetVolume(self, value, hard = False, channels = None):
        volume = []
        value = max(0.0, min(par.volume_max_hard if hard else par.volume_max_soft, value))

        # create a list of channels
        for i in range(0, len(self.volume)):
            # apply new value?
            if channels is None or i in channels:
                volume.append(value)
            else:
                volume.append(self.volume[i])

        return volume

    def getChangeVolume(self, up, hard = False, channels = None):
        volume = []

        # create a list of volumes
        for i in range(0, len(self.volume)):
            # apply new value?
            if channels is None or i in channels:
                volume.append(max(0.0, min(par.volume_max_hard if hard else par.volume_max_soft, self.volume[i] + (par.volume_step if up else -par.volume_step))))
            else:
                volume.append(self.volume[i])

        return volume

    def still_exists(self):
        """ Needs to be overridden! This returns false if the underlying
            volume instance no longer exists. """
        return False
