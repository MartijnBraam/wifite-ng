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


class Airodump(ShellTool):

    regex_ap = re.compile(r"""^(?P<bssid>(?:[0-9A-F]{2}[:-]){5}(?:[0-9A-F]{2})) # Match a mac address
                                    \s*,\s*
                                    (?P<firstseen>\d{4}-\d{2}-\d{2}\ \d{2}:\d{2}:\d{2}) # Match a airdump-ng datetime
                                    \s*,\s*
                                    (?P<lastseen>\d{4}-\d{2}-\d{2}\ \d{2}:\d{2}:\d{2}) # Match a airdump-ng datetime
                                    \s*,\s*
                                    (?P<channel>\d{1,2})
                                    ,\s*
                                    (?P<speed>\d{1,3})
                                    ,\s*
                                    (?P<privacy>[0-9A-Z]+)
                                    \s*,\s*
                                    (?P<cipher>[A-Z]+)
                                    \s*,\s*
                                    (?P<authentication>[A-Z]*)
                                    ,\s*
                                    (?P<power>-?\d+)
                                    ,\s*
                                    (?P<beacons>\d+)
                                    ,\s*
                                    (?P<iv>\d+)
                                    ,\s*
                                    (?P<ip>\d{1,3}\.[\s\d]+\.[\s\d]+\.[\s\d]+) # Match a padded IPv4 address
                                    ,\s*
                                    (?:\d+)
                                    ,\s*
                                    (?P<essid>[\w-]+)
                                    ,\s*
                                    (?P<key>[\w-]*)$ # Match the key, if it exists""", re.MULTILINE | re.VERBOSE)

    regex_client = re.compile(r"""^(?P<mac>(?:[0-9A-F]{2}[:-]){5}(?:[0-9A-F]{2})) # Match a mac address
                                    \s*,\s*
                                    (?P<firstseen>\d{4}-\d{2}-\d{2}\ \d{2}:\d{2}:\d{2}) # Match a airdump-ng datetime
                                    \s*,\s*
                                    (?P<lastseen>\d{4}-\d{2}-\d{2}\ \d{2}:\d{2}:\d{2}) # Match a airdump-ng datetime
                                    \s*,\s*
                                    (?P<power>-?\d+)
                                    ,\s*
                                    (?P<packets>\d+)
                                    ,\s*
                                    (?P<bssid>(?:[0-9A-F]{2}[:-]){5}(?:[0-9A-F]{2})) # Match a mac address
                                    ,\s*
                                    (?P<key>[\w-]*)$ # Match the probes, if they exist""", re.MULTILINE | re.VERBOSE)

    pass