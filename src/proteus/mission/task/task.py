import uuid

class Task(object):
    def __init__(self):
        self.id = uuid.uuid1()
    