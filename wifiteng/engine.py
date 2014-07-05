from wifiteng.aircrack import *


class Engine:

    def __init__(self, userinterface):
        self.ui = userinterface

    def run(self):
        airmon = Airmon()
        airmon.list()

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