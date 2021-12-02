class Node(object):
    def __init__(self, step, prev, nex, desc):
        self.id = step
        self.previous = prev
        self.next = nex
        self.description = desc

    def __str__(self):
        return "Node:%s, Description:%s"%(str(self.id), str(self.description))

    def previous(self):
        return self.previous

    def next(self):
        return self.next
    

