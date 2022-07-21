class Color(object):
    def __init__(self, id, r, g, b):
      self.id = id
      self.r = r 
      self.g = g 
      self.b = b
        
    def __str__(self):
        return "Color {} ({},{},{})".format(self.id, self.r, self.g, self.b)