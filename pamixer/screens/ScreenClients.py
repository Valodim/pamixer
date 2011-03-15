import curses 

from ..PulseAudio import PA_SINK_RUNNING, PA_SINK_SUSPENDED, PA_SINK_IDLE

MODE_NORMAL = 0
MODE_MOVE = 1

state_colors = { }
state_colors[PA_SINK_RUNNING] = 3
state_colors[PA_SINK_SUSPENDED] = 4
state_colors[PA_SINK_IDLE] = 1

class ScreenClients():

    def __init__(self):

        self.active_client = -1
        self.clientchars = "wertyuiopWERTYUIOP"

        self.show_data = True

        self.win = None
        self.wclientlist = None

        self.drawable = False

        return

    def layout(self, win):
        if win is None:
            self.drawable = False
            if self.active_client >= 0 and self.active_client < len(par.pa_clients.values()):
                par.pa_clients.values()[self.active_client].layout(None)
            return

        self.drawable = True

        self.win = win
        maxy, maxx = win.getmaxyx()

        # window for the client list
        self.wclientlist = win.derwin(1, maxx, 0, 0)

        # window for the active client
        self.wactiveclient = win.derwin(2, 0)

        # print the active client
        if len(par.pa_clients) > 0:
            # reset if invalid
            if self.active_client == -1 or self.active_client >= len(par.pa_clients):
                self.active_client = 0
            # show some controls
            par.pa_clients.values()[self.active_client].layout(self.wactiveclient)

        # initial redraw
        self.redraw()

    def redraw(self, recurse = False):
        if self.drawable is False:
            return

        if self.active_client == -1 and len(par.pa_clients) > 0:
            # self.active_client = 0
            par.pa_clients.values()[self.active_client].layout(self.wactiveclient)

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

            wclientlist.addstr(client.name, curses.A_BOLD if i == self.active_client else 0)

            if client.index in inputcount and inputcount[client.index] > 0:
                wclientlist.addstr(" [" + str(inputcount[client.index]) + "]")

            i += 1

        if recurse and self.active_client < len(par.pa_clients):
            par.pa_clients.values()[self.active_client].redraw(True)


        return

    def key_event(self, event):

        if True or self.mode == MODE_NORMAL:

            # cheating a little here, don't allow move on the own volume
            # if par.pa_sinks[self.active_sink].cursor >= 0 and event == ord("m"):
                # self.mode = MODE_MOVE
                # return True

            # sink range
            for i in range(0, min(len(par.pa_clients), len(self.clientchars))):
                if event == ord(self.clientchars[i]):
                    if self.active_client == i:
                        return True
                    par.pa_clients.values()[self.active_client].layout(None)
                    self.active_client = i
                    par.pa_clients.values()[self.active_client].layout(self.wactiveclient)
                    self.redraw()
                    return True

            return par.pa_clients.values()[self.active_client].key_event(event)

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

    def getActiveVolume(self):
        return par.pa_clients.values()[self.active_client].getActiveVolume()

    def draw_help(self, win):
        win.attron(curses.A_BOLD)
        win.addstr("  Keys - Clients\n")
        win.addstr("-----------------------------------------")
        win.attroff(curses.A_BOLD)
        win.addstr("""
       h / Left\t\t: Move Cursor left
       l / Right\t: Move Cursor right

       enter\t\t: detailed volume control

       k / Up\t\t: Volume Up
       j / Down\t\t: Volume Down
       K\t\t: Volume Up, ignore soft limit
       J\t\t: Volume Down, ignore soft limit
       n\t\t: Set selected volume to 1.0
       m\t\t: Set selected volume to 0.0 (Mute)
       N\t\t: Set all volumes to 1.0
       M\t\t: Set all volumes to 0.0 (Mute)

       X\t\t: Kill Sink Input


""")

from ..ParCur import par
