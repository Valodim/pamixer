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

import math  
import time
import datetime
class Sink():
    def __init__(self, index, name, volume, client, channels=1):

        self.index = index
        self.name = name
        self.client = client
        self.volume = volume
        self.channels = channels

        self.volume_meter = 0
        self.volume_meter_last_non_zero = time.mktime(datetime.datetime.now().timetuple())

        self.__previous_volume = 0

        self.volume_check = True
 
    def set_volume(self):

        current_volume = round(self.volume[1])
        step_volume = current_volume
        result = True

        if current_volume < self.client.volume_target:      
            step_volume = current_volume + self.client.volume_step
            if not self.client.fade_volume: step_volume = self.client.volume_target
        elif current_volume > self.client.volume_target: 
            step_volume = current_volume - self.client.volume_step
            if not self.client.fade_volume: step_volume = self.client.volume_target

        if step_volume > 100:
            step_volume = 100
        if step_volume < self.client.volume_step:
            step_volume = self.client.volume_step

        # we dont want to get stuck in a loop because volumes arn't exactly the same 
        result = math.fabs(self.__previous_volume - current_volume) >= self.client.volume_step
        volume_check = math.fabs(self.client.volume_target - current_volume) < self.client.volume_step

        if result:
            for i in range(0, self.channels+1):
                self.volume[i] = step_volume

            #print "\nAdjust Volume", self.client.name, step_volume

        if volume_check and not self.volume_check:
            self.volume_check = volume_check
            self.client.check_volume()

        self.volume_check = volume_check

        self.__previous_volume = step_volume       
        return result

