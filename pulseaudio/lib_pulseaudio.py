
# generation commands
# python h2xml.py -I $PWD -o pa.xml pulse/mainloop-api.h pulse/sample.h pulse/def.h pulse/operation.h pulse/context.h pulse/channelmap.h pulse/volume.h pulse/stream.h pulse/introspect.h pulse/subscribe.h pulse/scache.h pulse/version.h pulse/error.h pulse/xmalloc.h pulse/utf8.h pulse/thread-mainloop.h pulse/mainloop.h pulse/mainloop-signal.h pulse/util.h pulse/timeval.h
# python xml2py.py -k efst -o lib_pulseaudio.py -l 'pulse' pa.xml

from ctypes import *

_libraries = {}
_libraries['libpulse.so.0'] = CDLL('libpulse.so.0')
STRING = c_char_p
WSTRING = c_wchar_p


PA_CHANNEL_POSITION_AUX31 = 43
PA_CHANNEL_POSITION_AUX30 = 42
PA_CHANNEL_POSITION_AUX28 = 40
PA_CHANNEL_POSITION_AUX26 = 38
PA_CHANNEL_POSITION_AUX25 = 37
PA_CHANNEL_POSITION_AUX24 = 36
PA_CHANNEL_POSITION_AUX23 = 35
PA_CHANNEL_POSITION_AUX22 = 34
PA_CHANNEL_POSITION_AUX20 = 32
PA_CHANNEL_POSITION_AUX19 = 31
PA_CHANNEL_POSITION_AUX18 = 30
PA_CHANNEL_POSITION_AUX17 = 29
PA_IO_EVENT_ERROR = 8
PA_CHANNEL_POSITION_AUX14 = 26
PA_IO_EVENT_HANGUP = 4
PA_CHANNEL_POSITION_AUX13 = 25
PA_CHANNEL_POSITION_AUX12 = 24
PA_IO_EVENT_INPUT = 1
PA_CHANNEL_POSITION_AUX11 = 23
PA_IO_EVENT_NULL = 0
PA_CHANNEL_POSITION_AUX8 = 20
PA_STREAM_READY = 2
PA_CHANNEL_POSITION_AUX7 = 19
PA_CHANNEL_POSITION_AUX6 = 18
PA_CHANNEL_POSITION_AUX3 = 15
PA_CHANNEL_POSITION_AUX0 = 12
PA_CHANNEL_POSITION_SIDE_RIGHT = 11
PA_CHANNEL_POSITION_SIDE_LEFT = 10
PA_CHANNEL_POSITION_FRONT_LEFT_OF_CENTER = 8
PA_CHANNEL_POSITION_SUBWOOFER = 7
PA_CHANNEL_POSITION_LFE = 7
PA_CHANNEL_POSITION_REAR_RIGHT = 6
PA_CHANNEL_POSITION_REAR_LEFT = 5
PA_CHANNEL_POSITION_REAR_CENTER = 4
PA_CHANNEL_POSITION_CENTER = 3
PA_CHANNEL_POSITION_RIGHT = 2
PA_CHANNEL_POSITION_LEFT = 1
PA_CHANNEL_POSITION_FRONT_CENTER = 3
PA_CHANNEL_POSITION_FRONT_RIGHT = 2
PA_CHANNEL_POSITION_FRONT_LEFT = 1
PA_CHANNEL_POSITION_MONO = 0
PA_CHANNEL_POSITION_INVALID = -1
ITIMER_PROF = 2
ITIMER_VIRTUAL = 1
ITIMER_REAL = 0
PA_STREAM_FIX_CHANNELS = 256
PA_STREAM_NO_REMAP_CHANNELS = 16
PA_STREAM_AUTO_TIMING_UPDATE = 8
PA_STREAM_FIX_FORMAT = 64
PA_STREAM_NOT_MONOTONIC = 4
PA_STREAM_DONT_MOVE = 512
PA_STREAM_INTERPOLATE_TIMING = 2
PA_STREAM_VARIABLE_RATE = 1024
PA_STREAM_START_CORKED = 1
PA_STREAM_START_MUTED = 4096
PA_STREAM_NOFLAGS = 0
PA_STREAM_ADJUST_LATENCY = 8192
PA_STREAM_START_UNMUTED = 65536
PA_STREAM_FAIL_ON_SUSPEND = 131072
PA_SOURCE_SUSPENDED = 2
PA_OPERATION_CANCELLED = 2
PA_OPERATION_DONE = 1
PA_OPERATION_RUNNING = 0
_IEEE_ = -1
PA_CHANNEL_POSITION_AUX29 = 41
PA_CHANNEL_POSITION_AUX27 = 39
PA_CHANNEL_POSITION_AUX15 = 27
PA_SEEK_RELATIVE_END = 3
PA_SEEK_RELATIVE_ON_READ = 2
PA_SEEK_ABSOLUTE = 1
PA_SEEK_RELATIVE = 0
PA_CHANNEL_POSITION_AUX21 = 33
PA_CHANNEL_POSITION_AUX16 = 28
PA_IO_EVENT_OUTPUT = 2
PA_SOURCE_INVALID_STATE = -1
PA_CHANNEL_POSITION_AUX10 = 22
PA_CHANNEL_POSITION_AUX9 = 21
PA_CHANNEL_POSITION_AUX5 = 17
PA_STREAM_NODIRECTION = 0
PA_CHANNEL_POSITION_AUX1 = 13
PA_STREAM_TERMINATED = 4
PA_STREAM_FAILED = 3
PA_CHANNEL_POSITION_FRONT_RIGHT_OF_CENTER = 9
PA_STREAM_CREATING = 1
PA_STREAM_UNCONNECTED = 0
PA_SINK_INVALID_STATE = -1
PA_STREAM_RECORD = 2
PA_UPDATE_SET = 0
PA_STREAM_PLAYBACK = 1
PA_SUBSCRIPTION_EVENT_SERVER = 7
PA_STREAM_UPLOAD = 3
PA_SINK_FLAT_VOLUME = 64
PA_SINK_DECIBEL_VOLUME = 32
PA_SINK_HW_MUTE_CTRL = 16
PA_SINK_NETWORK = 8
PA_SINK_HARDWARE = 4
PA_SINK_LATENCY = 2
PA_SINK_HW_VOLUME_CTRL = 1
PA_CHANNEL_POSITION_AUX4 = 16
PA_SINK_RUNNING = 0
PA_CHANNEL_MAP_AIFF = 0
PA_SINK_SUSPENDED = 2
PA_SINK_INIT = -2
PA_CONTEXT_TERMINATED = 6
PA_CONTEXT_FAILED = 5
PA_CONTEXT_READY = 4
PA_CONTEXT_SETTING_NAME = 3
PA_CONTEXT_CONNECTING = 1
PA_SOURCE_NOFLAGS = 0
PA_SOURCE_HW_VOLUME_CTRL = 1
PA_SOURCE_LATENCY = 2
PA_SOURCE_HARDWARE = 4
PA_SOURCE_NETWORK = 8
PA_SOURCE_HW_MUTE_CTRL = 16
PA_CONTEXT_UNCONNECTED = 0
PA_CHANNEL_POSITION_AUX2 = 14
PA_SOURCE_DYNAMIC_LATENCY = 64
PA_SOURCE_DECIBEL_VOLUME = 32
_XOPEN_ = 1
PA_SAMPLE_MAX = 13
PA_SAMPLE_S24_32BE = 12
PA_SAMPLE_U8 = 0
PA_SAMPLE_ALAW = 1
PA_SAMPLE_ULAW = 2
PA_SAMPLE_S16LE = 3
PA_SAMPLE_S16BE = 4
PA_SAMPLE_S24LE = 9
PA_SAMPLE_FLOAT32LE = 5
PA_SAMPLE_INVALID = -1
PA_SAMPLE_FLOAT32BE = 6
PA_SAMPLE_S32BE = 8
PA_SAMPLE_S24BE = 10
PA_SAMPLE_S32LE = 7
PA_AUTOLOAD_SOURCE = 1
PA_ERR_MAX = 27
PA_ERR_BUSY = 26
PA_ERR_IO = 25
PA_ERR_FORKED = 24
PA_ERR_NOTIMPLEMENTED = 23
PA_ERR_UNKNOWN = 20
PA_ERR_NOTSUPPORTED = 19
PA_ERR_TOOLARGE = 18
PA_ERR_VERSION = 17
PA_ERR_NODATA = 16
PA_ERR_BADSTATE = 15
PA_ERR_MODINITFAILED = 14
PA_ERR_KILLED = 12
PA_ERR_CONNECTIONTERMINATED = 11
PA_ERR_INTERNAL = 10
PA_ERR_TIMEOUT = 8
PA_ERR_CONNECTIONREFUSED = 6
PA_ERR_NOENTITY = 5
PA_ERR_AUTHKEY = 9
PA_ERR_EXIST = 4
PA_ERR_INVALID = 3
PA_ERR_COMMAND = 2
PA_ERR_ACCESS = 1
PA_OK = 0
PA_SINK_DYNAMIC_LATENCY = 128
PA_AUTOLOAD_SINK = 0
PA_UPDATE_REPLACE = 2
PA_UPDATE_MERGE = 1
PA_SAMPLE_S24_32LE = 11
PA_SINK_NOFLAGS = 0
PA_STREAM_FIX_RATE = 128
PA_STREAM_PEAK_DETECT = 2048
FP_NORMAL = 4
FP_SUBNORMAL = 3
PA_STREAM_NO_REMIX_CHANNELS = 32
PA_SINK_IDLE = 1
PA_STREAM_DONT_INHIBIT_AUTO_SUSPEND = 32768
PA_STREAM_EARLY_REQUESTS = 16384
PA_ERR_OBSOLETE = 22
PA_SUBSCRIPTION_MASK_ALL = 767
PA_SUBSCRIPTION_MASK_CARD = 512
PA_SUBSCRIPTION_MASK_AUTOLOAD = 256
PA_SUBSCRIPTION_MASK_SERVER = 128
PA_ERR_NOEXTENSION = 21
PA_SUBSCRIPTION_MASK_CLIENT = 32
PA_SUBSCRIPTION_MASK_SOURCE_OUTPUT = 8
PA_SUBSCRIPTION_MASK_SINK_INPUT = 4
PA_SUBSCRIPTION_MASK_SOURCE = 2
PA_SUBSCRIPTION_MASK_SINK = 1
PA_SUBSCRIPTION_MASK_NULL = 0
PA_ERR_INVALIDSERVER = 13
PA_SINK_UNLINKED = -3
PA_CONTEXT_AUTHORIZING = 2
PA_SOURCE_UNLINKED = -3
PA_SOURCE_INIT = -2
PA_SOURCE_IDLE = 1
PA_ERR_PROTOCOL = 7
PA_SUBSCRIPTION_MASK_SAMPLE_CACHE = 64
FP_ZERO = 2
PA_SOURCE_RUNNING = 0
FP_INFINITE = 1
FP_NAN = 0
PA_SUBSCRIPTION_MASK_MODULE = 16
PA_SUBSCRIPTION_EVENT_NEW = 0
_ISOC_ = 3
_POSIX_ = 2
_SVID_ = 0
PA_CHANNEL_MAP_ALSA = 1
PA_CHANNEL_MAP_WAVEEX = 3
PA_SUBSCRIPTION_EVENT_TYPE_MASK = 48
PA_SUBSCRIPTION_EVENT_REMOVE = 32
PA_CHANNEL_MAP_AUX = 2
PA_SUBSCRIPTION_EVENT_CHANGE = 16
PA_CHANNEL_MAP_OSS = 4
PA_CHANNEL_MAP_DEF_MAX = 5
PA_SUBSCRIPTION_EVENT_FACILITY_MASK = 15
PA_SUBSCRIPTION_EVENT_CARD = 9
PA_SUBSCRIPTION_EVENT_AUTOLOAD = 8
PA_CHANNEL_MAP_DEFAULT = 0
PA_SUBSCRIPTION_EVENT_SAMPLE_CACHE = 6
PA_SUBSCRIPTION_EVENT_CLIENT = 5
PA_SUBSCRIPTION_EVENT_MODULE = 4
PA_SUBSCRIPTION_EVENT_SOURCE_OUTPUT = 3
PA_SUBSCRIPTION_EVENT_SINK_INPUT = 2
PA_SUBSCRIPTION_EVENT_SOURCE = 1
PA_SUBSCRIPTION_EVENT_SINK = 0
PA_CONTEXT_NOFAIL = 2
PA_CONTEXT_NOAUTOSPAWN = 1
PA_CHANNEL_POSITION_MAX = 51
PA_CHANNEL_POSITION_TOP_REAR_CENTER = 50
PA_CHANNEL_POSITION_TOP_REAR_RIGHT = 49
PA_CHANNEL_POSITION_TOP_REAR_LEFT = 48
PA_CONTEXT_NOFLAGS = 0
PA_CHANNEL_POSITION_TOP_FRONT_CENTER = 47
PA_CHANNEL_POSITION_TOP_FRONT_RIGHT = 46
PA_CHANNEL_POSITION_TOP_FRONT_LEFT = 45
PA_CHANNEL_POSITION_TOP_CENTER = 44

# values for enumeration 'pa_channel_position'
pa_channel_position = c_int # enum
pa_channel_position_t = pa_channel_position
uint64_t = c_uint64
pa_channel_position_mask_t = uint64_t

# values for enumeration 'pa_channel_map_def'
pa_channel_map_def = c_int # enum
pa_channel_map_def_t = pa_channel_map_def
class pa_channel_map(Structure):
    pass
uint8_t = c_uint8
pa_channel_map._fields_ = [
    ('channels', uint8_t),
    ('map', pa_channel_position_t * 32),
]
pa_channel_map_init = _libraries['libpulse.so.0'].pa_channel_map_init
pa_channel_map_init.restype = POINTER(pa_channel_map)
pa_channel_map_init.argtypes = [POINTER(pa_channel_map)]
pa_channel_map_init_mono = _libraries['libpulse.so.0'].pa_channel_map_init_mono
pa_channel_map_init_mono.restype = POINTER(pa_channel_map)
pa_channel_map_init_mono.argtypes = [POINTER(pa_channel_map)]
pa_channel_map_init_stereo = _libraries['libpulse.so.0'].pa_channel_map_init_stereo
pa_channel_map_init_stereo.restype = POINTER(pa_channel_map)
pa_channel_map_init_stereo.argtypes = [POINTER(pa_channel_map)]
pa_channel_map_init_auto = _libraries['libpulse.so.0'].pa_channel_map_init_auto
pa_channel_map_init_auto.restype = POINTER(pa_channel_map)
pa_channel_map_init_auto.argtypes = [POINTER(pa_channel_map), c_uint, pa_channel_map_def_t]
pa_channel_map_init_extend = _libraries['libpulse.so.0'].pa_channel_map_init_extend
pa_channel_map_init_extend.restype = POINTER(pa_channel_map)
pa_channel_map_init_extend.argtypes = [POINTER(pa_channel_map), c_uint, pa_channel_map_def_t]
pa_channel_position_to_string = _libraries['libpulse.so.0'].pa_channel_position_to_string
pa_channel_position_to_string.restype = STRING
pa_channel_position_to_string.argtypes = [pa_channel_position_t]
pa_channel_position_from_string = _libraries['libpulse.so.0'].pa_channel_position_from_string
pa_channel_position_from_string.restype = pa_channel_position_t
pa_channel_position_from_string.argtypes = [STRING]
pa_channel_position_to_pretty_string = _libraries['libpulse.so.0'].pa_channel_position_to_pretty_string
pa_channel_position_to_pretty_string.restype = STRING
pa_channel_position_to_pretty_string.argtypes = [pa_channel_position_t]
size_t = c_uint
pa_channel_map_snprint = _libraries['libpulse.so.0'].pa_channel_map_snprint
pa_channel_map_snprint.restype = STRING
pa_channel_map_snprint.argtypes = [STRING, size_t, POINTER(pa_channel_map)]
pa_channel_map_parse = _libraries['libpulse.so.0'].pa_channel_map_parse
pa_channel_map_parse.restype = POINTER(pa_channel_map)
pa_channel_map_parse.argtypes = [POINTER(pa_channel_map), STRING]
pa_channel_map_equal = _libraries['libpulse.so.0'].pa_channel_map_equal
pa_channel_map_equal.restype = c_int
pa_channel_map_equal.argtypes = [POINTER(pa_channel_map), POINTER(pa_channel_map)]
pa_channel_map_valid = _libraries['libpulse.so.0'].pa_channel_map_valid
pa_channel_map_valid.restype = c_int
pa_channel_map_valid.argtypes = [POINTER(pa_channel_map)]
class pa_sample_spec(Structure):
    pass
pa_channel_map_compatible = _libraries['libpulse.so.0'].pa_channel_map_compatible
pa_channel_map_compatible.restype = c_int
pa_channel_map_compatible.argtypes = [POINTER(pa_channel_map), POINTER(pa_sample_spec)]
pa_channel_map_superset = _libraries['libpulse.so.0'].pa_channel_map_superset
pa_channel_map_superset.restype = c_int
pa_channel_map_superset.argtypes = [POINTER(pa_channel_map), POINTER(pa_channel_map)]
pa_channel_map_can_balance = _libraries['libpulse.so.0'].pa_channel_map_can_balance
pa_channel_map_can_balance.restype = c_int
pa_channel_map_can_balance.argtypes = [POINTER(pa_channel_map)]
pa_channel_map_can_fade = _libraries['libpulse.so.0'].pa_channel_map_can_fade
pa_channel_map_can_fade.restype = c_int
pa_channel_map_can_fade.argtypes = [POINTER(pa_channel_map)]
pa_channel_map_to_name = _libraries['libpulse.so.0'].pa_channel_map_to_name
pa_channel_map_to_name.restype = STRING
pa_channel_map_to_name.argtypes = [POINTER(pa_channel_map)]
pa_channel_map_to_pretty_name = _libraries['libpulse.so.0'].pa_channel_map_to_pretty_name
pa_channel_map_to_pretty_name.restype = STRING
pa_channel_map_to_pretty_name.argtypes = [POINTER(pa_channel_map)]
pa_channel_map_has_position = _libraries['libpulse.so.0'].pa_channel_map_has_position
pa_channel_map_has_position.restype = c_int
pa_channel_map_has_position.argtypes = [POINTER(pa_channel_map), pa_channel_position_t]
pa_channel_map_mask = _libraries['libpulse.so.0'].pa_channel_map_mask
pa_channel_map_mask.restype = pa_channel_position_mask_t
pa_channel_map_mask.argtypes = [POINTER(pa_channel_map)]
class pa_context(Structure):
    pass
pa_context._fields_ = [
]
pa_context_notify_cb_t = CFUNCTYPE(None, POINTER(pa_context), c_void_p)
pa_context_success_cb_t = CFUNCTYPE(None, POINTER(pa_context), c_int, c_void_p)
class pa_proplist(Structure):
    pass
pa_context_event_cb_t = CFUNCTYPE(None, POINTER(pa_context), STRING, POINTER(pa_proplist), c_void_p)
class pa_mainloop_api(Structure):
    pass
pa_context_new = _libraries['libpulse.so.0'].pa_context_new
pa_context_new.restype = POINTER(pa_context)
pa_context_new.argtypes = [POINTER(pa_mainloop_api), STRING]
pa_context_new_with_proplist = _libraries['libpulse.so.0'].pa_context_new_with_proplist
pa_context_new_with_proplist.restype = POINTER(pa_context)
pa_context_new_with_proplist.argtypes = [POINTER(pa_mainloop_api), STRING, POINTER(pa_proplist)]
pa_context_unref = _libraries['libpulse.so.0'].pa_context_unref
pa_context_unref.restype = None
pa_context_unref.argtypes = [POINTER(pa_context)]
pa_context_ref = _libraries['libpulse.so.0'].pa_context_ref
pa_context_ref.restype = POINTER(pa_context)
pa_context_ref.argtypes = [POINTER(pa_context)]
pa_context_set_state_callback = _libraries['libpulse.so.0'].pa_context_set_state_callback
pa_context_set_state_callback.restype = None
pa_context_set_state_callback.argtypes = [POINTER(pa_context), pa_context_notify_cb_t, c_void_p]
pa_context_set_event_callback = _libraries['libpulse.so.0'].pa_context_set_event_callback
pa_context_set_event_callback.restype = None
pa_context_set_event_callback.argtypes = [POINTER(pa_context), pa_context_event_cb_t, c_void_p]
pa_context_errno = _libraries['libpulse.so.0'].pa_context_errno
pa_context_errno.restype = c_int
pa_context_errno.argtypes = [POINTER(pa_context)]
pa_context_is_pending = _libraries['libpulse.so.0'].pa_context_is_pending
pa_context_is_pending.restype = c_int
pa_context_is_pending.argtypes = [POINTER(pa_context)]

# values for enumeration 'pa_context_state'
pa_context_state = c_int # enum
pa_context_state_t = pa_context_state
pa_context_get_state = _libraries['libpulse.so.0'].pa_context_get_state
pa_context_get_state.restype = pa_context_state_t
pa_context_get_state.argtypes = [POINTER(pa_context)]

# values for enumeration 'pa_context_flags'
pa_context_flags = c_int # enum
pa_context_flags_t = pa_context_flags
class pa_spawn_api(Structure):
    pass
pa_context_connect = _libraries['libpulse.so.0'].pa_context_connect
pa_context_connect.restype = c_int
pa_context_connect.argtypes = [POINTER(pa_context), STRING, pa_context_flags_t, POINTER(pa_spawn_api)]
pa_context_disconnect = _libraries['libpulse.so.0'].pa_context_disconnect
pa_context_disconnect.restype = None
pa_context_disconnect.argtypes = [POINTER(pa_context)]
class pa_operation(Structure):
    pass
pa_context_drain = _libraries['libpulse.so.0'].pa_context_drain
pa_context_drain.restype = POINTER(pa_operation)
pa_context_drain.argtypes = [POINTER(pa_context), pa_context_notify_cb_t, c_void_p]
pa_context_exit_daemon = _libraries['libpulse.so.0'].pa_context_exit_daemon
pa_context_exit_daemon.restype = POINTER(pa_operation)
pa_context_exit_daemon.argtypes = [POINTER(pa_context), pa_context_success_cb_t, c_void_p]
pa_context_set_default_sink = _libraries['libpulse.so.0'].pa_context_set_default_sink
pa_context_set_default_sink.restype = POINTER(pa_operation)
pa_context_set_default_sink.argtypes = [POINTER(pa_context), STRING, pa_context_success_cb_t, c_void_p]
pa_context_set_default_source = _libraries['libpulse.so.0'].pa_context_set_default_source
pa_context_set_default_source.restype = POINTER(pa_operation)
pa_context_set_default_source.argtypes = [POINTER(pa_context), STRING, pa_context_success_cb_t, c_void_p]
pa_context_is_local = _libraries['libpulse.so.0'].pa_context_is_local
pa_context_is_local.restype = c_int
pa_context_is_local.argtypes = [POINTER(pa_context)]
pa_context_set_name = _libraries['libpulse.so.0'].pa_context_set_name
pa_context_set_name.restype = POINTER(pa_operation)
pa_context_set_name.argtypes = [POINTER(pa_context), STRING, pa_context_success_cb_t, c_void_p]
pa_context_get_server = _libraries['libpulse.so.0'].pa_context_get_server
pa_context_get_server.restype = STRING
pa_context_get_server.argtypes = [POINTER(pa_context)]
uint32_t = c_uint32
pa_context_get_protocol_version = _libraries['libpulse.so.0'].pa_context_get_protocol_version
pa_context_get_protocol_version.restype = uint32_t
pa_context_get_protocol_version.argtypes = [POINTER(pa_context)]
pa_context_get_server_protocol_version = _libraries['libpulse.so.0'].pa_context_get_server_protocol_version
pa_context_get_server_protocol_version.restype = uint32_t
pa_context_get_server_protocol_version.argtypes = [POINTER(pa_context)]

# values for enumeration 'pa_update_mode'
pa_update_mode = c_int # enum
pa_update_mode_t = pa_update_mode
pa_context_proplist_update = _libraries['libpulse.so.0'].pa_context_proplist_update
pa_context_proplist_update.restype = POINTER(pa_operation)
pa_context_proplist_update.argtypes = [POINTER(pa_context), pa_update_mode_t, POINTER(pa_proplist), pa_context_success_cb_t, c_void_p]
pa_context_proplist_remove = _libraries['libpulse.so.0'].pa_context_proplist_remove
pa_context_proplist_remove.restype = POINTER(pa_operation)
pa_context_proplist_remove.argtypes = [POINTER(pa_context), POINTER(STRING), pa_context_success_cb_t, c_void_p]
pa_context_get_index = _libraries['libpulse.so.0'].pa_context_get_index
pa_context_get_index.restype = uint32_t
pa_context_get_index.argtypes = [POINTER(pa_context)]
class pa_time_event(Structure):
    pass
pa_usec_t = uint64_t
class timeval(Structure):
    pass
__time_t = c_long
__suseconds_t = c_long
timeval._fields_ = [
    ('tv_sec', __time_t),
    ('tv_usec', __suseconds_t),
]
pa_time_event_cb_t = CFUNCTYPE(None, POINTER(pa_mainloop_api), POINTER(pa_time_event), POINTER(timeval), c_void_p)
pa_context_rttime_new = _libraries['libpulse.so.0'].pa_context_rttime_new
pa_context_rttime_new.restype = POINTER(pa_time_event)
pa_context_rttime_new.argtypes = [POINTER(pa_context), pa_usec_t, pa_time_event_cb_t, c_void_p]
pa_context_rttime_restart = _libraries['libpulse.so.0'].pa_context_rttime_restart
pa_context_rttime_restart.restype = None
pa_context_rttime_restart.argtypes = [POINTER(pa_context), POINTER(pa_time_event), pa_usec_t]

# values for enumeration 'pa_stream_state'
pa_stream_state = c_int # enum
pa_stream_state_t = pa_stream_state

# values for enumeration 'pa_operation_state'
pa_operation_state = c_int # enum
pa_operation_state_t = pa_operation_state

# values for enumeration 'pa_stream_direction'
pa_stream_direction = c_int # enum
pa_stream_direction_t = pa_stream_direction

# values for enumeration 'pa_stream_flags'
pa_stream_flags = c_int # enum
pa_stream_flags_t = pa_stream_flags
class pa_buffer_attr(Structure):
    pass
