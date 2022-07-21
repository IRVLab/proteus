class Blink(object):
    def __init__(self, per, iters):
        self.period = per
        self.iterations = iters
        
    def __str__(self):
        return " Blink {} times at a period {}".format(self.on, self.off, self.iterations, self.period)