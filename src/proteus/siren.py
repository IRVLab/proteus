import rospkg
rospack = rospkg.RosPack()

class SirenConfig(object):
    def __init__(self):
        self.clip_location = ""
        self.low_volume = 0
        self.high_volume = 20
        self.voice_language = "us"
        self.voice_id = 1
        self.voice_wpm = 120
    
    def parse_from_xml(self, xml):
        for item in xml:
            if item.tag == 'clips':
                package = str(item.get('pkg'))
                directory = str(item.get('directory'))
                self.clip_location = rospack.find(package) + "/" + directory

            elif item.tag == 'volume-range':
                self.low_volume = int(item.get('low'))
                self.high_volume = int(item.get('high'))

            elif item.tag == 'voice':
                self.voice_language = str(item.get('lang'))
                self.voice_id = int(item.get('id'))
                self.voice_wpm = int(item.get('wpm'))