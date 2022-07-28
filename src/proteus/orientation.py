class Orientation(object):
    def __init__(self, r=None, p=None ,y=None):
        self.roll = r
        self.pitch = p
        self.yaw = y

    def  __str__(self):
        return "ORIENTATION ({},{},{})".format(self.roll, self.pitch, self.yaw)

    def parse_from_xml(self, xml):
        self.roll = float(xml.get('roll'))
        self.pitch = float(xml.get('pitch'))
        self.yaw = float(xml.get('yaw'))