pa_buffer_attr._fields_ = [
    ('maxlength', uint32_t),
    ('tlength', uint32_t),
    ('prebuf', uint32_t),
    ('minreq', uint32_t),
    ('fragsize', uint32_t),
]

# values for unnamed enumeration

# values for enumeration 'pa_subscription_mask'
pa_subscription_mask = c_int # enum
pa_subscription_mask_t = pa_subscription_mask

# values for enumeration 'pa_subscription_event_type'
pa_subscription_event_type = c_int # enum
pa_subscription_event_type_t = pa_subscription_event_type
class pa_timing_info(Structure):
    pass
int64_t = c_int64
pa_timing_info._pack_ = 4
pa_timing_info._fields_ = [
    ('timestamp', timeval),
    ('synchronized_clocks', c_int),
    ('sink_usec', pa_usec_t),
    ('source_usec', pa_usec_t),
    ('transport_usec', pa_usec_t),
    ('playing', c_int),
    ('write_index_corrupt', c_int),
    ('write_index', int64_t),
    ('read_index_corrupt', c_int),
    ('read_index', int64_t),
    ('configured_sink_usec', pa_usec_t),
    ('configured_source_usec', pa_usec_t),
    ('since_underrun', int64_t),
]
pa_spawn_api._fields_ = [
    ('prefork', CFUNCTYPE(None)),
    ('postfork', CFUNCTYPE(None)),
    ('atfork', CFUNCTYPE(None)),
]

# values for enumeration 'pa_seek_mode'
pa_seek_mode = c_int # enum
pa_seek_mode_t = pa_seek_mode

# values for enumeration 'pa_sink_flags'
pa_sink_flags = c_int # enum
pa_sink_flags_t = pa_sink_flags

# values for enumeration 'pa_sink_state'
pa_sink_state = c_int # enum
pa_sink_state_t = pa_sink_state

# values for enumeration 'pa_source_flags'
pa_source_flags = c_int # enum
pa_source_flags_t = pa_source_flags

# values for enumeration 'pa_source_state'
pa_source_state = c_int # enum
pa_source_state_t = pa_source_state
pa_free_cb_t = CFUNCTYPE(None, c_void_p)
pa_strerror = _libraries['libpulse.so.0'].pa_strerror
pa_strerror.restype = STRING
pa_strerror.argtypes = [c_int]
class pa_sink_port_info(Structure):
    pass
pa_sink_port_info._fields_ = [
    ('name', STRING),
    ('description', STRING),
    ('priority', uint32_t),
]
class pa_sink_info(Structure):
    pass

# values for enumeration 'pa_sample_format'
pa_sample_format = c_int # enum
pa_sample_format_t = pa_sample_format
pa_sample_spec._fields_ = [
    ('format', pa_sample_format_t),
    ('rate', uint32_t),
    ('channels', uint8_t),
]
class pa_cvolume(Structure):
    pass
pa_volume_t = uint32_t
pa_cvolume._fields_ = [
    ('channels', uint8_t),
    ('values', pa_volume_t * 32),
]
pa_sink_info._pack_ = 4
pa_sink_info._fields_ = [
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
]
pa_sink_info_cb_t = CFUNCTYPE(None, POINTER(pa_context), POINTER(pa_sink_info), c_int, c_void_p)
pa_context_get_sink_info_by_name = _libraries['libpulse.so.0'].pa_context_get_sink_info_by_name
pa_context_get_sink_info_by_name.restype = POINTER(pa_operation)
pa_context_get_sink_info_by_name.argtypes = [POINTER(pa_context), STRING, pa_sink_info_cb_t, c_void_p]
pa_context_get_sink_info_by_index = _libraries['libpulse.so.0'].pa_context_get_sink_info_by_index
pa_context_get_sink_info_by_index.restype = POINTER(pa_operation)
pa_context_get_sink_info_by_index.argtypes = [POINTER(pa_context), uint32_t, pa_sink_info_cb_t, c_void_p]
pa_context_get_sink_info_list = _libraries['libpulse.so.0'].pa_context_get_sink_info_list
pa_context_get_sink_info_list.restype = POINTER(pa_operation)
pa_context_get_sink_info_list.argtypes = [POINTER(pa_context), pa_sink_info_cb_t, c_void_p]
pa_context_set_sink_volume_by_index = _libraries['libpulse.so.0'].pa_context_set_sink_volume_by_index
pa_context_set_sink_volume_by_index.restype = POINTER(pa_operation)
pa_context_set_sink_volume_by_index.argtypes = [POINTER(pa_context), uint32_t, POINTER(pa_cvolume), pa_context_success_cb_t, c_void_p]
pa_context_set_sink_volume_by_name = _libraries['libpulse.so.0'].pa_context_set_sink_volume_by_name
pa_context_set_sink_volume_by_name.restype = POINTER(pa_operation)
pa_context_set_sink_volume_by_name.argtypes = [POINTER(pa_context), STRING, POINTER(pa_cvolume), pa_context_success_cb_t, c_void_p]
pa_context_set_sink_mute_by_index = _libraries['libpulse.so.0'].pa_context_set_sink_mute_by_index
pa_context_set_sink_mute_by_index.restype = POINTER(pa_operation)
pa_context_set_sink_mute_by_index.argtypes = [POINTER(pa_context), uint32_t, c_int, pa_context_success_cb_t, c_void_p]
pa_context_set_sink_mute_by_name = _libraries['libpulse.so.0'].pa_context_set_sink_mute_by_name
pa_context_set_sink_mute_by_name.restype = POINTER(pa_operation)
pa_context_set_sink_mute_by_name.argtypes = [POINTER(pa_context), STRING, c_int, pa_context_success_cb_t, c_void_p]
pa_context_suspend_sink_by_name = _libraries['libpulse.so.0'].pa_context_suspend_sink_by_name
pa_context_suspend_sink_by_name.restype = POINTER(pa_operation)
pa_context_suspend_sink_by_name.argtypes = [POINTER(pa_context), STRING, c_int, pa_context_success_cb_t, c_void_p]
pa_context_suspend_sink_by_index = _libraries['libpulse.so.0'].pa_context_suspend_sink_by_index
pa_context_suspend_sink_by_index.restype = POINTER(pa_operation)
pa_context_suspend_sink_by_index.argtypes = [POINTER(pa_context), uint32_t, c_int, pa_context_success_cb_t, c_void_p]
pa_context_set_sink_port_by_index = _libraries['libpulse.so.0'].pa_context_set_sink_port_by_index
pa_context_set_sink_port_by_index.restype = POINTER(pa_operation)
pa_context_set_sink_port_by_index.argtypes = [POINTER(pa_context), uint32_t, STRING, pa_context_success_cb_t, c_void_p]
pa_context_set_sink_port_by_name = _libraries['libpulse.so.0'].pa_context_set_sink_port_by_name
pa_context_set_sink_port_by_name.restype = POINTER(pa_operation)
pa_context_set_sink_port_by_name.argtypes = [POINTER(pa_context), STRING, STRING, pa_context_success_cb_t, c_void_p]
class pa_source_port_info(Structure):
    pass
pa_source_port_info._fields_ = [
    ('name', STRING),
    ('description', STRING),
    ('priority', uint32_t),
]
class pa_source_info(Structure):
    pass
pa_source_info._pack_ = 4
pa_source_info._fields_ = [
    ('name', STRING),
    ('index', uint32_t),
    ('description', STRING),
    ('sample_spec', pa_sample_spec),
    ('channel_map', pa_channel_map),
    ('owner_module', uint32_t),
    ('volume', pa_cvolume),
    ('mute', c_int),
    ('monitor_of_sink', uint32_t),
    ('monitor_of_sink_name', STRING),
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
]
pa_source_info_cb_t = CFUNCTYPE(None, POINTER(pa_context), POINTER(pa_source_info), c_int, c_void_p)
pa_context_get_source_info_by_name = _libraries['libpulse.so.0'].pa_context_get_source_info_by_name
pa_context_get_source_info_by_name.restype = POINTER(pa_operation)
pa_context_get_source_info_by_name.argtypes = [POINTER(pa_context), STRING, pa_source_info_cb_t, c_void_p]
pa_context_get_source_info_by_index = _libraries['libpulse.so.0'].pa_context_get_source_info_by_index
pa_context_get_source_info_by_index.restype = POINTER(pa_operation)
pa_context_get_source_info_by_index.argtypes = [POINTER(pa_context), uint32_t, pa_source_info_cb_t, c_void_p]
pa_context_get_source_info_list = _libraries['libpulse.so.0'].pa_context_get_source_info_list
pa_context_get_source_info_list.restype = POINTER(pa_operation)
pa_context_get_source_info_list.argtypes = [POINTER(pa_context), pa_source_info_cb_t, c_void_p]
pa_context_set_source_volume_by_index = _libraries['libpulse.so.0'].pa_context_set_source_volume_by_index
pa_context_set_source_volume_by_index.restype = POINTER(pa_operation)
pa_context_set_source_volume_by_index.argtypes = [POINTER(pa_context), uint32_t, POINTER(pa_cvolume), pa_context_success_cb_t, c_void_p]
pa_context_set_source_volume_by_name = _libraries['libpulse.so.0'].pa_context_set_source_volume_by_name
pa_context_set_source_volume_by_name.restype = POINTER(pa_operation)
pa_context_set_source_volume_by_name.argtypes = [POINTER(pa_context), STRING, POINTER(pa_cvolume), pa_context_success_cb_t, c_void_p]
pa_context_set_source_mute_by_index = _libraries['libpulse.so.0'].pa_context_set_source_mute_by_index
pa_context_set_source_mute_by_index.restype = POINTER(pa_operation)
pa_context_set_source_mute_by_index.argtypes = [POINTER(pa_context), uint32_t, c_int, pa_context_success_cb_t, c_void_p]
pa_context_set_source_mute_by_name = _libraries['libpulse.so.0'].pa_context_set_source_mute_by_name
pa_context_set_source_mute_by_name.restype = POINTER(pa_operation)
pa_context_set_source_mute_by_name.argtypes = [POINTER(pa_context), STRING, c_int, pa_context_success_cb_t, c_void_p]
pa_context_suspend_source_by_name = _libraries['libpulse.so.0'].pa_context_suspend_source_by_name
pa_context_suspend_source_by_name.restype = POINTER(pa_operation)
pa_context_suspend_source_by_name.argtypes = [POINTER(pa_context), STRING, c_int, pa_context_success_cb_t, c_void_p]
pa_context_suspend_source_by_index = _libraries['libpulse.so.0'].pa_context_suspend_source_by_index
pa_context_suspend_source_by_index.restype = POINTER(pa_operation)
pa_context_suspend_source_by_index.argtypes = [POINTER(pa_context), uint32_t, c_int, pa_context_success_cb_t, c_void_p]
pa_context_set_source_port_by_index = _libraries['libpulse.so.0'].pa_context_set_source_port_by_index
pa_context_set_source_port_by_index.restype = POINTER(pa_operation)
pa_context_set_source_port_by_index.argtypes = [POINTER(pa_context), uint32_t, STRING, pa_context_success_cb_t, c_void_p]
pa_context_set_source_port_by_name = _libraries['libpulse.so.0'].pa_context_set_source_port_by_name
pa_context_set_source_port_by_name.restype = POINTER(pa_operation)
pa_context_set_source_port_by_name.argtypes = [POINTER(pa_context), STRING, STRING, pa_context_success_cb_t, c_void_p]
class pa_server_info(Structure):
    pass
pa_server_info._fields_ = [
    ('user_name', STRING),
    ('host_name', STRING),
    ('server_version', STRING),
    ('server_name', STRING),
    ('sample_spec', pa_sample_spec),
    ('default_sink_name', STRING),
    ('default_source_name', STRING),
    ('cookie', uint32_t),
    ('channel_map', pa_channel_map),
]
pa_server_info_cb_t = CFUNCTYPE(None, POINTER(pa_context), POINTER(pa_server_info), c_void_p)
pa_context_get_server_info = _libraries['libpulse.so.0'].pa_context_get_server_info
pa_context_get_server_info.restype = POINTER(pa_operation)
pa_context_get_server_info.argtypes = [POINTER(pa_context), pa_server_info_cb_t, c_void_p]
class pa_module_info(Structure):
    pass
pa_module_info._fields_ = [
    ('index', uint32_t),
    ('name', STRING),
    ('argument', STRING),
    ('n_used', uint32_t),
    ('auto_unload', c_int),
    ('proplist', POINTER(pa_proplist)),
]
pa_module_info_cb_t = CFUNCTYPE(None, POINTER(pa_context), POINTER(pa_module_info), c_int, c_void_p)
pa_context_get_module_info = _libraries['libpulse.so.0'].pa_context_get_module_info
pa_context_get_module_info.restype = POINTER(pa_operation)
pa_context_get_module_info.argtypes = [POINTER(pa_context), uint32_t, pa_module_info_cb_t, c_void_p]
pa_context_get_module_info_list = _libraries['libpulse.so.0'].pa_context_get_module_info_list
pa_context_get_module_info_list.restype = POINTER(pa_operation)
pa_context_get_module_info_list.argtypes = [POINTER(pa_context), pa_module_info_cb_t, c_void_p]
pa_context_index_cb_t = CFUNCTYPE(None, POINTER(pa_context), uint32_t, c_void_p)
pa_context_load_module = _libraries['libpulse.so.0'].pa_context_load_module
pa_context_load_module.restype = POINTER(pa_operation)
pa_context_load_module.argtypes = [POINTER(pa_context), STRING, STRING, pa_context_index_cb_t, c_void_p]
pa_context_unload_module = _libraries['libpulse.so.0'].pa_context_unload_module
pa_context_unload_module.restype = POINTER(pa_operation)
pa_context_unload_module.argtypes = [POINTER(pa_context), uint32_t, pa_context_success_cb_t, c_void_p]
class pa_client_info(Structure):
    pass
pa_client_info._fields_ = [
    ('index', uint32_t),
    ('name', STRING),
    ('owner_module', uint32_t),
    ('driver', STRING),
    ('proplist', POINTER(pa_proplist)),
]
pa_client_info_cb_t = CFUNCTYPE(None, POINTER(pa_context), POINTER(pa_client_info), c_int, c_void_p)
pa_context_get_client_info = _libraries['libpulse.so.0'].pa_context_get_client_info
pa_context_get_client_info.restype = POINTER(pa_operation)
pa_context_get_client_info.argtypes = [POINTER(pa_context), uint32_t, pa_client_info_cb_t, c_void_p]
pa_context_get_client_info_list = _libraries['libpulse.so.0'].pa_context_get_client_info_list
pa_context_get_client_info_list.restype = POINTER(pa_operation)
pa_context_get_client_info_list.argtypes = [POINTER(pa_context), pa_client_info_cb_t, c_void_p]
pa_context_kill_client = _libraries['libpulse.so.0'].pa_context_kill_client
pa_context_kill_client.restype = POINTER(pa_operation)
pa_context_kill_client.argtypes = [POINTER(pa_context), uint32_t, pa_context_success_cb_t, c_void_p]
class pa_card_profile_info(Structure):
    pass
pa_card_profile_info._fields_ = [
    ('name', STRING),
    ('description', STRING),
    ('n_sinks', uint32_t),
    ('n_sources', uint32_t),
    ('priority', uint32_t),
]
class pa_card_info(Structure):
    pass
pa_card_info._fields_ = [
    ('index', uint32_t),
    ('name', STRING),
    ('owner_module', uint32_t),
    ('driver', STRING),
    ('n_profiles', uint32_t),
    ('profiles', POINTER(pa_card_profile_info)),
    ('active_profile', POINTER(pa_card_profile_info)),
    ('proplist', POINTER(pa_proplist)),
]
pa_card_info_cb_t = CFUNCTYPE(None, POINTER(pa_context), POINTER(pa_card_info), c_int, c_void_p)
pa_context_get_card_info_by_index = _libraries['libpulse.so.0'].pa_context_get_card_info_by_index
pa_context_get_card_info_by_index.restype = POINTER(pa_operation)
pa_context_get_card_info_by_index.argtypes = [POINTER(pa_context), uint32_t, pa_card_info_cb_t, c_void_p]
pa_context_get_card_info_by_name = _libraries['libpulse.so.0'].pa_context_get_card_info_by_name
pa_context_get_card_info_by_name.restype = POINTER(pa_operation)
pa_context_get_card_info_by_name.argtypes = [POINTER(pa_context), STRING, pa_card_info_cb_t, c_void_p]
pa_context_get_card_info_list = _libraries['libpulse.so.0'].pa_context_get_card_info_list
pa_context_get_card_info_list.restype = POINTER(pa_operation)
pa_context_get_card_info_list.argtypes = [POINTER(pa_context), pa_card_info_cb_t, c_void_p]
pa_context_set_card_profile_by_index = _libraries['libpulse.so.0'].pa_context_set_card_profile_by_index
pa_context_set_card_profile_by_index.restype = POINTER(pa_operation)
pa_context_set_card_profile_by_index.argtypes = [POINTER(pa_context), uint32_t, STRING, pa_context_success_cb_t, c_void_p]
pa_context_set_card_profile_by_name = _libraries['libpulse.so.0'].pa_context_set_card_profile_by_name
pa_context_set_card_profile_by_name.restype = POINTER(pa_operation)
pa_context_set_card_profile_by_name.argtypes = [POINTER(pa_context), STRING, STRING, pa_context_success_cb_t, c_void_p]
class pa_sink_input_info(Structure):
    pass
pa_sink_input_info._pack_ = 4
pa_sink_input_info._fields_ = [
    ('index', uint32_t),
    ('name', STRING),
    ('owner_module', uint32_t),
    ('client', uint32_t),
    ('sink', uint32_t),
    ('sample_spec', pa_sample_spec),
    ('channel_map', pa_channel_map),
    ('volume', pa_cvolume),
    ('buffer_usec', pa_usec_t),
    ('sink_usec', pa_usec_t),
    ('resample_method', STRING),
    ('driver', STRING),
    ('mute', c_int),
    ('proplist', POINTER(pa_proplist)),
]
pa_sink_input_info_cb_t = CFUNCTYPE(None, POINTER(pa_context), POINTER(pa_sink_input_info), c_int, c_void_p)
pa_context_get_sink_input_info = _libraries['libpulse.so.0'].pa_context_get_sink_input_info
pa_context_get_sink_input_info.restype = POINTER(pa_operation)
pa_context_get_sink_input_info.argtypes = [POINTER(pa_context), uint32_t, pa_sink_input_info_cb_t, c_void_p]
pa_context_get_sink_input_info_list = _libraries['libpulse.so.0'].pa_context_get_sink_input_info_list
pa_context_get_sink_input_info_list.restype = POINTER(pa_operation)
pa_context_get_sink_input_info_list.argtypes = [POINTER(pa_context), pa_sink_input_info_cb_t, c_void_p]
pa_context_move_sink_input_by_name = _libraries['libpulse.so.0'].pa_context_move_sink_input_by_name
pa_context_move_sink_input_by_name.restype = POINTER(pa_operation)
pa_context_move_sink_input_by_name.argtypes = [POINTER(pa_context), uint32_t, STRING, pa_context_success_cb_t, c_void_p]
pa_context_move_sink_input_by_index = _libraries['libpulse.so.0'].pa_context_move_sink_input_by_index
pa_context_move_sink_input_by_index.restype = POINTER(pa_operation)
pa_context_move_sink_input_by_index.argtypes = [POINTER(pa_context), uint32_t, uint32_t, pa_context_success_cb_t, c_void_p]
pa_context_set_sink_input_volume = _libraries['libpulse.so.0'].pa_context_set_sink_input_volume
pa_context_set_sink_input_volume.restype = POINTER(pa_operation)
pa_context_set_sink_input_volume.argtypes = [POINTER(pa_context), uint32_t, POINTER(pa_cvolume), pa_context_success_cb_t, c_void_p]
pa_context_set_sink_input_mute = _libraries['libpulse.so.0'].pa_context_set_sink_input_mute
pa_context_set_sink_input_mute.restype = POINTER(pa_operation)
pa_context_set_sink_input_mute.argtypes = [POINTER(pa_context), uint32_t, c_int, pa_context_success_cb_t, c_void_p]
pa_context_kill_sink_input = _libraries['libpulse.so.0'].pa_context_kill_sink_input
pa_context_kill_sink_input.restype = POINTER(pa_operation)
pa_context_kill_sink_input.argtypes = [POINTER(pa_context), uint32_t, pa_context_success_cb_t, c_void_p]
class pa_source_output_info(Structure):
    pass
pa_source_output_info._pack_ = 4
pa_source_output_info._fields_ = [
    ('index', uint32_t),
    ('name', STRING),
    ('owner_module', uint32_t),
    ('client', uint32_t),
    ('source', uint32_t),
    ('sample_spec', pa_sample_spec),
    ('channel_map', pa_channel_map),
    ('buffer_usec', pa_usec_t),
    ('source_usec', pa_usec_t),
    ('resample_method', STRING),
    ('driver', STRING),
    ('proplist', POINTER(pa_proplist)),
]
pa_source_output_info_cb_t = CFUNCTYPE(None, POINTER(pa_context), POINTER(pa_source_output_info), c_int, c_void_p)
pa_context_get_source_output_info = _libraries['libpulse.so.0'].pa_context_get_source_output_info
pa_context_get_source_output_info.restype = POINTER(pa_operation)
pa_context_get_source_output_info.argtypes = [POINTER(pa_context), uint32_t, pa_source_output_info_cb_t, c_void_p]
pa_context_get_source_output_info_list = _libraries['libpulse.so.0'].pa_context_get_source_output_info_list
pa_context_get_source_output_info_list.restype = POINTER(pa_operation)
pa_context_get_source_output_info_list.argtypes = [POINTER(pa_context), pa_source_output_info_cb_t, c_void_p]
pa_context_move_source_output_by_name = _libraries['libpulse.so.0'].pa_context_move_source_output_by_name
pa_context_move_source_output_by_name.restype = POINTER(pa_operation)
pa_context_move_source_output_by_name.argtypes = [POINTER(pa_context), uint32_t, STRING, pa_context_success_cb_t, c_void_p]
pa_context_move_source_output_by_index = _libraries['libpulse.so.0'].pa_context_move_source_output_by_index
pa_context_move_source_output_by_index.restype = POINTER(pa_operation)
pa_context_move_source_output_by_index.argtypes = [POINTER(pa_context), uint32_t, uint32_t, pa_context_success_cb_t, c_void_p]
pa_context_kill_source_output = _libraries['libpulse.so.0'].pa_context_kill_source_output
pa_context_kill_source_output.restype = POINTER(pa_operation)
pa_context_kill_source_output.argtypes = [POINTER(pa_context), uint32_t, pa_context_success_cb_t, c_void_p]
class pa_stat_info(Structure):
    pass
pa_stat_info._fields_ = [
    ('memblock_total', uint32_t),
    ('memblock_total_size', uint32_t),
    ('memblock_allocated', uint32_t),
    ('memblock_allocated_size', uint32_t),
    ('scache_size', uint32_t),
]
pa_stat_info_cb_t = CFUNCTYPE(None, POINTER(pa_context), POINTER(pa_stat_info), c_void_p)
pa_context_stat = _libraries['libpulse.so.0'].pa_context_stat
pa_context_stat.restype = POINTER(pa_operation)
pa_context_stat.argtypes = [POINTER(pa_context), pa_stat_info_cb_t, c_void_p]
class pa_sample_info(Structure):
    pass
pa_sample_info._pack_ = 4
pa_sample_info._fields_ = [
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
]
pa_sample_info_cb_t = CFUNCTYPE(None, POINTER(pa_context), POINTER(pa_sample_info), c_int, c_void_p)
pa_context_get_sample_info_by_name = _libraries['libpulse.so.0'].pa_context_get_sample_info_by_name
pa_context_get_sample_info_by_name.restype = POINTER(pa_operation)
pa_context_get_sample_info_by_name.argtypes = [POINTER(pa_context), STRING, pa_sample_info_cb_t, c_void_p]
pa_context_get_sample_info_by_index = _libraries['libpulse.so.0'].pa_context_get_sample_info_by_index
pa_context_get_sample_info_by_index.restype = POINTER(pa_operation)
pa_context_get_sample_info_by_index.argtypes = [POINTER(pa_context), uint32_t, pa_sample_info_cb_t, c_void_p]
pa_context_get_sample_info_list = _libraries['libpulse.so.0'].pa_context_get_sample_info_list
pa_context_get_sample_info_list.restype = POINTER(pa_operation)
pa_context_get_sample_info_list.argtypes = [POINTER(pa_context), pa_sample_info_cb_t, c_void_p]

# values for enumeration 'pa_autoload_type'
pa_autoload_type = c_int # enum
pa_autoload_type_t = pa_autoload_type
class pa_autoload_info(Structure):
    pass
pa_autoload_info._fields_ = [
    ('index', uint32_t),
    ('name', STRING),
    ('type', pa_autoload_type_t),
    ('module', STRING),
    ('argument', STRING),
]
pa_autoload_info_cb_t = CFUNCTYPE(None, POINTER(pa_context), POINTER(pa_autoload_info), c_int, c_void_p)
pa_context_get_autoload_info_by_name = _libraries['libpulse.so.0'].pa_context_get_autoload_info_by_name
pa_context_get_autoload_info_by_name.restype = POINTER(pa_operation)
pa_context_get_autoload_info_by_name.argtypes = [POINTER(pa_context), STRING, pa_autoload_type_t, pa_autoload_info_cb_t, c_void_p]
pa_context_get_autoload_info_by_index = _libraries['libpulse.so.0'].pa_context_get_autoload_info_by_index
pa_context_get_autoload_info_by_index.restype = POINTER(pa_operation)
pa_context_get_autoload_info_by_index.argtypes = [POINTER(pa_context), uint32_t, pa_autoload_info_cb_t, c_void_p]
pa_context_get_autoload_info_list = _libraries['libpulse.so.0'].pa_context_get_autoload_info_list
pa_context_get_autoload_info_list.restype = POINTER(pa_operation)
pa_context_get_autoload_info_list.argtypes = [POINTER(pa_context), pa_autoload_info_cb_t, c_void_p]
pa_context_add_autoload = _libraries['libpulse.so.0'].pa_context_add_autoload
pa_context_add_autoload.restype = POINTER(pa_operation)
pa_context_add_autoload.argtypes = [POINTER(pa_context), STRING, pa_autoload_type_t, STRING, STRING, pa_context_index_cb_t, c_void_p]
pa_context_remove_autoload_by_name = _libraries['libpulse.so.0'].pa_context_remove_autoload_by_name
pa_context_remove_autoload_by_name.restype = POINTER(pa_operation)
pa_context_remove_autoload_by_name.argtypes = [POINTER(pa_context), STRING, pa_autoload_type_t, pa_context_success_cb_t, c_void_p]
pa_context_remove_autoload_by_index = _libraries['libpulse.so.0'].pa_context_remove_autoload_by_index
pa_context_remove_autoload_by_index.restype = POINTER(pa_operation)
pa_context_remove_autoload_by_index.argtypes = [POINTER(pa_context), uint32_t, pa_context_success_cb_t, c_void_p]

