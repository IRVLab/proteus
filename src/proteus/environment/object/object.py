import uuid

class Object(object):
    def __init__(self):
        self.id = uuid.uuid1()
