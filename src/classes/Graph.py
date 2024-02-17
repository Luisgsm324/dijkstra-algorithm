from classes.Vertice import Vertice
from take_data import take_station

class Graph:
  def __init__(self):
    self.nodes = {}
  
  def is_in_graph(self, station):
    if station not in self.nodes.keys():
      node = Vertice(station, take_station(station)["name_en"])
      self.nodes[station] = node
      return node, False
    
    return self.nodes[station], True
  
  def add_vertice(self, station, connections):
    initial_node = self.is_in_graph(station)[0]
    
    for connection in connections:
      target_id = connection["target_id"]
      node, is_in_graph = self.is_in_graph(target_id)
      
      if not is_in_graph:
        self.add_vertice(target_id, take_station(target_id)["connections"])
        
      node.pointers[station] = { "target": initial_node, "distance": connection["distance"], "type": connection["type"]}