# values for enumeration 'pa_io_event_flags'
pa_io_event_flags = c_int # enum
pa_io_event_flags_t = pa_io_event_flags
class pa_io_event(Structure):
    pass
pa_io_event._fields_ = [
]
pa_io_event_cb_t = CFUNCTYPE(None, POINTER(pa_mainloop_api), POINTER(pa_io_event), c_int, pa_io_event_flags_t, c_void_p)
pa_io_event_destroy_cb_t = CFUNCTYPE(None, POINTER(pa_mainloop_api), POINTER(pa_io_event), c_void_p)
pa_time_event._fields_ = [
]
pa_time_event_destroy_cb_t = CFUNCTYPE(None, POINTER(pa_mainloop_api), POINTER(pa_time_event), c_void_p)
class pa_defer_event(Structure):
    pass
pa_defer_event._fields_ = [
]
pa_defer_event_cb_t = CFUNCTYPE(None, POINTER(pa_mainloop_api), POINTER(pa_defer_event), c_void_p)
pa_defer_event_destroy_cb_t = CFUNCTYPE(None, POINTER(pa_mainloop_api), POINTER(pa_defer_event), c_void_p)
pa_mainloop_api._fields_ = [
    ('userdata', c_void_p),
    ('io_new', CFUNCTYPE(POINTER(pa_io_event), POINTER(pa_mainloop_api), c_int, pa_io_event_flags_t, pa_io_event_cb_t, c_void_p)),
    ('io_enable', CFUNCTYPE(None, POINTER(pa_io_event), pa_io_event_flags_t)),
    ('io_free', CFUNCTYPE(None, POINTER(pa_io_event))),
    ('io_set_destroy', CFUNCTYPE(None, POINTER(pa_io_event), pa_io_event_destroy_cb_t)),
    ('time_new', CFUNCTYPE(POINTER(pa_time_event), POINTER(pa_mainloop_api), POINTER(timeval), pa_time_event_cb_t, c_void_p)),
    ('time_restart', CFUNCTYPE(None, POINTER(pa_time_event), POINTER(timeval))),
    ('time_free', CFUNCTYPE(None, POINTER(pa_time_event))),
    ('time_set_destroy', CFUNCTYPE(None, POINTER(pa_time_event), pa_time_event_destroy_cb_t)),
    ('defer_new', CFUNCTYPE(POINTER(pa_defer_event), POINTER(pa_mainloop_api), pa_defer_event_cb_t, c_void_p)),
    ('defer_enable', CFUNCTYPE(None, POINTER(pa_defer_event), c_int)),
    ('defer_free', CFUNCTYPE(None, POINTER(pa_defer_event))),
    ('defer_set_destroy', CFUNCTYPE(None, POINTER(pa_defer_event), pa_defer_event_destroy_cb_t)),
    ('quit', CFUNCTYPE(None, POINTER(pa_mainloop_api), c_int)),
]
pa_mainloop_api_once = _libraries['libpulse.so.0'].pa_mainloop_api_once
pa_mainloop_api_once.restype = None
pa_mainloop_api_once.argtypes = [POINTER(pa_mainloop_api), CFUNCTYPE(None, POINTER(pa_mainloop_api), c_void_p), c_void_p]
class pa_signal_event(Structure):
    pass
pa_signal_event._fields_ = [
]
pa_signal_cb_t = CFUNCTYPE(None, POINTER(pa_mainloop_api), POINTER(pa_signal_event), c_int, c_void_p)
pa_signal_destroy_cb_t = CFUNCTYPE(None, POINTER(pa_mainloop_api), POINTER(pa_signal_event), c_void_p)
pa_signal_init = _libraries['libpulse.so.0'].pa_signal_init
pa_signal_init.restype = c_int
pa_signal_init.argtypes = [POINTER(pa_mainloop_api)]
pa_signal_done = _libraries['libpulse.so.0'].pa_signal_done
pa_signal_done.restype = None
pa_signal_done.argtypes = []
pa_signal_new = _libraries['libpulse.so.0'].pa_signal_new
pa_signal_new.restype = POINTER(pa_signal_event)
pa_signal_new.argtypes = [c_int, pa_signal_cb_t, c_void_p]
pa_signal_free = _libraries['libpulse.so.0'].pa_signal_free
pa_signal_free.restype = None
pa_signal_free.argtypes = [POINTER(pa_signal_event)]
pa_signal_set_destroy = _libraries['libpulse.so.0'].pa_signal_set_destroy
pa_signal_set_destroy.restype = None
pa_signal_set_destroy.argtypes = [POINTER(pa_signal_event), pa_signal_destroy_cb_t]
class pollfd(Structure):
    pass
pollfd._fields_ = [
]
class pa_mainloop(Structure):
    pass
pa_mainloop._fields_ = [
]
pa_mainloop_new = _libraries['libpulse.so.0'].pa_mainloop_new
pa_mainloop_new.restype = POINTER(pa_mainloop)
pa_mainloop_new.argtypes = []
pa_mainloop_free = _libraries['libpulse.so.0'].pa_mainloop_free
pa_mainloop_free.restype = None
pa_mainloop_free.argtypes = [POINTER(pa_mainloop)]
pa_mainloop_prepare = _libraries['libpulse.so.0'].pa_mainloop_prepare
pa_mainloop_prepare.restype = c_int
pa_mainloop_prepare.argtypes = [POINTER(pa_mainloop), c_int]
pa_mainloop_poll = _libraries['libpulse.so.0'].pa_mainloop_poll
pa_mainloop_poll.restype = c_int
pa_mainloop_poll.argtypes = [POINTER(pa_mainloop)]
pa_mainloop_dispatch = _libraries['libpulse.so.0'].pa_mainloop_dispatch
pa_mainloop_dispatch.restype = c_int
pa_mainloop_dispatch.argtypes = [POINTER(pa_mainloop)]
pa_mainloop_get_retval = _libraries['libpulse.so.0'].pa_mainloop_get_retval
pa_mainloop_get_retval.restype = c_int
pa_mainloop_get_retval.argtypes = [POINTER(pa_mainloop)]
pa_mainloop_iterate = _libraries['libpulse.so.0'].pa_mainloop_iterate
pa_mainloop_iterate.restype = c_int
pa_mainloop_iterate.argtypes = [POINTER(pa_mainloop), c_int, POINTER(c_int)]
pa_mainloop_run = _libraries['libpulse.so.0'].pa_mainloop_run
pa_mainloop_run.restype = c_int
pa_mainloop_run.argtypes = [POINTER(pa_mainloop), POINTER(c_int)]
pa_mainloop_get_api = _libraries['libpulse.so.0'].pa_mainloop_get_api
pa_mainloop_get_api.restype = POINTER(pa_mainloop_api)
pa_mainloop_get_api.argtypes = [POINTER(pa_mainloop)]
pa_mainloop_quit = _libraries['libpulse.so.0'].pa_mainloop_quit
pa_mainloop_quit.restype = None
pa_mainloop_quit.argtypes = [POINTER(pa_mainloop), c_int]
pa_mainloop_wakeup = _libraries['libpulse.so.0'].pa_mainloop_wakeup
pa_mainloop_wakeup.restype = None
pa_mainloop_wakeup.argtypes = [POINTER(pa_mainloop)]
pa_poll_func = CFUNCTYPE(c_int, POINTER(pollfd), c_ulong, c_int, c_void_p)
pa_mainloop_set_poll_func = _libraries['libpulse.so.0'].pa_mainloop_set_poll_func
pa_mainloop_set_poll_func.restype = None
pa_mainloop_set_poll_func.argtypes = [POINTER(pa_mainloop), pa_poll_func, c_void_p]
pa_operation._fields_ = [
]
pa_operation_ref = _libraries['libpulse.so.0'].pa_operation_ref
pa_operation_ref.restype = POINTER(pa_operation)
pa_operation_ref.argtypes = [POINTER(pa_operation)]
pa_operation_unref = _libraries['libpulse.so.0'].pa_operation_unref
pa_operation_unref.restype = None
pa_operation_unref.argtypes = [POINTER(pa_operation)]
pa_operation_cancel = _libraries['libpulse.so.0'].pa_operation_cancel
pa_operation_cancel.restype = None
pa_operation_cancel.argtypes = [POINTER(pa_operation)]
pa_operation_get_state = _libraries['libpulse.so.0'].pa_operation_get_state
pa_operation_get_state.restype = pa_operation_state_t
pa_operation_get_state.argtypes = [POINTER(pa_operation)]
pa_proplist._fields_ = [
]
pa_proplist_new = _libraries['libpulse.so.0'].pa_proplist_new
pa_proplist_new.restype = POINTER(pa_proplist)
pa_proplist_new.argtypes = []
pa_proplist_free = _libraries['libpulse.so.0'].pa_proplist_free
pa_proplist_free.restype = None
pa_proplist_free.argtypes = [POINTER(pa_proplist)]
pa_proplist_sets = _libraries['libpulse.so.0'].pa_proplist_sets
pa_proplist_sets.restype = c_int
pa_proplist_sets.argtypes = [POINTER(pa_proplist), STRING, STRING]
pa_proplist_setp = _libraries['libpulse.so.0'].pa_proplist_setp
pa_proplist_setp.restype = c_int
pa_proplist_setp.argtypes = [POINTER(pa_proplist), STRING]
pa_proplist_setf = _libraries['libpulse.so.0'].pa_proplist_setf
pa_proplist_setf.restype = c_int
pa_proplist_setf.argtypes = [POINTER(pa_proplist), STRING, STRING]
pa_proplist_set = _libraries['libpulse.so.0'].pa_proplist_set
pa_proplist_set.restype = c_int
pa_proplist_set.argtypes = [POINTER(pa_proplist), STRING, c_void_p, size_t]
pa_proplist_gets = _libraries['libpulse.so.0'].pa_proplist_gets
pa_proplist_gets.restype = STRING
pa_proplist_gets.argtypes = [POINTER(pa_proplist), STRING]
pa_proplist_get = _libraries['libpulse.so.0'].pa_proplist_get
pa_proplist_get.restype = c_int
pa_proplist_get.argtypes = [POINTER(pa_proplist), STRING, POINTER(c_void_p), POINTER(size_t)]
pa_proplist_update = _libraries['libpulse.so.0'].pa_proplist_update
pa_proplist_update.restype = None
pa_proplist_update.argtypes = [POINTER(pa_proplist), pa_update_mode_t, POINTER(pa_proplist)]
pa_proplist_unset = _libraries['libpulse.so.0'].pa_proplist_unset
pa_proplist_unset.restype = c_int
pa_proplist_unset.argtypes = [POINTER(pa_proplist), STRING]
pa_proplist_unset_many = _libraries['libpulse.so.0'].pa_proplist_unset_many
pa_proplist_unset_many.restype = c_int
pa_proplist_unset_many.argtypes = [POINTER(pa_proplist), POINTER(STRING)]
pa_proplist_iterate = _libraries['libpulse.so.0'].pa_proplist_iterate
pa_proplist_iterate.restype = STRING
pa_proplist_iterate.argtypes = [POINTER(pa_proplist), POINTER(c_void_p)]
pa_proplist_to_string = _libraries['libpulse.so.0'].pa_proplist_to_string
pa_proplist_to_string.restype = STRING
pa_proplist_to_string.argtypes = [POINTER(pa_proplist)]
pa_proplist_to_string_sep = _libraries['libpulse.so.0'].pa_proplist_to_string_sep
pa_proplist_to_string_sep.restype = STRING
pa_proplist_to_string_sep.argtypes = [POINTER(pa_proplist), STRING]
pa_proplist_from_string = _libraries['libpulse.so.0'].pa_proplist_from_string
pa_proplist_from_string.restype = POINTER(pa_proplist)
pa_proplist_from_string.argtypes = [STRING]
pa_proplist_contains = _libraries['libpulse.so.0'].pa_proplist_contains
pa_proplist_contains.restype = c_int
pa_proplist_contains.argtypes = [POINTER(pa_proplist), STRING]
pa_proplist_clear = _libraries['libpulse.so.0'].pa_proplist_clear
pa_proplist_clear.restype = None
pa_proplist_clear.argtypes = [POINTER(pa_proplist)]
pa_proplist_copy = _libraries['libpulse.so.0'].pa_proplist_copy
pa_proplist_copy.restype = POINTER(pa_proplist)
pa_proplist_copy.argtypes = [POINTER(pa_proplist)]
pa_proplist_size = _libraries['libpulse.so.0'].pa_proplist_size
pa_proplist_size.restype = c_uint
pa_proplist_size.argtypes = [POINTER(pa_proplist)]
pa_proplist_isempty = _libraries['libpulse.so.0'].pa_proplist_isempty
pa_proplist_isempty.restype = c_int
pa_proplist_isempty.argtypes = [POINTER(pa_proplist)]
pa_bytes_per_second = _libraries['libpulse.so.0'].pa_bytes_per_second
pa_bytes_per_second.restype = size_t
pa_bytes_per_second.argtypes = [POINTER(pa_sample_spec)]
pa_frame_size = _libraries['libpulse.so.0'].pa_frame_size
pa_frame_size.restype = size_t
pa_frame_size.argtypes = [POINTER(pa_sample_spec)]
pa_sample_size = _libraries['libpulse.so.0'].pa_sample_size
pa_sample_size.restype = size_t
pa_sample_size.argtypes = [POINTER(pa_sample_spec)]
pa_sample_size_of_format = _libraries['libpulse.so.0'].pa_sample_size_of_format
pa_sample_size_of_format.restype = size_t
pa_sample_size_of_format.argtypes = [pa_sample_format_t]
pa_bytes_to_usec = _libraries['libpulse.so.0'].pa_bytes_to_usec
pa_bytes_to_usec.restype = pa_usec_t
pa_bytes_to_usec.argtypes = [uint64_t, POINTER(pa_sample_spec)]
pa_usec_to_bytes = _libraries['libpulse.so.0'].pa_usec_to_bytes
pa_usec_to_bytes.restype = size_t
pa_usec_to_bytes.argtypes = [pa_usec_t, POINTER(pa_sample_spec)]
pa_sample_spec_init = _libraries['libpulse.so.0'].pa_sample_spec_init
pa_sample_spec_init.restype = POINTER(pa_sample_spec)
pa_sample_spec_init.argtypes = [POINTER(pa_sample_spec)]
pa_sample_spec_valid = _libraries['libpulse.so.0'].pa_sample_spec_valid
pa_sample_spec_valid.restype = c_int
pa_sample_spec_valid.argtypes = [POINTER(pa_sample_spec)]
pa_sample_spec_equal = _libraries['libpulse.so.0'].pa_sample_spec_equal
pa_sample_spec_equal.restype = c_int
pa_sample_spec_equal.argtypes = [POINTER(pa_sample_spec), POINTER(pa_sample_spec)]
pa_sample_format_to_string = _libraries['libpulse.so.0'].pa_sample_format_to_string
pa_sample_format_to_string.restype = STRING
pa_sample_format_to_string.argtypes = [pa_sample_format_t]
pa_parse_sample_format = _libraries['libpulse.so.0'].pa_parse_sample_format
pa_parse_sample_format.restype = pa_sample_format_t
pa_parse_sample_format.argtypes = [STRING]
pa_sample_spec_snprint = _libraries['libpulse.so.0'].pa_sample_spec_snprint
pa_sample_spec_snprint.restype = STRING
pa_sample_spec_snprint.argtypes = [STRING, size_t, POINTER(pa_sample_spec)]
pa_bytes_snprint = _libraries['libpulse.so.0'].pa_bytes_snprint
pa_bytes_snprint.restype = STRING
pa_bytes_snprint.argtypes = [STRING, size_t, c_uint]
pa_sample_format_is_le = _libraries['libpulse.so.0'].pa_sample_format_is_le
pa_sample_format_is_le.restype = c_int
pa_sample_format_is_le.argtypes = [pa_sample_format_t]
pa_sample_format_is_be = _libraries['libpulse.so.0'].pa_sample_format_is_be
pa_sample_format_is_be.restype = c_int
pa_sample_format_is_be.argtypes = [pa_sample_format_t]
pa_context_play_sample_cb_t = CFUNCTYPE(None, POINTER(pa_context), uint32_t, c_void_p)
class pa_stream(Structure):
    pass
pa_stream_connect_upload = _libraries['libpulse.so.0'].pa_stream_connect_upload
pa_stream_connect_upload.restype = c_int
pa_stream_connect_upload.argtypes = [POINTER(pa_stream), size_t]
pa_stream_finish_upload = _libraries['libpulse.so.0'].pa_stream_finish_upload
pa_stream_finish_upload.restype = c_int
pa_stream_finish_upload.argtypes = [POINTER(pa_stream)]
pa_context_remove_sample = _libraries['libpulse.so.0'].pa_context_remove_sample
pa_context_remove_sample.restype = POINTER(pa_operation)
pa_context_remove_sample.argtypes = [POINTER(pa_context), STRING, pa_context_success_cb_t, c_void_p]
pa_context_play_sample = _libraries['libpulse.so.0'].pa_context_play_sample
pa_context_play_sample.restype = POINTER(pa_operation)
pa_context_play_sample.argtypes = [POINTER(pa_context), STRING, STRING, pa_volume_t, pa_context_success_cb_t, c_void_p]
pa_context_play_sample_with_proplist = _libraries['libpulse.so.0'].pa_context_play_sample_with_proplist
pa_context_play_sample_with_proplist.restype = POINTER(pa_operation)
pa_context_play_sample_with_proplist.argtypes = [POINTER(pa_context), STRING, STRING, pa_volume_t, POINTER(pa_proplist), pa_context_play_sample_cb_t, c_void_p]
pa_stream._fields_ = [
]
pa_stream_success_cb_t = CFUNCTYPE(None, POINTER(pa_stream), c_int, c_void_p)
pa_stream_request_cb_t = CFUNCTYPE(None, POINTER(pa_stream), size_t, c_void_p)
pa_stream_notify_cb_t = CFUNCTYPE(None, POINTER(pa_stream), c_void_p)
pa_stream_event_cb_t = CFUNCTYPE(None, POINTER(pa_stream), STRING, POINTER(pa_proplist), c_void_p)
pa_stream_new = _libraries['libpulse.so.0'].pa_stream_new
pa_stream_new.restype = POINTER(pa_stream)
pa_stream_new.argtypes = [POINTER(pa_context), STRING, POINTER(pa_sample_spec), POINTER(pa_channel_map)]
pa_stream_new_with_proplist = _libraries['libpulse.so.0'].pa_stream_new_with_proplist
pa_stream_new_with_proplist.restype = POINTER(pa_stream)
pa_stream_new_with_proplist.argtypes = [POINTER(pa_context), STRING, POINTER(pa_sample_spec), POINTER(pa_channel_map), POINTER(pa_proplist)]
pa_stream_unref = _libraries['libpulse.so.0'].pa_stream_unref
pa_stream_unref.restype = None
pa_stream_unref.argtypes = [POINTER(pa_stream)]
pa_stream_ref = _libraries['libpulse.so.0'].pa_stream_ref
pa_stream_ref.restype = POINTER(pa_stream)
pa_stream_ref.argtypes = [POINTER(pa_stream)]
pa_stream_get_state = _libraries['libpulse.so.0'].pa_stream_get_state
pa_stream_get_state.restype = pa_stream_state_t
pa_stream_get_state.argtypes = [POINTER(pa_stream)]
pa_stream_get_context = _libraries['libpulse.so.0'].pa_stream_get_context
pa_stream_get_context.restype = POINTER(pa_context)
pa_stream_get_context.argtypes = [POINTER(pa_stream)]
pa_stream_get_index = _libraries['libpulse.so.0'].pa_stream_get_index
pa_stream_get_index.restype = uint32_t
pa_stream_get_index.argtypes = [POINTER(pa_stream)]
pa_stream_get_device_index = _libraries['libpulse.so.0'].pa_stream_get_device_index
pa_stream_get_device_index.restype = uint32_t
pa_stream_get_device_index.argtypes = [POINTER(pa_stream)]
pa_stream_get_device_name = _libraries['libpulse.so.0'].pa_stream_get_device_name
pa_stream_get_device_name.restype = STRING
pa_stream_get_device_name.argtypes = [POINTER(pa_stream)]
pa_stream_is_suspended = _libraries['libpulse.so.0'].pa_stream_is_suspended
pa_stream_is_suspended.restype = c_int
pa_stream_is_suspended.argtypes = [POINTER(pa_stream)]
pa_stream_is_corked = _libraries['libpulse.so.0'].pa_stream_is_corked
pa_stream_is_corked.restype = c_int
pa_stream_is_corked.argtypes = [POINTER(pa_stream)]
pa_stream_connect_playback = _libraries['libpulse.so.0'].pa_stream_connect_playback
pa_stream_connect_playback.restype = c_int
pa_stream_connect_playback.argtypes = [POINTER(pa_stream), STRING, POINTER(pa_buffer_attr), pa_stream_flags_t, POINTER(pa_cvolume), POINTER(pa_stream)]
pa_stream_connect_record = _libraries['libpulse.so.0'].pa_stream_connect_record
pa_stream_connect_record.restype = c_int
pa_stream_connect_record.argtypes = [POINTER(pa_stream), STRING, POINTER(pa_buffer_attr), pa_stream_flags_t]
pa_stream_disconnect = _libraries['libpulse.so.0'].pa_stream_disconnect
pa_stream_disconnect.restype = c_int
pa_stream_disconnect.argtypes = [POINTER(pa_stream)]
pa_stream_begin_write = _libraries['libpulse.so.0'].pa_stream_begin_write
pa_stream_begin_write.restype = c_int
pa_stream_begin_write.argtypes = [POINTER(pa_stream), POINTER(c_void_p), POINTER(size_t)]
pa_stream_cancel_write = _libraries['libpulse.so.0'].pa_stream_cancel_write
pa_stream_cancel_write.restype = c_int
pa_stream_cancel_write.argtypes = [POINTER(pa_stream)]
pa_stream_write = _libraries['libpulse.so.0'].pa_stream_write
pa_stream_write.restype = c_int
pa_stream_write.argtypes = [POINTER(pa_stream), c_void_p, size_t, pa_free_cb_t, int64_t, pa_seek_mode_t]
pa_stream_peek = _libraries['libpulse.so.0'].pa_stream_peek
pa_stream_peek.restype = c_int
pa_stream_peek.argtypes = [POINTER(pa_stream), POINTER(c_void_p), POINTER(size_t)]
pa_stream_drop = _libraries['libpulse.so.0'].pa_stream_drop
pa_stream_drop.restype = c_int
pa_stream_drop.argtypes = [POINTER(pa_stream)]
pa_stream_writable_size = _libraries['libpulse.so.0'].pa_stream_writable_size
pa_stream_writable_size.restype = size_t
pa_stream_writable_size.argtypes = [POINTER(pa_stream)]
pa_stream_readable_size = _libraries['libpulse.so.0'].pa_stream_readable_size
pa_stream_readable_size.restype = size_t
pa_stream_readable_size.argtypes = [POINTER(pa_stream)]
pa_stream_drain = _libraries['libpulse.so.0'].pa_stream_drain
pa_stream_drain.restype = POINTER(pa_operation)
pa_stream_drain.argtypes = [POINTER(pa_stream), pa_stream_success_cb_t, c_void_p]
pa_stream_update_timing_info = _libraries['libpulse.so.0'].pa_stream_update_timing_info
pa_stream_update_timing_info.restype = POINTER(pa_operation)
pa_stream_update_timing_info.argtypes = [POINTER(pa_stream), pa_stream_success_cb_t, c_void_p]
pa_stream_set_state_callback = _libraries['libpulse.so.0'].pa_stream_set_state_callback
pa_stream_set_state_callback.restype = None
pa_stream_set_state_callback.argtypes = [POINTER(pa_stream), pa_stream_notify_cb_t, c_void_p]
pa_stream_set_write_callback = _libraries['libpulse.so.0'].pa_stream_set_write_callback
pa_stream_set_write_callback.restype = None
pa_stream_set_write_callback.argtypes = [POINTER(pa_stream), pa_stream_request_cb_t, c_void_p]
pa_stream_set_read_callback = _libraries['libpulse.so.0'].pa_stream_set_read_callback
pa_stream_set_read_callback.restype = None
pa_stream_set_read_callback.argtypes = [POINTER(pa_stream), pa_stream_request_cb_t, c_void_p]
pa_stream_set_overflow_callback = _libraries['libpulse.so.0'].pa_stream_set_overflow_callback
pa_stream_set_overflow_callback.restype = None
pa_stream_set_overflow_callback.argtypes = [POINTER(pa_stream), pa_stream_notify_cb_t, c_void_p]
pa_stream_set_underflow_callback = _libraries['libpulse.so.0'].pa_stream_set_underflow_callback
pa_stream_set_underflow_callback.restype = None
pa_stream_set_underflow_callback.argtypes = [POINTER(pa_stream), pa_stream_notify_cb_t, c_void_p]
pa_stream_set_started_callback = _libraries['libpulse.so.0'].pa_stream_set_started_callback
pa_stream_set_started_callback.restype = None
pa_stream_set_started_callback.argtypes = [POINTER(pa_stream), pa_stream_notify_cb_t, c_void_p]
pa_stream_set_latency_update_callback = _libraries['libpulse.so.0'].pa_stream_set_latency_update_callback
pa_stream_set_latency_update_callback.restype = None
pa_stream_set_latency_update_callback.argtypes = [POINTER(pa_stream), pa_stream_notify_cb_t, c_void_p]
pa_stream_set_moved_callback = _libraries['libpulse.so.0'].pa_stream_set_moved_callback
pa_stream_set_moved_callback.restype = None
pa_stream_set_moved_callback.argtypes = [POINTER(pa_stream), pa_stream_notify_cb_t, c_void_p]
pa_stream_set_suspended_callback = _libraries['libpulse.so.0'].pa_stream_set_suspended_callback
pa_stream_set_suspended_callback.restype = None
pa_stream_set_suspended_callback.argtypes = [POINTER(pa_stream), pa_stream_notify_cb_t, c_void_p]
pa_stream_set_event_callback = _libraries['libpulse.so.0'].pa_stream_set_event_callback
pa_stream_set_event_callback.restype = None
pa_stream_set_event_callback.argtypes = [POINTER(pa_stream), pa_stream_event_cb_t, c_void_p]
pa_stream_set_buffer_attr_callback = _libraries['libpulse.so.0'].pa_stream_set_buffer_attr_callback
pa_stream_set_buffer_attr_callback.restype = None
pa_stream_set_buffer_attr_callback.argtypes = [POINTER(pa_stream), pa_stream_notify_cb_t, c_void_p]
pa_stream_cork = _libraries['libpulse.so.0'].pa_stream_cork
pa_stream_cork.restype = POINTER(pa_operation)
pa_stream_cork.argtypes = [POINTER(pa_stream), c_int, pa_stream_success_cb_t, c_void_p]
pa_stream_flush = _libraries['libpulse.so.0'].pa_stream_flush
pa_stream_flush.restype = POINTER(pa_operation)
pa_stream_flush.argtypes = [POINTER(pa_stream), pa_stream_success_cb_t, c_void_p]
pa_stream_prebuf = _libraries['libpulse.so.0'].pa_stream_prebuf
pa_stream_prebuf.restype = POINTER(pa_operation)
pa_stream_prebuf.argtypes = [POINTER(pa_stream), pa_stream_success_cb_t, c_void_p]
pa_stream_trigger = _libraries['libpulse.so.0'].pa_stream_trigger
pa_stream_trigger.restype = POINTER(pa_operation)
pa_stream_trigger.argtypes = [POINTER(pa_stream), pa_stream_success_cb_t, c_void_p]
pa_stream_set_name = _libraries['libpulse.so.0'].pa_stream_set_name
pa_stream_set_name.restype = POINTER(pa_operation)
pa_stream_set_name.argtypes = [POINTER(pa_stream), STRING, pa_stream_success_cb_t, c_void_p]
pa_stream_get_time = _libraries['libpulse.so.0'].pa_stream_get_time
pa_stream_get_time.restype = c_int
pa_stream_get_time.argtypes = [POINTER(pa_stream), POINTER(pa_usec_t)]
pa_stream_get_latency = _libraries['libpulse.so.0'].pa_stream_get_latency
pa_stream_get_latency.restype = c_int
pa_stream_get_latency.argtypes = [POINTER(pa_stream), POINTER(pa_usec_t), POINTER(c_int)]
pa_stream_get_timing_info = _libraries['libpulse.so.0'].pa_stream_get_timing_info
pa_stream_get_timing_info.restype = POINTER(pa_timing_info)
pa_stream_get_timing_info.argtypes = [POINTER(pa_stream)]
pa_stream_get_sample_spec = _libraries['libpulse.so.0'].pa_stream_get_sample_spec
pa_stream_get_sample_spec.restype = POINTER(pa_sample_spec)
pa_stream_get_sample_spec.argtypes = [POINTER(pa_stream)]
pa_stream_get_channel_map = _libraries['libpulse.so.0'].pa_stream_get_channel_map
pa_stream_get_channel_map.restype = POINTER(pa_channel_map)
pa_stream_get_channel_map.argtypes = [POINTER(pa_stream)]
pa_stream_get_buffer_attr = _libraries['libpulse.so.0'].pa_stream_get_buffer_attr
pa_stream_get_buffer_attr.restype = POINTER(pa_buffer_attr)
pa_stream_get_buffer_attr.argtypes = [POINTER(pa_stream)]
pa_stream_set_buffer_attr = _libraries['libpulse.so.0'].pa_stream_set_buffer_attr
pa_stream_set_buffer_attr.restype = POINTER(pa_operation)
pa_stream_set_buffer_attr.argtypes = [POINTER(pa_stream), POINTER(pa_buffer_attr), pa_stream_success_cb_t, c_void_p]
pa_stream_update_sample_rate = _libraries['libpulse.so.0'].pa_stream_update_sample_rate
pa_stream_update_sample_rate.restype = POINTER(pa_operation)
pa_stream_update_sample_rate.argtypes = [POINTER(pa_stream), uint32_t, pa_stream_success_cb_t, c_void_p]
pa_stream_proplist_update = _libraries['libpulse.so.0'].pa_stream_proplist_update
pa_stream_proplist_update.restype = POINTER(pa_operation)
pa_stream_proplist_update.argtypes = [POINTER(pa_stream), pa_update_mode_t, POINTER(pa_proplist), pa_stream_success_cb_t, c_void_p]
pa_stream_proplist_remove = _libraries['libpulse.so.0'].pa_stream_proplist_remove
pa_stream_proplist_remove.restype = POINTER(pa_operation)
pa_stream_proplist_remove.argtypes = [POINTER(pa_stream), POINTER(STRING), pa_stream_success_cb_t, c_void_p]
pa_stream_set_monitor_stream = _libraries['libpulse.so.0'].pa_stream_set_monitor_stream
pa_stream_set_monitor_stream.restype = c_int
pa_stream_set_monitor_stream.argtypes = [POINTER(pa_stream), uint32_t]
pa_stream_get_monitor_stream = _libraries['libpulse.so.0'].pa_stream_get_monitor_stream
pa_stream_get_monitor_stream.restype = uint32_t
pa_stream_get_monitor_stream.argtypes = [POINTER(pa_stream)]
pa_context_subscribe_cb_t = CFUNCTYPE(None, POINTER(pa_context), pa_subscription_event_type_t, uint32_t, c_void_p)
pa_context_subscribe = _libraries['libpulse.so.0'].pa_context_subscribe
pa_context_subscribe.restype = POINTER(pa_operation)
pa_context_subscribe.argtypes = [POINTER(pa_context), pa_subscription_mask_t, pa_context_success_cb_t, c_void_p]
pa_context_set_subscribe_callback = _libraries['libpulse.so.0'].pa_context_set_subscribe_callback
pa_context_set_subscribe_callback.restype = None
pa_context_set_subscribe_callback.argtypes = [POINTER(pa_context), pa_context_subscribe_cb_t, c_void_p]
class pa_threaded_mainloop(Structure):
    pass
