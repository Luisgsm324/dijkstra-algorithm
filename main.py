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
  print(element)
  #print(graph.nodes[element].pointers)
  for i in graph.nodes[element].pointers.values():
    print(f"Nome: {i['target'].name} ({i['target'].station}) Distância: {i['distance']}")
    count2 += 1
  print("---")
  #print(graph.nodes[element].station, "\n--")
  #for i in graph.nodes[element].pointers:
    #print(i)
    #count2 += 1
  #print("-------------")
  count += 1
  #for i in element:
    #print(i)

print(f"Total: {count}")
print(f"Total: {count2}")