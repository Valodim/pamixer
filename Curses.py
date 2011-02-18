import curses 
import time

class Curses():

    def __init__(self, par):
        self.par = par
        self.counter = 0
        self.screen = None

        self.modes = []
        self.modes.append(self.mode_help)
        self.modes.append(self.mode_sinks)

        self.active_mode = 1

    def update(self):
        # don't do anything if we aren't active
        if not self.screen:
            return

        maxy, maxx = self.screen.getmaxyx()

        self.screen.attrset(0)

        self.screen.clear()
        self.screen.move(0, 1)
        self.screen.addstr("1", curses.A_BOLD)# | (curses.COLOR_GREEN if self.active_mode == 1 else 0))
        self.screen.addstr(":Help  ")
        self.screen.addstr("2", curses.A_BOLD)
        self.screen.addstr(":Sinks")
        self.screen.hline(1, 0, curses.ACS_HLINE, maxx)

        self.modes[self.active_mode](self.screen.subwin(2,0))

        return

    def mode_help(self, win):
        return
    def mode_sinks(self, win):
        chars = "qwerty"

        win.move(0, 1)
        i = 0
        for sink in self.par.pa_sinks.values():
            i += 1
            win.addstr(chars[i], curses.A_BOLD)
            win.addstr(":" + sink.name)

        return

        left = 5

        for client in self.par.pa_clients_by_id.values():
            if len(client.sinks) == 0:
                continue

            window = self.screen.subwin(13, left)

            width = 0

            # draw all sinks. we do this first, accumulate the width
            # in the process, and draw the heading afterwards
            for sink in client.sinks.values():

                # reserve width for this sink-input
                width += 15

                # gauge, one bar for each channel
                gauge = window.derwin(22, sink.channels+2, 2, 6-(sink.channels/2))
                for i in range(0, sink.channels+1):
                    barheight = int(sink.volume[i] / 5)
                    gauge.vline(21-barheight, i+1, curses.ACS_BLOCK, barheight)

                window.move(25, 1)
                window.addstr(sink.name[0:15])

                # and a neat border for the gauge
                gauge.border()

            # draw a top line, with centered player name
            window.hline(0, 0, curses.ACS_HLINE, width)
            window.move(0, max( (width/2 -len(client.name)/2 -2, 0) ) )
            window.addstr("  " + client.name + "  ");

            # next one is drawn further to the right
            left += width + 5

        self.screen.border()
        self.screen.refresh()
        return

    def run(self):

        self.screen = curses.initscr() 
        # curses.start_color()

        curses.noecho()
        curses.curs_set(0)
        self.screen.keypad(1)

        self.update()
        while True: 
            event = self.screen.getch()
            if event == -1:
                self.update()
                continue

            self.update()
            # end of program, just break out
            if event == ord("q"): 
                break 

        curses.endwin()