pa_threaded_mainloop._fields_ = [
]
pa_threaded_mainloop_new = _libraries['libpulse.so.0'].pa_threaded_mainloop_new
pa_threaded_mainloop_new.restype = POINTER(pa_threaded_mainloop)
pa_threaded_mainloop_new.argtypes = []
pa_threaded_mainloop_free = _libraries['libpulse.so.0'].pa_threaded_mainloop_free
pa_threaded_mainloop_free.restype = None
pa_threaded_mainloop_free.argtypes = [POINTER(pa_threaded_mainloop)]
pa_threaded_mainloop_start = _libraries['libpulse.so.0'].pa_threaded_mainloop_start
pa_threaded_mainloop_start.restype = c_int
pa_threaded_mainloop_start.argtypes = [POINTER(pa_threaded_mainloop)]
pa_threaded_mainloop_stop = _libraries['libpulse.so.0'].pa_threaded_mainloop_stop
pa_threaded_mainloop_stop.restype = None
pa_threaded_mainloop_stop.argtypes = [POINTER(pa_threaded_mainloop)]
pa_threaded_mainloop_lock = _libraries['libpulse.so.0'].pa_threaded_mainloop_lock
pa_threaded_mainloop_lock.restype = None
pa_threaded_mainloop_lock.argtypes = [POINTER(pa_threaded_mainloop)]
pa_threaded_mainloop_unlock = _libraries['libpulse.so.0'].pa_threaded_mainloop_unlock
pa_threaded_mainloop_unlock.restype = None
pa_threaded_mainloop_unlock.argtypes = [POINTER(pa_threaded_mainloop)]
pa_threaded_mainloop_wait = _libraries['libpulse.so.0'].pa_threaded_mainloop_wait
pa_threaded_mainloop_wait.restype = None
pa_threaded_mainloop_wait.argtypes = [POINTER(pa_threaded_mainloop)]
pa_threaded_mainloop_signal = _libraries['libpulse.so.0'].pa_threaded_mainloop_signal
pa_threaded_mainloop_signal.restype = None
pa_threaded_mainloop_signal.argtypes = [POINTER(pa_threaded_mainloop), c_int]
pa_threaded_mainloop_accept = _libraries['libpulse.so.0'].pa_threaded_mainloop_accept
pa_threaded_mainloop_accept.restype = None
pa_threaded_mainloop_accept.argtypes = [POINTER(pa_threaded_mainloop)]
pa_threaded_mainloop_get_retval = _libraries['libpulse.so.0'].pa_threaded_mainloop_get_retval
pa_threaded_mainloop_get_retval.restype = c_int
pa_threaded_mainloop_get_retval.argtypes = [POINTER(pa_threaded_mainloop)]
pa_threaded_mainloop_get_api = _libraries['libpulse.so.0'].pa_threaded_mainloop_get_api
pa_threaded_mainloop_get_api.restype = POINTER(pa_mainloop_api)
pa_threaded_mainloop_get_api.argtypes = [POINTER(pa_threaded_mainloop)]
pa_threaded_mainloop_in_thread = _libraries['libpulse.so.0'].pa_threaded_mainloop_in_thread
pa_threaded_mainloop_in_thread.restype = c_int
pa_threaded_mainloop_in_thread.argtypes = [POINTER(pa_threaded_mainloop)]
pa_gettimeofday = _libraries['libpulse.so.0'].pa_gettimeofday
pa_gettimeofday.restype = POINTER(timeval)
pa_gettimeofday.argtypes = [POINTER(timeval)]
pa_timeval_diff = _libraries['libpulse.so.0'].pa_timeval_diff
pa_timeval_diff.restype = pa_usec_t
pa_timeval_diff.argtypes = [POINTER(timeval), POINTER(timeval)]
pa_timeval_cmp = _libraries['libpulse.so.0'].pa_timeval_cmp
pa_timeval_cmp.restype = c_int
pa_timeval_cmp.argtypes = [POINTER(timeval), POINTER(timeval)]
pa_timeval_age = _libraries['libpulse.so.0'].pa_timeval_age
pa_timeval_age.restype = pa_usec_t
pa_timeval_age.argtypes = [POINTER(timeval)]
pa_timeval_add = _libraries['libpulse.so.0'].pa_timeval_add
pa_timeval_add.restype = POINTER(timeval)
pa_timeval_add.argtypes = [POINTER(timeval), pa_usec_t]
pa_timeval_sub = _libraries['libpulse.so.0'].pa_timeval_sub
pa_timeval_sub.restype = POINTER(timeval)
pa_timeval_sub.argtypes = [POINTER(timeval), pa_usec_t]
pa_timeval_store = _libraries['libpulse.so.0'].pa_timeval_store
pa_timeval_store.restype = POINTER(timeval)
pa_timeval_store.argtypes = [POINTER(timeval), pa_usec_t]
pa_timeval_load = _libraries['libpulse.so.0'].pa_timeval_load
pa_timeval_load.restype = pa_usec_t
pa_timeval_load.argtypes = [POINTER(timeval)]
pa_utf8_valid = _libraries['libpulse.so.0'].pa_utf8_valid
pa_utf8_valid.restype = STRING
pa_utf8_valid.argtypes = [STRING]
pa_ascii_valid = _libraries['libpulse.so.0'].pa_ascii_valid
pa_ascii_valid.restype = STRING
pa_ascii_valid.argtypes = [STRING]
pa_utf8_filter = _libraries['libpulse.so.0'].pa_utf8_filter
pa_utf8_filter.restype = STRING
pa_utf8_filter.argtypes = [STRING]
pa_ascii_filter = _libraries['libpulse.so.0'].pa_ascii_filter
pa_ascii_filter.restype = STRING
pa_ascii_filter.argtypes = [STRING]
pa_utf8_to_locale = _libraries['libpulse.so.0'].pa_utf8_to_locale
pa_utf8_to_locale.restype = STRING
pa_utf8_to_locale.argtypes = [STRING]
pa_locale_to_utf8 = _libraries['libpulse.so.0'].pa_locale_to_utf8
pa_locale_to_utf8.restype = STRING
pa_locale_to_utf8.argtypes = [STRING]
pa_get_user_name = _libraries['libpulse.so.0'].pa_get_user_name
pa_get_user_name.restype = STRING
pa_get_user_name.argtypes = [STRING, size_t]
pa_get_host_name = _libraries['libpulse.so.0'].pa_get_host_name
pa_get_host_name.restype = STRING
pa_get_host_name.argtypes = [STRING, size_t]
pa_get_fqdn = _libraries['libpulse.so.0'].pa_get_fqdn
pa_get_fqdn.restype = STRING
pa_get_fqdn.argtypes = [STRING, size_t]
pa_get_home_dir = _libraries['libpulse.so.0'].pa_get_home_dir
pa_get_home_dir.restype = STRING
pa_get_home_dir.argtypes = [STRING, size_t]
pa_get_binary_name = _libraries['libpulse.so.0'].pa_get_binary_name
pa_get_binary_name.restype = STRING
pa_get_binary_name.argtypes = [STRING, size_t]
pa_path_get_filename = _libraries['libpulse.so.0'].pa_path_get_filename
pa_path_get_filename.restype = STRING
pa_path_get_filename.argtypes = [STRING]
pa_msleep = _libraries['libpulse.so.0'].pa_msleep
pa_msleep.restype = c_int
pa_msleep.argtypes = [c_ulong]
pa_get_library_version = _libraries['libpulse.so.0'].pa_get_library_version
pa_get_library_version.restype = STRING
pa_get_library_version.argtypes = []
pa_cvolume_equal = _libraries['libpulse.so.0'].pa_cvolume_equal
pa_cvolume_equal.restype = c_int
pa_cvolume_equal.argtypes = [POINTER(pa_cvolume), POINTER(pa_cvolume)]
pa_cvolume_init = _libraries['libpulse.so.0'].pa_cvolume_init
pa_cvolume_init.restype = POINTER(pa_cvolume)
pa_cvolume_init.argtypes = [POINTER(pa_cvolume)]
pa_cvolume_set = _libraries['libpulse.so.0'].pa_cvolume_set
pa_cvolume_set.restype = POINTER(pa_cvolume)
pa_cvolume_set.argtypes = [POINTER(pa_cvolume), c_uint, pa_volume_t]
pa_cvolume_snprint = _libraries['libpulse.so.0'].pa_cvolume_snprint
pa_cvolume_snprint.restype = STRING
pa_cvolume_snprint.argtypes = [STRING, size_t, POINTER(pa_cvolume)]
pa_sw_cvolume_snprint_dB = _libraries['libpulse.so.0'].pa_sw_cvolume_snprint_dB
pa_sw_cvolume_snprint_dB.restype = STRING
pa_sw_cvolume_snprint_dB.argtypes = [STRING, size_t, POINTER(pa_cvolume)]
pa_volume_snprint = _libraries['libpulse.so.0'].pa_volume_snprint
pa_volume_snprint.restype = STRING
pa_volume_snprint.argtypes = [STRING, size_t, pa_volume_t]
pa_sw_volume_snprint_dB = _libraries['libpulse.so.0'].pa_sw_volume_snprint_dB
pa_sw_volume_snprint_dB.restype = STRING
pa_sw_volume_snprint_dB.argtypes = [STRING, size_t, pa_volume_t]
pa_cvolume_avg = _libraries['libpulse.so.0'].pa_cvolume_avg
pa_cvolume_avg.restype = pa_volume_t
pa_cvolume_avg.argtypes = [POINTER(pa_cvolume)]
pa_cvolume_avg_mask = _libraries['libpulse.so.0'].pa_cvolume_avg_mask
pa_cvolume_avg_mask.restype = pa_volume_t
pa_cvolume_avg_mask.argtypes = [POINTER(pa_cvolume), POINTER(pa_channel_map), pa_channel_position_mask_t]
pa_cvolume_max = _libraries['libpulse.so.0'].pa_cvolume_max
pa_cvolume_max.restype = pa_volume_t
pa_cvolume_max.argtypes = [POINTER(pa_cvolume)]
pa_cvolume_max_mask = _libraries['libpulse.so.0'].pa_cvolume_max_mask
pa_cvolume_max_mask.restype = pa_volume_t
pa_cvolume_max_mask.argtypes = [POINTER(pa_cvolume), POINTER(pa_channel_map), pa_channel_position_mask_t]
pa_cvolume_min = _libraries['libpulse.so.0'].pa_cvolume_min
pa_cvolume_min.restype = pa_volume_t
pa_cvolume_min.argtypes = [POINTER(pa_cvolume)]
pa_cvolume_min_mask = _libraries['libpulse.so.0'].pa_cvolume_min_mask
pa_cvolume_min_mask.restype = pa_volume_t
pa_cvolume_min_mask.argtypes = [POINTER(pa_cvolume), POINTER(pa_channel_map), pa_channel_position_mask_t]
pa_cvolume_valid = _libraries['libpulse.so.0'].pa_cvolume_valid
pa_cvolume_valid.restype = c_int
pa_cvolume_valid.argtypes = [POINTER(pa_cvolume)]
pa_cvolume_channels_equal_to = _libraries['libpulse.so.0'].pa_cvolume_channels_equal_to
pa_cvolume_channels_equal_to.restype = c_int
pa_cvolume_channels_equal_to.argtypes = [POINTER(pa_cvolume), pa_volume_t]
pa_sw_volume_multiply = _libraries['libpulse.so.0'].pa_sw_volume_multiply
pa_sw_volume_multiply.restype = pa_volume_t
pa_sw_volume_multiply.argtypes = [pa_volume_t, pa_volume_t]
pa_sw_cvolume_multiply = _libraries['libpulse.so.0'].pa_sw_cvolume_multiply
pa_sw_cvolume_multiply.restype = POINTER(pa_cvolume)
pa_sw_cvolume_multiply.argtypes = [POINTER(pa_cvolume), POINTER(pa_cvolume), POINTER(pa_cvolume)]
pa_sw_cvolume_multiply_scalar = _libraries['libpulse.so.0'].pa_sw_cvolume_multiply_scalar
pa_sw_cvolume_multiply_scalar.restype = POINTER(pa_cvolume)
pa_sw_cvolume_multiply_scalar.argtypes = [POINTER(pa_cvolume), POINTER(pa_cvolume), pa_volume_t]
pa_sw_volume_divide = _libraries['libpulse.so.0'].pa_sw_volume_divide
pa_sw_volume_divide.restype = pa_volume_t
pa_sw_volume_divide.argtypes = [pa_volume_t, pa_volume_t]
pa_sw_cvolume_divide = _libraries['libpulse.so.0'].pa_sw_cvolume_divide
pa_sw_cvolume_divide.restype = POINTER(pa_cvolume)
pa_sw_cvolume_divide.argtypes = [POINTER(pa_cvolume), POINTER(pa_cvolume), POINTER(pa_cvolume)]
pa_sw_cvolume_divide_scalar = _libraries['libpulse.so.0'].pa_sw_cvolume_divide_scalar
pa_sw_cvolume_divide_scalar.restype = POINTER(pa_cvolume)
pa_sw_cvolume_divide_scalar.argtypes = [POINTER(pa_cvolume), POINTER(pa_cvolume), pa_volume_t]
pa_sw_volume_from_dB = _libraries['libpulse.so.0'].pa_sw_volume_from_dB
pa_sw_volume_from_dB.restype = pa_volume_t
pa_sw_volume_from_dB.argtypes = [c_double]
pa_sw_volume_to_dB = _libraries['libpulse.so.0'].pa_sw_volume_to_dB
pa_sw_volume_to_dB.restype = c_double
pa_sw_volume_to_dB.argtypes = [pa_volume_t]
pa_sw_volume_from_linear = _libraries['libpulse.so.0'].pa_sw_volume_from_linear
pa_sw_volume_from_linear.restype = pa_volume_t
pa_sw_volume_from_linear.argtypes = [c_double]
pa_sw_volume_to_linear = _libraries['libpulse.so.0'].pa_sw_volume_to_linear
pa_sw_volume_to_linear.restype = c_double
pa_sw_volume_to_linear.argtypes = [pa_volume_t]
pa_cvolume_remap = _libraries['libpulse.so.0'].pa_cvolume_remap
pa_cvolume_remap.restype = POINTER(pa_cvolume)
pa_cvolume_remap.argtypes = [POINTER(pa_cvolume), POINTER(pa_channel_map), POINTER(pa_channel_map)]
pa_cvolume_compatible = _libraries['libpulse.so.0'].pa_cvolume_compatible
pa_cvolume_compatible.restype = c_int
pa_cvolume_compatible.argtypes = [POINTER(pa_cvolume), POINTER(pa_sample_spec)]
pa_cvolume_compatible_with_channel_map = _libraries['libpulse.so.0'].pa_cvolume_compatible_with_channel_map
pa_cvolume_compatible_with_channel_map.restype = c_int
pa_cvolume_compatible_with_channel_map.argtypes = [POINTER(pa_cvolume), POINTER(pa_channel_map)]
pa_cvolume_get_balance = _libraries['libpulse.so.0'].pa_cvolume_get_balance
pa_cvolume_get_balance.restype = c_float
pa_cvolume_get_balance.argtypes = [POINTER(pa_cvolume), POINTER(pa_channel_map)]
pa_cvolume_set_balance = _libraries['libpulse.so.0'].pa_cvolume_set_balance
pa_cvolume_set_balance.restype = POINTER(pa_cvolume)
pa_cvolume_set_balance.argtypes = [POINTER(pa_cvolume), POINTER(pa_channel_map), c_float]
pa_cvolume_get_fade = _libraries['libpulse.so.0'].pa_cvolume_get_fade
pa_cvolume_get_fade.restype = c_float
pa_cvolume_get_fade.argtypes = [POINTER(pa_cvolume), POINTER(pa_channel_map)]
pa_cvolume_set_fade = _libraries['libpulse.so.0'].pa_cvolume_set_fade
pa_cvolume_set_fade.restype = POINTER(pa_cvolume)
pa_cvolume_set_fade.argtypes = [POINTER(pa_cvolume), POINTER(pa_channel_map), c_float]
pa_cvolume_scale = _libraries['libpulse.so.0'].pa_cvolume_scale
pa_cvolume_scale.restype = POINTER(pa_cvolume)
pa_cvolume_scale.argtypes = [POINTER(pa_cvolume), pa_volume_t]
pa_cvolume_scale_mask = _libraries['libpulse.so.0'].pa_cvolume_scale_mask
pa_cvolume_scale_mask.restype = POINTER(pa_cvolume)
pa_cvolume_scale_mask.argtypes = [POINTER(pa_cvolume), pa_volume_t, POINTER(pa_channel_map), pa_channel_position_mask_t]
pa_cvolume_set_position = _libraries['libpulse.so.0'].pa_cvolume_set_position
pa_cvolume_set_position.restype = POINTER(pa_cvolume)
pa_cvolume_set_position.argtypes = [POINTER(pa_cvolume), POINTER(pa_channel_map), pa_channel_position_t, pa_volume_t]
pa_cvolume_get_position = _libraries['libpulse.so.0'].pa_cvolume_get_position
pa_cvolume_get_position.restype = pa_volume_t
pa_cvolume_get_position.argtypes = [POINTER(pa_cvolume), POINTER(pa_channel_map), pa_channel_position_t]
pa_cvolume_merge = _libraries['libpulse.so.0'].pa_cvolume_merge
pa_cvolume_merge.restype = POINTER(pa_cvolume)
pa_cvolume_merge.argtypes = [POINTER(pa_cvolume), POINTER(pa_cvolume), POINTER(pa_cvolume)]
pa_cvolume_inc = _libraries['libpulse.so.0'].pa_cvolume_inc
pa_cvolume_inc.restype = POINTER(pa_cvolume)
pa_cvolume_inc.argtypes = [POINTER(pa_cvolume), pa_volume_t]
pa_cvolume_dec = _libraries['libpulse.so.0'].pa_cvolume_dec
pa_cvolume_dec.restype = POINTER(pa_cvolume)
pa_cvolume_dec.argtypes = [POINTER(pa_cvolume), pa_volume_t]
pa_xmalloc = _libraries['libpulse.so.0'].pa_xmalloc
pa_xmalloc.restype = c_void_p
pa_xmalloc.argtypes = [size_t]
pa_xmalloc0 = _libraries['libpulse.so.0'].pa_xmalloc0
pa_xmalloc0.restype = c_void_p
pa_xmalloc0.argtypes = [size_t]
pa_xrealloc = _libraries['libpulse.so.0'].pa_xrealloc
pa_xrealloc.restype = c_void_p
pa_xrealloc.argtypes = [c_void_p, size_t]
pa_xfree = _libraries['libpulse.so.0'].pa_xfree
pa_xfree.restype = None
pa_xfree.argtypes = [c_void_p]
pa_xstrdup = _libraries['libpulse.so.0'].pa_xstrdup
pa_xstrdup.restype = STRING
pa_xstrdup.argtypes = [STRING]
pa_xstrndup = _libraries['libpulse.so.0'].pa_xstrndup
pa_xstrndup.restype = STRING
pa_xstrndup.argtypes = [STRING, size_t]
pa_xmemdup = _libraries['libpulse.so.0'].pa_xmemdup
pa_xmemdup.restype = c_void_p
pa_xmemdup.argtypes = [c_void_p, size_t]
__assert_fail = _libraries['libpulse.so.0'].__assert_fail
__assert_fail.restype = None
__assert_fail.argtypes = [STRING, STRING, c_uint, STRING]
__assert_perror_fail = _libraries['libpulse.so.0'].__assert_perror_fail
__assert_perror_fail.restype = None
__assert_perror_fail.argtypes = [c_int, STRING, c_uint, STRING]
__assert = _libraries['libpulse.so.0'].__assert
__assert.restype = None
__assert.argtypes = [STRING, STRING, c_int]
acos = _libraries['libpulse.so.0'].acos
acos.restype = c_double
acos.argtypes = [c_double]
acosl = _libraries['libpulse.so.0'].acosl
acosl.restype = c_longdouble
acosl.argtypes = [c_longdouble]
acosf = _libraries['libpulse.so.0'].acosf
acosf.restype = c_float
acosf.argtypes = [c_float]
asinf = _libraries['libpulse.so.0'].asinf
asinf.restype = c_float
asinf.argtypes = [c_float]
asin = _libraries['libpulse.so.0'].asin
asin.restype = c_double
asin.argtypes = [c_double]
asinl = _libraries['libpulse.so.0'].asinl
asinl.restype = c_longdouble
asinl.argtypes = [c_longdouble]
atan = _libraries['libpulse.so.0'].atan
atan.restype = c_double
atan.argtypes = [c_double]
atanf = _libraries['libpulse.so.0'].atanf
atanf.restype = c_float
atanf.argtypes = [c_float]
atanl = _libraries['libpulse.so.0'].atanl
atanl.restype = c_longdouble
atanl.argtypes = [c_longdouble]
atan2 = _libraries['libpulse.so.0'].atan2
atan2.restype = c_double
atan2.argtypes = [c_double, c_double]
atan2f = _libraries['libpulse.so.0'].atan2f
atan2f.restype = c_float
atan2f.argtypes = [c_float, c_float]
atan2l = _libraries['libpulse.so.0'].atan2l
atan2l.restype = c_longdouble
atan2l.argtypes = [c_longdouble, c_longdouble]
cosl = _libraries['libpulse.so.0'].cosl
cosl.restype = c_longdouble
cosl.argtypes = [c_longdouble]
cos = _libraries['libpulse.so.0'].cos
cos.restype = c_double
cos.argtypes = [c_double]
cosf = _libraries['libpulse.so.0'].cosf
cosf.restype = c_float
cosf.argtypes = [c_float]
sinf = _libraries['libpulse.so.0'].sinf
sinf.restype = c_float
sinf.argtypes = [c_float]
sin = _libraries['libpulse.so.0'].sin
sin.restype = c_double
sin.argtypes = [c_double]
sinl = _libraries['libpulse.so.0'].sinl
sinl.restype = c_longdouble
sinl.argtypes = [c_longdouble]
tan = _libraries['libpulse.so.0'].tan
tan.restype = c_double
tan.argtypes = [c_double]
tanf = _libraries['libpulse.so.0'].tanf
tanf.restype = c_float
tanf.argtypes = [c_float]
tanl = _libraries['libpulse.so.0'].tanl
tanl.restype = c_longdouble
tanl.argtypes = [c_longdouble]
coshf = _libraries['libpulse.so.0'].coshf
coshf.restype = c_float
coshf.argtypes = [c_float]
cosh = _libraries['libpulse.so.0'].cosh
cosh.restype = c_double
cosh.argtypes = [c_double]
coshl = _libraries['libpulse.so.0'].coshl
coshl.restype = c_longdouble
coshl.argtypes = [c_longdouble]
sinhf = _libraries['libpulse.so.0'].sinhf
sinhf.restype = c_float
sinhf.argtypes = [c_float]
sinhl = _libraries['libpulse.so.0'].sinhl
sinhl.restype = c_longdouble
sinhl.argtypes = [c_longdouble]
sinh = _libraries['libpulse.so.0'].sinh
sinh.restype = c_double
sinh.argtypes = [c_double]
tanhf = _libraries['libpulse.so.0'].tanhf
tanhf.restype = c_float
tanhf.argtypes = [c_float]
tanhl = _libraries['libpulse.so.0'].tanhl
tanhl.restype = c_longdouble
tanhl.argtypes = [c_longdouble]
tanh = _libraries['libpulse.so.0'].tanh
tanh.restype = c_double
tanh.argtypes = [c_double]
sincosf = _libraries['libpulse.so.0'].sincosf
sincosf.restype = None
sincosf.argtypes = [c_float, POINTER(c_float), POINTER(c_float)]
sincosl = _libraries['libpulse.so.0'].sincosl
sincosl.restype = None
sincosl.argtypes = [c_longdouble, POINTER(c_longdouble), POINTER(c_longdouble)]
sincos = _libraries['libpulse.so.0'].sincos
sincos.restype = None
sincos.argtypes = [c_double, POINTER(c_double), POINTER(c_double)]
acoshl = _libraries['libpulse.so.0'].acoshl
acoshl.restype = c_longdouble
acoshl.argtypes = [c_longdouble]
acoshf = _libraries['libpulse.so.0'].acoshf
acoshf.restype = c_float
acoshf.argtypes = [c_float]
acosh = _libraries['libpulse.so.0'].acosh
acosh.restype = c_double
acosh.argtypes = [c_double]
asinh = _libraries['libpulse.so.0'].asinh
asinh.restype = c_double
asinh.argtypes = [c_double]
asinhl = _libraries['libpulse.so.0'].asinhl
asinhl.restype = c_longdouble
asinhl.argtypes = [c_longdouble]
asinhf = _libraries['libpulse.so.0'].asinhf
asinhf.restype = c_float
asinhf.argtypes = [c_float]
atanhl = _libraries['libpulse.so.0'].atanhl
atanhl.restype = c_longdouble
atanhl.argtypes = [c_longdouble]
atanhf = _libraries['libpulse.so.0'].atanhf
atanhf.restype = c_float
atanhf.argtypes = [c_float]
atanh = _libraries['libpulse.so.0'].atanh
atanh.restype = c_double
atanh.argtypes = [c_double]
exp = _libraries['libpulse.so.0'].exp
exp.restype = c_double
exp.argtypes = [c_double]
__expl = _libraries['libpulse.so.0'].__expl
__expl.restype = c_longdouble
__expl.argtypes = [c_longdouble]
expl = _libraries['libpulse.so.0'].expl
expl.restype = c_longdouble
expl.argtypes = [c_longdouble]
expf = _libraries['libpulse.so.0'].expf
expf.restype = c_float
expf.argtypes = [c_float]
frexpf = _libraries['libpulse.so.0'].frexpf
frexpf.restype = c_float
frexpf.argtypes = [c_float, POINTER(c_int)]
frexpl = _libraries['libpulse.so.0'].frexpl
frexpl.restype = c_longdouble
frexpl.argtypes = [c_longdouble, POINTER(c_int)]
frexp = _libraries['libpulse.so.0'].frexp
frexp.restype = c_double
frexp.argtypes = [c_double, POINTER(c_int)]
ldexp = _libraries['libpulse.so.0'].ldexp
ldexp.restype = c_double
ldexp.argtypes = [c_double, c_int]
ldexpf = _libraries['libpulse.so.0'].ldexpf
ldexpf.restype = c_float
ldexpf.argtypes = [c_float, c_int]
ldexpl = _libraries['libpulse.so.0'].ldexpl
ldexpl.restype = c_longdouble
ldexpl.argtypes = [c_longdouble, c_int]
logl = _libraries['libpulse.so.0'].logl
logl.restype = c_longdouble
logl.argtypes = [c_longdouble]
logf = _libraries['libpulse.so.0'].logf
logf.restype = c_float
logf.argtypes = [c_float]
log = _libraries['libpulse.so.0'].log
log.restype = c_double
log.argtypes = [c_double]
log10 = _libraries['libpulse.so.0'].log10
log10.restype = c_double
log10.argtypes = [c_double]
log10f = _libraries['libpulse.so.0'].log10f
log10f.restype = c_float
log10f.argtypes = [c_float]
log10l = _libraries['libpulse.so.0'].log10l
log10l.restype = c_longdouble
log10l.argtypes = [c_longdouble]
modff = _libraries['libpulse.so.0'].modff
modff.restype = c_float
modff.argtypes = [c_float, POINTER(c_float)]
modf = _libraries['libpulse.so.0'].modf
modf.restype = c_double
modf.argtypes = [c_double, POINTER(c_double)]
modfl = _libraries['libpulse.so.0'].modfl
modfl.restype = c_longdouble
modfl.argtypes = [c_longdouble, POINTER(c_longdouble)]
exp10f = _libraries['libpulse.so.0'].exp10f
exp10f.restype = c_float
exp10f.argtypes = [c_float]
exp10l = _libraries['libpulse.so.0'].exp10l
exp10l.restype = c_longdouble
exp10l.argtypes = [c_longdouble]
exp10 = _libraries['libpulse.so.0'].exp10
exp10.restype = c_double
exp10.argtypes = [c_double]
pow10 = _libraries['libpulse.so.0'].pow10
pow10.restype = c_double
pow10.argtypes = [c_double]
pow10f = _libraries['libpulse.so.0'].pow10f
pow10f.restype = c_float
pow10f.argtypes = [c_float]
pow10l = _libraries['libpulse.so.0'].pow10l
pow10l.restype = c_longdouble
pow10l.argtypes = [c_longdouble]
expm1f = _libraries['libpulse.so.0'].expm1f
expm1f.restype = c_float
expm1f.argtypes = [c_float]
expm1l = _libraries['libpulse.so.0'].expm1l
expm1l.restype = c_longdouble
expm1l.argtypes = [c_longdouble]
expm1 = _libraries['libpulse.so.0'].expm1
expm1.restype = c_double
expm1.argtypes = [c_double]
__expm1l = _libraries['libpulse.so.0'].__expm1l
__expm1l.restype = c_longdouble
__expm1l.argtypes = [c_longdouble]
log1p = _libraries['libpulse.so.0'].log1p
log1p.restype = c_double
log1p.argtypes = [c_double]
log1pl = _libraries['libpulse.so.0'].log1pl
log1pl.restype = c_longdouble
log1pl.argtypes = [c_longdouble]
log1pf = _libraries['libpulse.so.0'].log1pf
log1pf.restype = c_float
log1pf.argtypes = [c_float]
logb = _libraries['libpulse.so.0'].logb
logb.restype = c_double
logb.argtypes = [c_double]
logbf = _libraries['libpulse.so.0'].logbf
logbf.restype = c_float
logbf.argtypes = [c_float]
logbl = _libraries['libpulse.so.0'].logbl
logbl.restype = c_longdouble
logbl.argtypes = [c_longdouble]
exp2 = _libraries['libpulse.so.0'].exp2
exp2.restype = c_double
exp2.argtypes = [c_double]
exp2f = _libraries['libpulse.so.0'].exp2f
exp2f.restype = c_float
exp2f.argtypes = [c_float]
exp2l = _libraries['libpulse.so.0'].exp2l
exp2l.restype = c_longdouble
exp2l.argtypes = [c_longdouble]
log2 = _libraries['libpulse.so.0'].log2
log2.restype = c_double
log2.argtypes = [c_double]
log2f = _libraries['libpulse.so.0'].log2f
log2f.restype = c_float
log2f.argtypes = [c_float]
log2l = _libraries['libpulse.so.0'].log2l
log2l.restype = c_longdouble
log2l.argtypes = [c_longdouble]
pow = _libraries['libpulse.so.0'].pow
pow.restype = c_double
pow.argtypes = [c_double, c_double]
powl = _libraries['libpulse.so.0'].powl
powl.restype = c_longdouble
powl.argtypes = [c_longdouble, c_longdouble]
powf = _libraries['libpulse.so.0'].powf
powf.restype = c_float
powf.argtypes = [c_float, c_float]
sqrtf = _libraries['libpulse.so.0'].sqrtf
sqrtf.restype = c_float
sqrtf.argtypes = [c_float]
sqrt = _libraries['libpulse.so.0'].sqrt
sqrt.restype = c_double
sqrt.argtypes = [c_double]
sqrtl = _libraries['libpulse.so.0'].sqrtl
sqrtl.restype = c_longdouble
sqrtl.argtypes = [c_longdouble]
hypotl = _libraries['libpulse.so.0'].hypotl
hypotl.restype = c_longdouble
hypotl.argtypes = [c_longdouble, c_longdouble]
hypotf = _libraries['libpulse.so.0'].hypotf
hypotf.restype = c_float
hypotf.argtypes = [c_float, c_float]
hypot = _libraries['libpulse.so.0'].hypot
hypot.restype = c_double
hypot.argtypes = [c_double, c_double]
cbrtl = _libraries['libpulse.so.0'].cbrtl
cbrtl.restype = c_longdouble
cbrtl.argtypes = [c_longdouble]
cbrt = _libraries['libpulse.so.0'].cbrt
cbrt.restype = c_double
cbrt.argtypes = [c_double]
cbrtf = _libraries['libpulse.so.0'].cbrtf
cbrtf.restype = c_float
cbrtf.argtypes = [c_float]
ceilf = _libraries['libpulse.so.0'].ceilf
ceilf.restype = c_float
ceilf.argtypes = [c_float]
ceill = _libraries['libpulse.so.0'].ceill
ceill.restype = c_longdouble
ceill.argtypes = [c_longdouble]
ceil = _libraries['libpulse.so.0'].ceil
ceil.restype = c_double
ceil.argtypes = [c_double]
fabs = _libraries['libpulse.so.0'].fabs
fabs.restype = c_double
fabs.argtypes = [c_double]
fabsl = _libraries['libpulse.so.0'].fabsl
fabsl.restype = c_longdouble
fabsl.argtypes = [c_longdouble]
fabsf = _libraries['libpulse.so.0'].fabsf
fabsf.restype = c_float
fabsf.argtypes = [c_float]
floor = _libraries['libpulse.so.0'].floor
floor.restype = c_double
floor.argtypes = [c_double]
floorf = _libraries['libpulse.so.0'].floorf
floorf.restype = c_float
floorf.argtypes = [c_float]
floorl = _libraries['libpulse.so.0'].floorl
floorl.restype = c_longdouble
floorl.argtypes = [c_longdouble]
fmodl = _libraries['libpulse.so.0'].fmodl
fmodl.restype = c_longdouble
fmodl.argtypes = [c_longdouble, c_longdouble]
fmodf = _libraries['libpulse.so.0'].fmodf
fmodf.restype = c_float
fmodf.argtypes = [c_float, c_float]
fmod = _libraries['libpulse.so.0'].fmod
fmod.restype = c_double
fmod.argtypes = [c_double, c_double]
__isinf = _libraries['libpulse.so.0'].__isinf
__isinf.restype = c_int
__isinf.argtypes = [c_double]
__isinff = _libraries['libpulse.so.0'].__isinff
__isinff.restype = c_int
__isinff.argtypes = [c_float]
__isinfl = _libraries['libpulse.so.0'].__isinfl
__isinfl.restype = c_int
__isinfl.argtypes = [c_longdouble]
__finitef = _libraries['libpulse.so.0'].__finitef
__finitef.restype = c_int
__finitef.argtypes = [c_float]
__finite = _libraries['libpulse.so.0'].__finite
__finite.restype = c_int
__finite.argtypes = [c_double]
__finitel = _libraries['libpulse.so.0'].__finitel
__finitel.restype = c_int
__finitel.argtypes = [c_longdouble]
isinf = _libraries['libpulse.so.0'].isinf
isinf.restype = c_int
isinf.argtypes = [c_double]
isinff = _libraries['libpulse.so.0'].isinff
isinff.restype = c_int
isinff.argtypes = [c_float]
isinfl = _libraries['libpulse.so.0'].isinfl
isinfl.restype = c_int
isinfl.argtypes = [c_longdouble]
finitef = _libraries['libpulse.so.0'].finitef
finitef.restype = c_int
finitef.argtypes = [c_float]
finitel = _libraries['libpulse.so.0'].finitel
finitel.restype = c_int
finitel.argtypes = [c_longdouble]
finite = _libraries['libpulse.so.0'].finite
finite.restype = c_int
finite.argtypes = [c_double]
dremf = _libraries['libpulse.so.0'].dremf
dremf.restype = c_float
dremf.argtypes = [c_float, c_float]
dreml = _libraries['libpulse.so.0'].dreml
dreml.restype = c_longdouble
dreml.argtypes = [c_longdouble, c_longdouble]
drem = _libraries['libpulse.so.0'].drem
drem.restype = c_double
drem.argtypes = [c_double, c_double]
significandf = _libraries['libpulse.so.0'].significandf
significandf.restype = c_float
significandf.argtypes = [c_float]
significandl = _libraries['libpulse.so.0'].significandl
significandl.restype = c_longdouble
significandl.argtypes = [c_longdouble]
significand = _libraries['libpulse.so.0'].significand
significand.restype = c_double
significand.argtypes = [c_double]
copysign = _libraries['libpulse.so.0'].copysign
copysign.restype = c_double
copysign.argtypes = [c_double, c_double]
copysignf = _libraries['libpulse.so.0'].copysignf
copysignf.restype = c_float
copysignf.argtypes = [c_float, c_float]
copysignl = _libraries['libpulse.so.0'].copysignl
copysignl.restype = c_longdouble
copysignl.argtypes = [c_longdouble, c_longdouble]
nanf = _libraries['libpulse.so.0'].nanf
nanf.restype = c_float
nanf.argtypes = [STRING]
nanl = _libraries['libpulse.so.0'].nanl
nanl.restype = c_longdouble
nanl.argtypes = [STRING]
nan = _libraries['libpulse.so.0'].nan
nan.restype = c_double
nan.argtypes = [STRING]
__isnanf = _libraries['libpulse.so.0'].__isnanf
__isnanf.restype = c_int
__isnanf.argtypes = [c_float]
__isnanl = _libraries['libpulse.so.0'].__isnanl
__isnanl.restype = c_int
__isnanl.argtypes = [c_longdouble]
__isnan = _libraries['libpulse.so.0'].__isnan
__isnan.restype = c_int
__isnan.argtypes = [c_double]
isnanf = _libraries['libpulse.so.0'].isnanf
isnanf.restype = c_int
isnanf.argtypes = [c_float]
isnanl = _libraries['libpulse.so.0'].isnanl
isnanl.restype = c_int
isnanl.argtypes = [c_longdouble]
isnan = _libraries['libpulse.so.0'].isnan
isnan.restype = c_int
isnan.argtypes = [c_double]
j0l = _libraries['libpulse.so.0'].j0l
j0l.restype = c_longdouble
j0l.argtypes = [c_longdouble]
j0f = _libraries['libpulse.so.0'].j0f
j0f.restype = c_float
j0f.argtypes = [c_float]
j0 = _libraries['libpulse.so.0'].j0
j0.restype = c_double
j0.argtypes = [c_double]
j1 = _libraries['libpulse.so.0'].j1
j1.restype = c_double
j1.argtypes = [c_double]
j1l = _libraries['libpulse.so.0'].j1l
j1l.restype = c_longdouble
j1l.argtypes = [c_longdouble]
j1f = _libraries['libpulse.so.0'].j1f
j1f.restype = c_float
j1f.argtypes = [c_float]
jnf = _libraries['libpulse.so.0'].jnf
jnf.restype = c_float
jnf.argtypes = [c_int, c_float]
jn = _libraries['libpulse.so.0'].jn
jn.restype = c_double
jn.argtypes = [c_int, c_double]
jnl = _libraries['libpulse.so.0'].jnl
jnl.restype = c_longdouble
jnl.argtypes = [c_int, c_longdouble]
y0f = _libraries['libpulse.so.0'].y0f
y0f.restype = c_float
y0f.argtypes = [c_float]
y0l = _libraries['libpulse.so.0'].y0l
y0l.restype = c_longdouble
y0l.argtypes = [c_longdouble]
y0 = _libraries['libpulse.so.0'].y0
y0.restype = c_double
y0.argtypes = [c_double]
y1 = _libraries['libpulse.so.0'].y1
y1.restype = c_double
y1.argtypes = [c_double]
y1f = _libraries['libpulse.so.0'].y1f
y1f.restype = c_float
y1f.argtypes = [c_float]
y1l = _libraries['libpulse.so.0'].y1l
y1l.restype = c_longdouble
y1l.argtypes = [c_longdouble]
ynf = _libraries['libpulse.so.0'].ynf
ynf.restype = c_float
ynf.argtypes = [c_int, c_float]
ynl = _libraries['libpulse.so.0'].ynl
ynl.restype = c_longdouble
ynl.argtypes = [c_int, c_longdouble]
yn = _libraries['libpulse.so.0'].yn
yn.restype = c_double
yn.argtypes = [c_int, c_double]
erfl = _libraries['libpulse.so.0'].erfl
erfl.restype = c_longdouble
erfl.argtypes = [c_longdouble]
erf = _libraries['libpulse.so.0'].erf
erf.restype = c_double
erf.argtypes = [c_double]
erff = _libraries['libpulse.so.0'].erff
erff.restype = c_float
erff.argtypes = [c_float]
erfc = _libraries['libpulse.so.0'].erfc
erfc.restype = c_double
erfc.argtypes = [c_double]
erfcl = _libraries['libpulse.so.0'].erfcl
erfcl.restype = c_longdouble
erfcl.argtypes = [c_longdouble]
erfcf = _libraries['libpulse.so.0'].erfcf
erfcf.restype = c_float
erfcf.argtypes = [c_float]
lgamma = _libraries['libpulse.so.0'].lgamma
lgamma.restype = c_double
lgamma.argtypes = [c_double]
lgammaf = _libraries['libpulse.so.0'].lgammaf
lgammaf.restype = c_float
lgammaf.argtypes = [c_float]
lgammal = _libraries['libpulse.so.0'].lgammal
lgammal.restype = c_longdouble
lgammal.argtypes = [c_longdouble]
tgamma = _libraries['libpulse.so.0'].tgamma
tgamma.restype = c_double
tgamma.argtypes = [c_double]
tgammaf = _libraries['libpulse.so.0'].tgammaf
tgammaf.restype = c_float
tgammaf.argtypes = [c_float]
tgammal = _libraries['libpulse.so.0'].tgammal
tgammal.restype = c_longdouble
tgammal.argtypes = [c_longdouble]
gammaf = _libraries['libpulse.so.0'].gammaf
gammaf.restype = c_float
gammaf.argtypes = [c_float]
gammal = _libraries['libpulse.so.0'].gammal
gammal.restype = c_longdouble
gammal.argtypes = [c_longdouble]
gamma = _libraries['libpulse.so.0'].gamma
gamma.restype = c_double
gamma.argtypes = [c_double]
lgamma_r = _libraries['libpulse.so.0'].lgamma_r
lgamma_r.restype = c_double
lgamma_r.argtypes = [c_double, POINTER(c_int)]
lgammal_r = _libraries['libpulse.so.0'].lgammal_r
lgammal_r.restype = c_longdouble
lgammal_r.argtypes = [c_longdouble, POINTER(c_int)]
lgammaf_r = _libraries['libpulse.so.0'].lgammaf_r
lgammaf_r.restype = c_float
lgammaf_r.argtypes = [c_float, POINTER(c_int)]
rintf = _libraries['libpulse.so.0'].rintf
rintf.restype = c_float
rintf.argtypes = [c_float]
rintl = _libraries['libpulse.so.0'].rintl
rintl.restype = c_longdouble
rintl.argtypes = [c_longdouble]
rint = _libraries['libpulse.so.0'].rint
rint.restype = c_double
rint.argtypes = [c_double]
nextafterf = _libraries['libpulse.so.0'].nextafterf
nextafterf.restype = c_float
nextafterf.argtypes = [c_float, c_float]
nextafter = _libraries['libpulse.so.0'].nextafter
nextafter.restype = c_double
nextafter.argtypes = [c_double, c_double]
nextafterl = _libraries['libpulse.so.0'].nextafterl
nextafterl.restype = c_longdouble
nextafterl.argtypes = [c_longdouble, c_longdouble]
nexttowardf = _libraries['libpulse.so.0'].nexttowardf
nexttowardf.restype = c_float
nexttowardf.argtypes = [c_float, c_longdouble]
nexttoward = _libraries['libpulse.so.0'].nexttoward
nexttoward.restype = c_double
nexttoward.argtypes = [c_double, c_longdouble]
nexttowardl = _libraries['libpulse.so.0'].nexttowardl
nexttowardl.restype = c_longdouble
nexttowardl.argtypes = [c_longdouble, c_longdouble]
remainder = _libraries['libpulse.so.0'].remainder
remainder.restype = c_double
remainder.argtypes = [c_double, c_double]
remainderf = _libraries['libpulse.so.0'].remainderf
remainderf.restype = c_float
remainderf.argtypes = [c_float, c_float]
remainderl = _libraries['libpulse.so.0'].remainderl
remainderl.restype = c_longdouble
remainderl.argtypes = [c_longdouble, c_longdouble]
scalbnf = _libraries['libpulse.so.0'].scalbnf
scalbnf.restype = c_float
scalbnf.argtypes = [c_float, c_int]
scalbnl = _libraries['libpulse.so.0'].scalbnl
scalbnl.restype = c_longdouble
scalbnl.argtypes = [c_longdouble, c_int]
scalbn = _libraries['libpulse.so.0'].scalbn
scalbn.restype = c_double
scalbn.argtypes = [c_double, c_int]
ilogbf = _libraries['libpulse.so.0'].ilogbf
ilogbf.restype = c_int
ilogbf.argtypes = [c_float]
ilogb = _libraries['libpulse.so.0'].ilogb
ilogb.restype = c_int
ilogb.argtypes = [c_double]
ilogbl = _libraries['libpulse.so.0'].ilogbl
ilogbl.restype = c_int
ilogbl.argtypes = [c_longdouble]
scalblnl = _libraries['libpulse.so.0'].scalblnl
scalblnl.restype = c_longdouble
scalblnl.argtypes = [c_longdouble, c_long]
scalbln = _libraries['libpulse.so.0'].scalbln
scalbln.restype = c_double
scalbln.argtypes = [c_double, c_long]
scalblnf = _libraries['libpulse.so.0'].scalblnf
scalblnf.restype = c_float
scalblnf.argtypes = [c_float, c_long]
nearbyint = _libraries['libpulse.so.0'].nearbyint
nearbyint.restype = c_double
nearbyint.argtypes = [c_double]
nearbyintf = _libraries['libpulse.so.0'].nearbyintf
nearbyintf.restype = c_float
nearbyintf.argtypes = [c_float]
nearbyintl = _libraries['libpulse.so.0'].nearbyintl
nearbyintl.restype = c_longdouble
nearbyintl.argtypes = [c_longdouble]
round = _libraries['libpulse.so.0'].round
round.restype = c_double
round.argtypes = [c_double]
roundf = _libraries['libpulse.so.0'].roundf
roundf.restype = c_float
roundf.argtypes = [c_float]
roundl = _libraries['libpulse.so.0'].roundl
roundl.restype = c_longdouble
roundl.argtypes = [c_longdouble]
truncf = _libraries['libpulse.so.0'].truncf
truncf.restype = c_float
truncf.argtypes = [c_float]
truncl = _libraries['libpulse.so.0'].truncl
truncl.restype = c_longdouble
truncl.argtypes = [c_longdouble]
trunc = _libraries['libpulse.so.0'].trunc
trunc.restype = c_double
trunc.argtypes = [c_double]
remquo = _libraries['libpulse.so.0'].remquo
remquo.restype = c_double
remquo.argtypes = [c_double, c_double, POINTER(c_int)]
remquof = _libraries['libpulse.so.0'].remquof
remquof.restype = c_float
remquof.argtypes = [c_float, c_float, POINTER(c_int)]
remquol = _libraries['libpulse.so.0'].remquol
remquol.restype = c_longdouble
remquol.argtypes = [c_longdouble, c_longdouble, POINTER(c_int)]
lrint = _libraries['libpulse.so.0'].lrint
lrint.restype = c_long
lrint.argtypes = [c_double]
lrintf = _libraries['libpulse.so.0'].lrintf
lrintf.restype = c_long
lrintf.argtypes = [c_float]
lrintl = _libraries['libpulse.so.0'].lrintl
lrintl.restype = c_long
lrintl.argtypes = [c_longdouble]
llrintf = _libraries['libpulse.so.0'].llrintf
llrintf.restype = c_longlong
llrintf.argtypes = [c_float]
llrintl = _libraries['libpulse.so.0'].llrintl
llrintl.restype = c_longlong
llrintl.argtypes = [c_longdouble]
llrint = _libraries['libpulse.so.0'].llrint
llrint.restype = c_longlong
llrint.argtypes = [c_double]
lround = _libraries['libpulse.so.0'].lround
lround.restype = c_long
lround.argtypes = [c_double]
lroundf = _libraries['libpulse.so.0'].lroundf
lroundf.restype = c_long
lroundf.argtypes = [c_float]
lroundl = _libraries['libpulse.so.0'].lroundl
lroundl.restype = c_long
lroundl.argtypes = [c_longdouble]
llroundf = _libraries['libpulse.so.0'].llroundf
llroundf.restype = c_longlong
llroundf.argtypes = [c_float]
llroundl = _libraries['libpulse.so.0'].llroundl
llroundl.restype = c_longlong
llroundl.argtypes = [c_longdouble]
llround = _libraries['libpulse.so.0'].llround
llround.restype = c_longlong
llround.argtypes = [c_double]
fdiml = _libraries['libpulse.so.0'].fdiml
fdiml.restype = c_longdouble
fdiml.argtypes = [c_longdouble, c_longdouble]
fdimf = _libraries['libpulse.so.0'].fdimf
fdimf.restype = c_float
fdimf.argtypes = [c_float, c_float]
fdim = _libraries['libpulse.so.0'].fdim
fdim.restype = c_double
fdim.argtypes = [c_double, c_double]
fmax = _libraries['libpulse.so.0'].fmax
fmax.restype = c_double
fmax.argtypes = [c_double, c_double]
fmaxf = _libraries['libpulse.so.0'].fmaxf
fmaxf.restype = c_float
fmaxf.argtypes = [c_float, c_float]
fmaxl = _libraries['libpulse.so.0'].fmaxl
fmaxl.restype = c_longdouble
fmaxl.argtypes = [c_longdouble, c_longdouble]
fminf = _libraries['libpulse.so.0'].fminf
fminf.restype = c_float
fminf.argtypes = [c_float, c_float]
fminl = _libraries['libpulse.so.0'].fminl
fminl.restype = c_longdouble
fminl.argtypes = [c_longdouble, c_longdouble]
fmin = _libraries['libpulse.so.0'].fmin
fmin.restype = c_double
fmin.argtypes = [c_double, c_double]
__fpclassify = _libraries['libpulse.so.0'].__fpclassify
__fpclassify.restype = c_int
__fpclassify.argtypes = [c_double]
__fpclassifyf = _libraries['libpulse.so.0'].__fpclassifyf
__fpclassifyf.restype = c_int
__fpclassifyf.argtypes = [c_float]
__fpclassifyl = _libraries['libpulse.so.0'].__fpclassifyl
__fpclassifyl.restype = c_int
__fpclassifyl.argtypes = [c_longdouble]
__signbitl = _libraries['libpulse.so.0'].__signbitl
__signbitl.restype = c_int
__signbitl.argtypes = [c_longdouble]
__signbit = _libraries['libpulse.so.0'].__signbit
__signbit.restype = c_int
__signbit.argtypes = [c_double]
__signbitf = _libraries['libpulse.so.0'].__signbitf
__signbitf.restype = c_int
__signbitf.argtypes = [c_float]
fma = _libraries['libpulse.so.0'].fma
fma.restype = c_double
fma.argtypes = [c_double, c_double, c_double]
fmal = _libraries['libpulse.so.0'].fmal
fmal.restype = c_longdouble
fmal.argtypes = [c_longdouble, c_longdouble, c_longdouble]
fmaf = _libraries['libpulse.so.0'].fmaf
fmaf.restype = c_float
fmaf.argtypes = [c_float, c_float, c_float]
scalb = _libraries['libpulse.so.0'].scalb
scalb.restype = c_double
scalb.argtypes = [c_double, c_double]
scalbf = _libraries['libpulse.so.0'].scalbf
scalbf.restype = c_float
scalbf.argtypes = [c_float, c_float]
scalbl = _libraries['libpulse.so.0'].scalbl
scalbl.restype = c_longdouble
scalbl.argtypes = [c_longdouble, c_longdouble]
float_t = c_longdouble
double_t = c_longdouble
pthread_t = c_ulong
class __pthread_internal_slist(Structure):
    pass
