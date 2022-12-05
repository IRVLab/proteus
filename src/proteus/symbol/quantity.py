class Quantity(object):
    def __init__(self, param=None, disp=None, amax=None, amin=None):
        self.parameter = param
        self.display_on= disp
        self.max_amount = amax
        self.min_amount = amin
        

    def __str__(self):
        return "QUANT on ({},{}) of {}".format(self.min_amount, self.max_amount, self.display_on)

    def parse_from_xml(self, xml):
        self.parameter = str(xml.get('parameter'))
        self.display_on = str(xml.get('display_on'))
        self.max_amount = float(xml.get('max'))
        self.min_amount = float(xml.get('min'))