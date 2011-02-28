import curses 

from pulseaudio.PulseAudio import PA_VOLUME_CONVERSION_FACTOR, PA_SINK_RUNNING, PA_SINK_SUSPENDED, PA_SINK_IDLE

MODE_NORMAL = 0
MODE_MOVE = 1

state_colors = { }
state_colors[PA_SINK_RUNNING] = 3
state_colors[PA_SINK_SUSPENDED] = 4
state_colors[PA_SINK_IDLE] = 1


class CursesSink():

    def __init__(self):

        self.active_sink = 0
        self.sinkchars = "werty"

        self.show_data = True

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

        inputcount = { }
        for input in par.pa_sink_inputs.values():
            if input.sink in inputcount:
                inputcount[input.sink] += 1
            else:
                inputcount[input.sink] = 1

        # print the available sinks
        for sink in par.pa_sinks.values():
            if i > 0:
                win.addstr(" | ")
            win.addstr(self.sinkchars[i] + ": ")

            win.addstr(sink.name, curses.color_pair(state_colors[sink.state]) | (curses.A_BOLD if i == self.active_sink else 0))

            if sink.index in inputcount and inputcount[sink.index] > 0:
                win.addstr(" [" + str(inputcount[sink.index]) + "]")

            i += 1

        # print the active sink
        if len(par.pa_sinks) > 0:
            # show some controls
            par.pa_sinks[self.active_sink].draw_controls(win.derwin(2, 0), self.cursor)

            # and some statistics and data
            if self.show_data:
                par.pa_sinks[self.active_sink].draw_info(win.derwin(34, 0))

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