__pthread_internal_slist._fields_ = [
    ('__next', POINTER(__pthread_internal_slist)),
]
__pthread_slist_t = __pthread_internal_slist
class __pthread_mutex_s(Structure):
    pass
class N15pthread_mutex_t17__pthread_mutex_s3DOT_6E(Union):
    pass
N15pthread_mutex_t17__pthread_mutex_s3DOT_6E._fields_ = [
    ('__spins', c_int),
    ('__list', __pthread_slist_t),
]
__pthread_mutex_s._anonymous_ = ['_0']
__pthread_mutex_s._fields_ = [
    ('__lock', c_int),
    ('__count', c_uint),
    ('__owner', c_int),
    ('__kind', c_int),
    ('__nusers', c_uint),
    ('_0', N15pthread_mutex_t17__pthread_mutex_s3DOT_6E),
]
class N14pthread_cond_t3DOT_9E(Structure):
    pass
N14pthread_cond_t3DOT_9E._pack_ = 4
N14pthread_cond_t3DOT_9E._fields_ = [
    ('__lock', c_int),
    ('__futex', c_uint),
    ('__total_seq', c_ulonglong),
    ('__wakeup_seq', c_ulonglong),
    ('__woken_seq', c_ulonglong),
    ('__mutex', c_void_p),
    ('__nwaiters', c_uint),
    ('__broadcast_seq', c_uint),
]
pthread_key_t = c_uint
pthread_once_t = c_int
class N16pthread_rwlock_t4DOT_12E(Structure):
    pass
