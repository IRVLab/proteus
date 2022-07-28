import xml.etree.ElementTree as ET

class SectorSegment(object):
    def __init__(self):
        self.ring = None
        self.start = None
        self.end = None
        self.resolved = False

    def __str__(self):
        return "SEG ({}), start: {}, end: {}".format(self.ring, self.start, self.end)

    def parse_from_xml(self, xml):
        self.ring = str(xml.get('ring'))
        self.start = str(xml.get('start'))
        self.end = str(xml.get('end'))

    def resolve_indexes(self, rings):
        if self.resolved:
            return 

        relevant_ring = rings[self.ring]
        start_formula = self.start
        end_formula = self.end
        
        start_formula = start_formula.replace("top", str(relevant_ring.top))
        start_formula = start_formula.replace("left", str(relevant_ring.left))
        start_formula = start_formula.replace("bot", str(relevant_ring.bot))
        start_formula = start_formula.replace("right", str(relevant_ring.right))
        self.start = eval(start_formula)

        end_formula = end_formula.replace("top", str(relevant_ring.top))
        end_formula = end_formula.replace("left", str(relevant_ring.left))
        end_formula = end_formula.replace("bot", str(relevant_ring.bot))
        end_formula = end_formula.replace("right", str(relevant_ring.right))
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

        self.resolved = True

        return

class RelativeSectorSegment(object):
    def __init__(self):
        self.ring = None
        self.center = None
        self.width = None

    def __str__(self):
        return "REL-SEG ({}), center: {}, width: {}".format(self.ring, self.center, self.width)

    def parse_from_xml(self, xml):
        self.ring = str(xml.get('ring'))
        self.center = str(xml.get('center'))
        self.width = int(xml.get('width'))

    # TODO return a dynamic sector, based on the input data, the center point, and width of the relative sector.
    def get_dynamic_sector(self, data):
        pass

class Sector(object):
    def __init__(self):
      self.id = None
      self.segments = list()
        
    def __str__(self):
        ret = "SECTOR {}: ".format(self.id)
        for seg in self.segments:
            ret += "{},".format(seg)
        return ret

    def parse_from_xml(self, xml):
        self.id = xml.get('id')
        for sdef in xml:
            if sdef.tag == 'sector-segment':
                seg = SectorSegment()
            elif sdef.tag == 'relative-sector-segment':
                seg = RelativeSectorSegment()
            
            seg.parse_from_xml(sdef)
            self.segments.append(seg)

    def resolve_indexes(self, rings):
        for s in self.segments:
            if type(s) == SectorSegment:
                s.resolve_indexes(rings)