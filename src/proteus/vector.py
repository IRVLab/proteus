class Vector(object):
    def __init__(self, dir):
        self.name = None
        self.type = None
        self.direction = dir

        self.definition_file = None

    def __str__(self):
        return "    VEC-%s: %s of type %s, defined in %s\n"%(self.direction, self.name, self.type, self.definition_file)
    
    def parse_from_xml(self, xml_object):
        self.name = str(xml_object.get('name'))
        self.type = str(xml_object.get('type'))
        self.definition_file = str(xml_object.text)