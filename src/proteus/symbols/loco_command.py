#HACK HACK HACK HACK HACK
# Please, for the love of God do not use this class. 
# LoCO needs a proper autopilot and an RCVM implementation to match. 
# However, I do not have the time to do that right now, so I'm making this bodge to allow me to complete this degree.
# If you use this method in the future, I will find you. 

class LoCOCommand(object):
    def __init__(self):
        self.throttle = 0
        self.pitch = 0
        self.yaw = 0

    def parse_from_xml(self, xml):
        self.throttle = float(xml.get('throttle'))
        self.pitch = float(xml.get('pitch'))
        self.yaw = float(xml.get('yaw'))