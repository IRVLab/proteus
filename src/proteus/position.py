class Position(object):
    def __init__(self, x, y, z):
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)
    
    def __str__(self):
        return "%f x, %f y, %f z,"%(self.x, self.y, self.z)
