import time
import sys

from ParCur import par
from Curses import Curses

if __name__ == '__main__':

    cur = Curses()

    par.run(cur)
    cur.run()
    sys.exit(1)

    while True:
        time.sleep(1)
    # par.exit()
