import curses 

MODE_NORMAL = 0
MODE_MOVE = 1

class CursesSink():

    def __init__(self, par):
        self.par = par

        self.active_sink = 0
        self.sinkchars = "werty"

        # -1 is volume, 0 and above are sink inputs
        self.cursor = -1
        # 0 = 
        self.mode = MODE_NORMAL
        return

    def draw(self, win):

        win.move(0, 1)
        i = 0
        for sink in self.par.pa_sinks.values():
            win.addstr(self.sinkchars[i], curses.A_BOLD)
            win.addstr(": #" + str(sink.index) + " " + sink.name + " ")
            i += 1

        if len(self.par.pa_sinks) == 0:
           return

        self.par.pa_sinks[self.active_sink].draw(win.derwin(2, 0), self.par, self.cursor)

        return

    def key_event(self, event):
        if self.mode == MODE_NORMAL:

            if self.cursor >= 0 and event == ord("m"):
                self.mode = MODE_MOVE

            # change focus
            if event == curses.KEY_LEFT or event == curses.KEY_RIGHT:
                self.cursor += -1 if event == curses.KEY_LEFT else +1

                sink_inputs = self.par.get_sink_inputs_by_sink(self.index)

                # special case: no sink inputs at all
                if len(sink_inputs) == 0 or self.cursor < -1:
                    self.cursor = -1
                elif self.cursor >= len(sink_inputs):
                    self.cursor = len(sink_inputs) -1

            elif event == curses.KEY_UP or event == curses.KEY_DOWN:
                self.par.pa_sinks[self.active_sink].changeVolume(self.par, self.cursor, event == curses.KEY_UP)
                return True

            # sink range
            for i in range(0, len(self.sinkchars)):
                if event == ord(self.sinkchars[i]) and self.par.pa_sinks.has_key(i):
                    self.active_sink = i
                    return True

        elif self.mode == MODE_MOVE:

            # sink range
            for i in range(0, len(self.sinkchars)):
                if event == ord(self.sinkchars[i]) and self.par.pa_sinks.has_key(i):
                    # get the sink inputs of current sink
                    sink_inputs = self.par.get_sink_inputs_by_sink(i)
                    # move the selected sink input to the new sink
                    par.move_sink_input(sink_inputs[self.cursor].index, self.par.pa_sinks[i].index)
                    return True

            self.mode = MODE_NORMAL

        return

