class Quantity(object):
    def __init__(self, disp, amnt):
        self.display_on= str(disp)
        self.amount = float(amnt)

    def __str__(self):
        return "Display quantity on {} of {}".format(self.amount, self.display_on)