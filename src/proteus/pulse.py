class Pulse(object):
    def __init__(self):
        self.vary = None
        self.step = None
        self.frequency = None

    def __str__(self):
        return "PULSE on {}, frequency {}, step size of {}".format(self.vary, self.frequency, self.step)

    def parse_from_xml(self, xml):
        self.vary = str(xml.get('vary_param'))
        self.step = float(xml.get('step'))
        self.frequency = float(xml.get('freq'))