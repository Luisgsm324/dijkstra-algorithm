from classes.Graph import Graph
from take_data import take_stations, take_station

stations = take_stations()

graph = Graph()

for key_station in stations:
  station = take_station(key_station)
  graph.add_vertice(key_station, station["connections"] )

count = 0
count2 = 0

print("Início :)")

for element in graph.nodes:
  #print(element)
  #print(graph.nodes[element].pointers)
  for i in graph.nodes[element].pointers.values():
    #print(f"Nome: {i['target'].name} ({i['target'].station}) Distância: {i['distance']}")
    count2 += 1
  #print("---")
  #print(graph.nodes[element].station, "\n--")
  #for i in graph.nodes[element].pointers:
    #print(i)
    #count2 += 1
  #print("-------------")
  count += 1
  #for i in element:
    #print(i)

def know_distance(start_vertice, final_vertice):
  distance = 0
  for i in graph.nodes[start_vertice].pointers.values():
    print(i)
    if i['target'].station == final_vertice:
      distance = i['distance']
  return distance

def search_nodes(node, marked_nodes):
  for adjacent_nodes in graph.nodes[node].pointers.values():
    if adjacent_nodes['target'].start_distance > graph.nodes[node].start_distance + adjacent_nodes['distance']:
      adjacent_nodes['target'].start_distance = graph.nodes[node].start_distance + adjacent_nodes['distance']
      adjacent_nodes['target'].predecessor = graph.nodes[node].station
      print(graph.nodes[adjacent_nodes['target'].station].station, graph.nodes[adjacent_nodes['target'].station].start_distance)
      marked_nodes.append(graph.nodes[adjacent_nodes['target'].station])
  

def dijkstra_algorithm(start_vertice, final_vertice):
  unvisited_node = []
  marked_nodes = []
  # fazer a lista dos não visitados
  for node in graph.nodes:
    unvisited_node.append(graph.nodes[node])
  
  minimum_node = None
  graph.nodes[start_vertice].start_distance = 0
  
  while graph.nodes[final_vertice] in unvisited_node:
    if graph.nodes[start_vertice] in unvisited_node:
      unvisited_node.remove(graph.nodes[start_vertice])
      search_nodes(start_vertice, marked_nodes)
    else:
      marked_nodes.remove(graph.nodes[start_vertice])
      
    minimum_node = min(marked_nodes, key=lambda x:x.start_distance)
    start_vertice = minimum_node.station
    print(start_vertice)

final_graph = 'S21'

dijkstra_algorithm('A01', final_graph)
print(graph.nodes[final_graph].start_distance)


while final_graph is not None:
  print(graph.nodes[final_graph].predecessor, end=" ")
  final_graph = graph.nodes[final_graph].predecessor


print(f"Total: {count}")
print(f"Total: {count2}")