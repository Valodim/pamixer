import curses 

import sys

import math
import dbus

from Equalizer import prop_iface

device_iface='org.PulseAudio.Core1.Device'
eq_iface='org.PulseAudio.Ext.Equalizing1.Equalizer'

NORM_GRANULARITY = 100
MAX_AMP = 1.5
MIN_AMP = 2.5
GRANULARITY = int(MAX_AMP * NORM_GRANULARITY)
MIN_GRANULARITY = int(MIN_AMP * NORM_GRANULARITY)
STEP = NORM_GRANULARITY/10

class EqSink():

    # DEFAULT_FREQUENCIES = map(float,[25,50,75,100,150,200,300,400,500,800,1e3,1.5e3,3e3,5e3,7e3,10e3,15e3,20e3])
    DEFAULT_FREQUENCIES=[31.75,63.5,125,250,500,1e3,2e3,4e3,8e3,16e3]

    def __init__(self, index, sink):

        self.wcontrols = None
        self.winfol = None
        self.winfor = None

        self.drawable = False

        self.index = index

        sink_props = dbus.Interface(sink, dbus_interface=prop_iface)
        sink = dbus.Interface(sink, dbus_interface=eq_iface)

        self.name = sink_props.Get(device_iface, 'Name')

        self.sample_rate = sink_props.Get(eq_iface, 'SampleRate')
        self.filter_rate = sink_props.Get(eq_iface, 'FilterSampleRate')
        self.channels = sink_props.Get(eq_iface, 'NChannels')
        self.channel = self.channels

        base_freqs = self.freq_proper(EqSink.DEFAULT_FREQUENCIES)
        self.set_frequency_values(EqSink.subdivide(base_freqs, 18))
        # self.set_frequency_values(self.freq_proper(EqSink.DEFAULT_FREQUENCIES))

        self.update(sink)

        # -1 is volume, 0 and above are sink inputs
        self.cursor = -1
        self.padding = 0

        #set the signal listener for this sink
        core_iface='org.PulseAudio.Core1'
        core_path='/org/pulseaudio/core1'
        manager_path='/org/pulseaudio/equalizing1'
        core_obj = Equalizer.bus.get_object(object_path=core_path)
        core = dbus.Interface(core_obj,dbus_interface=core_iface)

        #temporary hack until signal filtering works properly
        core.ListenForSignal('',[dbus.ObjectPath(self.index),dbus.ObjectPath(manager_path)])
        self.sink.connect_to_signal('FilterChanged', self.update)

    def update(self, sink = None):

        if sink is not None:
            self.sink_props = dbus.Interface(sink, dbus_interface=prop_iface)
            self.sink = dbus.Interface(sink, dbus_interface=eq_iface)

        coefs, preamp = self.sink.FilterAtPoints(self.channel, self.filter_frequencies)
        self.coefficients = coefs
        self.preamp = preamp

        eq.callback.update()

        # sys.stderr.write(str(map(EqSink.hz2str, self.frequencies)))
        # sys.stderr.write(str(map(EqSink.coef2slider, self.coefficients)))
        # sys.stderr.write(str(self.sample_rate//2))

    def layout(self, win):
        # just clean up?
        if win is None:
            self.drawable = False
            return

        self.drawable = True

        maxy, maxx = win.getmaxyx()

        # got enough space for the info windows?
        if maxy > 48:
            win.attron(curses.color_pair(2))
            win.hline(32, 0, curses.ACS_HLINE, maxx)
            win.attroff(curses.color_pair(2))

            self.winfol = win.derwin(15, 45, 33, 2)

            # right side, too?
            if maxx > 87:
                win.attron(curses.color_pair(2))
                win.vline(32, 49, curses.ACS_VLINE, maxy)
                win.addch(32, 49, curses.ACS_TTEE)
                win.attroff(curses.color_pair(2))

                self.winfor = win.derwin(33, 52)
            else:
                # no right side info window..
                self.winfor = None

        else:
            # too bad, don't show this either.
            self.winfol = None
            self.winfor = None

        self.wcontrols = win.derwin(30, maxx, 1, 0)

    def redraw(self, recurse = False, active = False):
        self.draw_controls(active)
        self.draw_info()

    def draw_controls(self, active = False):
        # don't proceed if it's not even our turn to draw
        if self.drawable is False:
            return

        # if we aren't active, this needn't even be considered
        self.cursorCheck()

        wcontrols = self.wcontrols
        wcontrols.erase()

        # how much horizontal space do we got?
        maxy, maxx = wcontrols.getmaxyx()

        graph = wcontrols.derwin(25, (len(self.frequencies)+1)*8 +2, 0, 4)
        graph.border()

        self.drawSlider(wcontrols, graph, 26, 5, "Preamp", self.preamp, -1 == self.cursor)
        self.drawSlider(wcontrols, graph, 26, 12, "DC", self.coefficients[0], 0 == self.cursor)
        for i in range(1, len(self.frequencies)-1):
            self.drawSlider(wcontrols, graph, 26, i*8+12, EqSink.hz2str(self.frequencies[i]), self.coefficients[i], i == self.cursor)
        self.drawSlider(wcontrols, graph, 26, len(self.frequencies)*8+4, "Coda", self.coefficients[-1], len(self.frequencies)-1 == self.cursor)

    def drawSlider(self, win, graph, y, x, label, value, active):

        win.move(y, x+1)
        win.addstr(label.center(8), (curses.A_BOLD if active else 0))

        win.move(y+1, x+1)
        win.addstr("{:.1f}".format(EqSink.coef2slider(value)*10.0/NORM_GRANULARITY).center(8))

        # the height is the slider normalized to [25..0]
        height = 23-int( float(EqSink.coef2slider(value)+MIN_GRANULARITY)/NORM_GRANULARITY/(MAX_AMP+MIN_AMP)*23 )
        height = max(0, min(23, height))

        graph.addch( height, x, curses.ACS_BLOCK, (curses.A_BOLD if active else 0) )


    def draw_info(self):
        """ Draws a bunch of information on the winfol and winfor windows """
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

        if self.drawable is False:
            return

        if self.winfol is None:
            return

        wleft = self.winfol
        wleft.erase()

        wleft.move(0, 0)
        wleft.addstr(self.name.center(36) + "\n")

        # wleft.addstr("\nDriver:\t\t" + self.driver)
        # wleft.addstr("\nState:\t\t" + state_names[self.state])
        # wleft.addstr("\nActual Latency:\t" + '{:3.2f}ms'.format(self.latency / 1000))
        # wleft.addstr("\nConfig Latency:\t" + '{:3.2f}ms'.format(self.configured_latency / 1000))

        if self.winfor is None:
            return

        wright = self.winfor
        wright.erase()

    def cursorCheck(self):
        """
        Moves the cursor to the left until there is a sink input,
        or it's at the sink's volume.
        """
        while self.cursor >= len(self.frequencies):
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
            self.moveSlider(self.cursor, event == ord('k') or event == ord('K'), event == ord('K') or event == ord('J'))

            return True

        elif event == ord('n'):
            self.setSlider(self.cursor, 1.0)

            return True

        elif event == ord('m'):
            self.setSlider(self.cursor, 0.0)

            return True

        elif event == ord('X'):
            if self.cursor >= 0:
                par.get_sink_inputs_by_sink(self.index)[self.cursor].kill()

            self.draw_controls()
            return True

    def moveSlider(self, cursor, up, hard):
        if cursor == -1:
            self.preamp = EqSink.slider2coef( EqSink.coef2slider(self.preamp) + (STEP if up else -STEP) )
            self.preamp = max(0, min(10, self.preamp))
        else:
            self.coefficients[cursor] = EqSink.slider2coef( EqSink.coef2slider(self.coefficients[cursor]) + (STEP if up else -STEP) )
            self.coefficients[cursor] = max(0, min(10, self.coefficients[cursor]))

        self.sink.SeedFilter(self.channel, self.filter_frequencies, self.coefficients, self.preamp)

        self.draw_controls()

    def setSlider(self, cursor, to):
        if cursor == -1:
            self.preamp = to
            self.preamp = max(0, min(10, self.preamp))
        else:
            self.coefficients[cursor] = to
            self.coefficients[cursor] = max(0, min(10, self.coefficients[cursor]))

        self.sink.SeedFilter(self.channel, self.filter_frequencies, self.coefficients, self.preamp)

        self.draw_controls()

    def still_exists(self):
        return self.index in eq.eq_sinks

    def freq_proper(self,xs):
        return [0]+xs+[self.sample_rate//2]
    def set_frequency_values(self,freqs):
        self.frequencies = freqs
        #print 'base',self.frequencies
        self.filter_frequencies = map(lambda x: int(round(x)), \
                self.translate_rates(self.filter_rate,self.sample_rate,
                    self.frequencies) \
                )
        self.coefficients = [0.0]*len(self.frequencies)
        self.preamp = 1.0

    # most of those static methods were taken from qpaeq, the reference implementation :)

    @staticmethod
    def translate_rates(dst,src,rates):
        return list(map(lambda x: x*dst/src,rates))

    @staticmethod
    def slider2coef(x):
        #map x to ~ [-1, 1], divide by dB constant and convert to linear term
        return math.pow(10.0, x/(NORM_GRANULARITY*2.0))

    @staticmethod
    def coef2slider(x):
        try:
            return int(round(math.log10(x)*2.0*NORM_GRANULARITY))
        except ValueError, e:
            return -GRANULARITY

    @staticmethod
    def safe_log(k,b):
        i=0
        while k//b!=0:
            i+=1
            k=k//b
        return i

    @staticmethod
    def hz2str(hz):
        if hz == 0:
            return 'DC'
        p = EqSink.safe_log(hz, 10.0)
        if p < 3:
            return '%dHz' %(hz,)
        elif hz%1000==0:
            return '%dKHz' %(hz/(10.0**3),)
        else:
            return '%.1fKHz' %(hz/(10.0**3),)

    @staticmethod
    def subdivide(xs, t_points):
        while len(xs)<t_points:
            m=[0]*(2*len(xs)-1)
            m[0:len(m):2]=xs
            for i in range(1,len(m),2):
                m[i]=(m[i-1]+m[i+1])//2
            xs=m
        p_drop=len(xs)-t_points
        p_drop_left=p_drop//2
        p_drop_right=p_drop-p_drop_left
        #print 'xs',xs
        #print 'dropping %d, %d left, %d right' %(p_drop,p_drop_left,p_drop_right)
        c=len(xs)//2
        left=xs[0:p_drop_left*2:2]+xs[p_drop_left*2:c]
        right=list(reversed(xs[c:]))
        right=right[0:p_drop_right*2:2]+right[p_drop_right*2:]
        right=list(reversed(right))
        return left+right


from ..pulse.ParCur import par
from Equalizer import eq
import Equalizer
