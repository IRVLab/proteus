from proteus.node import Node
from proteus.blink import Blink
from proteus.color_map import ColorMapping
from proteus.color import Color
from proteus.fill import Fill
from proteus.illumination import Illumination
from proteus.pulse import Pulse
from proteus.ring import Ring
from proteus.sector import Sector

class LNode(Node):
    def __init__(self, id, desc, sector):
        super().__init__(id, desc)
        self.sector_id = sector

    def __str__(self):
        return "{0} SEC({1.sector_id})".format(super().__str__(), self)

class LNodeStatic(LNode):
    def __init__(self, id, desc, sector, ill, dur):
        super().__init__(id, desc, sector)
        self.illumination = ill
        self.duration = dur

    def __str__(self):
        return "{0} ILL({1.illumination}) DUR({1.duration}) ".format(super().__str__(), self)

class LNodeBlink(LNode):
    def __init__(self, id, desc, sector, on_ill, off_ill, blink):
        super().__init__(id, desc, sector)
        self.on_illumination = on_ill
        self.off_llumination = off_ill
        self.blink = blink

    def __str__(self):
        return "{0} ON-ILL({1.on_illumination}) OFF-ILL({1.off_illumination}) BLINK({1.blink}) ".format(super().__str__(), self)

class LNodePulse(LNode):
    def __init__(self, id, desc, sector, hi_ill, lo_ill, pulse):
        super().__init__(id, desc, sector)
        self.high_illumination = hi_ill
        self.low_llumination = lo_ill
        self.pulse = pulse

    def __str__(self):
        return "{0} HIGH-ILL({1.high_illumination}) LOW-ILL({1.low_illumination}) PULSE({1.pulse}) ".format(super().__str__(), self)

class LNodeFill(LNode):
    pass

class Luceme(object):
    def __init__(self):
        self.name = None
        self.id = None
        self.call_type = None
        self.lnodes = list()

    def __str__(self):
        s = "LUC (%s) %s\n"%(self.id, self.name)
        for l in self.lnodes:
            s += "... %s\n"%(str(l))
        return s

    def set_call_type(self, call_type):
        self.call_type = call_type

    def parse_from_xml(self, xml_object, rings, sectors, colors):
        self.name = xml_object.get('name')
        self.id = xml_object.get('id')
        # Can't set symbol or call_type here, we'll do that later, we've gotta do that once we do a match between symbol ids and luceme ids.

        #TODO Add error handling to kick back lucemes with LNodes that don't match their trigger type. This needs to be dealt with at this level, not at the execution level.
        #TODO Additionally, we should have a sdf syntax checker that can be run seperately.

        # Now we have to parse the KNodes.
        for n in xml_object:
            type = n.tag
            if type == 'lnode-static':
                step = int(n.get('step'))
                description = n.get('description')
                sector_id = n.get('sector')

                ill = Illumination(n[0].get('color'), n[0].get('brightness'))
                dur = Duration(n[1].get('seconds'))
                self.lnodes.append(LNodeStatic(step, description, sector, ill, duration))

            elif type == 'lnode-blink':
                pass 

            elif type == 'lnode-pulse': 
                pass

            elif type == 'lnode-move': 
                pass

            elif type == 'lnode-fill': 
                pass
            
            else:
                print("NO LNODE TYPE RECOGNIZED.")