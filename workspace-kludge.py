#!/usr/bin/env python3

from gi.repository import Wnck, Gtk, Notify
from threading import Timer
import signal, time

class Kludge:
    def __init__(self):
        self.first = True
        signal.signal(signal.SIGINT, signal.SIG_DFL)
        self.screen = Wnck.Screen.get_default()
        Notify.init("Workspace Switch Notifier")

    def fire_the_kludge(self, data_a, data_b):
        if self.popup:
            self.popup.close()

        try:
            active_workspace = self.screen.get_active_workspace()
            workspace_name = str(active_workspace.get_name())
            workspace_number = active_workspace.get_number()
            workspace_x = active_workspace.get_layout_column()
            workspace_y = active_workspace.get_layout_row()
            print("Workspace %d (%d,%d)" % (workspace_number, workspace_x, workspace_y))
            print(self.workspace_grid(workspace_x, workspace_y))

            message = workspace_name + "\n" + self.workspace_grid(workspace_x, workspace_y)
        except:
            message = "Workspace Kludge: Some error happened"

        self.popup = Notify.Notification.new(message)
        self.popup_count += 1
        self.popup.show()
        t = Timer(2, self.close_callback)
        t.start()

    def close_callback(self):
        if self.popup_count > 1:
            self.popup_count -= 1
            return

        if self.popup:
            self.popup.close()
        self.popup = None

        self.popup_count -= 1
        print("close_callback");

    def workspace_grid(self, x, y):
        string = ''
        for j in range(self.rows):
            # top line
            for i in range(self.columns*2 + 1):
                string += '-'
            string += '\n'

            # content line
            for i in range(self.columns*2 + 1):
                if i == (x*2+1) and j == y:
                    string += '*'
                elif (i == 0 or i == (self.columns*2) or ((i%2) == 0)):
                    string += '|'
                else:
                    string += ' '
            string += '\n'
        # bottom line
        for i in range(self.columns*2 + 1):
            string += '-'
        string += '\n'
        return string

    def main(self):
        self.screen.connect("active-workspace-changed", self.fire_the_kludge)
        self.columns = 3
        self.rows = 4
        self.popup = None
        self.popup_count = 0
        Gtk.main()

if __name__ == '__main__':
    print("Here comes the kludge")
    kludge = Kludge()
    kludge.main()
