from proteus.vector.node import Node
from proteus.symbol.position import Position
from proteus.symbol.orientation import Orientation
from proteus.symbol.velocity import Velocity
from proteus.symbol.depth import Depth
from proteus.symbol.duration import Duration
from proteus.symbol.quantity import Quantity
from proteus.symbol.loco_command import LoCOCommand

class KNode(Node):
    def __init__(self):
        super().__init__()
        self.duration = Duration()

    def __str__(self):
        return "{0} DUR({1.duration})".format(super().__str__(), self)

    def parse_from_xml(self, xml):
        super().parse_from_xml(xml)
        for item in xml:
            if item.tag == 'duration':
                self.duration.parse_from_xml(item)

class KNodeDeadGuess(KNode):
    def __init__(self):
        super().__init__()
        self.command = LoCOCommand()

    def __str__(self):
        return "{0} CMD({1.command}) ".format(super().__str__(), self)

    def parse_from_xml(self, xml):
        super().parse_from_xml(xml)
        for item in xml:
            if item.tag == 'loco-cmd':
                self.command.parse_from_xml(item)

class KNodeAbsolute(KNode):
    def __init__(self):
        super().__init__()
        self.orientation = Orientation()
        self.velocity = Velocity()

    def __str__(self):
        return "{0} ORR({1.orientation}) VEL({1.velocity}) ".format(super().__str__(), self)

    def parse_from_xml(self, xml):
        super().parse_from_xml(xml)
        for item in xml:
            if item.tag == 'orientation':
                self.orientation.parse_from_xml(item)
            elif item.tag == 'velocity':
                self.velocity.parse_from_xml(item)
            

class KNodePause(KNode):
    def __init__(self):
        super().__init__()
        
    def __str__(self):
        return "{0} ".format(super().__str__(), self)

    def parse_from_xml(self, xml):
        super().parse_from_xml(xml)

class KNodeDepth(KNode):
    def __init__(self):
        super().__init__()
        self.depth = Depth()
        self.velocity = Velocity()
        
    def __str__(self):
        return "{0} DEPTH {1.depth} VEL {1.velocity}".format(super().__str__(), self)

    def parse_from_xml(self, xml):
        super().parse_from_xml(xml)
        for item in xml:
            if item.tag == 'depth':
                self.depth.parse_from_xml(item)
            elif item.tag == 'velocity':
                self.velocity.parse_from_xml(item)

class KNodeDirectional(KNode):
    def __init__(self):
        super(KNodeDirectional, self).__init__()

    def __str__(self):
        return "{0} ".format(super(KNodeDirectional, self).__str__())

    def parse_from_xml(self, xml):
        super(KNodeDirectional, self).parse_from_xml(xml)

class KNodeQuantity(KNode):
    def __init__(self):
        super().__init__()
        self.quantity = Quantity()
    def __str__(self):
        return "{0} Quantity {1.quantity}".format(super().__str__(), self)

    def parse_from_xml(self, xml):
        super().parse_from_xml(xml)
        for item in xml:
            if item.tag == 'quantity':
                self.quantity.parse_from_xml(item)
    
            
class Kineme(object):
    def __init__(self):
        self.name = None
        self.id = None
        self.call_type = None
        self.knodes = list()

    def __str__(self):
        s = "KIN (%s) %s\n"%(self.id, self.name)
        for k in self.knodes:
            s += "... %s\n"%(str(k))
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
        for kdef in xml_object:
            type = kdef.tag
            if type == 'knode-abs':
                k = KNodeAbsolute()
                k.parse_from_xml(kdef)
                self.knodes.append(k)

            elif type == 'knode-dir': 
                k = KNodeDirectional()
                k.parse_from_xml(kdef)
                self.knodes.append(k)

            elif type == 'knode-tar': 
                pass

            elif type == 'knode-quant': 
                k = KNodeQuantity()
                k.parse_from_xml(kdef)
                self.knodes.append(k)

            elif type == 'knode-pause': 
                k = KNodePause()
                k.parse_from_xml(kdef)
                self.knodes.append(k)
            elif type == 'knode-depth': 
                k = KNodeDepth()
                k.parse_from_xml(kdef)
                self.knodes.append(k)

            # THIS SUCKS, DONT USE IT.    
            elif type == 'knode-dg':
                k = KNodeDeadGuess()
                k.parse_from_xml(kdef)
                self.knodes.append(k)
            else:
                print("NO KNODE TYPE RECOGNIZED.")