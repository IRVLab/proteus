class Velocity(object):
    def __init__(self):
        self.surge = None
        self.sway = None
        self.heave = None

    def __str__(self):
        return "VELOCITY {} surge, {} sway, {} heave".format(self.surge, self.sway, self.heave)

    def parse_from_xml(self, xml):
        self.surge = float(xml.get('surge'))
        self.sway = float(xml.get('sway'))
        self.heave = float(xml.get('heave'))