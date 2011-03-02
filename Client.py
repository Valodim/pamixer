# Ear Candy - Pulseaduio sound managment tool
# Copyright (C) 2008 Jason Taylor
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import re
import time
import datetime
from xml.dom.minidom import *

class Client():

    def __init__(self, index, struct, proplist):
        self.index = index

        self.update(index, struct, proplist)

    def update(self, index, struct, proplist):
        self.name = struct.name
        self.clean_name = self.clean_client_name(struct.name)
        if 'pid' in proplist:
            self.pid = proplist['pid']

    def is_active(self):

        # If ear candy did pause then consider active
        if self.__pause_status > 0: return True

        # no sinks then not active
        if len(self.sinks.values()) == 0: return False

        timestamp = time.mktime(datetime.datetime.now().timetuple())

        # check meter levels on others
        if self.apply_volume_meter_hack:
            for sink in self.sinks.values():

                if sink.volume_meter > 0:
                    self.__pause_status = 0
                    return True

                # HACK: Check how long its been inactive... and if more than a second count as expired
                if timestamp - sink.volume_meter_last_non_zero < 1:
                    self.__pause_status = 0
                    return True

            return False

        self.__pause_status = 0
        return True

    def set_primary(self, value):
        if value or self.category == "default":
            self.__fade_in()
            if self.__pause_status > 0:
                for plugin in self.plugins:
                    if plugin.enabled and not plugin.is_playing():
                        if plugin.set_pause(False): 
                            self.__pause_status = 0
        else:
            self.__fade_mute()
            if self.is_active() and self.__pause_status == 0:                 
                self.__pause_status = 1

    # called by sink, check if all sinks are at correct volume
    def check_volume(self):
        result = True
        for sink in self.sinks.values():
            result = result and sink.volume_check

        if result and self.__pause_status == 1:
           for plugin in self.plugins:
                if plugin.enabled and plugin.is_playing():
                    plugin.set_pause(True)
           self.__pause_status = 2

    def move_to_output(self, output):
        if not self.output == output:
            self.output = output
            self.core.move_client(self)

    def clean_client_name(self, name):
        name = name.strip()
        alsa_plugin = "ALSA plug-in ["
        if name.startswith(alsa_plugin):
            name = name[len(alsa_plugin):-1]
        return name