N16pthread_rwlock_t4DOT_12E._fields_ = [
    ('__lock', c_int),
    ('__nr_readers', c_uint),
    ('__readers_wakeup', c_uint),
    ('__writer_wakeup', c_uint),
    ('__nr_readers_queued', c_uint),
    ('__nr_writers_queued', c_uint),
    ('__flags', c_ubyte),
    ('__shared', c_ubyte),
    ('__pad1', c_ubyte),
    ('__pad2', c_ubyte),
    ('__writer', c_int),
]
pthread_spinlock_t = c_int
__sig_atomic_t = c_int
class __sigset_t(Structure):
    pass
__sigset_t._fields_ = [
    ('__val', c_ulong * 32),
]
__u_char = c_ubyte
__u_short = c_ushort
__u_int = c_uint
__u_long = c_ulong
__int8_t = c_byte
__uint8_t = c_ubyte
__int16_t = c_short
__uint16_t = c_ushort
__int32_t = c_int
__uint32_t = c_uint
__int64_t = c_longlong
__uint64_t = c_ulonglong
__quad_t = c_longlong
__u_quad_t = c_ulonglong
__dev_t = __u_quad_t
__uid_t = c_uint
__gid_t = c_uint
__ino_t = c_ulong
__ino64_t = __u_quad_t
__mode_t = c_uint
__nlink_t = c_uint
__off_t = c_long
__off64_t = __quad_t
__pid_t = c_int
class __fsid_t(Structure):
    pass
__fsid_t._fields_ = [
    ('__val', c_int * 2),
]
__clock_t = c_long
__rlim_t = c_ulong
__rlim64_t = __u_quad_t
__id_t = c_uint
__useconds_t = c_uint
__daddr_t = c_int
__swblk_t = c_long
__key_t = c_int
__clockid_t = c_int
__timer_t = c_void_p
__blksize_t = c_long
__blkcnt_t = c_long
__blkcnt64_t = __quad_t
__fsblkcnt_t = c_ulong
__fsblkcnt64_t = __u_quad_t
__fsfilcnt_t = c_ulong
__fsfilcnt64_t = __u_quad_t
__ssize_t = c_int
__loff_t = __off64_t
__qaddr_t = POINTER(__quad_t)
__caddr_t = STRING
__intptr_t = c_int
__socklen_t = c_uint
class N4wait4DOT_19E(Structure):
    pass
N4wait4DOT_19E._fields_ = [
    ('__w_termsig', c_uint, 7),
    ('__w_coredump', c_uint, 1),
    ('__w_retcode', c_uint, 8),
    ('', c_uint, 16),
]
class N4wait4DOT_20E(Structure):
    pass
N4wait4DOT_20E._fields_ = [
    ('__w_stopval', c_uint, 8),
    ('__w_stopsig', c_uint, 8),
    ('', c_uint, 16),
]
class imaxdiv_t(Structure):
    pass
imaxdiv_t._pack_ = 4
imaxdiv_t._fields_ = [
    ('quot', c_longlong),
    ('rem', c_longlong),
]
intmax_t = c_longlong
imaxabs = _libraries['libpulse.so.0'].imaxabs
imaxabs.restype = intmax_t
imaxabs.argtypes = [intmax_t]
imaxdiv = _libraries['libpulse.so.0'].imaxdiv
imaxdiv.restype = imaxdiv_t
imaxdiv.argtypes = [intmax_t, intmax_t]
strtoimax = _libraries['libpulse.so.0'].strtoimax
strtoimax.restype = intmax_t
strtoimax.argtypes = [STRING, POINTER(STRING), c_int]
uintmax_t = c_ulonglong
strtoumax = _libraries['libpulse.so.0'].strtoumax
strtoumax.restype = uintmax_t
strtoumax.argtypes = [STRING, POINTER(STRING), c_int]
wcstoimax = _libraries['libpulse.so.0'].wcstoimax
wcstoimax.restype = intmax_t
wcstoimax.argtypes = [WSTRING, POINTER(WSTRING), c_int]
wcstoumax = _libraries['libpulse.so.0'].wcstoumax
wcstoumax.restype = uintmax_t
wcstoumax.argtypes = [WSTRING, POINTER(WSTRING), c_int]

# values for unnamed enumeration

# values for enumeration '_LIB_VERSION_TYPE'
_LIB_VERSION_TYPE = c_int # enum
class __exception(Structure):
    pass
__exception._pack_ = 4
__exception._fields_ = [
    ('type', c_int),
    ('name', STRING),
    ('arg1', c_double),
    ('arg2', c_double),
    ('retval', c_double),
]
matherr = _libraries['libpulse.so.0'].matherr
matherr.restype = c_int
matherr.argtypes = [POINTER(__exception)]
int8_t = c_int8
int16_t = c_int16
int32_t = c_int32
uint16_t = c_uint16
int_least8_t = c_byte
int_least16_t = c_short
int_least32_t = c_int
int_least64_t = c_longlong
uint_least8_t = c_ubyte
uint_least16_t = c_ushort
uint_least32_t = c_uint
uint_least64_t = c_ulonglong
int_fast8_t = c_byte
int_fast16_t = c_int
int_fast32_t = c_int
int_fast64_t = c_longlong
uint_fast8_t = c_ubyte
uint_fast16_t = c_uint
uint_fast32_t = c_uint
uint_fast64_t = c_ulonglong
intptr_t = c_int
uintptr_t = c_uint
class div_t(Structure):
    pass
div_t._fields_ = [
    ('quot', c_int),
    ('rem', c_int),
]
class ldiv_t(Structure):
    pass
ldiv_t._fields_ = [
    ('quot', c_long),
    ('rem', c_long),
]
class lldiv_t(Structure):
    pass
lldiv_t._pack_ = 4
lldiv_t._fields_ = [
    ('quot', c_longlong),
    ('rem', c_longlong),
]
__ctype_get_mb_cur_max = _libraries['libpulse.so.0'].__ctype_get_mb_cur_max
__ctype_get_mb_cur_max.restype = size_t
__ctype_get_mb_cur_max.argtypes = []
atof = _libraries['libpulse.so.0'].atof
atof.restype = c_double
atof.argtypes = [STRING]
atoi = _libraries['libpulse.so.0'].atoi
atoi.restype = c_int
atoi.argtypes = [STRING]
atol = _libraries['libpulse.so.0'].atol
atol.restype = c_long
atol.argtypes = [STRING]
atoll = _libraries['libpulse.so.0'].atoll
atoll.restype = c_longlong
atoll.argtypes = [STRING]
strtod = _libraries['libpulse.so.0'].strtod
strtod.restype = c_double
strtod.argtypes = [STRING, POINTER(STRING)]
strtof = _libraries['libpulse.so.0'].strtof
strtof.restype = c_float
strtof.argtypes = [STRING, POINTER(STRING)]
strtold = _libraries['libpulse.so.0'].strtold
strtold.restype = c_longdouble
strtold.argtypes = [STRING, POINTER(STRING)]
strtol = _libraries['libpulse.so.0'].strtol
strtol.restype = c_long
strtol.argtypes = [STRING, POINTER(STRING), c_int]
strtoul = _libraries['libpulse.so.0'].strtoul
strtoul.restype = c_ulong
strtoul.argtypes = [STRING, POINTER(STRING), c_int]
strtoq = _libraries['libpulse.so.0'].strtoq
strtoq.restype = c_longlong
strtoq.argtypes = [STRING, POINTER(STRING), c_int]
strtouq = _libraries['libpulse.so.0'].strtouq
strtouq.restype = c_ulonglong
strtouq.argtypes = [STRING, POINTER(STRING), c_int]
strtoll = _libraries['libpulse.so.0'].strtoll
strtoll.restype = c_longlong
strtoll.argtypes = [STRING, POINTER(STRING), c_int]
strtoull = _libraries['libpulse.so.0'].strtoull
strtoull.restype = c_ulonglong
strtoull.argtypes = [STRING, POINTER(STRING), c_int]
class __locale_struct(Structure):
    pass
__locale_t = POINTER(__locale_struct)
strtol_l = _libraries['libpulse.so.0'].strtol_l
strtol_l.restype = c_long
strtol_l.argtypes = [STRING, POINTER(STRING), c_int, __locale_t]
strtoul_l = _libraries['libpulse.so.0'].strtoul_l
strtoul_l.restype = c_ulong
strtoul_l.argtypes = [STRING, POINTER(STRING), c_int, __locale_t]
strtoll_l = _libraries['libpulse.so.0'].strtoll_l
strtoll_l.restype = c_longlong
strtoll_l.argtypes = [STRING, POINTER(STRING), c_int, __locale_t]
strtoull_l = _libraries['libpulse.so.0'].strtoull_l
strtoull_l.restype = c_ulonglong
strtoull_l.argtypes = [STRING, POINTER(STRING), c_int, __locale_t]
strtod_l = _libraries['libpulse.so.0'].strtod_l
strtod_l.restype = c_double
strtod_l.argtypes = [STRING, POINTER(STRING), __locale_t]
strtof_l = _libraries['libpulse.so.0'].strtof_l
strtof_l.restype = c_float
strtof_l.argtypes = [STRING, POINTER(STRING), __locale_t]
strtold_l = _libraries['libpulse.so.0'].strtold_l
strtold_l.restype = c_longdouble
strtold_l.argtypes = [STRING, POINTER(STRING), __locale_t]
l64a = _libraries['libpulse.so.0'].l64a
l64a.restype = STRING
l64a.argtypes = [c_long]
a64l = _libraries['libpulse.so.0'].a64l
a64l.restype = c_long
a64l.argtypes = [STRING]
random = _libraries['libpulse.so.0'].random
random.restype = c_long
random.argtypes = []
srandom = _libraries['libpulse.so.0'].srandom
srandom.restype = None
srandom.argtypes = [c_uint]
initstate = _libraries['libpulse.so.0'].initstate
initstate.restype = STRING
initstate.argtypes = [c_uint, STRING, size_t]
setstate = _libraries['libpulse.so.0'].setstate
setstate.restype = STRING
setstate.argtypes = [STRING]
class random_data(Structure):
    pass
random_data._fields_ = [
    ('fptr', POINTER(int32_t)),
    ('rptr', POINTER(int32_t)),
    ('state', POINTER(int32_t)),
    ('rand_type', c_int),
    ('rand_deg', c_int),
    ('rand_sep', c_int),
    ('end_ptr', POINTER(int32_t)),
]
random_r = _libraries['libpulse.so.0'].random_r
random_r.restype = c_int
random_r.argtypes = [POINTER(random_data), POINTER(int32_t)]
srandom_r = _libraries['libpulse.so.0'].srandom_r
srandom_r.restype = c_int
srandom_r.argtypes = [c_uint, POINTER(random_data)]
initstate_r = _libraries['libpulse.so.0'].initstate_r
initstate_r.restype = c_int
initstate_r.argtypes = [c_uint, STRING, size_t, POINTER(random_data)]
setstate_r = _libraries['libpulse.so.0'].setstate_r
setstate_r.restype = c_int
setstate_r.argtypes = [STRING, POINTER(random_data)]
rand = _libraries['libpulse.so.0'].rand
rand.restype = c_int
rand.argtypes = []
srand = _libraries['libpulse.so.0'].srand
srand.restype = None
srand.argtypes = [c_uint]
rand_r = _libraries['libpulse.so.0'].rand_r
rand_r.restype = c_int
rand_r.argtypes = [POINTER(c_uint)]
drand48 = _libraries['libpulse.so.0'].drand48
drand48.restype = c_double
drand48.argtypes = []
erand48 = _libraries['libpulse.so.0'].erand48
erand48.restype = c_double
erand48.argtypes = [POINTER(c_ushort)]
lrand48 = _libraries['libpulse.so.0'].lrand48
lrand48.restype = c_long
lrand48.argtypes = []
nrand48 = _libraries['libpulse.so.0'].nrand48
nrand48.restype = c_long
nrand48.argtypes = [POINTER(c_ushort)]
mrand48 = _libraries['libpulse.so.0'].mrand48
mrand48.restype = c_long
mrand48.argtypes = []
jrand48 = _libraries['libpulse.so.0'].jrand48
jrand48.restype = c_long
jrand48.argtypes = [POINTER(c_ushort)]
srand48 = _libraries['libpulse.so.0'].srand48
srand48.restype = None
srand48.argtypes = [c_long]
seed48 = _libraries['libpulse.so.0'].seed48
seed48.restype = POINTER(c_ushort)
seed48.argtypes = [POINTER(c_ushort)]
lcong48 = _libraries['libpulse.so.0'].lcong48
lcong48.restype = None
lcong48.argtypes = [POINTER(c_ushort)]
class drand48_data(Structure):
    pass
drand48_data._pack_ = 4
drand48_data._fields_ = [
    ('__x', c_ushort * 3),
    ('__old_x', c_ushort * 3),
    ('__c', c_ushort),
    ('__init', c_ushort),
    ('__a', c_ulonglong),
]
drand48_r = _libraries['libpulse.so.0'].drand48_r
drand48_r.restype = c_int
drand48_r.argtypes = [POINTER(drand48_data), POINTER(c_double)]
erand48_r = _libraries['libpulse.so.0'].erand48_r
erand48_r.restype = c_int
erand48_r.argtypes = [POINTER(c_ushort), POINTER(drand48_data), POINTER(c_double)]
lrand48_r = _libraries['libpulse.so.0'].lrand48_r
lrand48_r.restype = c_int
lrand48_r.argtypes = [POINTER(drand48_data), POINTER(c_long)]
nrand48_r = _libraries['libpulse.so.0'].nrand48_r
nrand48_r.restype = c_int
nrand48_r.argtypes = [POINTER(c_ushort), POINTER(drand48_data), POINTER(c_long)]
mrand48_r = _libraries['libpulse.so.0'].mrand48_r
mrand48_r.restype = c_int
mrand48_r.argtypes = [POINTER(drand48_data), POINTER(c_long)]
jrand48_r = _libraries['libpulse.so.0'].jrand48_r
jrand48_r.restype = c_int
jrand48_r.argtypes = [POINTER(c_ushort), POINTER(drand48_data), POINTER(c_long)]
srand48_r = _libraries['libpulse.so.0'].srand48_r
srand48_r.restype = c_int
srand48_r.argtypes = [c_long, POINTER(drand48_data)]
seed48_r = _libraries['libpulse.so.0'].seed48_r
seed48_r.restype = c_int
seed48_r.argtypes = [POINTER(c_ushort), POINTER(drand48_data)]
lcong48_r = _libraries['libpulse.so.0'].lcong48_r
lcong48_r.restype = c_int
lcong48_r.argtypes = [POINTER(c_ushort), POINTER(drand48_data)]
malloc = _libraries['libpulse.so.0'].malloc
malloc.restype = c_void_p
malloc.argtypes = [size_t]
calloc = _libraries['libpulse.so.0'].calloc
calloc.restype = c_void_p
calloc.argtypes = [size_t, size_t]
realloc = _libraries['libpulse.so.0'].realloc
realloc.restype = c_void_p
realloc.argtypes = [c_void_p, size_t]
free = _libraries['libpulse.so.0'].free
free.restype = None
free.argtypes = [c_void_p]
cfree = _libraries['libpulse.so.0'].cfree
cfree.restype = None
cfree.argtypes = [c_void_p]
valloc = _libraries['libpulse.so.0'].valloc
valloc.restype = c_void_p
valloc.argtypes = [size_t]
posix_memalign = _libraries['libpulse.so.0'].posix_memalign
posix_memalign.restype = c_int
posix_memalign.argtypes = [POINTER(c_void_p), size_t, size_t]
abort = _libraries['libpulse.so.0'].abort
abort.restype = None
abort.argtypes = []
on_exit = _libraries['libpulse.so.0'].on_exit
on_exit.restype = c_int
on_exit.argtypes = [CFUNCTYPE(None, c_int, c_void_p), c_void_p]
exit = _libraries['libpulse.so.0'].exit
exit.restype = None
exit.argtypes = [c_int]
quick_exit = _libraries['libpulse.so.0'].quick_exit
quick_exit.restype = None
quick_exit.argtypes = [c_int]
_Exit = _libraries['libpulse.so.0']._Exit
_Exit.restype = None
_Exit.argtypes = [c_int]
getenv = _libraries['libpulse.so.0'].getenv
getenv.restype = STRING
getenv.argtypes = [STRING]
__secure_getenv = _libraries['libpulse.so.0'].__secure_getenv
__secure_getenv.restype = STRING
__secure_getenv.argtypes = [STRING]
putenv = _libraries['libpulse.so.0'].putenv
putenv.restype = c_int
putenv.argtypes = [STRING]
setenv = _libraries['libpulse.so.0'].setenv
setenv.restype = c_int
setenv.argtypes = [STRING, STRING, c_int]
unsetenv = _libraries['libpulse.so.0'].unsetenv
unsetenv.restype = c_int
unsetenv.argtypes = [STRING]
clearenv = _libraries['libpulse.so.0'].clearenv
clearenv.restype = c_int
clearenv.argtypes = []
mktemp = _libraries['libpulse.so.0'].mktemp
mktemp.restype = STRING
mktemp.argtypes = [STRING]
mkstemp = _libraries['libpulse.so.0'].mkstemp
mkstemp.restype = c_int
mkstemp.argtypes = [STRING]
mkstemp64 = _libraries['libpulse.so.0'].mkstemp64
mkstemp64.restype = c_int
mkstemp64.argtypes = [STRING]
mkstemps = _libraries['libpulse.so.0'].mkstemps
mkstemps.restype = c_int
mkstemps.argtypes = [STRING, c_int]
mkstemps64 = _libraries['libpulse.so.0'].mkstemps64
mkstemps64.restype = c_int
mkstemps64.argtypes = [STRING, c_int]
mkdtemp = _libraries['libpulse.so.0'].mkdtemp
mkdtemp.restype = STRING
mkdtemp.argtypes = [STRING]
mkostemp = _libraries['libpulse.so.0'].mkostemp
mkostemp.restype = c_int
mkostemp.argtypes = [STRING, c_int]
mkostemp64 = _libraries['libpulse.so.0'].mkostemp64
mkostemp64.restype = c_int
mkostemp64.argtypes = [STRING, c_int]
mkostemps = _libraries['libpulse.so.0'].mkostemps
mkostemps.restype = c_int
mkostemps.argtypes = [STRING, c_int, c_int]
mkostemps64 = _libraries['libpulse.so.0'].mkostemps64
mkostemps64.restype = c_int
mkostemps64.argtypes = [STRING, c_int, c_int]
system = _libraries['libpulse.so.0'].system
system.restype = c_int
system.argtypes = [STRING]
canonicalize_file_name = _libraries['libpulse.so.0'].canonicalize_file_name
canonicalize_file_name.restype = STRING
canonicalize_file_name.argtypes = [STRING]
realpath = _libraries['libpulse.so.0'].realpath
realpath.restype = STRING
realpath.argtypes = [STRING, STRING]
__compar_fn_t = CFUNCTYPE(c_int, c_void_p, c_void_p)
comparison_fn_t = __compar_fn_t
__compar_d_fn_t = CFUNCTYPE(c_int, c_void_p, c_void_p, c_void_p)
bsearch = _libraries['libpulse.so.0'].bsearch
bsearch.restype = c_void_p
bsearch.argtypes = [c_void_p, c_void_p, size_t, size_t, __compar_fn_t]
qsort = _libraries['libpulse.so.0'].qsort
qsort.restype = None
qsort.argtypes = [c_void_p, size_t, size_t, __compar_fn_t]
qsort_r = _libraries['libpulse.so.0'].qsort_r
qsort_r.restype = None
qsort_r.argtypes = [c_void_p, size_t, size_t, __compar_d_fn_t, c_void_p]
abs = _libraries['libpulse.so.0'].abs
abs.restype = c_int
abs.argtypes = [c_int]
labs = _libraries['libpulse.so.0'].labs
labs.restype = c_long
labs.argtypes = [c_long]
llabs = _libraries['libpulse.so.0'].llabs
llabs.restype = c_longlong
llabs.argtypes = [c_longlong]
div = _libraries['libpulse.so.0'].div
div.restype = div_t
div.argtypes = [c_int, c_int]
ldiv = _libraries['libpulse.so.0'].ldiv
ldiv.restype = ldiv_t
ldiv.argtypes = [c_long, c_long]
lldiv = _libraries['libpulse.so.0'].lldiv
lldiv.restype = lldiv_t
lldiv.argtypes = [c_longlong, c_longlong]
ecvt = _libraries['libpulse.so.0'].ecvt
ecvt.restype = STRING
ecvt.argtypes = [c_double, c_int, POINTER(c_int), POINTER(c_int)]
fcvt = _libraries['libpulse.so.0'].fcvt
fcvt.restype = STRING
fcvt.argtypes = [c_double, c_int, POINTER(c_int), POINTER(c_int)]
gcvt = _libraries['libpulse.so.0'].gcvt
gcvt.restype = STRING
gcvt.argtypes = [c_double, c_int, STRING]
qecvt = _libraries['libpulse.so.0'].qecvt
qecvt.restype = STRING
qecvt.argtypes = [c_longdouble, c_int, POINTER(c_int), POINTER(c_int)]
qfcvt = _libraries['libpulse.so.0'].qfcvt
qfcvt.restype = STRING
qfcvt.argtypes = [c_longdouble, c_int, POINTER(c_int), POINTER(c_int)]
qgcvt = _libraries['libpulse.so.0'].qgcvt
qgcvt.restype = STRING
qgcvt.argtypes = [c_longdouble, c_int, STRING]
ecvt_r = _libraries['libpulse.so.0'].ecvt_r
ecvt_r.restype = c_int
ecvt_r.argtypes = [c_double, c_int, POINTER(c_int), POINTER(c_int), STRING, size_t]
fcvt_r = _libraries['libpulse.so.0'].fcvt_r
fcvt_r.restype = c_int
fcvt_r.argtypes = [c_double, c_int, POINTER(c_int), POINTER(c_int), STRING, size_t]
qecvt_r = _libraries['libpulse.so.0'].qecvt_r
qecvt_r.restype = c_int
qecvt_r.argtypes = [c_longdouble, c_int, POINTER(c_int), POINTER(c_int), STRING, size_t]
qfcvt_r = _libraries['libpulse.so.0'].qfcvt_r
qfcvt_r.restype = c_int
qfcvt_r.argtypes = [c_longdouble, c_int, POINTER(c_int), POINTER(c_int), STRING, size_t]
mblen = _libraries['libpulse.so.0'].mblen
mblen.restype = c_int
mblen.argtypes = [STRING, size_t]
mbtowc = _libraries['libpulse.so.0'].mbtowc
mbtowc.restype = c_int
mbtowc.argtypes = [WSTRING, STRING, size_t]
wctomb = _libraries['libpulse.so.0'].wctomb
wctomb.restype = c_int
wctomb.argtypes = [STRING, c_wchar]
mbstowcs = _libraries['libpulse.so.0'].mbstowcs
mbstowcs.restype = size_t
mbstowcs.argtypes = [WSTRING, STRING, size_t]
wcstombs = _libraries['libpulse.so.0'].wcstombs
wcstombs.restype = size_t
wcstombs.argtypes = [STRING, WSTRING, size_t]
rpmatch = _libraries['libpulse.so.0'].rpmatch
rpmatch.restype = c_int
rpmatch.argtypes = [STRING]
getsubopt = _libraries['libpulse.so.0'].getsubopt
getsubopt.restype = c_int
getsubopt.argtypes = [POINTER(STRING), POINTER(STRING), POINTER(STRING)]
posix_openpt = _libraries['libpulse.so.0'].posix_openpt
posix_openpt.restype = c_int
posix_openpt.argtypes = [c_int]
grantpt = _libraries['libpulse.so.0'].grantpt
grantpt.restype = c_int
grantpt.argtypes = [c_int]
unlockpt = _libraries['libpulse.so.0'].unlockpt
unlockpt.restype = c_int
unlockpt.argtypes = [c_int]
ptsname = _libraries['libpulse.so.0'].ptsname
ptsname.restype = STRING
ptsname.argtypes = [c_int]
ptsname_r = _libraries['libpulse.so.0'].ptsname_r
ptsname_r.restype = c_int
ptsname_r.argtypes = [c_int, STRING, size_t]
getpt = _libraries['libpulse.so.0'].getpt
getpt.restype = c_int
getpt.argtypes = []
getloadavg = _libraries['libpulse.so.0'].getloadavg
getloadavg.restype = c_int
getloadavg.argtypes = [POINTER(c_double), c_int]
sigset_t = __sigset_t
suseconds_t = __suseconds_t
__fd_mask = c_long
class fd_set(Structure):
    pass
