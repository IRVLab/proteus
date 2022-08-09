import rospkg
rospack = rospkg.RosPack()

class HREyeConfig(object):
    def __init__(self):
        self.clip_location = ""
    
    def parse_from_xml(self, xml):
        for item in xml:
            if item.tag == 'clips':
                package = str(item.get('pkg'))
                directory = str(item.get('directory'))
        
        self.clip_location = rospack.find(package) + "/" + directory