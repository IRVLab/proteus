class Ring(object):
    def __init__(self, id=None, start=None, end=None, dir=None, t=None, r=None, b=None, l=None ):
        self.id = id
        self.start= start
        self.end = end
        self.direction = dir
        self.top = t
        self.right = r 
        self.bot = b
        self.left = l
        
    def __str__(self):
        return "RING ({}), {} from {} to {}, cardinals ({},{},{},{})".format(self.id, self.direction, self.start, self.end, self.top, self.right, self.bot, self.left)

    def parse_from_xml(self, xml):
        self.id = str(xml.get('id'))
        self.start = int(xml.get('start'))
        self.end = int(xml.get('end'))
        self.direction = str(xml.get('dir'))
        self.top = int(xml.get('top'))
        self.right = int(xml.get('right'))
        self.bot = int(xml.get('bot'))
        self.left = int(xml.get('left'))