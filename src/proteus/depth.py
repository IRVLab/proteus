class Depth(object):
    def __init__(self, amnt=None, mode=None):
        self.amount = float(amnt)
        self.mode = str(mode)

    def __str__(self):
        return "DEPTH: {}m, {} mode".format(self.amount, self.mode)

    def parse_from_xml(self, xml):
        self.amount = float(xml.get('amount'))
        self.mode = float(xml.get('mode'))