class Color(object):
    def __init__(self, id='Null', r=0, g=0, b=0):
      self.id = id
      self.r = r 
      self.g = g 
      self.b = b
        
    def __str__(self):
        return "Color {} ({},{},{})".format(self.id, self.r, self.g, self.b)

    def parse_from_xml(self, xml):
      self.id = str(xml.get('id'))
      self.r = int(xml.get('r'))
      self.g = int(xml.get('g'))
      self.b = int(xml.get('b'))