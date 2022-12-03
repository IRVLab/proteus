import rospkg

rospack = rospkg.RosPack()

class Vector(object):
    def __init__(self, dir):
        self.name = None
        self.id = None
        self.namespace_prefix = None

        self.explicitness = None
        self.has_static = None
        self.has_dynamic = None
        self.direction = dir
        self.medium = None

        self.pkg = None
        self.definition_file = None

    def __str__(self):
        return f"VEC_{self.direction} ({self.name}): {self.explicitness} communication via {self.medium} [Static: {self.has_static}, Dynamic: {self.has_dynamic}]"

    def parse_from_rosparam(self, name, rosparam_obj):
        self.name = name
        self.id = rosparam_obj['id']
        self.namespace_prefix = rosparam_obj['ns_prefix']
        self.explicitness = rosparam_obj['explicitness']
        self.has_static = bool(rosparam_obj['static'])
        self.has_dynamic = bool(rosparam_obj['dynamic'])
        self.medium = rosparam_obj['medium']
        self.definition_file = rosparam_obj['definition_file']
    
    def parse_from_xml(self, xml_object):
        self.name = str(xml_object.get('name'))
        self.id = str(xml_object.get('id'))
        self.namespace_prefix = str(xml_object.get('ns_prefix'))
        self.explicitness = str(xml_object.get('type'))
        self.has_static = eval(xml_object.get('static', False))
        self.has_dynamic = eval(xml_object.get('dynamic', False))
        self.medium = str(xml_object.get('medium'))
        self.pkg = str(xml_object.get('pkg'))
        filename = str(xml_object.get('file'))
        self.definition_file = rospack.get_path(self.pkg) + '/symbol_definitions/' + filename