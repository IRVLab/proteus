import uuid

class Agent(object):
    def __init__(self):
        self.id = uuid.uuid1()
        self.mobile = None
        self.intelligent = None