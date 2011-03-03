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
import curses

from xml.dom.minidom import *
from CursesHelpers import *

class Sample():

    def __init__(self, index, struct):
        self.index = index

        self.update(index, struct)

        # -1 is volume, 0 and above are sink inputs
        self.cursor = -1

    def update(self, index, struct):
        self.name = struct.name

from ParCur import par
