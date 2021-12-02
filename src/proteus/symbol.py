class Symbol(object):
    def __init__(self, dir):
        self.direction = dir

        self.id = None
        self.name = None
        self.call_type = None

        self.description = None
        self.tags = None

    def __str__(self):
        return "    SYM-%s: (%s) %s, %s \n"%(self.direction, self.id, self.name, self.description)

    def parse_from_xml(self, xml_object):
        self.id = str(xml_object.get('id'))
        self.name = str(xml_object.get('name'))
        self.call_type = str(xml_object.get('call_type'))
        self.description = str(xml_object.get('description'))

        self.tags = list()
        tags = xml_object.get('tags')
        for t in tags.split(','):
            self.tags.append(str(t))



    
