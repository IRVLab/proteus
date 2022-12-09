from proteus.environment.agent import Agent

class Animal(Agent):
    def __init__(self):
        super().__init__()
        self.mobile = True
        self.intelligent = True