fd_set._fields_ = [
    ('fds_bits', __fd_mask * 32),
]
fd_mask = __fd_mask
select = _libraries['libpulse.so.0'].select
select.restype = c_int
select.argtypes = [c_int, POINTER(fd_set), POINTER(fd_set), POINTER(fd_set), POINTER(timeval)]
class timespec(Structure):
    pass
timespec._fields_ = [
    ('tv_sec', __time_t),
    ('tv_nsec', c_long),
]
pselect = _libraries['libpulse.so.0'].pselect
pselect.restype = c_int
pselect.argtypes = [c_int, POINTER(fd_set), POINTER(fd_set), POINTER(fd_set), POINTER(timespec), POINTER(__sigset_t)]
gnu_dev_major = _libraries['libpulse.so.0'].gnu_dev_major
gnu_dev_major.restype = c_uint
gnu_dev_major.argtypes = [c_ulonglong]
gnu_dev_minor = _libraries['libpulse.so.0'].gnu_dev_minor
gnu_dev_minor.restype = c_uint
gnu_dev_minor.argtypes = [c_ulonglong]
gnu_dev_makedev = _libraries['libpulse.so.0'].gnu_dev_makedev
gnu_dev_makedev.restype = c_ulonglong
gnu_dev_makedev.argtypes = [c_uint, c_uint]
class timezone(Structure):
    pass
timezone._fields_ = [
    ('tz_minuteswest', c_int),
    ('tz_dsttime', c_int),
]
__timezone_ptr_t = POINTER(timezone)
gettimeofday = _libraries['libpulse.so.0'].gettimeofday
gettimeofday.restype = c_int
gettimeofday.argtypes = [POINTER(timeval), __timezone_ptr_t]
settimeofday = _libraries['libpulse.so.0'].settimeofday
settimeofday.restype = c_int
settimeofday.argtypes = [POINTER(timeval), POINTER(timezone)]
adjtime = _libraries['libpulse.so.0'].adjtime
adjtime.restype = c_int
adjtime.argtypes = [POINTER(timeval), POINTER(timeval)]

# values for enumeration '__itimer_which'
__itimer_which = c_int # enum
class itimerval(Structure):
    pass
itimerval._fields_ = [
    ('it_interval', timeval),
    ('it_value', timeval),
]
__itimer_which_t = c_int
getitimer = _libraries['libpulse.so.0'].getitimer
getitimer.restype = c_int
getitimer.argtypes = [__itimer_which_t, POINTER(itimerval)]
setitimer = _libraries['libpulse.so.0'].setitimer
setitimer.restype = c_int
setitimer.argtypes = [__itimer_which_t, POINTER(itimerval), POINTER(itimerval)]
utimes = _libraries['libpulse.so.0'].utimes
utimes.restype = c_int
utimes.argtypes = [STRING, POINTER(timeval)]
lutimes = _libraries['libpulse.so.0'].lutimes
lutimes.restype = c_int
lutimes.argtypes = [STRING, POINTER(timeval)]
futimes = _libraries['libpulse.so.0'].futimes
futimes.restype = c_int
futimes.argtypes = [c_int, POINTER(timeval)]
futimesat = _libraries['libpulse.so.0'].futimesat
futimesat.restype = c_int
futimesat.argtypes = [c_int, STRING, POINTER(timeval)]
u_char = __u_char
u_short = __u_short
u_int = __u_int
u_long = __u_long
quad_t = __quad_t
u_quad_t = __u_quad_t
fsid_t = __fsid_t
loff_t = __loff_t
ino_t = __ino_t
ino64_t = __ino64_t
dev_t = __dev_t
gid_t = __gid_t
mode_t = __mode_t
nlink_t = __nlink_t
uid_t = __uid_t
off_t = __off_t
off64_t = __off64_t
id_t = __id_t
ssize_t = __ssize_t
daddr_t = __daddr_t
caddr_t = __caddr_t
key_t = __key_t
useconds_t = __useconds_t
ulong = c_ulong
ushort = c_ushort
uint = c_uint
u_int8_t = c_ubyte
u_int16_t = c_ushort
u_int32_t = c_uint
u_int64_t = c_ulonglong
register_t = c_int
blksize_t = __blksize_t
blkcnt_t = __blkcnt_t
fsblkcnt_t = __fsblkcnt_t
fsfilcnt_t = __fsfilcnt_t
blkcnt64_t = __blkcnt64_t
fsblkcnt64_t = __fsblkcnt64_t
fsfilcnt64_t = __fsfilcnt64_t
clock_t = __clock_t
time_t = __time_t
clockid_t = __clockid_t
timer_t = __timer_t
class tm(Structure):
    pass
tm._fields_ = [
    ('tm_sec', c_int),
    ('tm_min', c_int),
    ('tm_hour', c_int),
    ('tm_mday', c_int),
    ('tm_mon', c_int),
    ('tm_year', c_int),
    ('tm_wday', c_int),
    ('tm_yday', c_int),
    ('tm_isdst', c_int),
    ('tm_gmtoff', c_long),
    ('tm_zone', STRING),
]
class itimerspec(Structure):
    pass
itimerspec._fields_ = [
    ('it_interval', timespec),
    ('it_value', timespec),
]
class sigevent(Structure):
    pass
sigevent._fields_ = [
]
pid_t = __pid_t
clock = _libraries['libpulse.so.0'].clock
clock.restype = clock_t
clock.argtypes = []
time = _libraries['libpulse.so.0'].time
time.restype = time_t
time.argtypes = [POINTER(time_t)]
difftime = _libraries['libpulse.so.0'].difftime
difftime.restype = c_double
difftime.argtypes = [time_t, time_t]
mktime = _libraries['libpulse.so.0'].mktime
mktime.restype = time_t
mktime.argtypes = [POINTER(tm)]
strftime = _libraries['libpulse.so.0'].strftime
strftime.restype = size_t
strftime.argtypes = [STRING, size_t, STRING, POINTER(tm)]
strptime = _libraries['libpulse.so.0'].strptime
strptime.restype = STRING
strptime.argtypes = [STRING, STRING, POINTER(tm)]
strftime_l = _libraries['libpulse.so.0'].strftime_l
strftime_l.restype = size_t
strftime_l.argtypes = [STRING, size_t, STRING, POINTER(tm), __locale_t]
strptime_l = _libraries['libpulse.so.0'].strptime_l
strptime_l.restype = STRING
strptime_l.argtypes = [STRING, STRING, POINTER(tm), __locale_t]
gmtime = _libraries['libpulse.so.0'].gmtime
gmtime.restype = POINTER(tm)
gmtime.argtypes = [POINTER(time_t)]
localtime = _libraries['libpulse.so.0'].localtime
localtime.restype = POINTER(tm)
localtime.argtypes = [POINTER(time_t)]
gmtime_r = _libraries['libpulse.so.0'].gmtime_r
gmtime_r.restype = POINTER(tm)
gmtime_r.argtypes = [POINTER(time_t), POINTER(tm)]
localtime_r = _libraries['libpulse.so.0'].localtime_r
localtime_r.restype = POINTER(tm)
localtime_r.argtypes = [POINTER(time_t), POINTER(tm)]
asctime = _libraries['libpulse.so.0'].asctime
asctime.restype = STRING
asctime.argtypes = [POINTER(tm)]
ctime = _libraries['libpulse.so.0'].ctime
ctime.restype = STRING
ctime.argtypes = [POINTER(time_t)]
asctime_r = _libraries['libpulse.so.0'].asctime_r
asctime_r.restype = STRING
asctime_r.argtypes = [POINTER(tm), STRING]
ctime_r = _libraries['libpulse.so.0'].ctime_r
ctime_r.restype = STRING
ctime_r.argtypes = [POINTER(time_t), STRING]
tzset = _libraries['libpulse.so.0'].tzset
tzset.restype = None
tzset.argtypes = []
stime = _libraries['libpulse.so.0'].stime
stime.restype = c_int
stime.argtypes = [POINTER(time_t)]
timegm = _libraries['libpulse.so.0'].timegm
timegm.restype = time_t
timegm.argtypes = [POINTER(tm)]
timelocal = _libraries['libpulse.so.0'].timelocal
timelocal.restype = time_t
timelocal.argtypes = [POINTER(tm)]
dysize = _libraries['libpulse.so.0'].dysize
dysize.restype = c_int
dysize.argtypes = [c_int]
nanosleep = _libraries['libpulse.so.0'].nanosleep
nanosleep.restype = c_int
nanosleep.argtypes = [POINTER(timespec), POINTER(timespec)]
clock_getres = _libraries['libpulse.so.0'].clock_getres
clock_getres.restype = c_int
clock_getres.argtypes = [clockid_t, POINTER(timespec)]
clock_gettime = _libraries['libpulse.so.0'].clock_gettime
clock_gettime.restype = c_int
clock_gettime.argtypes = [clockid_t, POINTER(timespec)]
clock_settime = _libraries['libpulse.so.0'].clock_settime
clock_settime.restype = c_int
clock_settime.argtypes = [clockid_t, POINTER(timespec)]
clock_nanosleep = _libraries['libpulse.so.0'].clock_nanosleep
clock_nanosleep.restype = c_int
clock_nanosleep.argtypes = [clockid_t, c_int, POINTER(timespec), POINTER(timespec)]
clock_getcpuclockid = _libraries['libpulse.so.0'].clock_getcpuclockid
clock_getcpuclockid.restype = c_int
clock_getcpuclockid.argtypes = [pid_t, POINTER(clockid_t)]
timer_create = _libraries['libpulse.so.0'].timer_create
timer_create.restype = c_int
timer_create.argtypes = [clockid_t, POINTER(sigevent), POINTER(timer_t)]
timer_delete = _libraries['libpulse.so.0'].timer_delete
timer_delete.restype = c_int
timer_delete.argtypes = [timer_t]
timer_settime = _libraries['libpulse.so.0'].timer_settime
timer_settime.restype = c_int
timer_settime.argtypes = [timer_t, c_int, POINTER(itimerspec), POINTER(itimerspec)]
timer_gettime = _libraries['libpulse.so.0'].timer_gettime
timer_gettime.restype = c_int
timer_gettime.argtypes = [timer_t, POINTER(itimerspec)]
timer_getoverrun = _libraries['libpulse.so.0'].timer_getoverrun
timer_getoverrun.restype = c_int
timer_getoverrun.argtypes = [timer_t]
getdate = _libraries['libpulse.so.0'].getdate
getdate.restype = POINTER(tm)
getdate.argtypes = [STRING]
getdate_r = _libraries['libpulse.so.0'].getdate_r
getdate_r.restype = c_int
getdate_r.argtypes = [STRING, POINTER(tm)]
class __locale_data(Structure):
    pass
