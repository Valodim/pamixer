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
