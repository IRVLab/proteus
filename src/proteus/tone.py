class Tone(object):
    def __init__(self):
        pass

    def __str__(self):
        return "TONE ".format()

    def parse_from_xml(self, xml):
        pass

class VariableTone(Tone):
    def __init__(self):
        super().__init__()
    
    def __str__(self):
        return "VAR-AUDIO ".format()

    def parse_from_xml(self, xml):
        super().parse_from_xml(xml)