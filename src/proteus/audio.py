class Audio(object):
    def __init__(self):
        self.volume = 50
        self.speed = 1
        self.filename = "duck_test.ogg"

    def __str__(self):
        return "AUDIO (vol {} speed {}), {}.".format(self.volume, self.speed, self.filename)

    def parse_from_xml(self, xml):
        self.volume = int(xml.get('volume'))
        self.speed = float(xml.get('speed'))
        self.filename = str(xml.get('filename'))

class VariableAudio(Audio):
    def __init__(self):
        super().__init__()
        self.options = list()
    
    def __str__(self):
        return "VAR-AUDIO (vol {} speed {}), {}.".format(self.volume, self.speed, self.filename)

    def parse_from_xml(self, xml):
        super().parse_from_xml(xml)

        options = str(xml.get("options"))
        for opt in options.split(';'):
            self.options.append(opt)

    def get_dyn_fname(self, option):
        if option not in self.options:
            raise KeyError("No such option: {} for Variable audio".format(option))
    
        return self.filename.format(option)