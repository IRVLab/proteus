import uuid

class Illumination(object):
    def __init__(self, id=None, col=None, bright=None):
        self.id = id
        self.color_id = col
        self.brightness = bright
        
    def __str__(self):
        return "ILLUMINATION({}) {} at {} brightness".format(self.id, self.color_id, self.brightness)

    def parse_from_xml(self, xml):
        self.id = str(xml.get('id', default=uuid.uuid1()))
        self.color_id = str(xml.get('color'))
        self.brightness = float(xml.get('brightness'))