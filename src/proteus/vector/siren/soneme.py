from proteus.vector.node import Node
from proteus.symbol.audio import Audio, VariableAudio
from proteus.symbol.speech import Speech, VariableSpeech
from proteus.symbol import Quantity, Duration
from proteus.symbol.tone import Tone, RunTone, VariableTone

class SNode(Node):
    def __init__(self):
        super().__init__()

    def __str__(self):
        return "{0}".format(super().__str__(), self)

    def parse_from_xml(self, xml):
        super().parse_from_xml(xml)

class SNodeClip(SNode):
    def __init__(self):
        super().__init__()
        self.audios = list()

    def __str__(self):
        ret = "{} [".format(super().__str__(), self)
        for a in self.audios:
            ret += str(a) + ' '
        ret += "]"
        return ret

    def parse_from_xml(self, xml):
        super().parse_from_xml(xml)
        
        for item in xml:
            if item.tag == 'audio':
                a = Audio()
                a.parse_from_xml(item)
                self.audios.append(a)
            elif item.tag =='variable-audio':
                a = VariableAudio()
                a.parse_from_xml(item)
                self.audios.append(a)
            else:
                print("Unexpected component of SNodeClip")

class SNodeSpeech(SNode):
    def __init__(self):
        super().__init__()
        self.speeches = list()

    def __str__(self):
        ret = "{} [".format(super().__str__(), self)
        for s in self.speeches:
            ret += str(s) + ' '
        ret += "]"
        return ret

    def parse_from_xml(self, xml):
        super().parse_from_xml(xml)
        
        for item in xml:
            if item.tag == 'speech':
                s = Speech()
                s.parse_from_xml(item)
                self.speeches.append(s)
            elif item.tag =='variable-speech':
                s = VariableSpeech()
                s.parse_from_xml(item)
                self.speeches.append(s)
            else:
                print("Unexpected component of SNodeSpeech")

class SNodeTone(SNode):
    def __init__(self):
        super().__init__()
        self.tones = list()
        self.duration = None
        self.quantity = None

    def __str__(self):
        ret = "{} [".format(super().__str__(), self)
        if len(self.tones) > 0 :
            for t in self.tones:
                ret += str(t) + ' '
        else:
            ret += "Rest"

        ret += "]; "
        ret += str(self.duration)
        return ret

    def parse_from_xml(self, xml):
        super().parse_from_xml(xml)
        
        for item in xml:
            if item.tag == 'tone':
                t = Tone()
                t.parse_from_xml(item)
                self.tones.append(t)
            elif item.tag =='variable-tone':
                t = VariableTone()
                t.parse_from_xml(item)
                self.tones.append(t)
            elif item.tag =='run-tone':
                t = RunTone()
                t.parse_from_xml(item)
                self.tones.append(t)
            elif item.tag == 'duration':
                d = Duration()
                d.parse_from_xml(item)
                self.duration = d
            elif item.tag == 'quantity':
                q = Quantity()
                q.parse_from_xml(item)
                self.quantity = q
            else:
                print("Unexpected component of SNodeTone")

class Soneme(object):
    def __init__(self):
        self.name = None
        self.id = None
        self.call_type = None
        self.snodes = list()

    def __str__(self):
        ret = "SON (%s) %s\n"%(self.id, self.name)
        for snode in self.snodes:
            ret += "  ... %s\n"%(str(snode))
        return ret

    def set_call_type(self, call_type):
        self.call_type = call_type

    def parse_from_xml(self, xml_object, default_state=False):
        
        self.name = str(xml_object.get('name'))
        self.id = str(xml_object.get('id'))
        # Can't set symbol or call_type here, we'll do that later, we've gotta do that once we do a match between symbol ids and luceme ids.

        #TODO Add error handling to kick back lucemes with LNodes that don't match their trigger type. This needs to be dealt with at this level, not at the execution level.
        #TODO Additionally, we should have a sdf syntax checker that can be run seperately.

        # Now we have to parse the KNodes.
        for sdef in xml_object:
            type = sdef.tag
            if type == 'snode-clip':
                s = SNodeClip()
                s.parse_from_xml(sdef)
                self.snodes.append(s)
            elif type == 'snode-speech':
                s = SNodeSpeech()
                s.parse_from_xml(sdef)
                self.snodes.append(s)
            elif type == 'snode-tone':
                s = SNodeTone()
                s.parse_from_xml(sdef)
                self.snodes.append(s)
            else:
                print("UNRECOGNIZED SNODE TYPE.")