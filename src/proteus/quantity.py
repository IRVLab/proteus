class Quantity(object):
    def __init__(self, disp=None, amnt=None):
        self.display_on= disp
        self.amount = amnt

    def __str__(self):
        return "QUANT on {} of {}".format(self.amount, self.display_on)

    def parse_from_xml(self, xml):
        self.display_on = str(xml.get('display-on'))
        self.amount = float(xml.get('amount'))