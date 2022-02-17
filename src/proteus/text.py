class Text(object):
    def __init__(self, data):
        self.data = str(data)

    def __str__(self):
        return "%s"%(self.data)
