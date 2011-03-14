#!/usr/bin/env python2.7

import time
import sys
import argparse

try:
    import pulseaudio.lib_pulseaudio
except ImportError:
    sys.stderr.write("Could not find lib_pulseaudio - Did you initialize the git submodule?\n")
    sys.stderr.write("See README for more details.\n")
    sys.exit(1)

from pamixer.ParCur import par
from pamixer.Curses import Curses

if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--server', dest='server', default=None, metavar='host', help='the server hostname to connect to')
    parser.add_argument('-v', '--verbose', dest='verbose', action='store_true', help='turn on verbose output to stderr')
    args = parser.parse_args()

    cur = Curses(args.verbose)

    # ok now we update
    par.run(args.server)

    time.sleep(0.1)

    par.cur = cur
    # and run
    cur.run()
