import uuid

class Goal(object):
    def __init__(self):
        self.id = uuid.uuid1()
    