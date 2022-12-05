class Depth(object):
    def __init__(self,):
        self.amount = None
        self.mode = None

    def __str__(self):
        return "DEPTH: {}m, {} mode".format(self.amount, self.mode)

    def parse_from_xml(self, xml):
        self.amount = float(xml.get('amount'))
        self.mode = str(xml.get('mode'))