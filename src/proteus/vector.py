import rospkg

rospack = rospkg.RosPack()

class Vector(object):
    def __init__(self, dir):
        self.name = None
        self.explicitness = None
        self.has_static = None
        self.has_dynamic = None
        self.direction = dir
        self.medium = None

        self.pkg = None
        self.definition_file = None

    def __str__(self):
        return f"    VEC{self.direction} ({self.name}): {self.explicitness} communication via {self.medium} [Static: {self.has_static} Dynamic: {self.has_dynamic}]\n"

    def parse_from_rosparam(self, name, rosparam_obj):
        self.name = name
        self.explicitness = rosparam_obj['explicitness']
        self.has_static = rosparam_obj['static']
        self.has_dynamic = rosparam_obj['dynamic']
        self.medium = rosparam_obj['medium']
    
    def parse_from_xml(self, xml_object):
        self.name = str(xml_object.get('name'))
        self.explicitness = str(xml_object.get('type'))
        self.has_static = bool(xml_object.get('static'))
        self.has_dynamic = bool(xml_object.get('dynamic'))
        self.medium = str(xml_object.get('medium'))
        self.pkg = str(xml_object.get('pkg'))
        filename = str(xml_object.get('file'))
        self.definition_file = rospack.get_path(self.pkg) + '/symbol_definitions/' + filename