class Ring(object):
    def __init__(self, id, start, end, dir, t, r, b, l ):
        self.id = id
        self.start= start
        self.end = end
        self.direction = dir
        self.top = t
        self.right = r 
        self.bot = b
        self.left = l
        
    def __str__(self):
        return "Ring {}, {} from {} to {}, cardinals ({},{},{},{})".format(self.id, self.direction, self.start, self.end, self.top, self.right, self.bot, self.left)