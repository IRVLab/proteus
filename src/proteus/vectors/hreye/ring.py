import math

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

    def get_angle_centered_indexes(self, angle, width):
        print("For {}".format(self.id))
        print("Input angle {} rad, {} deg".format(angle, angle * (180/math.pi)))
        all_indexes = [x for x in range(self.start, self.end+1)]
        if self.direction == 'counter-clockwise':
            all_indexes.reverse()

        per_index_angle = (2*math.pi)/ len(all_indexes)

        if angle != 0:
            center_index = int(angle/per_index_angle)
        else:
            center_index = all_indexes.index(self.top)

        width = width - 1 # One less, because we have the center index.
        start_index = center_index - int(width/2)
        stop_index = center_index + int(width/2)

        # Enforces wrapping.
        if start_index < 0:
            start_index = start_index + len(all_indexes)
        elif start_index >= len(all_indexes):
            start_index = start_index% len(all_indexes)

        if stop_index < 0:
            stop_index = stop_index + len(all_indexes)
        elif stop_index >= len(all_indexes):
            stop_index = stop_index% len(all_indexes)


        print(center_index, start_index, stop_index)

        # Manages indexes in different directions.
        if start_index > stop_index:
            ret = all_indexes[start_index:]
            ret.extend(all_indexes[0:stop_index])
        else:
            ret = all_indexes[start_index:stop_index]

        print("Indexes: {}".format(ret))

        return ret
