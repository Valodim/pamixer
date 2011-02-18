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
    def __init__(self, core, name, pid=0):
        self.core = core

        self.name = name
        self.description = self.core.clean_client_name(name)
        self.volume_default = 100
        self.volume_mute = -1
        self.rule_re_window_title = re.compile("")
        self.rule_re_command = re.compile("")
        self.rule_re_application = re.compile("")
        self.category = "" # music | video | phone
        self.apply_volume_meter_hack = True
        self.fade_volume = True
        self.output = ""
        self.dbus_name = ""

        self.pid = pid
        self.volume_step = 2
        self.has_focus = False
        self.fullscreen = False
        self.icon = None
        self.icon_name = ""
        self.iter = None
        self.balance = 0

        self.__pause_status = 0

        self.volume_target = self.volume_default

        self.sinks = {}

        self.generate_rules()

        self.plugins = []

        # TODO: remove these
        self.window_position_fade = False
        self.matched = False

    def get_volume(self):
        v = 0
        count = 0
        for sink in self.sinks.values():
            v = v + sink.volume[0]
            count = count + 1
        if count > 0: return v / count
        return v

    def get_volume_meter(self):
        v = 0
        count = 0
        for sink in self.sinks.values():
            v = v + sink.volume_meter
            count = count + 1
        if count > 0: return v / count
        return v

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

    def has_rule(self):
        return self.rule_re_command.pattern or self.rule_re_window_title.pattern or self.rule_re_application.pattern

    def generate_rules(self, app=None):
        if not app:
            app = self.core.clean_client_name(self.name).lower()
        else:
            app = app.lower()

        self.rule_re_application = re.compile(app, re.IGNORECASE)
        self.rule_re_command = re.compile(".*\/" + app , re.IGNORECASE)

    def test_focus_window(self, pid, title, command, app):

        # This should work by matching the clint pid to the window pid works 95% of the time
        # It will fail for things like gstreamer preview and nautilus that have no process link
        # until thats fixed at a lower level we have our trusty regular expressions
        if pid and self.pid and pid == self.pid:
            #print "Match PID", pid, self.pid
            return True

        # Fall back rules if pid matching fails
        if  (self.rule_re_window_title.pattern and self.rule_re_window_title.match( title )):
            self.has_focus = True
            #print "Match 1",self.rule_re_window_title.pattern, title
            return True
        elif(self.rule_re_command.pattern and self.rule_re_command.match( command )):
            self.has_focus = True
            #print "Match 2",self.rule_re_command.pattern, command
            return True
        elif(self.rule_re_application.pattern and self.rule_re_application.match( app )):
            self.has_focus = True
            #print "Match 3",self.rule_re_application.pattern, app
            return True
        elif(self.rule_re_application.pattern and self.rule_re_application.match( command )):
            self.has_focus = True
            #print "Match 4",self.rule_re_application.pattern, command
            return True
        return False

    def __fade_in(self):
        self.volume_target = self.volume_default

    def __fade_out(self):
        if self.volume_mute == -1:
            self.volume_target = self.core.mute_level
        else:
            self.volume_target = self.volume_mute

    def __fade_mute(self):
        self.volume_target = self.volume_step # if we goto 0 than our volume meter will never register a value
    
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


    def to_xml(self, el):

        # Set attributes to user element
        el.setAttribute("name", self.name)
        el.setAttribute("description", str(self.description))
        el.setAttribute("volume_default", str(self.volume_default))
        el.setAttribute("volume_mute", str(self.volume_mute))
        el.setAttribute("rule_re_window_title",self.rule_re_window_title.pattern)
        el.setAttribute("rule_re_command",self.rule_re_command.pattern)
        el.setAttribute("rule_re_application",self.rule_re_application.pattern)
        el.setAttribute("category",self.category)
        el.setAttribute("window_position_fade", str(self.window_position_fade))
        el.setAttribute("icon_name", str(self.icon_name))
        el.setAttribute("apply_volume_meter_hack", str(self.apply_volume_meter_hack))
        el.setAttribute("fade_volume", str(self.fade_volume))
        el.setAttribute("output", self.output)

        if self.category == "default":
            self.category = "event"

    def from_xml(self, el):
        if(el.hasAttribute("name")) :                   self.name = el.getAttribute("name")
        if(el.hasAttribute("description")) :            self.description = el.getAttribute("description")
        if(el.hasAttribute("icon_name")) :              self.icon_name = el.getAttribute("icon_name")
        if(el.hasAttribute("volume_default")) :         self.volume_default = int(el.getAttribute("volume_default"))
        #self.volume_mute = int(el.getAttribute("volume_mute"))
        if(el.hasAttribute("rule_re_window_title")) :   self.rule_re_window_title = re.compile(el.getAttribute("rule_re_window_title"), re.IGNORECASE)
        if(el.hasAttribute("rule_re_command")) :        self.rule_re_command = re.compile(el.getAttribute("rule_re_command"), re.IGNORECASE)
        if(el.hasAttribute("rule_re_application")) :    self.rule_re_application = re.compile(el.getAttribute("rule_re_application"), re.IGNORECASE)
        if(el.hasAttribute("category")) :               self.category = el.getAttribute("category")
        if(el.hasAttribute("window_position_fade")) :   self.window_position_fade = el.getAttribute("window_position_fade") == "True"
        if(el.hasAttribute("apply_volume_meter_hack")): self.apply_volume_meter_hack = el.getAttribute("apply_volume_meter_hack") == "True"
        if(el.hasAttribute("fade_volume")):             self.fade_volume = el.getAttribute("fade_volume") == "True"
        if(el.hasAttribute("output")):                  self.output = el.getAttribute("output")