__locale_struct._fields_ = [
    ('__locales', POINTER(__locale_data) * 13),
    ('__ctype_b', POINTER(c_ushort)),
    ('__ctype_tolower', POINTER(c_int)),
    ('__ctype_toupper', POINTER(c_int)),
    ('__names', STRING * 13),
]
__locale_data._fields_ = [
]
locale_t = __locale_t
ptrdiff_t = c_int
__all__ = ['pa_context_set_name',
           'pa_context_get_source_info_by_index',
           'pa_time_event_destroy_cb_t', 'PA_IO_EVENT_HANGUP',
           'pa_client_info', 'pa_context_set_sink_volume_by_name',
           'pa_stream_request_cb_t', 'wctomb', 'mkstemps', 'cbrtl',
           'ctime', 'PA_STREAM_UPLOAD', 'PA_SUBSCRIPTION_MASK_SOURCE',
           'int_fast32_t', 'acosl', 'pa_context_get_protocol_version',
           'pa_channel_map_def_t', 'clock_getres', 'acosf',
           'pa_context_set_card_profile_by_name',
           'pa_context_get_server_info', 'sinf', 'ldexpf', 'log2f',
           'pa_stream_set_buffer_attr',
           'pa_context_get_sample_info_by_index', 'uint8_t',
           'pa_get_host_name', 'ilogb', '__signbitf',
           'pa_bytes_to_usec', 'pa_free_cb_t', 'mktime',
           'pa_context_get_client_info_list',
           'pa_threaded_mainloop_in_thread', 'pa_xfree',
           'pa_proplist_iterate', 'exit',
           'pa_context_move_sink_input_by_index',
           'pa_context_suspend_sink_by_name', 'PA_CONTEXT_NOFAIL',
           'random', 'rand_r', 'atan2l', 'scalbnf', 'ctime_r',
           'pa_stream_set_name', 'pa_stream_set_event_callback',
           'pa_channel_map_valid', 'getloadavg',
           'PA_CHANNEL_POSITION_SUBWOOFER', 'truncl',
           'pa_signal_destroy_cb_t',
           'pa_channel_position_from_string', '__time_t',
           'pa_seek_mode', 'PA_SUBSCRIPTION_MASK_CLIENT', 'qecvt',
           'pa_context_set_sink_volume_by_index',
           'pa_context_get_module_info', 'pa_sample_spec_init', 'y1',
           'pa_channel_position_mask_t', 'PA_SINK_LATENCY',
           'scalblnf', 'strftime', 'uint_fast16_t', 'imaxdiv',
           'pa_cvolume_set_fade',
           'pa_context_remove_autoload_by_name',
           'pa_mainloop_get_retval', 'round', 'ldexpl', 'system',
           'cosf', 'PA_SINK_UNLINKED', '__uint64_t', 'nexttoward',
           'coshl', 'log1pl', 'pa_subscription_event_type_t',
           'PA_ERR_TIMEOUT', 'cosh',
           'pa_context_get_source_output_info_list', 'pa_sample_spec',
           'atof', 'pa_context_play_sample_with_proplist', 'strtod',
           '_POSIX_', 'sincos', 'lgammaf_r', 'getitimer',
           'PA_ERR_NOTSUPPORTED', 'asin', 'pa_stream_get_channel_map',
           'nanl', 'pa_channel_map_parse', 'pa_channel_map_equal',
           'PA_SUBSCRIPTION_EVENT_SINK_INPUT', 'y1f', '__timer_t',
           'PA_STREAM_AUTO_TIMING_UPDATE', 'nanf', 'grantpt',
           'clock_settime', '__expm1l', 'llroundl', 'id_t', 'expm1l',
           'llroundf', 'pa_context_get_autoload_info_by_index',
           'log1pf', 'pa_context_play_sample_cb_t', 'fmax',
           'pa_proplist_size', 'pa_xstrdup', 'qfcvt',
           'pa_stream_get_timing_info', 'significandf', 'localtime_r',
           'pa_cvolume_get_position', 'PA_CHANNEL_POSITION_AUX18',
           'PA_CHANNEL_POSITION_AUX19', 'sinl', 'strtof', 'drem',
           'sinh', 'pa_signal_init', 'PA_CHANNEL_POSITION_AUX10',
           'PA_CHANNEL_POSITION_AUX11', 'PA_CHANNEL_POSITION_AUX12',
           'PA_CHANNEL_POSITION_AUX13', 'PA_CHANNEL_POSITION_AUX14',
           'PA_CHANNEL_POSITION_AUX15', 'PA_CHANNEL_POSITION_AUX16',
           'PA_CHANNEL_POSITION_AUX17',
           'pa_stream_set_moved_callback', 'pa_stream_trigger',
           'pa_timeval_age', 'PA_SAMPLE_U8', 'PA_SINK_HARDWARE',
           'lroundl', 'pthread_t', 'pa_stream_get_device_index',
           'pa_cvolume_max', 'log2l',
           'pa_cvolume_compatible_with_channel_map',
           'pa_stream_state_t', 'pa_proplist_from_string',
           'PA_CHANNEL_POSITION_INVALID', 'PA_ERR_INTERNAL', 'exp2f',
           'pa_cvolume_avg', 'pa_stream_state', 'cbrt', '__mode_t',
           'PA_CONTEXT_UNCONNECTED', 'PA_SUBSCRIPTION_EVENT_MODULE',
           'PA_ERR_TOOLARGE', 'PA_CHANNEL_MAP_ALSA',
           'PA_STREAM_FIX_FORMAT', '__off_t', 'PA_SOURCE_HARDWARE',
           'strptime_l', 'PA_CHANNEL_POSITION_CENTER', 'select',
           'fsid_t', 'pa_context_set_source_volume_by_index',
           'u_quad_t', 'PA_SINK_DECIBEL_VOLUME', 'fdimf', 'remainder',
           'pa_stream_get_index', 'fsfilcnt64_t',
           'pa_channel_position_t', 'pa_sample_format_t', 'cfree',
           'lrand48_r', 'pa_stream_flush', 'PA_SEEK_ABSOLUTE',
           'wcstoimax', 'int_least64_t', 'srand', 'qecvt_r', 'exp10',
           'PA_SOURCE_INVALID_STATE', 'log10f',
           'pa_stream_set_write_callback', 'nexttowardf',
           'PA_SOURCE_LATENCY', '__int8_t', '__fsblkcnt64_t', 'expm1',
           'PA_STREAM_READY', 'pa_cvolume_set_position',
           'gettimeofday', 'pa_sample_info', 'llrintl',
           '_LIB_VERSION_TYPE', 'pa_subscription_mask_t',
           'PA_SUBSCRIPTION_EVENT_SOURCE', 'int_fast64_t', '__assert',
           'llrintf', 'pa_io_event_flags', 'erand48_r',
           'pa_context_errno', 'PA_CONTEXT_READY', 'PA_SAMPLE_S24BE',
           'pid_t', 'pa_threaded_mainloop_wait',
           'pa_stream_connect_record', 'mkostemps',
           'pa_context_remove_autoload_by_index',
           'PA_SEEK_RELATIVE_END', 'erf', 'pa_timing_info',
           'pa_path_get_filename', 'pa_stream_get_buffer_attr',
           'pthread_key_t', 'ldiv_t', 'pa_defer_event',
           'pa_get_binary_name', 'pa_channel_map_can_balance',
           '__locale_struct', 'u_int8_t',
           'pa_stream_set_buffer_attr_callback', 'PA_CHANNEL_MAP_OSS',
           'N16pthread_rwlock_t4DOT_12E', 'intptr_t', 'off_t',
           'strtold', 'pa_context_get_server_protocol_version',
           'pa_sample_format_is_be', 'PA_SUBSCRIPTION_EVENT_CLIENT',
           'pa_stream_ref', '__fsblkcnt_t', '__fpclassifyf', 'tan',
           '__locale_t', 'lcong48', 'getpt', 'blkcnt64_t', 'atanf',
           'PA_SOURCE_HW_VOLUME_CTRL', 'ssize_t', 'lrand48',
           'PA_ERR_ACCESS', 'PA_CHANNEL_POSITION_TOP_FRONT_RIGHT',
           'atanl', 'pa_defer_event_destroy_cb_t', 'pa_strerror',
           '_IEEE_', 'tgamma', 'pa_channel_map_snprint',
           'PA_STREAM_FIX_RATE', 'sin', 'pa_context_drain', 'bsearch',
           'pa_stream_direction_t',
           'PA_SUBSCRIPTION_EVENT_SAMPLE_CACHE', 'unsetenv',
           '__assert_perror_fail', 'mrand48_r', 'ptrdiff_t',
           'srand48_r', 'pa_signal_new', 'random_r',
           'PA_SAMPLE_S24_32BE', 'on_exit', 'valloc',
           'PA_SOURCE_NETWORK', 'PA_SUBSCRIPTION_EVENT_FACILITY_MASK',
           'gammal', '__swblk_t', 'ITIMER_PROF', 'pa_xstrndup',
           'ITIMER_VIRTUAL', 'PA_SEEK_RELATIVE', 'pa_module_info',
           'PA_SUBSCRIPTION_MASK_CARD', 'PA_ERR_IO',
           'pa_stream_flags_t', '__pthread_internal_slist',
           'pa_timeval_sub', 'pa_timeval_add',
           'PA_CHANNEL_POSITION_TOP_REAR_CENTER',
           'PA_CONTEXT_CONNECTING', 'pa_context_add_autoload',
           'pa_sw_cvolume_divide', '__u_short',
           'pa_context_set_source_mute_by_name',
           'PA_SUBSCRIPTION_MASK_AUTOLOAD', 'pa_stream_cancel_write',
           '__fsfilcnt_t', 'PA_SINK_HW_MUTE_CTRL',
           'PA_CHANNEL_POSITION_AUX21', 'PA_CHANNEL_POSITION_AUX20',
           'PA_CHANNEL_POSITION_AUX23', 'PA_CHANNEL_POSITION_AUX22',
           'PA_CHANNEL_POSITION_AUX25', 'PA_CHANNEL_POSITION_AUX24',
           'PA_CHANNEL_POSITION_AUX27', 'PA_CHANNEL_POSITION_AUX26',
           'PA_CHANNEL_POSITION_AUX29', 'PA_CHANNEL_POSITION_AUX28',
           'strtouq', 'roundl', 'pa_stream_set_started_callback',
           'log10l', 'u_int32_t', 'initstate', 'PA_SINK_FLAT_VOLUME',
           'finitef', 'size_t', 'pa_context_flags', 'finitel',
           'pa_utf8_to_locale', 'jnl', 'pa_proplist_sets',
           'pa_proplist_setp', 'strtol_l',
           'PA_ERR_CONNECTIONTERMINATED', '__exception',
           'pa_sw_cvolume_divide_scalar', 'pa_operation_cancel',
           'PA_CHANNEL_POSITION_TOP_FRONT_CENTER', 'uint_least16_t',
           'roundf', 'gid_t', 'pa_proplist_setf', 'pa_cvolume_set',
           'mkostemps64', 'pa_bytes_per_second', 'fsblkcnt64_t',
           'pthread_once_t', 'pa_stream', 'remquo', 'strtoll',
           'PA_ERR_COMMAND', 'PA_SUBSCRIPTION_MASK_SINK_INPUT',
           'pa_channel_map_to_pretty_name', 'pa_card_info', 'yn',
           'PA_CONTEXT_SETTING_NAME', 'PA_IO_EVENT_OUTPUT',
           'getdate_r', 'pa_context_set_card_profile_by_index',
           'matherr', 'PA_CHANNEL_POSITION_FRONT_LEFT_OF_CENTER',
           'int32_t', 'pa_sample_info_cb_t', 'uid_t', 'pow10f',
           'u_int64_t', 'pa_source_state', 'pa_channel_map_init_mono',
           'pow10l', 'pa_stream_readable_size', 'srandom', 'ynl',
           'nexttowardl', 'pa_stream_set_suspended_callback',
           'pa_cvolume_scale_mask', 'sigset_t', 'localtime', 'ynf',
           'pa_stream_begin_write', 'gcvt', 'pa_stream_get_time',
           '__itimer_which', 'pa_cvolume', 'useconds_t',
           'pa_context_set_state_callback', '__int32_t',
           'pa_sw_cvolume_multiply', 'modf',
           'PA_CHANNEL_POSITION_REAR_LEFT', 'off64_t', 'PA_ERR_EXIST',
           'pa_threaded_mainloop_lock', 'pa_io_event',
           'pthread_spinlock_t', 'clock_gettime',
           'pa_proplist_unset_many', 'PA_SAMPLE_MAX',
           'PA_SOURCE_DECIBEL_VOLUME', 'pa_stream_get_state', 'sqrtl',
           'pa_frame_size', 'sigevent', '__fd_mask',
           'pa_sample_size_of_format', 'PA_SAMPLE_FLOAT32LE',
           'PA_STREAM_FIX_CHANNELS', 'PA_CONTEXT_NOFLAGS',
           'PA_STREAM_EARLY_REQUESTS', 'pa_update_mode_t',
           'pa_proplist_unset', 'abort', 'PA_ERR_PROTOCOL',
           'initstate_r', 'PA_SOURCE_HW_MUTE_CTRL',
           'pa_context_set_subscribe_callback', 'atan',
           'uint_fast32_t', 'clock_t', 'div_t',
           'pa_context_set_default_sink', 'PA_SAMPLE_S24_32LE',
           'pa_context_get_client_info', 'timespec',
           'pa_stream_notify_cb_t', 'pa_context_index_cb_t',
           'pa_cvolume_merge', 'asinhf', 'atan2f', 'pa_signal_done',
           'uint_least8_t', 'pa_threaded_mainloop_new', '__signbit',
           'pa_channel_map_init_extend', 'PA_SUBSCRIPTION_MASK_SINK',
           'pa_context_set_sink_mute_by_name', 'pa_sample_spec_equal',
           'free', 'pa_mainloop_api_once',
           'pa_threaded_mainloop_stop',
           'pa_context_move_source_output_by_index', 'atoll',
           'asctime_r', 'pa_timeval_cmp', 'qsort_r',
           'pa_source_flags_t', 'pa_sink_flags', 'finite',
           'pa_io_event_cb_t', 'pa_mainloop_get_api',
           'PA_CHANNEL_MAP_DEF_MAX', 'pa_usec_to_bytes', 'putenv',
           'PA_ERR_VERSION', 'pa_stream_prebuf',
           'PA_SOURCE_DYNAMIC_LATENCY', 'PA_IO_EVENT_NULL', 'erff',
           'jrand48', 'PA_OPERATION_RUNNING', 'erfc',
           'PA_CHANNEL_POSITION_LEFT', 'pow10', 'uint',
           'pa_cvolume_min', 'PA_CHANNEL_POSITION_RIGHT', 'ino_t',
           'strtoll_l', 'PA_SINK_INVALID_STATE', 'isnanf', 'rand',
           'PA_SUBSCRIPTION_EVENT_SINK', 'pa_io_event_flags_t',
           'floorf', '__suseconds_t', 'pa_channel_map_init_stereo',
           'rint', 'floorl', '__caddr_t', 'ldexp', '__blksize_t',
           'PA_CHANNEL_MAP_AUX', 'pa_threaded_mainloop_unlock',
           '__pthread_slist_t', 'PA_SINK_RUNNING', 'ulong', 'mkdtemp',
           'strtoull_l', 'copysignf', 'ecvt', 'pa_source_flags',
           'exp2', 'pa_stream_proplist_remove',
           'pa_get_library_version', 'qsort', 'PA_SINK_NETWORK',
           'pa_stream_event_cb_t', 'pa_mainloop_wakeup',
           'comparison_fn_t', '__daddr_t', 'ino64_t', 'isnanl',
           'PA_SUBSCRIPTION_EVENT_SOURCE_OUTPUT', 'mkstemp64', 'fma',
           'nearbyintl', 'cosl', 'pa_source_state_t', 'pa_xmalloc0',
           'nearbyintf', 'itimerval', '__u_char', '__secure_getenv',
           'PA_UPDATE_SET', 'pa_stream_update_timing_info',
           '__sig_atomic_t', 'llrint', 'mkostemp',
           'PA_SUBSCRIPTION_EVENT_REMOVE', 'pa_stat_info',
           'PA_CONTEXT_AUTHORIZING', 'pa_proplist_new',
           'PA_SOURCE_INIT', 'pa_mainloop', 'qgcvt',
           'pa_stream_writable_size', 'pa_stream_cork',
           'pa_context_set_sink_port_by_name', 'lcong48_r',
           'pa_sw_cvolume_snprint_dB',
           'PA_SUBSCRIPTION_MASK_SAMPLE_CACHE', 'quad_t',
           'uint_fast64_t', 'quick_exit',
           'PA_STREAM_INTERPOLATE_TIMING',
           'pa_context_set_sink_input_volume',
           'pa_stream_proplist_update', '__fsfilcnt64_t', 'y0f',
           'powl', 'pa_volume_snprint',
           'pa_context_get_sink_info_by_name', 'int16_t', 'uint64_t',
           'expf', 'y0l', 'pa_spawn_api',
           'PA_CHANNEL_POSITION_TOP_FRONT_LEFT', 'drand48_r', 'abs',
           '__assert_fail', '__rlim64_t',
           'pa_context_set_sink_input_mute',
           'PA_CHANNEL_POSITION_TOP_CENTER', 'pselect',
           '__ctype_get_mb_cur_max', 'pa_get_home_dir', 'itimerspec',
           'pa_operation_unref', '__u_int', 'PA_ERR_BADSTATE',
           'FP_ZERO', '__rlim_t', 'pa_mainloop_iterate', 'nrand48',
           'PA_SUBSCRIPTION_MASK_NULL', 'nlink_t', '__uint8_t',
           'PA_SOURCE_NOFLAGS', 'pa_sample_format_is_le',
           'pa_xmalloc', 'PA_ERR_MODINITFAILED', 'timeval', 'timegm',
           'pa_sample_spec_snprint', 'frexpl',
           'pa_stream_get_sample_spec', 'cbrtf',
           'PA_STREAM_START_UNMUTED', 'PA_STREAM_TERMINATED',
           'mktemp', 'timer_getoverrun',
           'pa_context_get_card_info_list', 'pa_cvolume_scale', 'y1l',
           'pa_proplist', 'pa_cvolume_init',
           'pa_stream_set_read_callback', '__clock_t',
           'pa_server_info', 'logbf', 'PA_SAMPLE_ALAW', 'u_int',
           'PA_SUBSCRIPTION_MASK_MODULE', 'PA_STREAM_FAILED', 'logbl',
           'pa_sw_volume_divide', 'getenv', 'pa_stream_finish_upload',
           'srand48', 'pa_sw_volume_from_dB', 'fsblkcnt_t',
           'drand48_data', 'PA_ERR_AUTHKEY', '__quad_t',
           '__blkcnt64_t', 'PA_SUBSCRIPTION_EVENT_NEW', '__key_t',
           'exp', 'PA_CHANNEL_POSITION_MAX', 'dev_t', '__uid_t',
           'utimes', 'remainderf', 'pa_source_output_info', '_SVID_',
           'pa_context_state_t',
           'PA_STREAM_DONT_INHIBIT_AUTO_SUSPEND', 'a64l',
           'pa_io_event_destroy_cb_t', 'PA_ERR_MAX', 'coshf',
           'pa_proplist_to_string', 'PA_CHANNEL_POSITION_SIDE_RIGHT',
           'pa_context_stat', 'log2', 'pa_locale_to_utf8', 'mode_t',
           'strtoull', 'pa_context_set_source_port_by_index',
           'pa_stream_set_latency_update_callback', 'realloc',
           'pa_operation_state_t', '_Exit', 'PA_UPDATE_MERGE',
           'strtol', 'pa_context_get_state', 'fmodl', 'PA_ERR_FORKED',
           'pa_source_info', 'lrint', '__fpclassify',
           'PA_CHANNEL_POSITION_FRONT_RIGHT_OF_CENTER',
           'PA_ERR_CONNECTIONREFUSED',
           'PA_CHANNEL_POSITION_FRONT_RIGHT', 'frexp',
           'pa_sample_size', 'pa_msleep', 'strtof_l', 'qfcvt_r',
           'getdate', 'strtoq', '__loff_t',
           'PA_CHANNEL_POSITION_AUX30', 'PA_CHANNEL_POSITION_AUX31',
           'lgammaf', 'PA_SAMPLE_INVALID', 'PA_SAMPLE_ULAW',
           'pa_usec_t', 'int_fast8_t', 'lgammal_r',
           'pa_autoload_info_cb_t', 'pa_gettimeofday', 'lgammal',
           'ceil', 'setstate_r', 'key_t', 'pa_card_info_cb_t',
           'ptsname_r', '__itimer_which_t', 'strtod_l',
           'PA_STREAM_ADJUST_LATENCY', 'fmaf', 'FP_NAN',
           'PA_IO_EVENT_ERROR', 'pa_context_set_sink_port_by_index',
           'pa_threaded_mainloop_get_api', 'pa_bytes_snprint',
           'dremf', 'pa_context_event_cb_t', 'settimeofday',
           'pa_cvolume_valid', 'pa_context_rttime_restart',
           'pa_mainloop_poll', 'N14pthread_cond_t3DOT_9E',
           '__int16_t', 'jnf', 'futimes', 'timer_delete', 'mbtowc',
           'nextafterl', 'strtoul', '__ssize_t',
           'PA_STREAM_NO_REMAP_CHANNELS', 'nextafterf',
           'pa_mainloop_free', 'j0', 'j1', 'PA_SINK_SUSPENDED',
           'pa_threaded_mainloop_start', 'pa_mainloop_run', '__pid_t',
           'pa_autoload_type', 'pa_threaded_mainloop', 'y0',
           '__locale_data', 'PA_SINK_DYNAMIC_LATENCY',
           'pa_context_kill_client', 'pa_sink_state',
           'pa_stream_write', '__sigset_t', 'pa_sink_port_info',
           'isnan', 'pa_mainloop_new',
           'pa_context_get_source_info_by_name',
           'PA_STREAM_NO_REMIX_CHANNELS', 'significandl',
           'pa_context_remove_sample', 'scalbnl',
           'PA_STREAM_FAIL_ON_SUSPEND', 'erfcf', 'posix_memalign',
           'pa_context_get_sink_info_list',
           'pa_stream_set_state_callback', '__off64_t', 'erfcl',
           'pa_client_info_cb_t', 'pa_stream_connect_playback',
           'pa_context_unref', 'FP_INFINITE',
           'pa_context_new_with_proplist', 'strtold_l', 'scalbln',
           'strftime_l', 'copysign', 'timer_t', 'expl', 'timelocal',
           'PA_CHANNEL_POSITION_TOP_REAR_LEFT', 'ilogbl', 'jn',
           'stime', 'PA_SUBSCRIPTION_EVENT_AUTOLOAD',
           'PA_CHANNEL_POSITION_FRONT_CENTER',
           'PA_SEEK_RELATIVE_ON_READ', 'pa_channel_position',
           'pa_mainloop_api', 'nearbyint', 'pa_proplist_gets',
           'pa_context_set_default_source', 'PA_CHANNEL_POSITION_LFE',
           'futimesat', 'cos', 'pa_sample_format', 'ilogbf',
           'pa_cvolume_min_mask', 'adjtime', 'PA_STREAM_PEAK_DETECT',
           'atanhf', 'ushort', 'PA_IO_EVENT_INPUT',
           'PA_STREAM_VARIABLE_RATE', 'clockid_t', 'mbstowcs',
           'PA_ERR_NODATA', 'gnu_dev_makedev', 'fd_set', 'caddr_t',
           'timer_settime', 'pa_channel_position_to_pretty_string',
           'seed48_r', 'uint16_t', 'pa_stream_is_corked', 'wcstoumax',
           'pa_context_get_sink_input_info', 'gmtime_r',
           'pa_module_info_cb_t', 'pa_sw_volume_snprint_dB', 'acoshf',
           'N15pthread_mutex_t17__pthread_mutex_s3DOT_6E', 'fmaxf',
           'pa_context_move_source_output_by_name',
           'pa_stream_get_device_name', 'double_t',
           'pa_operation_state', 'fmaxl', 'pa_channel_map_mask',
           'fabsl', 'pa_stream_disconnect', 'fmal',
           'pa_cvolume_set_balance', 'pa_get_user_name', 'l64a',
           'blkcnt_t', '__intptr_t', 'hypotf',
           'pa_proplist_to_string_sep', 'PA_STREAM_START_MUTED',
           'pa_parse_sample_format', 'register_t',
           'pa_threaded_mainloop_accept', 'hypotl', 'acoshl',
           'nanosleep', 'PA_SAMPLE_S32LE', 'pa_context_notify_cb_t',
           '__finite', 'pa_context_set_source_mute_by_index',
           'gnu_dev_major', 'fminf', 'strtoimax', 'acosh',
           'PA_SOURCE_IDLE', 'pa_context_suspend_source_by_index',
           '__isnan', 'fminl', 'atanhl', 'asinh', 'j0l', 'asinl',
           'pa_context_play_sample', 'fcvt_r', 'asinf',
           'pa_channel_map_to_name', 'j0f',
           'pa_context_get_module_info_list', 'pa_operation',
           '__dev_t', 'PA_STREAM_RECORD', 'PA_AUTOLOAD_SOURCE',
           '__isnanl', '__qaddr_t',
           'pa_context_get_card_info_by_name', 'lroundf', 'tgammaf',
           'drand48', 'tanl', 'pa_context_subscribe',
           'PA_AUTOLOAD_SINK', 'tanh', 'tanf',
           'pa_context_get_source_info_list', 'u_long', 'scalblnl',
           'truncf', 'pa_timeval_diff', 'lgamma', 'PA_SOURCE_RUNNING',
           'pa_server_info_cb_t', 'ecvt_r', 'pa_context_ref',
           'pa_sw_cvolume_multiply_scalar', 'strptime', 'clearenv',
           'pa_time_event_cb_t', 'malloc', 'pa_stream_get_latency',
           'pa_xmemdup', 'PA_CHANNEL_POSITION_MONO',
           'PA_CHANNEL_MAP_DEFAULT', 'PA_OPERATION_DONE',
           'pa_mainloop_dispatch', 'uintmax_t', 'remainderl',
           'int_fast16_t', 'pa_proplist_set', 'PA_SINK_INIT',
           '__blkcnt_t', 'pa_cvolume_max_mask', 'clock_nanosleep',
           'time_t', 'u_short', 'PA_STREAM_NODIRECTION', 'fabs',
           'pa_autoload_info', 'logf', 'sqrt', 'pa_operation_ref',
           'imaxabs', 'pa_sink_info_cb_t', 'pa_channel_map_superset',
           'PA_SUBSCRIPTION_MASK_SOURCE_OUTPUT',
           'pa_card_profile_info', 'pa_context_get_sample_info_list',
           'nextafter', 'setstate', 'dysize', 'ceilf', 'scalbn',
           '__pthread_mutex_s', 'pa_subscription_mask', 'ceill',
           'PA_STREAM_DONT_MOVE', 'pa_threaded_mainloop_free',
           'PA_SAMPLE_S16BE', 'pa_stream_connect_upload', 'isinff',
           '__ino_t', 'exp10f', 'clock_getcpuclockid', 'calloc',
           'isinfl', 'PA_ERR_KILLED',
           'pa_context_get_source_output_info', 'pa_stat_info_cb_t',
           'pa_ascii_filter', 'pa_context_get_autoload_info_list',
           'setitimer', 'PA_STREAM_PLAYBACK', 'lldiv_t', 'u_char',
           '__int64_t', 'pa_sw_volume_to_dB', 'scalb',
           'pa_sink_state_t', 'uint32_t', 'jrand48_r', 'pa_volume_t',
           'PA_STREAM_UNCONNECTED', 'powf', 'suseconds_t', 'rintf',
           '__isinff', 'PA_CHANNEL_MAP_WAVEEX', 'nan',
           'pa_channel_map_init', '__isinfl', 'rintl', 'mkstemps64',
           'pa_stream_new_with_proplist', 'PA_STREAM_NOFLAGS',
           'pa_stream_success_cb_t', 'PA_STREAM_NOT_MONOTONIC',
           '__fsid_t', '_ISOC_', 'clock', 'pa_stream_drain', 'dreml',
           'PA_SINK_IDLE', 'random_data', 'pa_context_new',
           'u_int16_t', 'fabsf', 'lrintl', '__uint32_t',
           'pa_context_suspend_sink_by_index', 'pa_cvolume_dec',
           'PA_CONTEXT_TERMINATED', 'pa_context_rttime_new', 'ldiv',
           '_XOPEN_', 'ptsname', 'PA_CHANNEL_POSITION_TOP_REAR_RIGHT',
           'pa_stream_peek', 'setenv', 'pow', '__ino64_t', 'labs',
           'pa_channel_map_can_fade', 'PA_CONTEXT_FAILED', 'fmodf',
           'loff_t', 'pa_context_set_sink_mute_by_index', 'scalbf',
           'exp10l', 'blksize_t', 'pa_sink_info', 'scalbl',
           'int_least32_t', 'pa_sample_spec_valid', '__fpclassifyl',
           'pa_operation_get_state', 'srandom_r', 'fsfilcnt_t',
           'pa_context_proplist_remove', 'FP_NORMAL',
           'pa_timeval_load', 'pa_get_fqdn', 'pa_stream_unref', 'div',
           'pa_stream_set_monitor_stream', 'gnu_dev_minor',
           'PA_CHANNEL_POSITION_FRONT_LEFT', 'uint_fast8_t',
           'pa_mainloop_quit', 'pa_channel_map_init_auto', 'float_t',
           'pa_cvolume_inc', 'mblen', 'pa_cvolume_get_balance',
           'timer_create', 'pa_source_info_cb_t',
           'pa_context_get_index', 'pa_signal_free',
           'pa_cvolume_compatible', 'tanhl', 'tm', 'PA_SAMPLE_S32BE',
           'lldiv', 'pa_cvolume_get_fade', 'rpmatch', 'pa_context',
           'tanhf', 'mrand48', 'pa_utf8_filter', 'llabs', 'seed48',
           'gammaf', 'pa_stream_update_sample_rate', 'hypot',
           'pa_sw_volume_multiply', 'pa_cvolume_snprint',
           'pa_cvolume_equal', '__id_t', 'pa_stream_flags',
           'PA_CHANNEL_POSITION_AUX2', 'PA_CHANNEL_POSITION_AUX3',
           'PA_CHANNEL_POSITION_AUX0', 'PA_SAMPLE_S16LE',
           'PA_CHANNEL_POSITION_AUX6', 'PA_CHANNEL_POSITION_AUX7',
           'PA_CHANNEL_POSITION_AUX4', 'PA_CHANNEL_POSITION_AUX5',
           'pa_xrealloc', 'PA_CHANNEL_POSITION_AUX8',
           'PA_CHANNEL_POSITION_AUX9', 'PA_SOURCE_SUSPENDED',
           'pa_defer_event_cb_t', 'pa_threaded_mainloop_signal',
           'PA_STREAM_START_CORKED', 'pa_time_event',
           'PA_CHANNEL_MAP_AIFF', 'lutimes', 'atanh', 'asctime',
           '__signbitl', '__clockid_t', 'PA_ERR_NOENTITY',
           'int_least16_t', 'PA_CHANNEL_POSITION_REAR_RIGHT',
           'pa_stream_get_context', 'pa_sw_volume_to_linear',
           'pa_source_output_info_cb_t', 'fmod', 'tgammal',
           'pa_cvolume_remap', 'pa_proplist_clear',
           'pa_context_get_server', 'pa_stream_set_overflow_callback',
           'gmtime', 'PA_ERR_BUSY', '__nlink_t', 'atan2',
           'FP_SUBNORMAL', 'tzset', '__compar_fn_t', 'timer_gettime',
           'getsubopt', 'pa_utf8_valid', 'exp2l', 'pa_proplist_free',
           'pa_stream_set_underflow_callback', 'pa_channel_map',
           'pa_update_mode', 'canonicalize_file_name',
           'PA_UPDATE_REPLACE', '__compar_d_fn_t',
           'pa_stream_is_suspended', 'PA_SAMPLE_S24LE', 'lrintf',
           'fmin', 'llround', 'acos', 'trunc',
           'pa_context_get_card_info_by_index', 'gamma', 'fcvt',
           'remquol', 'j1l', 'pa_context_get_sample_info_by_name',
           'modfl', 'j1f', 'PA_SINK_HW_VOLUME_CTRL', 'uint_least64_t',
           'PA_OPERATION_CANCELLED',
           'pa_context_get_sink_input_info_list', 'fdiml',
           'pa_threaded_mainloop_get_retval', 'mkostemp64',
           'PA_SUBSCRIPTION_MASK_SERVER', '__u_long',
           'pa_proplist_copy', 'pa_context_proplist_update',
           '__timezone_ptr_t', 'sqrtf', 'PA_SAMPLE_FLOAT32BE',
           'pa_context_get_sink_info_by_index', '__gid_t',
           'pa_proplist_update', 'log', 'logl', 'lround',
           'PA_ERR_UNKNOWN', 'pa_stream_drop', 'pa_signal_cb_t',
           'pa_context_set_source_volume_by_name',
           'pa_context_subscribe_cb_t', 'pa_source_port_info',
           'nrand48_r', 'log10', 'PA_SINK_NOFLAGS',
           'PA_CHANNEL_POSITION_SIDE_LEFT', 'uintptr_t', '__uint16_t',
           'PA_SUBSCRIPTION_EVENT_CHANGE', 'int8_t', 'PA_OK',
           '__finitel', 'pa_channel_position_to_string', 'atoi',
           'pa_context_load_module', 'atol', 'pa_context_connect',
           '__isinf', '__finitef', 'erand48', 'erfl',
           'uint_least32_t', 'unlockpt', 'pa_autoload_type_t',
           'PA_SUBSCRIPTION_EVENT_CARD',
           'PA_CHANNEL_POSITION_REAR_CENTER', 'PA_ERR_INVALID',
           'pa_channel_map_def', 'pa_proplist_get', 'fdim',
           'int_least8_t', 'pa_context_flags_t', 'intmax_t',
           'PA_ERR_NOEXTENSION', 'pa_signal_set_destroy',
           'pa_poll_func', 'expm1f', '__useconds_t',
           'pa_timeval_store', 'PA_SUBSCRIPTION_EVENT_TYPE_MASK',
           'logb', 'pa_proplist_isempty', 'log1p', 'fd_mask', 'sinhf',
           'pa_cvolume_avg_mask', 'pa_context_exit_daemon',
           'pa_context_suspend_source_by_name',
           'pa_context_set_event_callback', '__isnanf',
           'PA_ERR_NOTIMPLEMENTED', 'ITIMER_REAL', 'strtoumax',
           'pa_subscription_event_type', 'realpath',
           'pa_context_move_sink_input_by_name', 'lgamma_r',
           'int64_t', 'timezone', 'pa_mainloop_set_poll_func',
           'pa_context_kill_sink_input', 'PA_ERR_OBSOLETE',
           'wcstombs', 'pa_mainloop_prepare', '__expl',
           'posix_openpt', 'imaxdiv_t', 'floor',
           'pa_context_is_pending', 'daddr_t', 'PA_STREAM_CREATING',
           'copysignl', 'pa_context_get_autoload_info_by_name',
           'pa_context_state', 'pa_ascii_valid',
           'pa_context_disconnect', '__u_quad_t', 'modff',
           'pa_channel_map_compatible',
           'PA_SUBSCRIPTION_EVENT_SERVER', 'pa_stream_direction',
           'mkstemp', 'sinhl', 'PA_SOURCE_UNLINKED',
           'pa_sink_flags_t', 'pa_seek_mode_t',
           'pa_context_set_source_port_by_name',
           'pa_context_is_local', 'pa_context_kill_source_output',
           'pa_stream_new', 'PA_SUBSCRIPTION_MASK_ALL',
           'pa_proplist_contains', 'PA_ERR_INVALIDSERVER',
           'pa_stream_get_monitor_stream', 'PA_CHANNEL_POSITION_AUX1',
           'isinf', 'pa_sink_input_info_cb_t', 'significand',
           'pa_channel_map_has_position', 'PA_CONTEXT_NOAUTOSPAWN',
           'pa_sw_volume_from_linear', 'pa_cvolume_channels_equal_to',
           'frexpf', 'strtoul_l', 'locale_t',
           'pa_context_unload_module', 'remquof', 'N4wait4DOT_19E',
           '__socklen_t', 'difftime', 'pa_signal_event',
           'pa_sink_input_info', 'pa_sample_format_to_string',
           'pollfd', 'pa_context_success_cb_t', 'sincosl', 'time',
           'N4wait4DOT_20E', 'sincosf', 'pa_buffer_attr', 'asinhl']
