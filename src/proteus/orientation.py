class Orientation(object):
    def __init__(self, r, p ,y):
        self.roll = float(r)
        self.pitch = float(p)
        self.yaw = float(y)

    def  __str__(self):
        return "%f roll, %f pitch, %f yaw"%(self.roll, self.pitch, self.yaw)