import uuid

class Mission(object):
    def __init__(self):
        self.id = uuid.uuid1()
    