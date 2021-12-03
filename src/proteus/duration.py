class Duration(object):
    def __init__(self, sec):
        self.seconds = float(sec)

    def __str__(self):
        return "%fs"%(self.seconds)
