from proteus.environment.agent import Agent

class Robot(Agent):
    def __init__(self, is_self):
        super().__init__()
        self.me = is_self
        self.mobile = True
        self.intelligent = True