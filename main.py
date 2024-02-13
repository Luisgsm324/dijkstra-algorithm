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
for i in graph.nodes['N17'].pointers.values():
  pass 
  #print(i['target'].station, i['distance'])

for element in graph.nodes:
  print(element)
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

def search_nodes(node):
  for adjacent_nodes in graph.nodes[node].pointers.values():
    if adjacent_nodes['target'].start_distance > graph.nodes[node].start_distance:
      adjacent_nodes['target'].start_distance = graph.nodes[node].start_distance + adjacent_nodes['distance']
      print(adjacent_nodes['target'].start_distance)


def dijkstra_algorithm(start_vertice, final_vertice):
  unvisited_node = []
  # fazer a lista dos não visitados
  for node in graph.nodes:
    unvisited_node.append(graph.nodes[node])
  graph.nodes[start_vertice].start_distance = 0
  search_nodes(start_vertice)
  

dijkstra_algorithm('N17', 'N18')

print(f"Total: {count}")
print(f"Total: {count2}")