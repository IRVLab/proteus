class Duration(object):
    def __init__(self, sec=None):
        self.seconds = sec

    def __str__(self):
        return "DURATION of {} seconds.".format(self.seconds)

    def parse_from_xml(self, xml):
        self.second = float(xml.get('seconds'))
