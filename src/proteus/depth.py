class Depth(object):
    def __init__(self, amnt, mode):
        self.amount = float(amnt)
        self.mode = str(mode)

    def __str__(self):
        return "{} depth in meters, {} mode".format(self.amount, self.mode)