class Speech(object):
    def __init__(self):
        self.volume = 50
        self.speed = 1.0
        self.text = ""

    def __str__(self):
        return "SPEECH (vol {} speed {}), {}.".format(self.volume, self.speed, self.text)

    def parse_from_xml(self, xml):
        self.volume = float(xml.get('volume'))
        self.speed = float(xml.get('speed'))
        self.text = str(xml.get('text'))

class VariableSpeech(Speech):
    def __init__(self):
        super().__init__()

    def __str__(self):
        return "VAR-SPEECH (vol {} speed {}), {}.".format(self.volume, self.speed, self.text)

    def parse_from_xml(self, xml):
        super().parse_from_xml(xml)

    def get_dyn_text(self, variable):
        return self.text.format(variable)