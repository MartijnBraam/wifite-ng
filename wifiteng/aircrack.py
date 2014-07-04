from wifiteng.helpers import ShellTool
from wifiteng.datastructures import Interface
import re


class Airmon(ShellTool):
    """This class handles all the communication with the airmon-ng tool from the aircrack-ng suite."""
    regex_list = re.compile(r"(?P<interface>[a-z]+[0-9]+)\s+(\w+)\s+(?P<driver>\w+)\s-\s\[(?P<device>[a-z]+[0-9]+)\]")

    def start(self, interface, channel=None):
        """ Set an interface in monitor mode
        :param interface: interface name (like wlan0).
        :param channel: optional channel number to tune to.
        :return: None
        """
        command = ["airmon-ng", "start", interface]
        if not channel is None:
            command.append(str(channel))

        self.call_and_communicate(command, 10)

    def stop(self, interface):
        """ Disable monitor mode for an interface
        :param interface: interface name (like wlan0)
        :return: None
        """
        command = ["airmon-ng", "stop", interface, 10]
        self.call_and_communicate(command)

    def list(self):
        """ Retrieve a list of wireless interfaces and their associated physical device
        :return: List of Interface objects
        """
        command = ["airmon-ng"]
        (returncode, stdout, stderr) = self.call_and_communicate(command, 10)
        interfaces = Airmon.regex_list.findall(stdout)
        returnvalue = []
        for interface in interfaces:
            returnvalue.append(Interface.from_tuple(interface))
        return returnvalue