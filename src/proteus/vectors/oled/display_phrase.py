from builtins import super
from proteus.symbols.node import Node
from proteus.symbols.text import Text
from proteus.symbols.duration import Duration

class DNode(Node):
    def __init__(self):
        super().__init__()
        self.text = None
        self.duration = None

    def __str__(self):
        return "{0} TEXT({1.text}) DUR({1.duration})".format(super().__str__(), self)

    def parse_from_xml(self, xml):
        super().parse_from_xml(xml)

        for item in xml:
            if item.tag == 'text':
                self.text = Text()
                self.text.parse_from_xml(item)
            elif item.tag == 'duration':
                self.duration = Duration()
                self.duration.parse_from_xml(item)

class DisplayPhrase(object):
    def __init__(self):
        self.name = None
        self.id = None
        self.call_type = None
        self.dnodes = list()

    def __str__(self):
        s = "DISLAYP PHRASE (%s) %s\n"%(self.id, self.name)
        for d in self.dnodes:
            s += "... %s\n"%(str(d))
        return s

    def set_call_type(self, call_type):
        self.call_type = call_type
    
    def parse_from_xml(self, xml_object):
        self.name = xml_object.get('name')
        self.id = xml_object.get('id')
        # Can't set symbol or call_type here, we'll do that later, we've gotta do that once we do a match between symbol ids and kineme ids.

        #TODO Add error handling to kick back kinemes with KNodes that don't match their trigger type. This needs to be dealt with at this level, not at the execution level.
        #TODO Additionally, we should have a sdf syntax checker that can be run seperately.

        # Now we have to parse the KNodes.
        for ddef in xml_object:
            type = ddef.tag
            if type == 'dnode':
                d = DNode()
                d.parse_from_xml(ddef)
                self.dnodes.append(d)
