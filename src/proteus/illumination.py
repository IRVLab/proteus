import uuid

class Illumination(object):
    def __init__(self, id=None, col=None, bright=None):
        self.color = col
        self.brightness = bright

        if id:
            self.id = id
        else:
            self.id= uuid.uuid1()
        
    def __str__(self):
        return "ID({}) {} illuminated at {} brightness".format(self.id, self.color, self.brightness)