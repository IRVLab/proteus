class Blink(object):
    def __init__(self, per=None, iters=None):
        self.period = per
        self.iterations = iters
        
    def __str__(self):
        return " BLINK {}x, period {}".format(self.iterations, self.period)

    def parse_from_xml(self, xml):
        self.period = int(xml.get('period'))
        self.iterations = int(xml.get('iterations'))