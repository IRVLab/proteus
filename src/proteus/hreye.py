from proteus.luceme import Luceme
from proteus.ring import Ring
from proteus.sector import Sector
from proteus.color import Color

class HREyeConfig(object):
    def __init__(self):
        self.rings = dict()
        self.sectors = dict()
        self.colors = dict()
        self.default_state = Luceme()

    def __str__(self):
        ret = "HREyeConfig: \n  Rings:\n"
        for k, r in self.rings.items():
            ret += "       {}\n".format(r)

        ret += "\n  Sectors: \n"
        for k, s in self.sectors.items():
            ret += "      {}\n".format(s)
        
        ret += "\n  Colors: \n"
        for k, c in self.colors.items():
            ret += "      {}\n".format(c)

        ret += "\n  Default State: \n     {}".format(self.default_state)
        return ret
        
    
    def parse_from_xml(self, xml):
        for item in xml:
            if item.tag == 'rings':
                for rdef in item:
                    r = Ring()
                    r.parse_from_xml(rdef)
                    self.rings[r.id] = r

            elif item.tag == 'sectors':
                for sdef in item:
                    s = Sector()
                    s.parse_from_xml(sdef)
                    self.sectors[s.id] = s

            elif item.tag == 'colors':
                for cdef in item:
                    c = Color()
                    c.parse_from_xml(cdef)
                    self.colors[c.id] = c

            elif item.tag == 'default-state':
                self.default_state.parse_from_xml(item, default_state=True) # Default state is defined as a luceme, so we can just parse from there.

    # Resolve sector indexes from their definition form to their actual coordinates.
    def resolve_sector_indexes(self):
        for k, s in self.sectors.items():
            s.resolve_indexes(self.rings)