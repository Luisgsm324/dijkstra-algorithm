from classes.Graph import Graph
from take_data import take_stations, take_station
from dijkstra import dijkstra_algorithm

stations = take_stations()

graph = Graph()

for key_station in stations:
  station = take_station(key_station)
  graph.add_vertice(key_station, station["connections"] )
  
dijkstra_algorithm("A13", "A01", graph)

