class Tone(object):
    def __init__(self):
        self.track_id = None
        self.note = None
        self.octave = None
        self.end_note = None

    def __str__(self):
        if self.end_note:
            return "TONE {}{}, ending on {}".format(self.note, self.octave, self.end_note)
        else: 
            return "TONE {}{}".format(self.note, self.octave)

    def parse_from_xml(self, xml):
        self.track_id = str(xml.get('track'))
        notestring = str(xml.get('note'))
        self.note = notestring[:-1]
        self.octave = int(notestring[-1])
       
        end_ret = xml.get('end_note')
        if end_ret:
            self.end_note = str(end_ret)

class VariableTone(Tone):
    def __init__(self):
        super().__init__()
    
    def __str__(self):
        return "VAR-AUDIO ".format()

    def parse_from_xml(self, xml):
        super().parse_from_xml(xml)