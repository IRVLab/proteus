import xml.etree.ElementTree as ET

class SectorSegment(object):
    def __init__(self):
        self.ring = None
        self.start = None
        self.end = None
        self.indexes = list()
        self.resolved = False

    def __str__(self):
        if self.resolved:
            return "SEG ({}), indexes {}".format(self.ring, self.indexes)
        else:
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
        
        start_formula = start_formula.replace("start", str(relevant_ring.start))
        start_formula = start_formula.replace("end", str(relevant_ring.end))
        start_formula = start_formula.replace("top", str(relevant_ring.top))
        start_formula = start_formula.replace("left", str(relevant_ring.left))
        start_formula = start_formula.replace("bot", str(relevant_ring.bot))
        start_formula = start_formula.replace("right", str(relevant_ring.right))
        self.start = eval(start_formula)

        end_formula = end_formula.replace("start", str(relevant_ring.start))
        end_formula = end_formula.replace("end", str(relevant_ring.end))
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

        if self.start < self.end:
            self.indexes = list(range(self.start, self.end+1))

            for k, i in enumerate(self.indexes):
                if i < 0:
                    self.indexes[k] = relevant_ring.end + i

        else:
            start_a = self.start
            end_a = relevant_ring.end

            start_b = relevant_ring.start
            end_b = self.end

            self.indexes = list(range(start_a, end_a))
            self.indexes.extend(list(range(start_b, end_b)))

        self.resolved = True

        return

class CenterRelativeSectorSegment(object):
    def __init__(self):
        self.ring = None
        self.center = None
        self.width = None

    def __str__(self):
        return "REL-SEG[Center] ({}), center: {}, width: {}".format(self.ring, self.center, self.width)

    def parse_from_xml(self, xml):
        self.ring = str(xml.get('ring'))
        self.center = str(xml.get('center'))
        self.width = int(xml.get('width'))

    # TODO return a dynamic sector, based on the input data, the center point, and width of the relative sector.
    def get_indexes(self, data):
        pass

class PointRelativeSectorSegment(object):
    def __init__(self):
        self.ring = None
        self.start = None
        self.max_length = None

    def __str__(self):
        return "REL-SEG[Start] ({}), start: {}, max_length: {}".format(self.ring, self.start, self.max_length)

    def parse_from_xml(self, xml):
        self.ring = str(xml.get('ring'))
        self.start = str(xml.get('start'))
        self.max_length = int(xml.get('max_length'))


    # TODO return a dynamic sector, based on the input data, the center point, and width of the relative sector.
    def get_indexes(self, data):
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
            elif sdef.tag == 'center-relative-sector-segment':
                seg = CenterRelativeSectorSegment()
            elif sdef.tag == 'point-relative-sector-segment':
                seg = PointRelativeSectorSegment()
            
            seg.parse_from_xml(sdef)
            self.segments.append(seg)

    def resolve_indexes(self, rings):
        for s in self.segments:
            if type(s) == SectorSegment:
                s.resolve_indexes(rings)

    def get_indexes(self, data=None):
        indexes = []
        for s in self.segments:
            if type(s) is SectorSegment:
                indexes.extend(s.indexes)
            elif type(s) is CenterRelativeSectorSegment:
                indexes.extend(s.get_indexes(data)) 
            elif type(s) is PointRelativeSectorSegment:
                indexes.extend(s.get_indexes(data)) 

        return indexes

    