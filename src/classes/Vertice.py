class Vertice:
  def __init__(self, station, name):
    self.name = name
    self.station = station
    self.pointers = {}
    self.start_distance = None
    self.predecessor = None
    self.type = None