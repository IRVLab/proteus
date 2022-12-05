import uuid

class State(object):
    def __init__(self):
        self.id = uuid.uuid1()
    