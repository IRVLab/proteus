from proteus.node import Node
from proteus.position import Position
from proteus.orientation import Orientation
from proteus.velocity import Velocity
from proteus.duration import Duration

class KNode(Node):
    def __init__(self, id, desc, dur):
        super().__init__(id, desc)
        self.duration = dur

    def __str__(self):
        return "{0} DUR({1.duration})".format(super().__str__(), self)

class KNodeAbsolute(KNode):
    def __init__(self, id, desc, pos, orr, velo, dur):
        super().__init__(id, desc, dur)
        self.position = pos
        self.orientation = orr
        self.velocity = velo

    def __str__(self):
        return "{0} POS({1.position}) ORR({1.orientation}) VEL({1.velocity}) ".format(super().__str__(), self)

class KNodeDirectional(KNode):
    def __init__(self, id, desc, mode, velo, dur):
        super().__init__(id, desc, dur)
        self.mode = mode
        self.velocity = velo

    def __str__(self):
        return "{0} MODE ({1.mode}) VEL({1.velocity}) ".format(super().__str__(), self)
            
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

        # Now we have to parse the KNodes.
        for n in xml_object:
            type = n.tag
            if type == 'knode-abs':
                step = int(n.get('step'))
                description = n.get('description')

                pos = Position(n[0].get('x'), n[0].get('y'), n[0].get('z'))
                orr = Orientation(n[1].get('roll'), n[1].get('pitch'), n[1].get('yaw'))
                vel = Velocity(n[2].get('linear'),n[2].get('angular'))
                dur = Duration(n[3].get('seconds'))

                self.knodes.append(KNodeAbsolute(step, description, pos, orr, vel, dur))

            elif type == 'knode-dir': 
                step = int(n.get('step'))
                description = n.get('description')

                mode = n[0].get('type')
                vel = Velocity(n[1].get('linear'),n[1].get('angular'))
                dur = Duration(n[2].get('seconds'))

                self.knodes.append(KNodeDirectional(step, description, mode, vel, dur))

            elif type == 'knode-tar': 
                pass
            else:
                print("NO KNODE TYPE RECOGNIZED.")
            

