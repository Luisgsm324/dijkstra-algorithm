from classes.Graph import Graph
from take_data import take_stations, take_station
<<<<<<< HEAD:src/main.py
from dijkstra import dijkstra_algorithm
=======
from visualization import show_graph
>>>>>>> 23ffd1a629f07d66f09180accbd3c4b8674e99b7:main.py

stations = take_stations()

graph = Graph()

for key_station in stations:
  station = take_station(key_station)
  graph.add_vertice(key_station, station["connections"] )
<<<<<<< HEAD:src/main.py
  
dijkstra_algorithm("A13", "A01", graph)


=======

show_graph(graph.nodes)
>>>>>>> 23ffd1a629f07d66f09180accbd3c4b8674e99b7:main.py
