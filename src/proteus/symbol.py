class Symbol(object):
    def __init__(self, dir):
        self.direction = dir

        self.id = None
        self.name = None
        self.input_required= None

        self.description = None
        self.content_tags = None

    def __str__(self):
        return f"SYM-{self.direction}: ({self.id}) {self.name}, {self.input_required} \n"

    def parse_from_rosparam(self, id, rosparam_obj):
        self.name = id
        self.input_required = rosparam_obj['input_required']
        self.content_tags = rosparam_obj['content_tags']
    
    def parse_from_xml(self, xml_object):
        self.id = str(xml_object.get('id'))
        self.name = str(xml_object.get('name'))
        self.input_required = str(xml_object.get('input'))
        self.description = str(xml_object.get('description'))

        self.content_tags = list()
        tags = xml_object.get('tags')
        for t in tags.split(','):
            self.content_tags.append(str(t).strip())