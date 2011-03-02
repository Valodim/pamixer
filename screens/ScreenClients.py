import curses 

from pulseaudio.PulseAudio import PA_VOLUME_CONVERSION_FACTOR, PA_SINK_RUNNING, PA_SINK_SUSPENDED, PA_SINK_IDLE

MODE_NORMAL = 0
MODE_MOVE = 1

state_colors = { }
state_colors[PA_SINK_RUNNING] = 3
state_colors[PA_SINK_SUSPENDED] = 4
state_colors[PA_SINK_IDLE] = 1

class ScreenClients():

    def __init__(self):

        self.active_client = -1
        self.clientchars = "werty"

        self.show_data = True

        self.win = None
        self.wclientlist = None

        # 0 = 
        self.mode = MODE_NORMAL
        return

    def layout(self, win):
        self.win = win

        maxy, maxx = win.getmaxyx()

        # window for the sink list
        self.wclientlist = win.derwin(1, maxx, 0, 0)

        # window for the active sink
        self.wactiveclient = win.derwin(2, 0)

        # print the active sink
        if len(par.pa_sinks) > 0:
            # show some controls
            par.pa_clients[self.active_client].layout(self.wactiveclient)

        # initial redraw
        self.redraw()

    def redraw(self, recurse = False):
        if self.wclientlist is None:
            return

        if self.active_client == -1 and len(par.pa_clients) > 0:
            # self.active_client = 0
            par.pa_clients[self.active_client].layout(self.wactiveclient)

        inputcount = { }
        for input in par.pa_sink_inputs.values():
            if input.client in inputcount:
                inputcount[input.client] += 1
            else:
                inputcount[input.client] = 1

        wclientlist = self.wclientlist

        wclientlist.erase()
        wclientlist.move(0, 1)

        i = 0
        # print the available clients
        for client in par.pa_clients.values():
            if i > 0:
                wclientlist.addstr(" | ")
            wclientlist.addstr(self.clientchars[i] + ": ")

            wclientlist.addstr(client.name, curses.color_pair(curses.A_BOLD if i == self.active_client else 0))

            if client.index in inputcount and inputcount[client.index] > 0:
                wclientlist.addstr(" [" + str(inputcount[client.index]) + "]")

            i += 1

        if recurse and self.active_client in par.pa_clients:
            par.pa_clients[self.active_client].redraw(True)

        wclientlist.refresh()

        return

    def key_event(self, event):
        return False

        if self.mode == MODE_NORMAL:

            # cheating a little here, don't allow move on the own volume
            if par.pa_sinks[self.active_sink].cursor >= 0 and event == ord("m"):
                self.mode = MODE_MOVE
                return True

            # sink range
            for i in range(0, len(self.sinkchars)):
                if event == ord(self.sinkchars[i]) and par.pa_sinks.has_key(i):
                    par.pa_sinks[self.active_sink].layout(None)
                    self.active_sink = i
                    par.pa_sinks[self.active_sink].layout(self.wactivesink)
                    self.redraw()
                    return True

            return par.pa_sinks[self.active_sink].key_event(event)

        elif self.mode == MODE_MOVE:

            # sink range
            for i in range(0, len(self.sinkchars)):
                if event == ord(self.sinkchars[i]) and par.pa_sinks.has_key(i):
                    # tell the sink to move this thing around
                    par.pa_sinks[self.active_sink].moveInput(i)
                    # return to normal mode
                    self.mode = MODE_NORMAL
                    return False

            self.mode = MODE_NORMAL

        return False

from ParCur import par
