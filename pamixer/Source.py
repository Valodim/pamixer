import curses 

from PulseAudio import PA_SINK_RUNNING, PA_SINK_SUSPENDED, PA_SINK_IDLE

from classes.SubVolume import SubVolume

state_names = { }
state_names[PA_SINK_RUNNING] = "running"
state_names[PA_SINK_SUSPENDED] = "suspended"
state_names[PA_SINK_IDLE] = "idle"

class Source(SubVolume):
    def __init__(self, index, struct, props):

        self.wcontrols = None
        self.winfol = None
        self.winfor = None

        self.is_monitor = False
        self.is_tunnel = False

        self.drawable = False

        SubVolume.__init__(self)

        self.index = index
        self.update(struct, props)

    def update(self, struct, props):
        self.name = struct.name
        self.driver = struct.driver
        self.latency = struct.latency
        self.state = struct.state
        self.props = props

        self.is_monitor = 'device.class' in self.props and self.props['device.class'] == 'monitor'

        # some name magic
        pieces = self.name.strip().split('.')
        if self.is_monitor:
            del(pieces[-1])

        if pieces[0] == 'tunnel':
            self.is_tunnel = True
            self.origin = pieces[0] + '.' + pieces[1]
        else:
            self.is_tunnel = False
            self.origin = pieces[0]
        self.clean_name = pieces[-1]

        SubVolume.update(self, struct)

        if(self.driver == "module-tunnel.c") and 'tunnel.remote.fqdn' in self.props:
            remote_source = self.props['tunnel.remote.source']
            if remote_source.rfind('.') > 0:
                self.short_name = self.props['tunnel.remote.fqdn'] + '/' + remote_source[remote_source.rfind('.')+1:]
            else:
                self.short_name = self.props['tunnel.remote.fqdn'] + '/' + remote_source
        else:
            # stuff with dots in the name is usually just overhead
            if self.name.rfind('.') > 0:
                self.short_name = self.name[self.name.rfind('.')+1:]
            else:
                self.short_name = self.name

    def draw_control(self, win, active = False):

        # gauge, one bar for each channel
        gauge = win.derwin(22, self.channels+2, 2, 10-(self.channels/2))
        for i in range(0, self.channels):
            barheight = min(22, int(self.volume[i] * 18))
            # lowest eight
            if barheight > 0:
                gauge.attron(curses.color_pair(3))
                gauge.vline(21-min(8, barheight), i+1, curses.ACS_BLOCK, min(8, barheight))
                gauge.attroff(curses.color_pair(3))
            # mid seven
            if barheight > 8:
                gauge.vline(13-min(7, barheight-8), i+1, curses.ACS_BLOCK, min(7, barheight-8))
            # top three
            if barheight > 15:
                gauge.attron(curses.color_pair(6))
                gauge.vline(6-min(3, barheight-15), i+1, curses.ACS_BLOCK, min(3, barheight-15))
                gauge.attroff(curses.color_pair(6))
            # over the top (clipping and stuff)
            if barheight > 18:
                gauge.attron(curses.color_pair(2))
                gauge.vline(3-min(3, barheight-18), i+1, curses.ACS_BLOCK, min(3, barheight-18))
                gauge.attroff(curses.color_pair(2))
        gauge.border()

        win.move(25, 2)
        if self.origin != 'local':
            win.addstr(self.origin[0:20].center(20), (curses.A_BOLD if active == -1 else 0) | (curses.color_pair(3) if self.is_tunnel else 0))
        win.move(26, 2)
        win.addstr(self.clean_name[0:20].center(20), (curses.A_BOLD if active == -1 else 0) | (curses.color_pair(2) if self.is_monitor else 0))
        win.move(27, 7)
        if par.use_dezibel:
            volume_db_avg = round(sum(self.volume_db) / len(self.volume_db), 2)
            win.addstr(('{:+3.2f}'.format(volume_db_avg) + " dB").rjust(9), curses.color_pair(2) if not self.volume_uniform() else 0)
        else:
            volume_avg = round(sum(self.volume) / len(self.volume), 2)
            win.addstr(('{:3.2f}'.format(volume_avg * 100) + " %").rjust(9), curses.color_pair(2) if not self.volume_uniform() else 0)

    def draw_info(self, active):
        wleft = self.winfol
        wright = self.winfor

        wleft.erase()
        wright.erase()

        wleft.move(0, 0)
        wleft.addstr(self.name.center(36) + "\n")

        wleft.addstr("\nDriver:\t\t" + self.driver)
        wleft.addstr("\nLatency:\t" + str(self.latency * 100))
        wleft.addstr("\nState:\t\t" + state_names[self.state])

        if active == -1:
            if(self.driver == "module-alsa-card.c") and 'alsa.card_name' in self.props:
                wright.addstr("\nCard Name:\t" + self.props['alsa.card_name'])
            elif(self.driver == "module-tunnel.c"):
                # wright.addstr("\nServer:\t\t" + self.props['tunnel.remote.server'])
                # wright.addstr("\nRemote User:\t" + self.props['tunnel.remote.user'])
                # wright.addstr("\nRemote Source:\t" + self.props['tunnel.remote.description'])
                pass
        else:
            par.get_source_outputs_by_source(self.index)[active].draw_info(wright)

    def clean_name_origin(self, name):
        return name

    def key_event(self, event):

        if event in [ ord('k'), ord('K'), ord('j'), ord('J') ]:
            self.changeVolume(event == ord('k') or event == ord('K'), event == ord('K') or event == ord('J'))
            return True

        elif event == ord('n'):
            self.setVolume(1.0)
            return True

        elif event == ord('m'):
            self.setVolume(0.0)
            return True

    def setVolume(self, value, hard = False, channels = None):
        volume = self.getSetVolume(value, hard, channels)
        par.set_source_volume(self.index, volume)

    def changeVolume(self, up, hard = False, channels = None):
        volume = self.getChangeVolume(up, hard, channels)
        par.set_source_volume(self.index, volume)

    def getActiveVolume(self):
        self.cursorCheck()
        if self.cursor == -1:
            return self
        return par.get_source_outputs_by_source(self.index)[self.cursor]

    def still_exists(self):
        return self.index in par.pa_sources

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
    ('flags', pa_source_flags_t),
    ('proplist', POINTER(pa_proplist)),
    ('configured_latency', pa_usec_t),
    ('base_volume', pa_volume_t),
    ('state', pa_source_state_t),
    ('n_volume_steps', uint32_t),
    ('card', uint32_t),
    ('n_ports', uint32_t),
    ('ports', POINTER(POINTER(pa_source_port_info))),
    ('active_port', POINTER(pa_source_port_info)),
    """

from ParCur import par
