import time
import sys

from ParCur import par
from Curses import Curses

if __name__ == '__main__':

    server = None
    if len(sys.argv) > 1 and sys.argv[1] == '--server':
        server = sys.argv[2]
    elif len(sys.argv) > 1:
        print "Usage: parcur [--server host]"
        sys.exit(1)

    cur = Curses()

    # ok now we update
    par.cur = cur
    par.run(server)

    # and run
    cur.run()
