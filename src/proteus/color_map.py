class ColorMapping(object):
    def __init__(self, target=None, mapping=dict()):
        self.target = target
        self.mapping = mapping
        
    def __str__(self):
        return "COLOR-MAP value {}, map def:{}".format(self.target, self.mapping)

    def parse_from_xml(self, xml):
        self.target = str(xml.get('target'))
        mapping_string = str(xml.get('mapping'))

        for map in mapping_string.split(';'):
            id = map.split('=')[0]
            values = map.split('=')[1]
            bot = int(values.split(':')[0])
            top = int(values.split(':')[1])

            self.mapping[id] = (bot, top)