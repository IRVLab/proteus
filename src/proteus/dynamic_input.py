
class DynamicInput(object):
    def __init__(self):
        self.topic = ''
        self.type = ''

    def parse_from_xml(self, xml):
        self.topic = str(xml.get('topic'))
        self.type = str(xml.get('type'))

