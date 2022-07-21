class Pulse(object):
    def __init__(self, hi, lo, vary, step, freq):
        self.high = hi
        self.low = lo
        self.vary_param = vary
        self.step_size = step
        self.frequency = freq
        
    def __str__(self):
        return "Pulse from {} to {} on the {} param, at a frequency of {} and a step size of {}".format(self.high, self.low, self.vary_param, self.frequency, self.step_size)