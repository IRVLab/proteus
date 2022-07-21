class ColorMapping(object):
    def __init__(self, target, mapping):
        self.target = target
        self.mapping = mapping
        
    def __str__(self):
        return "Color mapping to value {}, map def:{}".format(self.target, self.mapping)