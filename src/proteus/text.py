class Text(object):
    def __init__(self):
        self.data = ""

    def __str__(self):
        return "TEXT {}".format(self.data)

    def parse_from_xml(self, xml):
        self.data = str(xml.get('data'))
