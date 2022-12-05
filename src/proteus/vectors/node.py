class Node(object):
    def __init__(self):
        self.step = None
        self.description = None

    def __str__(self):
        return "Node {0.step} ({0.description}): ".format(self)

    def parse_from_xml(self, xml):
        self.step = int(xml.get('step'))
        self.description = str(xml.get('description'))

