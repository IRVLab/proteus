from proteus.node import Node
from proteus.position import Position
from proteus.orientation import Orientation
from proteus.velocity import Velocity
from proteus.depth import Depth
from proteus.duration import Duration
from proteus.quantity import Quantity

class KNode(Node):
    def __init__(self, id, desc, dur):
        super().__init__(id, desc)
        self.duration = dur

    def __str__(self):
        return "{0} DUR({1.duration})".format(super().__str__(), self)

class KNodeAbsolute(KNode):
    def __init__(self, id, desc, orr, velo, dur):
        super().__init__(id, desc, dur)
        self.orientation = orr
        self.velocity = velo

    def __str__(self):
        return "{0} ORR({1.orientation}) VEL({1.velocity}) ".format(super().__str__(), self)

class KNodePause(KNode):
    def __init__(self, id, desc, dur):
        super().__init__(id, desc, dur)
        
    def __str__(self):
        return "{0} ".format(super().__str__(), self)

class KNodeDepth(KNode):
    def __init__(self, id, desc, depth, vel, dur):
        super().__init__(id, desc, dur)
        self.depth = depth
        self.velocity = vel
        
    def __str__(self):
        return "{0} DEPTH {1.depth} VEL {1.velocity}".format(super().__str__(), self)

class KNodeDirectional(KNode):
    def __init__(self, id, desc, dur):
        super().__init__(id, desc, dur)

    def __str__(self):
        return "{0} ".format(super().__str__())

class KNodeQuantity(KNode):
    def __init__(self, id, desc, quant, dur):
        super().__init__(id, desc, dur)
        self.quantity = quant
    def __str__(self):
        return "{0} Quantity {1.quantity}".format(super().__str__(), self)
    
            
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
        for n in xml_object:
            type = n.tag
            if type == 'knode-abs':
                step = int(n.get('step'))
                description = n.get('description')

                orr = Orientation(n[0].get('roll'), n[0].get('pitch'), n[0].get('yaw'))
                vel = Velocity(n[1].get('surge'),n[1].get('sway'), n[1].get('heave'))
                dur = Duration(n[2].get('seconds'))

                self.knodes.append(KNodeAbsolute(step, description, orr, vel, dur))

            elif type == 'knode-dir': 
                step = int(n.get('step'))
                description = n.get('description')

                dur = Duration(n[0].get('seconds'))

                self.knodes.append(KNodeDirectional(step, description, dur))

            elif type == 'knode-tar': 
                pass

            elif type == 'knode-quant': 
                step = int(n.get('step'))
                description = n.get('description')

                quant = Quantity(n[0].get('display_on'), n[0].get('amount'))
                dur = Duration(n[1].get('seconds'))

                self.knodes.append(KNodeQuantity(step, description, quant, dur))

            elif type == 'knode-pause': 
                step = int(n.get('step'))
                description = n.get('description')
                dur = Duration(n[0].get('seconds'))

                self.knodes.append(KNodePause(step, description, dur))
            elif type == 'knode-depth': 
                step = int(n.get('step'))
                description = n.get('description')
                
                depth = Depth(n[0].get('amount'),n[0].get('mode'))
                vel = Velocity(n[1].get('surge'),n[1].get('sway'), n[1].get('heave'))
                dur = Duration(n[2].get('seconds'))

                self.knodes.append(KNodeDepth(step, description, depth, vel, dur))
            else:
                print("NO KNODE TYPE RECOGNIZED.")
            

