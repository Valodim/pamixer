#!/usr/bin/env python

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

import time
import datetime
import re
import os
import copy
import sys
import time
import shutil
from xml.dom.minidom import *

from pulseaudio.PulseAudio import PulseAudio 
from Client import Client
from Sink import Sink
from SinkInput import SinkInput
from Curses import Curses

class ParCur():

    def __init__(self):
        self.version = 0.6
        self.active = True
        self.cur = None
        self.display = {"": "[ unknown ]", "phone" : "Phone (VoIP)", "video" : "Video Player", "music" : "Music Player", "event" : "Notification" }
        self.ignore = ["EsounD client (UNIX socket client)", "parcur client", "Native client (UNIX socket client)", "PulseAudio Volume Control"]

        pass

    def init(self):

        self.is_mute = False
        self.mute_phone = False
        self.pa_clients_by_id = {}  # clients by id
        self.pa_sinks = {}
        self.pa_sink_inputs = {}
        self.pa_outputs = {}
        self.client_with_focus = None # client that has a focused window
        self.last_application = None
        self.primary_client = None # Client that gets foreground sound regardless of window focus
        self.managed_output_name = ""
        self.current_source_name = ""
        self.fade_timer_speed = 0.1 
        self.mute_level = 20
        self.follow_new_outputs = True

        self.apply_volume_thread_running = False 
        self.select_client_thread_running = False

    def reset_all(self):
        # tricky we want to delete all client settings and reload our default xml file
        self.pa.disconnect()
        self.init()
        self.pa = PulseAudio(self.on_new_pa_client, self.on_remove_pa_client, self.on_new_pa_sink, self.on_remove_pa_sink, self.on_new_pa_sink_input, self.on_remove_pa_sink_input, self.on_volume_change, self.pa_volume_meter)
        return

    def run(self, cur):

        # self.cur = cur

        self.init()
        self.pa = PulseAudio(self.on_new_pa_client, self.on_remove_pa_client, self.on_new_pa_sink, self.on_remove_pa_sink, self.on_new_pa_sink_input, self.on_remove_pa_sink_input, self.on_volume_change, self.pa_volume_meter)

    def set_mute(self, mute):
        self.is_mute = mute
        if self.slider: self.slider.update_mute_status()

    def get_current_sink_volume(self):
        self.pa.get_sink_info_by_name(self.managed_output_name)

    def __adjust_volumes(self):

        # Always update based on active sinks
        for sink in self.pa_sink_inputs.values():
            if sink.set_volume():
                # set pa volume
                self.pa.set_sink_volume(sink.index, sink.volume, sink.channels)  

    def on_volume_change(self, level):
        return
        #print self.managed_output_name, level

    def on_remove_pa_output(self, index):
        if self.pa_outputs.has_key(index):
            self.__print("removed pa output", self.pa_outputs[index])
            del self.pa_outputs[index]

    # add new output to ours
    def on_new_pa_output(self, index, struct, startup):
        if not self.pa_outputs.has_key(index):
            output = Output(struct)
            self.__print("new pa output", output)
            self.pa_outputs[index] = output

    def move_all_sinks(self):
        if self.managed_output_name:
            for sink in self.pa_sink_inputs.values():
                if not sink.client.output:
                    self.pa.move_sink(sink.index, self.managed_output_name)

    def move_client(self, client):
        self.__print("move client", client.name)

        for sink in client.sinks.values(): 
            if client.output:
                self.__print("move", sink.name, "to", sink.client.output)
                self.pa.move_sink(sink.index, sink.client.output)
            else:
                self.__print("move", sink.name, "to", self.managed_output_name)
                self.pa.move_sink(sink.index, self.managed_output_name)

    def on_new_pa_client(self, index, name, pid, proplist):
        if not pid: pid = -1
        # Link all clients with same name into same object

        if not self.pa_clients_by_id.has_key(index):
            self.__print("new client: ", "index:", index, "name:", name, "pid: ", int(pid))

            client = Client(self, self.clean_client_name(name), int(pid))
        else:
            client = self.pa_clients_by_id[index]
            client.pid = int(pid)

            client.name = self.clean_client_name(name)
            self.__print("changed client: ", "index:", index, "name:", name, "pid: ", client.pid)

        # always set the index to the new client
        self.pa_clients_by_id[index] = client

        # and update view
        if self.cur:
            self.cur.update()

    def on_remove_pa_client(self, index):
        if self.pa_clients_by_id.has_key(index):
            client = self.pa_clients_by_id[index]

            self.__print("remove client", index, client.name)

            # remove from by ID list
            del self.pa_clients_by_id[index]

            if self.cur:
                self.cur.update()

    def on_new_pa_sink(self, index, struct):
        if not self.pa_sinks.has_key(index):
            self.__print("new sink:", index, struct.name)
            # create new
            self.pa_sinks[index] = Sink(index, struct)
        else:
            self.__print("changed sink:", index, struct.name)
            # update old
            self.pa_sinks[index].update(struct)

    def on_remove_pa_sink(self, index):
        self.__print("remove sink", index)
        del self.pa_sinks[index]

    def on_new_pa_sink_input(self, index, struct):
        if not self.pa_sink_inputs.has_key(index):
            self.__print("new sink input:", index, struct.name)
            self.pa_sink_inputs[index] = SinkInput(index, struct)
        else:
            self.__print("changed sink input:", index, struct.name)
            self.pa_sink_inputs[index].volume = volume
            self.pa_sink_inputs[index].name = self.clean_client_name(name)

        if self.cur:
            self.cur.update()

    def on_remove_pa_sink_input(self, index):
        if self.pa_sink_inputs.has_key(index):
            self.__print("remove sink input", index)
            del self.pa_sink_inputs[index]

            if self.cur:
                self.cur.update()

    def pa_volume_meter(self, index, level):
        if self.pa_sink_inputs.has_key(index):
            sink = self.pa_sink_inputs[index]
            sink.volume_meter = level
            if(level > sink.client.volume_step): sink.volume_meter_last_non_zero = time.mktime(datetime.datetime.now().timetuple())

    def get_unregistered_clients(self):
        clients = []
        # client names to skip from adding to list
        skip = copy.copy(self.ignore)
        count = 0
        for client in self.pa_clients_by_id.values():
            if client.category == "" and not client.icon and not client.name in skip:
                clients.append(client)
                skip.append( client.name )
        return clients

    def clean_client_name(self, name):
        name = name.strip()
        alsa_plugin = "ALSA plug-in ["
        if name.startswith(alsa_plugin):
            name = name[len(alsa_plugin):-1]
        return name

    def get_sink_inputs_by_sink(self, index):
        result = []
        for input in self.pa_sink_inputs.values():
            if input.sink == index:
                result.append(input)
        return result


    def exit(self):
        # Reset all volumes
        self.reset_all_volumes()
        sys.exit(0)

    def reset_all_volumes(self, deleteFile=True):
        self.__print("Resetting all volume levels...")
        for sink in self.pa_sink_inputs.values():
            self.pa.set_sink_volume(sink.index, [100, 100, 100], sink.channels)

    def __print(self, *args):
        # print args
        return

if __name__ == '__main__':

    par = ParCur()
    cur = Curses(par)

    par.run(cur)
    cur.run()

    # while True:
        # time.sleep(10)

    # par.exit()
