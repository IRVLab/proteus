from proteus.vector import Vector
from proteus.symbol import Symbol

class Language(object):
    def __init__(self):
        self.name = None
        self.robot = None
        self.description = None
        self.directory = None

        self.in_symbols = list()
        self.in_vectors = list()
        self.in_actions = list()

        self.out_symbols = list()
        self.out_vectors = list()
        self.out_actions = list()

    def __str__(self):
        s = "LANGUAGE: %s for %s\n"%(self.name, self.robot)

        s += "-IN SYMBOLS\n"
        for sym in self.in_symbols:
            s += str(sym)

        s += "-IN VECTORS\n"
        for vec in self.in_vectors:
            s += str(vec)

        s += "-IN ACTIONS\n"
        for act in self.in_actions:
            s += str(act)

        s += "-OUT SYMBOLS\n"
        for sym in self.out_symbols:
            s += str(sym)

        s += "-OUT VECTORS\n"
        for vec in self.out_vectors:
            s += str(vec)

        s += "-OUT ACTIONS\n"
        for act in self.out_actions:
            s += str(act)

        return s


    def parse_from_xml(self, xml_object):
        for c in xml_object:
            if c.tag == 'meta':
                self.name = str(c[0].text)
                self.robot = str(c[1].text)
                self.description = str(c[2].text)
                self.directory = str(c[3].text)
                
            elif c.tag == 'input':
                continue
            elif c.tag == 'output':
                for gc in c:
                    if gc.tag == 'symbols':
                        for symbol in gc:
                            s = Symbol('out')
                            s.parse_from_xml(symbol)
                            self.out_symbols.append(s)
                    elif gc.tag == 'vectors':
                        for vector in gc:
                            v = Vector('out')
                            v.parse_from_xml(vector, self.directory)
                            self.out_vectors.append(v)
                    elif gc.tag == 'actions':
                        continue
                    else:
                        rospy.logwarn('Unexpected tag in language definition file: %s'%c.tag)
                
            elif c.tag == 'state':
                continue
            elif c.tag == 'context':
                continue
            elif c.tag == 'actions':
                continue
            else:
                rospy.logwarn('Unexpected tag in language definition file: %s'%c.tag)


        # self.name = 
        # self.robot
        # self.description
