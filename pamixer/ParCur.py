import time
import datetime
import re
import os
import copy
import sys
import shutil
from xml.dom.minidom import *

from pamixer.PulseAudio import PulseAudio 

class ParCur():

    def __init__(self):
        self.cur = None

        self.pa_samples = {}  # samples by id
        self.pa_clients = {}  # clients by id
        self.pa_sinks = {}
        self.pa_sink_inputs = {}
        self.pa_sources = {}
        self.pa_source_outputs = {}

        # whether to use dB or linear for numeric volume display
        self.use_dezibel = True
        self.volume_step = 0.05
        self.volume_max_soft = 1.00
        self.volume_max_hard = 1.50

    def run(self, server = None):
        self.pa = PulseAudio(self.on_new_pa_client, self.on_remove_pa_client, self.on_new_pa_sink, self.on_remove_pa_sink, self.on_new_pa_sink_input, self.on_remove_pa_sink_input, self.on_volume_change, self.on_new_sample, self.on_remove_sample, self.on_new_pa_source, self.on_remove_pa_source, self.on_new_pa_source_output, self.on_remove_pa_source_output, server)

        # set some helper functions
        self.volume_to_linear = self.pa.volume_to_linear
        self.volume_to_dB = self.pa.volume_to_dB

    def on_volume_change(self, level):
        self.update()
        return
        #print self.managed_output_name, level

    def on_remove_pa_source(self, index):
        if self.pa_sources.has_key(index):
            self.__print("removed pa output", self.pa_sources[index])
            del self.pa_sources[index]

            self.update()

    def on_new_pa_source(self, index, struct, props):
        if not self.pa_sources.has_key(index):
            self.__print("new source:", index, struct.name)
            # create new
            self.pa_sources[index] = Source(index, struct, props)
        else:
            self.__print("changed source:", index, struct.name)
            # update old
            self.pa_sources[index].update(struct, props)

        self.update()

    def on_new_pa_source_output(self, index, struct, props):
        if not self.pa_source_outputs.has_key(index):
            self.__print("new source output:", index, struct.name)
            self.pa_source_outputs[index] = SourceOutput(index, struct, props)
        else:
            self.__print("changed source output:", index, struct.name)
            self.pa_source_outputs[index].update(struct, props)

        self.update()

    def on_remove_pa_source_output(self, index):
        if self.pa_source_outputs.has_key(index):
            self.__print("remove source output", index)
            del self.pa_source_outputs[index]

            self.update()

    def request_update(self):
        self.pa.pa_request_update()

    def move_all_sinks(self):
        if self.managed_output_name:
            for sink in self.pa_sink_inputs.values():
                if not sink.client.output:
                    self.pa.move_sink(sink.index, self.managed_output_name)

    def on_new_pa_client(self, index, struct, proplist):
        # Link all clients with same name into same object
        if not self.pa_clients.has_key(index):
            self.__print("new client: ", "index:")

            self.pa_clients[index] = Client(index, struct, proplist)
        else:
            self.pa_clients[index].update(index, struct, proplist)
            self.__print("changed client: ", "index:")

        # and update view
        self.update()

    def on_remove_pa_client(self, index):
        if self.pa_clients.has_key(index):
            client = self.pa_clients[index]

            self.__print("remove client", index, client.name)

            # remove from by ID list
            del self.pa_clients[index]

            self.update()

    def on_new_pa_sink(self, index, struct, props):
        if not self.pa_sinks.has_key(index):
            self.__print("new sink:", index, struct.name)
            # create new
            self.pa_sinks[index] = Sink(index, struct, props)
        else:
            self.__print("changed sink:", index, struct.name)
            # update old
            self.pa_sinks[index].update(struct, props)

        self.update()

    def on_remove_pa_sink(self, index):
        self.__print("remove sink", index)
        del self.pa_sinks[index]

        self.update()

    def on_new_pa_sink_input(self, index, struct):
        if not self.pa_sink_inputs.has_key(index):
            self.__print("new sink input:", index, struct.name)
            self.pa_sink_inputs[index] = SinkInput(index, struct)
        else:
            self.__print("changed sink input:", index, struct.name)
            self.pa_sink_inputs[index].update(struct)

        self.update()

    def on_remove_pa_sink_input(self, index):
        if self.pa_sink_inputs.has_key(index):
            self.__print("remove sink input", index)
            del self.pa_sink_inputs[index]

            self.update()

    def on_new_sample(self, index, struct, props):
        if not self.pa_samples.has_key(index):
            self.__print("new sample:", index, struct.name)
            self.pa_samples[index] = Sample(index, struct, props)
        else:
            self.__print("changed sample:", index, struct.name)
            self.pa_samples[index].update(struct, props)

        self.update()
        return

    def on_remove_sample(self, index):
        if self.pa_samples.has_key(index):
            self.__print("remove sample", index)
            del self.pa_samples[index]

        self.update()
        return

    def get_sink_inputs_by_client(self, index):
        result = []
        for input in self.pa_sink_inputs.values():
            if input.client == index:
                result.append(input)
        return result

    def get_sink_inputs_by_sink(self, index):
        result = []
        for input in self.pa_sink_inputs.values():
            if input.sink == index:
                result.append(input)
        return result

    def get_source_outputs_by_source(self, index):
        result = []
        for output in self.pa_source_outputs.values():
            if output.source == index:
                result.append(output)
        return result

    def move_sink_input(self, sink_input_index, sink_index):
        self.pa.move_sink_input(sink_input_index, sink_index)

    def sample_play(self, name, sink_index):
        self.pa.sample_play(name, self.pa_sinks.values()[0].name if sink_index == -1 else self.pa_sinks[sink_index].name)

    def move_client(self, client):
        self.__print("move client", client.name)

        for sink in client.sinks.values(): 
            if client.output:
                self.__print("move", sink.name, "to", sink.client.output)
                self.pa.move_sink(sink.index, sink.client.output)
            else:
                self.__print("move", sink.name, "to", self.managed_output_name)
                self.pa.move_sink(sink.index, self.managed_output_name)

    def set_sink_volume(self, index, volume):
        cvolume = self.pa.volume_from_linear(volume)
        self.pa.set_sink_volume(index, cvolume)

    def set_sink_input_volume(self, index, volume):
        cvolume = self.pa.volume_from_linear(volume)
        self.pa.set_sink_input_volume(index, cvolume)

    def set_source_volume(self, index, volume):
        cvolume = self.pa.volume_from_linear(volume)
        self.pa.set_source_volume(index, cvolume)

    def set_source_output_volume(self, index, volume):
        cvolume = self.pa.volume_from_linear(volume)
        self.pa.set_source_output_volume(index, cvolume)

    def kill_sink_input(self, index):
        self.pa.kill_sink_input(index)

    def update(self):
        sys.stdout.write("\a")
        sys.stdout.flush()
        # return
        if self.cur:
            self.cur.update()

    def __print(self, *args):
        if self.cur and self.cur.verbose:
            sys.stderr.write(str(args))
        return

par = ParCur()

from Curses import Curses
from Client import Client
from Sink import Sink
from SinkInput import SinkInput
from Source import Source
from SourceOutput import SourceOutput
from Sample import Sample
