class Velocity(object):
    def __init__(self, lin, ang):
        self.linear = float(lin)
        self.angular = float(ang)

    def __str__(self):
        return "%f lin, %f ang"%(self.linear, self.angular)