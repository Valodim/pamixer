from pulseaudio.lib_pulseaudio import *
import sys 
import os
import ctypes

from PulseAudio import PA_VOLUME_NORM

# A null method that can be given to pulse methods
def null_cb(a=None, b=None, c=None, d=None):
    #print "NULL CB"
    return

class PulseAudio():
    def __init__(self, new_client_cb, remove_client_cb, new_sink_cb, remove_sink_cb, new_sink_input_cb, remove_sink_input_cb, volume_change_cb, new_sample_cb, remove_sample_cb, new_source_cb, remove_source_cb, new_source_output_cb, remove_source_output_cb, server = None):

        self.sinks = {}
        self.monitor_sinks = []
        self.module_stream_restore_argument = ""

        self.new_client_cb = new_client_cb
        self.new_sink_input_cb = new_sink_input_cb
        self.remove_sink_input_cb = remove_sink_input_cb
        self.remove_client_cb = remove_client_cb
        self.new_sink_cb = new_sink_cb
        self.remove_sink_cb = remove_sink_cb
        self.new_sample_cb = new_sample_cb
        self.remove_sample_cb = remove_sample_cb
        self.new_source_cb = new_source_cb
        self.new_source_output_cb = new_source_output_cb
        self.remove_source_cb = remove_source_cb
        self.remove_source_output_cb = remove_source_output_cb
        self.volume_change_cb = volume_change_cb

        self.pa_mainloop = pa_threaded_mainloop_new()
        self.pa_mainloop_api = pa_threaded_mainloop_get_api(self.pa_mainloop)

        self._context = pa_context_new(self.pa_mainloop_api, "pamixer")
        self._context_notify_cb = pa_context_notify_cb_t(self.context_notify_cb)
        pa_context_set_state_callback(self._context, self._context_notify_cb, None)
        pa_context_connect(self._context, server, 0, None);

        pa_threaded_mainloop_start(self.pa_mainloop)

    def disconnect(self):
        pa_context_disconnect(self._context)

    # pulseaudio connection status    
    def context_notify_cb(self, context, userdata):

        try:
            ctc = pa_context_get_state(context)
            if ctc == PA_CONTEXT_READY:
                self.__print("== pulseaudio server ==")
                self.__print("pulseaudio connection ready...")

                self._null_cb = pa_context_success_cb_t(null_cb)
                self._pa_context_success_cb = pa_context_success_cb_t(self.pa_context_success_cb)
                self._pa_stream_request_cb = pa_stream_request_cb_t(self.pa_stream_request_cb)
                self._pa_stream_notify_cb = pa_stream_notify_cb_t(self.pa_stream_request_cb)
                self._pa_sink_info_cb = pa_sink_info_cb_t(self.pa_sink_info_cb)
                self._pa_context_subscribe_cb = pa_context_subscribe_cb_t(self.pa_context_subscribe_cb)
                self._pa_source_info_cb = pa_source_info_cb_t(self.pa_source_info_cb)
                self._pa_source_output_info_cb = pa_source_output_info_cb_t(self.pa_source_output_info_cb)
                self._pa_sample_info_list_cb = pa_sample_info_cb_t(self.pa_sample_info_cb)
                self._pa_sink_input_info_list_cb = pa_sink_input_info_cb_t(self.pa_sink_input_info_cb)
                self._pa_client_info_list_cb = pa_client_info_cb_t(self.pa_client_info_cb)
                self._pa_module_info_cb = pa_module_info_cb_t(self.pa_module_info_cb)
                self._pa_context_index_cb = pa_context_index_cb_t(self.pa_context_index_cb) 

                self.pa_request_update()

                pa_context_set_subscribe_callback(self._context, self._pa_context_subscribe_cb, None);
                o = pa_context_subscribe(self._context, (pa_subscription_mask_t)
                                               (PA_SUBSCRIPTION_MASK_SINK|
                                                PA_SUBSCRIPTION_MASK_SOURCE|
                                                PA_SUBSCRIPTION_MASK_SINK_INPUT|
                                                PA_SUBSCRIPTION_MASK_SOURCE_OUTPUT|
                                                PA_SUBSCRIPTION_MASK_CLIENT|
                                                PA_SUBSCRIPTION_MASK_SAMPLE_CACHE|
                                                PA_SUBSCRIPTION_MASK_SERVER), self._null_cb, None)  

                pa_operation_unref(o)

            if ctc == PA_CONTEXT_FAILED :
                print
                print "== pulseaudio server =="
                print "connection failed"
                pa_threaded_mainloop_signal(self.pa_mainloop, 0)
                sys.exit(1)

            if ctc == PA_CONTEXT_TERMINATED:
                print
                print "== pulseaudio server =="
                print "pulseaudio connection terminated"
                pa_threaded_mainloop_signal(self.pa_mainloop, 0)

        except Exception, text:
            print "ERROR context_notify_cb %s" % text
            raise Exception

    def pa_request_update(self):
        o = pa_context_get_module_info_list(self._context, self._pa_module_info_cb, True)
        pa_operation_unref(o)

        o = pa_context_get_source_info_list(self._context, self._pa_source_info_cb, True)
        pa_operation_unref(o)

        o = pa_context_get_client_info_list(self._context, self._pa_client_info_list_cb, None)
        pa_operation_unref(o)

        o = pa_context_get_source_output_info_list(self._context, self._pa_source_output_info_cb, None)
        pa_operation_unref(o)

        o = pa_context_get_sink_info_list(self._context, self._pa_sink_info_cb, None)
        pa_operation_unref(o)

        o = pa_context_get_sample_info_list(self._context, self._pa_sample_info_list_cb, True)
        pa_operation_unref(o)

        o = pa_context_get_sink_input_info_list(self._context, self._pa_sink_input_info_list_cb, True)
        pa_operation_unref(o)

    def pa_context_index_cb(self, context, index, user_data):
        # Do nothing....
        return

    def load_module_stream_restore(self):
        # print "Reloading module-stream-restore " 
        pa_context_load_module(self._context, "module-stream-restore", self.module_stream_restore_argument, self._pa_context_index_cb, None)


    def pa_module_info_cb(self, context, pa_module_info, eol, user_data):
        if user_data and pa_module_info:

            """if pa_module_info.contents.name == "module-stream-restore":
                print
                print "Found 'module-stream-restore'... unloading.."  
                self.module_stream_restore_argument = pa_module_info.contents.argument
                pa_context_unload_module(context, pa_module_info.contents.index, self._null_cb, None)"""
        return

    def pa_source_info_cb(self, context, struct, eol, user_data):
        if eol: return

        try:
            if struct:
                self.new_source_cb(struct.contents.index, struct.contents, self.dict_from_proplist(struct.contents.proplist))

        except Exception, text:
            self.__print( "pa :: ERROR pa_source_info_cb %s" % text)
            raise Exception

    def pa_stream_request_cb(self, stream, length, index):

        # This isnt quite right... maybe not a float.. ?

        #null_ptr = ctypes.c_void_p()
        data = POINTER(c_float)()
        pa_stream_peek(stream, data, ctypes.c_ulong(length)) 
        v = data[length / 4 -1] * 100
        if (v < 0):
            v = 0
        if (v > 100):
            v = 100
        pa_stream_drop(stream)

        # self.volume_meter_cb(index, v)

    def pa_create_monitor_stream_for_sink_input(self, index, monitor_index, name):

        if not index in self.monitor_sinks:
            self.monitor_sinks.append(index)
            # Create new stream
            ss = pa_sample_spec()
            ss.channels = 1
            ss.format = 5
            ss.rate = 25
            pa_stream = pa_stream_new(self._context, "Peak detect - " + name, ss, None)

            pa_stream_set_monitor_stream(pa_stream, index);
            pa_stream_set_read_callback(pa_stream, self._pa_stream_request_cb, index);
            pa_stream_set_suspended_callback(pa_stream, self._pa_stream_notify_cb, None);

            attr = pa_buffer_attr()
            attr.fragsize = 4
            attr.maxlength = 10
            attr.tlength = 0
            attr.prebuf = 0
            attr.minreq = 0

            pa_stream_connect_record(pa_stream, str(monitor_index), attr, 10752) 

    def pa_context_success_cb(self, context, c_int,  user_data):
        return

    def pa_source_output_info_cb(self, context, struct, index, user_data):
        if struct and user_data:

            # here we go...
            self.__print( "source output info")
            # self.__print( pa_proplist_to_string(struct.contents.proplist))

            self.new_source_output_cb(struct.contents.index, struct.contents, pa_proplist_to_string(struct.contents.proplist))
        return

    def pa_context_subscribe_cb(self, context, event_type, index, user_data):

        try:
            et = event_type & PA_SUBSCRIPTION_EVENT_FACILITY_MASK

            if et == PA_SUBSCRIPTION_EVENT_CLIENT:

                if event_type & PA_SUBSCRIPTION_EVENT_TYPE_MASK == PA_SUBSCRIPTION_EVENT_REMOVE:
                    self.remove_client_cb(int(index))
                else:
                    o = pa_context_get_client_info(self._context, index, self._pa_client_info_list_cb, None)
                    pa_operation_unref(o)

            if et == PA_SUBSCRIPTION_EVENT_SINK:
                if event_type & PA_SUBSCRIPTION_EVENT_TYPE_MASK == PA_SUBSCRIPTION_EVENT_REMOVE:
                     self.remove_sink_cb(int(index))
                else:
                    o = pa_context_get_sink_info_by_index(self._context, int(index), self._pa_sink_info_cb, True)
                    pa_operation_unref(o)

            if et == PA_SUBSCRIPTION_EVENT_SAMPLE_CACHE:
                if event_type & PA_SUBSCRIPTION_EVENT_TYPE_MASK == PA_SUBSCRIPTION_EVENT_REMOVE:
                     self.remove_sample_cb(int(index))
                     # self.monitor_sinks.remove(index)
                else:
                    o = pa_context_get_sample_info_by_index(self._context, int(index), self._pa_sample_info_list_cb, True)
                    pa_operation_unref(o)

            if et == PA_SUBSCRIPTION_EVENT_SINK_INPUT:
                if event_type & PA_SUBSCRIPTION_EVENT_TYPE_MASK == PA_SUBSCRIPTION_EVENT_REMOVE:
                     self.remove_sink_input_cb(int(index))
                     # self.monitor_sinks.remove(index)
                else:
                    o = pa_context_get_sink_input_info(self._context, int(index), self._pa_sink_input_info_list_cb, True)
                    pa_operation_unref(o)

            if et == PA_SUBSCRIPTION_EVENT_SOURCE:
                if event_type & PA_SUBSCRIPTION_EVENT_TYPE_MASK == PA_SUBSCRIPTION_EVENT_REMOVE:
                    # Remove output source
                    self.remove_source_cb( int(index) )
                else:
                    o = pa_context_get_source_info_by_index(self._context, int(index), self._pa_source_info_cb, True)
                    pa_operation_unref(o)

            if et == PA_SUBSCRIPTION_EVENT_SOURCE_OUTPUT:
                if event_type & PA_SUBSCRIPTION_EVENT_TYPE_MASK == PA_SUBSCRIPTION_EVENT_REMOVE:
                    # Remove output source
                    self.remove_source_output_cb( int(index) )
                else:
                    o = pa_context_get_source_output_info(self._context, int(index), self._pa_source_output_info_cb, True)
                    pa_operation_unref(o)

        except Exception, text:
            self.__print("pa :: ERROR pa_context_subscribe_cb %s" % text)
            raise Exception

    def dict_from_proplist(self, proplist):
        props = { }
        for prop in pa_proplist_to_string(proplist).split("\n"):
            left, _, right = prop.partition('=')
            props[left.strip()] = right.strip()[1:-1]
        return props

    def pa_client_info_cb(self, context, struct, c_int, user_data):
        try:
            if struct :
                self.new_client_cb(struct.contents.index, struct.contents, self.dict_from_proplist(struct.contents.proplist))

        except Exception, text:
            self.__print( "pa :: ERROR pa_client_info_cb %s" % text)    
            raise Exception

    def pa_sample_info_cb(self, context, struct, index, user_data):
        if struct and user_data:

            # here we go...
            self.__print( "SAMPLE INFO")
            # self.__print( pa_proplist_to_string(struct.contents.proplist))

            self.new_sample_cb(int(struct.contents.index), struct.contents, self.dict_from_proplist(struct.contents.proplist))

    def pa_sink_input_info_cb(self, context, struct, index, user_data):
        if struct and user_data:

            # here we go...
            self.__print( "SINK INPUT INFO")
            # self.__print( pa_proplist_to_string(struct.contents.proplist))

            self.new_sink_input_cb(int(struct.contents.index), struct.contents)

    # Move a playing stream to a differnt output sink
    def move_sink_input(self, sink_input_index, sink_index):
        self.__print("move_sink")
        pa_context_move_sink_input_by_index(self._context, sink_input_index, sink_index, self._pa_context_success_cb, None)

    def volume_from_linear(self, volume):
        cvolume = pa_cvolume()
        cvolume.channels = len(volume)
        v = pa_volume_t * 32
        cvolume.values = v()

        for i in range(0, len(volume)):
            cvolume.values[i] = pa_sw_volume_from_linear(volume[i])
        return cvolume

    def volume_to_dB(self, cvolume):
        volume = []
        for i in range(0, cvolume.channels):
            volume.append(pa_sw_volume_to_dB(cvolume.values[i]))
        return volume

    def volume_to_linear(self, cvolume):
        volume = []
        for i in range(0, cvolume.channels):
            volume.append(pa_sw_volume_to_linear(cvolume.values[i]))
        return volume

    def set_source_volume(self, index, cvolume):
        self.__print("set_source_volume")

        # Note setting volume causes a trigger of sink_input_info which will gives us back new volume!
        o = pa_context_set_source_volume_by_index(self._context, index, cvolume, self._null_cb, None) # NOTE: dont pass in any thing here causes a seg fault
        pa_operation_unref(o)

    def set_source_output_volume(self, index, cvolume):
        self.__print("set_source_output_volume")

        # Note setting volume causes a trigger of sink_input_info which will gives us back new volume!
        o = pa_context_set_source_output_volume(self._context, index, cvolume, self._null_cb, None) # NOTE: dont pass in any thing here causes a seg fault
        pa_operation_unref(o)

    def set_sink_volume(self, index, cvolume):
        self.__print("set_sink_volume")

        # Note setting volume causes a trigger of sink_input_info which will gives us back new volume!
        o = pa_context_set_sink_volume_by_index(self._context, index, cvolume, self._null_cb, None) # NOTE: dont pass in any thing here causes a seg fault
        pa_operation_unref(o)

    def set_sink_input_volume(self, index, cvolume):
        self.__print("set_sink_input_volume")

        # Note setting volume causes a trigger of sink_input_info which will gives us back new volume!
        o = pa_context_set_sink_input_volume(self._context, index, cvolume, self._null_cb, None) # NOTE: dont pass in any thing here causes a seg fault
        pa_operation_unref(o)

    def kill_sink_input(self, index):
        self.__print("kill_sink_input")

        # Note setting volume causes a trigger of sink_input_info which will gives us back new volume!
        o = pa_context_kill_sink_input(self._context, index, self._null_cb, None) # NOTE: dont pass in any thing here causes a seg fault
        pa_operation_unref(o)

    def sample_play(self, name, sink_name, volume = PA_VOLUME_NORM):
        self.__print("play sample: " + name + " on " + str(sink_name))
        o = pa_context_play_sample(self._context, name, sink_name, volume, self._null_cb, None)
        pa_operation_unref(o)

    def get_sink_info_by_name(self, sink_name):
        self.__print("get_sink_info_by_name")
        o = pa_context_get_sink_info_by_name(self._context, sink_name, self._pa_sink_info_cb, False)
        pa_operation_unref(o)

    def pa_sink_info_cb(self, context, struct, index, data):
        if struct:
            self.__print("pa_sink_info_cb")
            self.new_sink_cb(int(struct.contents.index), struct.contents, self.dict_from_proplist(struct.contents.proplist))

    def pa_ext_stream_restore_delete( self, stream):
        names = (c_char_p * 1)()
        names[0] = stream
        pa_ext_stream_restore_delete(self._context, names, self._pa_context_success_cb, None)

    def __print(self, text):
        # sys.stderr.write(str(text))
        return
