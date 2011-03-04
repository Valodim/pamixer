#!/usr/bin/env python

import time
import sys
import argparse

from ParCur import par
from Curses import Curses

if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--server', dest='server', default=None, metavar='host', help='the server hostname to connect to')
    parser.add_argument('-v', '--verbose', dest='verbose', action='store_true', help='turn on verbose output to stderr')
    args = parser.parse_args()

    cur = Curses(args.verbose)

    # ok now we update
    par.cur = cur
    par.run(args.server)

    # and run
    cur.run()
