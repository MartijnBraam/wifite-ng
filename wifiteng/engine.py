from wifiteng.aircrack import *


class Engine:

    def __init__(self, userinterface):
        self.ui = userinterface

    def run(self):
        airmon = Airmon()
        interfaces = airmon.list()

        # Check if any interface is in monitor mode
        if any(x.is_monitor for x in interfaces):
            self.ui.warning("Interface in monitor mode found.")
            no_reset = self.ui.ask("Do you want to use the current monitor configuration?")
            if no_reset:
                self.ui.info("Using current monitor configuration")
            else:
                self.ui.info("")


        self.ui.menu("Main menu", [
            "Scan networks",
            "List cracked networks",
            "Quit"])

        self.ui.info("Scanning for 5 seconds...")
        airodump = Airodump()
        stations = airodump.get_stations('mon0')
        columns = ("ESSID", "BSSID", "Power", "Security", "Packets")
        data = []
        for ap in stations[0]:
            row = (ap.essid, ap.bssid, str(ap.power), str(ap.security), str(ap.iv))
            data.append(row)
        self.ui.table(columns, data)