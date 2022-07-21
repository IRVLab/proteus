import xml.etree.ElementTree as ET

class SectorSegment(object):
    def __init__(self, ring="", start=-1, end=-1):
        self.ring = ring
        self.start = start
        self.end = end

    def parse_from_xml(self, xml, rings):
        self.ring = str(xml.get('ring'))

        relevant_ring = rings[self.ring]
        start_formula = str(xml.get('start'))
        end_formula = str(xml.get('end'))
        
        start_formula.replace("top", relevant_ring.top)
        start_formula.replace("left", relevant_ring.left)
        start_formula.replace("bot", relevant_ring.bot)
        start_formula.replace("right", relevant_ring.right)
        self.start = eval(start_formula)

        end_formula.replace("top", relevant_ring.top)
        end_formula.replace("left", relevant_ring.left)
        end_formula.replace("bot", relevant_ring.bot)
        end_formula.replace("right", relevant_ring.right)
        self.end = eval(end_formula)

        # Enforcing ring index wrapping
        if self.start < relevant_ring.start:
            self.start + relevant_ring.end
        if self.end < relevant_ring.start:
            self.end + relevant_ring.end

        # Enforcing ring index wrapping
        if self.start > relevant_ring.end:
            self.start - relevant_ring.end
        if self.end > relevant_ring.end:
            self.end - relevant_ring.end

    def __str__(self):
        return "Segement on {}, starting at {} and ending at {}".format(self.ring, self.start, self.end)

class Sector(object):
    def __init__(self, id, segs):
      self.id = id
      self.segments = segs
        
    def __str__(self):
        ret = "Sector {}, segements: ".format(self.id)
        for seg in self.segements:
            ret += "\n" + str(seg)
        return ret