import curses 
import time

class Curses():

    def __init__(self, par):
        self.par = par
        self.counter = 0
        self.screen = None

    def update(self):
        # don't do anything if we aren't active
        if not self.screen:
            return

        self.screen.clear()
        self.screen.addstr("ParCur\n\n")
        for client in self.par.pa_clients_by_id.values():
            self.screen.addstr(client.name + "\n");
            for sink in client.sinks.values():
                self.screen.addstr(" - " + sink.name + "\n");
        self.screen.refresh()
        return

    def run(self):

        self.screen = curses.initscr() 

        curses.noecho()
        curses.curs_set(0)
        self.screen.keypad(1)

        self.update()
        while True: 
            event = self.screen.getch()
            if event == -1:
                continue

            self.update()
            # end of program, just break out
            if event == ord("q"): 
                break 

        curses.endwin()
