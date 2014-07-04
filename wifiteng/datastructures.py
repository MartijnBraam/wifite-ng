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