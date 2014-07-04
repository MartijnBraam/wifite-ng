from wifiteng.helpers import ShellTool


class Airmon(ShellTool):

    def start(self, interface, channel=None):
        command = ["airmon-ng", "start", interface]
        if not channel is None:
            command.append(channel)

        self.call_and_communicate(command, 10)

    def stop(self, interface):
        command = ["airmon-ng", "stop", interface]
        self.call_and_communicate(command)