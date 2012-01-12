
# class Equalizer(Object):

    # def set_connection(self):
        # self.connection=connect()
        # self.manager_obj=self.connection.get_object(object_path=self.manager_path)
        # manager_props=dbus.Interface(self.manager_obj,dbus_interface=prop_iface)
        # self.sinks=manager_props.Get(self.manager_iface,'EqualizedSinks')
    # # def set_callbacks(self):
        # manager=dbus.Interface(self.manager_obj,dbus_interface=self.manager_iface)
        # manager.connect_to_signal('ProfilesChanged',self.update_profiles)
        # manager.connect_to_signal('SinkAdded',self.sink_added)
        # manager.connect_to_signal('SinkRemoved',self.sink_removed)
