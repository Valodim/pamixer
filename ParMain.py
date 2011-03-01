import time
import sys

from ParCur import par
from Curses import Curses

if __name__ == '__main__':

    cur = Curses()

    par.run()
    # give pulseaudio a chance to report on stuff first
    time.sleep(0.1)
    # and run
    cur.run()
    # ok now we update
    par.cur = cur
    sys.exit(1)

    while True:
        time.sleep(1)
    # par.exit()
