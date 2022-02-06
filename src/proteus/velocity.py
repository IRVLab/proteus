class Velocity(object):
    def __init__(self, surge, sway, heave):
        self.surge = float(surge)
        self.sway = float(sway)
        self.heave = float(heave)

    def __str__(self):
        return "{} surge, {} sway, {} heave".format(self.surge, self.sway, self.heave)