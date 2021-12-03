class Node(object):
    def __init__(self, step, desc):
        self.id = step
        self.description = desc

    def __str__(self):
        return "Node {0.id} ({0.description}): ".format(self)

