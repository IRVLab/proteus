import uuid

class Illumination(object):
    def __init__(self, id=None, col=None, bright=None):
        self.color_id = col
        self.brightness = bright

        if id:
            self.id = id
        else:
            self.id= str(uuid.uuid1())
        
    def __str__(self):
        return "ILLUMINATION({}) {} at {} brightness".format(self.id, self.color_id, self.brightness)

    def parse_from_xml(self, xml):
        self.color_id = str(xml.get('color'))
        self.brightness = float(xml.get('brightness'))