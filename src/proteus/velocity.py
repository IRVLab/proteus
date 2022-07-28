class Velocity(object):
    def __init__(self, surge, sway, heave):
        self.surge = float(surge)
        self.sway = float(sway)
        self.heave = float(heave)

    def __str__(self):
        return "VELOCITY {} surge, {} sway, {} heave".format(self.surge, self.sway, self.heave)

    def parse_from_xml(self, xml):
        self.surge = str(xml.get('surge'))
        self.sway = str(xml.get('sway'))
        self.heave = str(xml.get('heave'))