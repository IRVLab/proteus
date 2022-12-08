from proteus.environment.agent import Agent

class Diver(Agent):
    def __init__(self, id):
        super().__init__(self)
        self.readable_id = id
        self.mobile = True
        self.intelligent = True
        