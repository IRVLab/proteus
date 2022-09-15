from proteus.node import Node
from proteus.blink import Blink
from proteus.color_map import ColorMapping
from proteus.color import Color
from proteus.fill import Fill
from proteus.illumination import Illumination
from proteus.pulse import Pulse
from proteus.ring import Ring
from proteus.sector import Sector
from proteus.duration import Duration

class LNode(Node):
    def __init__(self):
        super().__init__()
        self.sector_id = None

    def __str__(self):
        return "{0} SEC-ID({1.sector_id})".format(super().__str__(), self)

    def parse_from_xml(self, xml):
        super().parse_from_xml(xml)
        self.sector_id = str(xml.get('sector'))

class LNodeStatic(LNode):
    def __init__(self):
        super().__init__()
        self.illuminations = dict()
        self.duration = Duration()

    def __str__(self):
        ret = "{} ILLS[".format(super().__str__())
        for k, i in self.illuminations.items():
            ret += str(i) + ' '
        ret += "] {}".format(self.duration)
        return ret

    def parse_from_xml(self, xml):
        super().parse_from_xml(xml)
        for item in xml:
            if item.tag == 'illumination':
                ill = Illumination()
                ill.parse_from_xml(item)
                self.illuminations[ill.id] = ill
            elif item.tag == 'duration':
                self.duration.parse_from_xml(item)
            else:
                print("Unexpected component of LNodeStatic")

    def get_duration_seconds(self):
        return self.duration.seconds


class LNodeBlink(LNode):
    def __init__(self):
        super().__init__()
        self.illuminations = dict()
        self.blink = Blink()

    def __str__(self):
        ret = "{} ILLS[".format(super().__str__())
        for k, i in self.illuminations.items():
            ret += str(i) + ' '
        ret += "] {}".format(self.blink)
        return ret

    def parse_from_xml(self, xml):
        super().parse_from_xml(xml)
        for item in xml:
            if item.tag == 'illumination':
                ill = Illumination()
                ill.parse_from_xml(item)
                self.illuminations[ill.id] = ill

            elif item.tag == 'blink':
                self.blink.parse_from_xml(item)
            else:
                print("Unexpected component of LNodeStatic")

    def get_duration_seconds(self):
        return (self.blink.period * self.blink.iterations)

class LNodePulse(LNode):
    def __init__(self):
        super().__init__()
        self.illuminations = dict()
        self.pulse = Pulse()
        self.duration = Duration()

    def __str__(self):
        ret = "{} ILLS[".format(super().__str__())
        for k, i in self.illuminations.items():
            ret += str(i) + ' '
        ret += "] {} {}".format(self.pulse, self.duration)
        return ret

    def parse_from_xml(self, xml):
        super().parse_from_xml(xml)
        for item in xml:
            if item.tag == 'illumination':
                ill = Illumination()
                ill.parse_from_xml(item)
                self.illuminations[ill.id] = ill              
            elif item.tag == 'pulse':
                self.pulse.parse_from_xml(item)
            elif item.tag == 'duration':
                self.duration.parse_from_xml(item)
            else:
                print("Unexpected component of LNodeStatic")

    def get_duration_seconds(self):
        return self.duration.seconds

class LNodeFill(LNode):
    def __init__(self):
        super().__init__()
        self.illuminations = dict()
        self.fill = Fill()
        self.color_map = ColorMapping()
        self.duration = Duration()

    def __str__(self):
        ret = "{} ILLS[".format(super().__str__())
        for k, i in self.illuminations.items():
            ret += str(i) + ' '
        ret += "] {} {} {}".format(self.fill, self.color_map, self.duration)
        return ret

    def parse_from_xml(self, xml):
        super().parse_from_xml(xml)

        for item in xml:
            if item.tag == 'illumination':
                ill = Illumination()
                ill.parse_from_xml(item)
                self.illuminations[ill.id] = ill              
            elif item.tag == 'fill':
                self.fill.parse_from_xml(item)
            elif item.tag == 'color-map':
                self.color_map.parse_from_xml(item)
            elif item.tag == 'duration':
                self.duration.parse_from_xml(item)
            else:
                print("Unexpected component of LNodeStatic")

    def get_duration_seconds(self):
        return self.duration.seconds


class Luceme(object):
    def __init__(self):
        self.name = None
        self.id = None
        self.call_type = None
        self.lnodes = list()

    def __str__(self):
        s = "LUC (%s) %s\n"%(self.id, self.name)
        for l in self.lnodes:
            s += "  ... %s\n"%(str(l))
        return s

    def set_call_type(self, call_type):
        self.call_type = call_type

    def parse_from_xml(self, xml_object, default_state=False):
        
        if default_state:
            self.name = "Default HREye State"
            self.id = "default-state"
        else:
            self.name = str(xml_object.get('name'))
            self.id = str(xml_object.get('id'))
        # Can't set symbol or call_type here, we'll do that later, we've gotta do that once we do a match between symbol ids and luceme ids.

        #TODO Add error handling to kick back lucemes with LNodes that don't match their trigger type. This needs to be dealt with at this level, not at the execution level.
        #TODO Additionally, we should have a sdf syntax checker that can be run seperately.

        # Now we have to parse the KNodes.
        for lndef in xml_object:
            type = lndef.tag
            if type == 'lnode-static':
                l = LNodeStatic()
                l.parse_from_xml(lndef)
                self.lnodes.append(l)
            elif type == 'lnode-blink':
                l = LNodeBlink()
                l.parse_from_xml(lndef)
                self.lnodes.append(l)

            elif type == 'lnode-pulse': 
                l = LNodePulse()
                l.parse_from_xml(lndef)
                self.lnodes.append(l)

            elif type == 'lnode-fill': 
                l = LNodeFill()
                l.parse_from_xml(lndef)
                self.lnodes.append(l)
            
            else:
                print("UNRECOGNIZED LNODE TYPE.")

    def get_luceme_duration(self):
        step_durations = []
        current_step = 0
        for l in self.lnodes:
            if l.step == current_step:
                step_durations.append(l.get_duration_seconds())
                current_step += 1
            else:
                continue

        return step_durations