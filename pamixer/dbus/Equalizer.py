import sys
import os

import dbus

from dbus.mainloop.glib import DBusGMainLoop
DBusGMainLoop(set_as_default=True)

# taken directly from qpaeq
def connect():
    try:
        if 'PULSE_DBUS_SERVER' in os.environ:
            address = os.environ['PULSE_DBUS_SERVER']
        else:
            bus = dbus.SessionBus() # Should be UserBus, but D-Bus doesn't implement that yet.
            server_lookup = bus.get_object('org.PulseAudio1', '/org/pulseaudio/server_lookup1')
            address = server_lookup.Get('org.PulseAudio.ServerLookup1', 'Address', dbus_interface='org.freedesktop.DBus.Properties')
        return dbus.connection.Connection(address)
    except Exception,e:
        self.__print('error: could not connect')

bus = connect()

prop_iface='org.freedesktop.DBus.Properties'

class Equalizer():

    manager_path='/org/pulseaudio/equalizing1'
    manager_iface='org.PulseAudio.Ext.Equalizing1.Manager'
    core_iface='org.PulseAudio.Core1'
    core_path='/org/pulseaudio/core1'

    def __init__(self):
        self.callback = None

        self.eq_sinks = { }

        # whether to use dB or linear for numeric volume display
        self.use_dezibel = True
        self.volume_step = 0.05
        self.volume_step_hard = 0.01
        self.volume_max_soft = 1.00
        self.volume_max_hard = 5.00

    def run(self, server = None):

        # get dbus objects
        self.manager_obj = bus.get_object(object_path=self.manager_path)

        # register a bunch of signals
        manager = dbus.Interface(self.manager_obj, dbus_interface=self.manager_iface)
        manager.connect_to_signal('ProfilesChanged', self.update_profiles)
        manager.connect_to_signal('SinkAdded', self.update_sinks)
        manager.connect_to_signal('SinkRemoved', self.update_sinks)

        # initial updates
        self.update_profiles()
        self.update_sinks()

    def update_profiles(self):
        #print 'update profiles called!'
        manager_props = dbus.Interface(self.manager_obj, dbus_interface=prop_iface)
        self.profiles = manager_props.Get(self.manager_iface, 'Profiles')

    def update_sinks(self):
        manager_props = dbus.Interface(self.manager_obj, dbus_interface=prop_iface)
        # get all equalized sinks
        sinks = manager_props.Get(self.manager_iface, 'EqualizedSinks')
        # and get them into a list (with names)

        # self.eq_sinks = { }

        for x in sinks:
            sink = bus.get_object(object_path=x)
            if x not in self.eq_sinks:
                self.eq_sinks[x] = EqSink(x, sink)
            else:
                self.eq_sinks[x].update(sink)

    def update(self):
        # sys.stdout.write("\a")
        # sys.stdout.flush()
        # return
        if self.callback:
            self.callback.update()

    def __print(self, *args):
        if self.callback and self.callback.verbose:
            sys.stderr.write(str(args))
        return

eq = Equalizer()

from EqSink import EqSink
