class Position(object):
    def __init__(self, x=None, y=None, z=None):
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)
    
    def __str__(self):
        return "POSITION: ({},{},{})".format(self.x, self.y, self.z)

    def parse_from_xml(self, xml):
        self.x = float(xml.get('x'))
        self.y = float(xml.get('y'))
        self.z = float(xml.get('z'))
