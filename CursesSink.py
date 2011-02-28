import curses 

MODE_NORMAL = 0
MODE_MOVE = 1

class CursesSink():

    def __init__(self):

        self.active_sink = 0
        self.sinkchars = "werty"

        # -1 is volume, 0 and above are sink inputs
        self.cursor = -1
        # 0 = 
        self.mode = MODE_NORMAL
        return

    def cursorCheck(self):
        """
        Moves the cursor to the left until there is a sink input,
        or it's at the sink's volume.
        """
        sink_inputs = par.get_sink_inputs_by_sink(self.active_sink)
        while self.cursor >= len(sink_inputs):
            self.cursor -= 1
        if self.cursor < -1:
            self.cursor = -1

    def draw(self, win):
        self.cursorCheck()

        win.move(0, 1)
        i = 0
        for sink in par.pa_sinks.values():
            if i > 0:
                win.addstr(" | ")
            win.addstr(self.sinkchars[i] + ": ")
            win.addstr(sink.name, curses.A_BOLD if i == self.active_sink else 0)
            i += 1

        if len(par.pa_sinks) == 0:
           return

        par.pa_sinks[self.active_sink].draw(win.derwin(2, 0), self.cursor)

        return

    def key_event(self, event):
        if self.mode == MODE_NORMAL:

            if self.cursor >= 0 and event == ord("m"):
                self.mode = MODE_MOVE
                return False

            # change focus
            if event == curses.KEY_LEFT or event == curses.KEY_RIGHT:
                self.cursor += -1 if event == curses.KEY_LEFT else +1
                return False

            elif event == curses.KEY_UP or event == curses.KEY_DOWN:
                par.pa_sinks[self.active_sink].changeVolume(self.cursor, event == curses.KEY_UP)
                return False

            # sink range
            for i in range(0, len(self.sinkchars)):
                if event == ord(self.sinkchars[i]) and par.pa_sinks.has_key(i):
                    self.active_sink = i
                    self.cursorCheck()
                    return False

        elif self.mode == MODE_MOVE:

            # sink range
            for i in range(0, len(self.sinkchars)):
                if event == ord(self.sinkchars[i]) and par.pa_sinks.has_key(i):
                    # get the sink inputs of current sink
                    sink_inputs = par.get_sink_inputs_by_sink(self.active_sink)
                    # move the selected sink input to the new sink
                    par.move_sink_input(sink_inputs[self.cursor].index, par.pa_sinks[i].index)
                    self.mode = MODE_NORMAL
                    return False

            self.mode = MODE_NORMAL

        return False

from ParCur import par