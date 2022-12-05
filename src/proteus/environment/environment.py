import uuid

class Environment(object):
    def __init__(self):
        self.id = uuid.uuid1()
    