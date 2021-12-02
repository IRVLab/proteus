from proteus.node import Node

class KNode(Node):
    def __init__(self, id, prev, nex, desc, pos, orr, velo, dur):
        super().__init__(id, prev, nex, desc)
        self.position = pos
        self.orientation = orr
        self.velocity = velo
        self.duration = dur

class Kineme(object):
    def __init__(self):
        self.name = None
        self.id = None
        self.symbol = None
    
    def parse_from_xml(self, xml_object):
        pass