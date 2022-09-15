import rospkg
rospack = rospkg.RosPack()
from proteus.synth_track import SynthTrack

class SirenConfig(object):
    def __init__(self):
        self.clip_location = ""
        self.volume = 0
        self.voice_language = "us"
        self.voice_id = 1
        self.voice_wpm = 120
        self.synth_tracks = dict()
        self.save_wavs = False
    
    def parse_from_xml(self, xml):
        for item in xml:
            if item.tag == 'clips':
                package = str(item.get('pkg'))
                directory = str(item.get('directory'))
                self.clip_location = rospack.get_path(package) + "/" + directory
                self.volume = float(item.get('volume'))

            elif item.tag == 'voice':
                self.voice_language = str(item.get('lang'))
                self.voice_id = int(item.get('id'))
                self.voice_wpm = int(item.get('wpm'))
                self.volume = float(item.get("volume"))

            elif item.tag == 'synth-track':
                st = SynthTrack()
                st.parse_from_xml(item)
                self.synth_tracks[st.id] = st