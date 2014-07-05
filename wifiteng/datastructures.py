from datetime import datetime


class Interface:

    def __init__(self, interface, chipset, driver, device):
        self.interface = interface
        self.chipset = chipset
        self.driver = driver
        self.device = device

    @staticmethod
    def from_tuple(input_tuple):
        interface = input_tuple[0]
        chipset = input_tuple[1]
        driver = input_tuple[2]
        device = input_tuple[3]
        return Interface(interface, chipset, driver, device)

    @property
    def is_monitor(self):
        return self.interface.startswith("mon")

    def __repr__(self):
        return "<Interface {} driver={} chipset={} device={}>".format(self.interface, self.driver, self.chipset, self.device)


class Security:

    def __init__(self, privacy, cipher, authentication):
        self.privacy = privacy
        self.cipher = cipher
        self.authentication = authentication

    def __repr__(self):
        if self.privacy == "WEP":
            return "<Security WEP>"
        else:
            return "<Security {} {} {}>".format(self.privacy, self.cipher, self.authentication)

    def __str__(self):
        if self.privacy == "WEP":
            return "WEP"
        else:
            return "{} {} {}".format(self.privacy, self.cipher, self.authentication)


class Accesspoint:

    def __init__(self, bssid, essid, channel, power, speed, security, beacons, iv, first, last, ip, key=None):
        self.bssid = bssid
        self.essid = essid
        self.channel = channel
        self.power = power
        self.security = security
        self.beacons = beacons
        self.iv = iv
        self.first = first
        self.last = last
        self.ip = ip
        self.key = key

    @staticmethod
    def from_tuple(input_tuple):
        bssid = input_tuple[0]
        first = datetime.strptime(input_tuple[1], "%Y-%m-%d %H:%M:%S")
        last = datetime.strptime(input_tuple[2], "%Y-%m-%d %H:%M:%S")
        channel = int(input_tuple[3])
        speed = int(input_tuple[4])
        privacy = input_tuple[5]
        cipher = input_tuple[6]
        authentication = input_tuple[7]
        power = int(input_tuple[8])
        beacons = int(input_tuple[9])
        iv = int(input_tuple[10])
        ip = input_tuple[11].replace(" ", "")
        essid = input_tuple[12]
        key = input_tuple[13]

        if key == "":
            key = None

        security = Security(privacy, cipher, authentication)

        return Accesspoint(bssid, essid, channel, power, speed, security, beacons, iv, first, last, ip, key)

    def __repr__(self):
        return "<Accesspoint {} ssid={} channel={} power={} key={}>".format(self.bssid, self.essid, self.channel, self.power, self.key)