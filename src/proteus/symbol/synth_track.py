class SynthTrack(object):
    def __init__(self):
        self.id = ""
        self.wave_type = "sine"
        self.vibrato = None
        self.vibrato_variance = 15.0
        self.attack = None
        self.decay = None

    def set_idx(self, idx):
        self.index = idx

    def parse_from_xml(self, xml):
        self.id = str(xml.get('id'))
        self.wave_type = str(xml.get('wave'))
        self.vibrato = float(xml.get('vibrato'))
        self.vibrato_variance = float(xml.get("variance"))
        self.attack = float(xml.get("attack"))
        self.decay = float(xml.get("decay"))