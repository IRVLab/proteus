import numpy as np


notes_sharps = ['c', 'c#', 'd', 'd#', 'e', 'f', 'f#', 'g', 'g#', 'a' ,' a#', 'b']
notes_flats = ['c', 'db', 'd', 'eb', 'e', 'f', 'gb', 'g', 'ab', 'a' ,' bb', 'b']

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

class RunTone(object):
    def __init__(self):
        self.track_id = None
        self.start_note = None
        self.start_octave = None
        self.stop_note = None
        self.stop_octave = None
        self.glissando = False

    def __str__(self):
        return "RUN-TONE from {}{} to {}{}, glissando {}".format(self.start_note, self.start_octave, self.stop_note, self.stop_octave, self.glissando)

    def parse_from_xml(self, xml):
        self.track_id = str(xml.get('track'))

        start_notestring = str(xml.get('start_note'))
        self.start_note = start_notestring[:-1]
        self.start_octave = int(start_notestring[-1])

        stop_notestring = str(xml.get('stop_note'))
        self.stop_note = stop_notestring[:-1]
        self.stop_octave = int(stop_notestring[-1])

        gliss_str = str(xml.get('glissando'))
        self.glissando = (gliss_str == "True" ) or (gliss_str == "true")
    
    def get_dyn_notes(self, value, duration, min_value, max_value):
        ret_vals = list() # A list of three values: note, octave, duration. If note/octave is None, that's a rest.

        # First, we need to create a list of notes from the start note to the stop note, and associate them with values.
        try: 
            start_idx = notes_sharps.index(self.start_note)
        except ValueError:
            start_idx = notes_flats.index(self.start_note)

        try: 
            stop_idx = notes_sharps.index(self.stop_note)
        except ValueError:
            stop_idx = notes_flats.index(self.stop_note)

        if self.start_octave == self.stop_octave:
            # in this case, it's just a slice of notes
            raw_notes = notes_sharps[start_idx:stop_idx]
            raw_octaves = [self.start_octave] * len(raw_notes)

    # If the start octave is higher, we need to add the start and end of the notes list, and as many iterations of the whole list as required.
        elif self.start_octave < self.stop_octave:
            raw_notes = notes_sharps[start_idx:]
            raw_octaves = [self.start_octave] * len(raw_notes)

            for i in range((self.stop_octave - self.start_octave) -1):
                raw_notes.extend(notes_sharps)
                raw_octaves.extend([(self.start_octave + (i+1))] * len(notes_sharps))

            raw_notes.extend(notes_sharps[:stop_idx])
            raw_octaves.extend([self.stop_octave] * len(notes_sharps[:stop_idx]))

        # If the start octave is lower, we just have to reverse it.
        elif self.start_octave > self.stop_octave:
            raw_notes = notes_sharps[:start_idx]
            raw_octaves = [self.start_octave] * len(raw_notes)

            for i in range((self.start_octave - self.stop_octave) -1):
                raw_notes.extend(notes_sharps)
                raw_octaves.extend([(self.start_octave - (i+1))] * len(notes_sharps))

            raw_notes.extend(notes_sharps[stop_idx:])
            raw_octaves.extend([self.stop_octave] * len(notes_sharps[stop_idx:]))


        raw_values = np.linspace(min_value, max_value, len(raw_notes))
        
        # Okay, now we have notes, octaves, and values to match them. 
        # Now we select the ones we need, decide on durations based on the glissando value, and return.

        idx = min(range(len(raw_values)), key=lambda i: abs(raw_values[i]-value)) # This isn't super fast, but the list is going to be short and sorted.
        notes = raw_notes[:idx]
        octaves = raw_octaves[:idx]
        durations = [duration/len(notes)] * len(notes)

        for k in range(len(notes)):
            ret_vals.append([notes[k], octaves[k], durations[k]])
            if not self.glissando:
                ret_vals.append([None, None, 0.2])

        return ret_vals

class VariableTone(object):
    def __init__(self):
        self.track_id = None
        self.parameter = None
        self.options = None
    
    def __str__(self):
        return "VAR-AUDIO ".format()

    def parse_from_xml(self, xml):
        self.track_id = str(xml.get('track'))
        self.parameter = str(xml.get('param'))
        self.options = list()

        options = str(xml.get('options')).split(';')
        for o in options:
            note = o[:-1]
            octave = int(o[-1])
            self.options.append([note, octave])

    