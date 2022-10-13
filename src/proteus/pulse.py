class Pulse(object):
    def __init__(self):
        self.vary = None
        self.cycles = None

    def __str__(self):
        return "PULSE on {}, {} cycles".format(self.vary, self.frequency)

    def parse_from_xml(self, xml):
        self.vary = str(xml.get('vary_param'))
        self.cycles = int(xml.get('cycles'))