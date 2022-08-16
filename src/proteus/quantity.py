class Quantity(object):
    def __init__(self, disp=None, max=None, min=None):
        self.display_on= disp
        self.max_amount = max
        self.min_amount = min

    def __str__(self):
        return "QUANT on ({},{}) of {}".format(self.min_amount, self.max_amount, self.display_on)

    def parse_from_xml(self, xml):
        self.display_on = str(xml.get('display-on'))
        self.max_amount = float(xml.get('max'))
        self.min_amount = float(xml.get('min'))