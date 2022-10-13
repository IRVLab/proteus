class Fill(object):
    def __init__(self, t=None, direction=None, start=None):
      self.type = t
      self.direction = direction
      self.start = start
      self.length = None
        
    def __str__(self):
        return "FILL {}, {} starting from {}.".format(self.type, self.direction, self.start)

    def parse_from_xml(self, xml):
      self.type = str(xml.get('type'))
      self.direction = str(xml.get('direction'))
      self.start = str(xml.get('start'))

      if self.type == 'segment-move':
        self.length = int(xml.get('length'))