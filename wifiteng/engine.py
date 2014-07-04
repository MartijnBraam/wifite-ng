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