from proteus.node import Node
from proteus.text import Text
from proteus.duration import Duration

class DNode(Node):
    def __init__(self, id, desc, text, dur):
        super().__init__(id, desc)
        self.text = text
        self.duration = dur

    def __str__(self):
        return "{0} TEXT({1.text}) DUR({1.duration})".format(super().__str__(), self)

class DisplayPhrase(object):
    def __init__(self):
        self.name = None
        self.id = None
        self.call_type = None
        self.dnodes = list()

    def __str__(self):
        s = "DP (%s) %s\n"%(self.id, self.name)
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
        for n in xml_object:
            type = n.tag
            if type == 'dnode':
                step = int(n.get('step'))
                description = n.get('description')

                text = Text(n[0].get('data'))
                dur = Duration(n[1].get('seconds'))

                self.dnodes.append(DNode(step, description, text, dur))
