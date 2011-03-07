import curses 

from PulseAudio import PA_SINK_RUNNING, PA_SINK_SUSPENDED, PA_SINK_IDLE

state_names = { }
state_names[PA_SINK_RUNNING] = "running"
state_names[PA_SINK_SUSPENDED] = "suspended"
state_names[PA_SINK_IDLE] = "idle"

class Sink():
    def __init__(self, index, struct, props):

        self.wcontrols = None
        self.winfol = None
        self.winfor = None

        self.index = index
        self.update(struct, props)

        # -1 is volume, 0 and above are sink inputs
        self.cursor = -1

    def update(self, struct, props):
        self.name = struct.name
        self.channels = struct.volume.channels
        self.driver = struct.driver
        self.latency = struct.latency
        self.mute = struct.mute
        self.state = struct.state
        self.props = props

        self.volume = par.volume_to_linear(struct.volume)
        self.volume_db = par.volume_to_dB(struct.volume)

        if(self.driver == "module-tunnel.c") and 'tunnel.remote.fqdn' in self.props:
            remote_sink = self.props['tunnel.remote.sink']
            if remote_sink.rfind('.') > 0:
                self.short_name = self.props['tunnel.remote.fqdn'] + '/' + remote_sink[remote_sink.rfind('.')+1:]
            else:
                self.short_name = self.props['tunnel.remote.fqdn'] + '/' + remote_sink
        else:
            # stuff with dots in the name is usually just overhead
            if self.name.rfind('.') > 0:
                self.short_name = self.name[self.name.rfind('.')+1:]
            else:
                self.short_name = self.name

        self.redraw()

    def layout(self, win):
        # just clean up?
        if win is None:
            self.wcontrols = None
            self.winfol = None
            self.winfor = None
            return

        maxy, maxx = win.getmaxyx()

        if maxy > 32:
            win.attron(curses.color_pair(2))
            win.hline(32, 0, curses.ACS_HLINE, maxx)
            win.vline(32, 49, curses.ACS_VLINE, maxy)
            win.addch(32, 49, curses.ACS_TTEE)
            win.attroff(curses.color_pair(2))

        win.refresh()

        self.wcontrols = win.derwin(30, maxx, 1, 0)

        self.winfol = win.derwin(15, 45, 33, 2) if maxy > 33 else None
        self.winfor = win.derwin(33, 52) if maxy > 33 else None

        self.redraw()

    def redraw(self, recurse = False):
        self.draw_controls()
        self.draw_info()

    def draw_controls(self):
        # don't proceed if it's not even our turn to draw
        if self.wcontrols is None:
            return

        # if we aren't active, this needn't even be considered
        self.cursorCheck()

        wcontrols = self.wcontrols
        wcontrols.erase()

        # gauge, one bar for each channel
        gauge = wcontrols.derwin(22, self.channels+2, 2, 10-(self.channels/2))
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

        wcontrols.move(26, 6)
        wcontrols.addstr("Sink Volume", curses.A_BOLD if self.cursor == -1 else 0)
        wcontrols.move(27, 7)
        if par.use_dezibel:
            volume_db_avg = round(sum(self.volume_db) / len(self.volume_db), 2)
            wcontrols.addstr(('{:+3.2f}'.format(volume_db_avg) + " dB").rjust(9), curses.color_pair(2) if not self.volume_uniform() else 0)
        else:
            volume_avg = round(sum(self.volume) / len(self.volume), 2)
            wcontrols.addstr(('{:3.2f}'.format(volume_avg * 100) + " %").rjust(9), curses.color_pair(2) if not self.volume_uniform() else 0)

        inputs = par.get_sink_inputs_by_sink(self.index)
        i = 0
        for input in inputs:
            input.draw_control(wcontrols.derwin(2, 22 + i*25), self.cursor == i)
            i += 1

        wcontrols.refresh()

    def volume_uniform(self):
        if self.channels == 0:
            return True
        for i in range(1, self.channels):
            if self.volume[i] != self.volume[0]:
                return False
        return True

    def draw_info(self):
        if self.winfol is None or self.winfor is None:
            return

        wleft = self.winfol
        wright = self.winfor

        wleft.erase()
        wright.erase()

        wleft.move(0, 0)
        wleft.addstr(self.name.center(36) + "\n")

        wleft.addstr("\nDriver:\t\t" + self.driver)
        wleft.addstr("\nLatency:\t" + str(self.latency * 100))
        wleft.addstr("\nState:\t\t" + state_names[self.state])

        if self.cursor == -1:
            if(self.driver == "module-alsa-sink.c") and 'alsa.card_name' in self.props:
                wright.addstr("\nCard Name:\t" + self.props['alsa.card_name'])
            elif(self.driver == "module-tunnel.c"):
                wright.addstr("\nServer:\t\t" + self.props['tunnel.remote.server'])
                wright.addstr("\nRemote User:\t" + self.props['tunnel.remote.user'])
                wright.addstr("\nRemote Sink:\t" + self.props['tunnel.remote.description'])
        else:
            par.get_sink_inputs_by_sink(self.index)[self.cursor].draw_info(wright)

        wright.refresh()
        wleft.refresh()

    def cursorCheck(self):
        """
        Moves the cursor to the left until there is a sink input,
        or it's at the sink's volume.
        """
        sink_inputs = par.get_sink_inputs_by_sink(self.index)
        while self.cursor >= len(sink_inputs):
            self.cursor -= 1
        if self.cursor < -1:
            self.cursor = -1

    def key_event(self, event):

        # change focus
        if event == ord('h') or event == ord('l'):
            self.cursor += -1 if event == ord('h') else +1
            # cursorCheck happens here, too!
            self.draw_controls()
            self.draw_info()
            return True

        elif event in [ ord('k'), ord('K'), ord('j'), ord('J') ]:
            if self.cursor == -1:
                self.changeVolume(event == ord('k') or event == ord('K'), event == ord('K') or event == ord('J'))
            else:
                par.get_sink_inputs_by_sink(self.index)[self.cursor].changeVolume(event == ord('k') or event == ord('K'), event == ord('K') or event == ord('J'))

            self.draw_controls()
            return True

        elif event == ord('n'):
            if self.cursor == -1:
                self.setVolume(1.0)
            else:
                par.get_sink_inputs_by_sink(self.index)[self.cursor].setVolume(1.0)

            self.draw_controls()
            return True

        elif event == ord('N'):
            self.setVolume(1.0)
            sink_inputs = par.get_sink_inputs_by_sink(self.index)
            for sink_input in sink_inputs:
                sink_input.setVolume(1.0)

            self.draw_controls()
            return True

        elif event == ord('m'):
            if self.cursor == -1:
                self.setVolume(0.0)
            else:
                par.get_sink_inputs_by_sink(self.index)[self.cursor].setVolume(0.0)

            self.draw_controls()
            return True

        elif event == ord('X'):
            if self.cursor >= 0:
                par.get_sink_inputs_by_sink(self.index)[self.cursor].kill()

            self.draw_controls()
            return True

    def setVolume(self, value, hard = False):
        volume = []
        value = max(0.0, min(par.volume_max_hard if hard else par.volume_max_soft, value))
        for i in range(0, len(self.volume)):
            volume.append(value)
        par.set_sink_volume(self.index, volume)

    def changeVolume(self, up, hard = False):
        volume = []
        for i in range(0, len(self.volume)):
            volume.append(max(0.0, min(par.volume_max_hard if hard else par.volume_max_soft, self.volume[i] + (par.volume_step if up else -par.volume_step))))
        par.set_sink_volume(self.index, volume)

    def moveInput(self, index):
        # get the sink inputs of current sink
        sink_inputs = par.get_sink_inputs_by_sink(self.index)
        # move the selected sink input to the new sink
        par.move_sink_input(sink_inputs[self.cursor].index, index)

    def getActiveSinkInput(self):
        self.cursorCheck()
        if self.cursor == -1:
            return None
        return par.get_sink_inputs_by_sink(self.index)[self.cursor]

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
