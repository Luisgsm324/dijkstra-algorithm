from classes.Graph import Graph
from take_data import take_stations, take_station
from visualization import show_graph

stations = take_stations()

graph = Graph()

for key_station in stations:
  station = take_station(key_station)
  graph.add_vertice(key_station, station["connections"] )

show_graph(graph.nodes)