from wifiteng.helpers import ShellTool
from wifiteng.datastructures import Interface
import re


class Airmon(ShellTool):

    regex_list = re.compile(r"(?P<interface>[a-z]+[0-9]+)\s+(\w+)\s+(?P<driver>\w+)\s-\s\[(?P<device>[a-z]+[0-9]+)\]")

    def start(self, interface, channel=None):
        command = ["airmon-ng", "start", interface]
        if not channel is None:
            command.append(channel)

        self.call_and_communicate(command, 10)

    def stop(self, interface):
        command = ["airmon-ng", "stop", interface, 10]
        self.call_and_communicate(command)

    def list(self):
        command = ["airmon-ng"]
        (returncode, stdout, stderr) = self.call_and_communicate(command, 10)
        interfaces = Airmon.regex_list.findall(stdout)
        returnvalue = []
        for interface in interfaces:
            returnvalue.append(Interface.from_tuple(interface))
        return returnvalue