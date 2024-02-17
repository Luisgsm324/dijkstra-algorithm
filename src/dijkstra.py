def dijkstra_algorithm(start_vertice, final_vertice, graph):
  for node in graph.nodes:
    graph.nodes[node].start_distance = float("inf")
    graph.nodes[node].predecessor = None
  
  def search_nodes(node, marked_nodes):
    for adjacent_nodes in graph.nodes[node].pointers.values():
      distance = graph.nodes[node].start_distance + adjacent_nodes['distance']
      
      if adjacent_nodes['target'].start_distance > distance:
        target = adjacent_nodes['target']
        target.start_distance = distance
        target.type = adjacent_nodes['type']
        target.predecessor = graph.nodes[node].station
        marked_nodes.append(graph.nodes[adjacent_nodes['target'].station])
  
  
  unvisited_node = []
  marked_nodes = []
  for node in graph.nodes:
    unvisited_node.append(graph.nodes[node])
  
  minimum_node = None
  graph.nodes[start_vertice].start_distance = 0
  
  while graph.nodes[final_vertice] in unvisited_node:
    node = graph.nodes[start_vertice]
    
    if node in unvisited_node:
      unvisited_node.remove(node)
      search_nodes(start_vertice, marked_nodes)
    else:
      marked_nodes.remove(node)
      
    minimum_node = min(marked_nodes, key=lambda x:x.start_distance)
    start_vertice = minimum_node.station

  path = {}
  
  while final_vertice is not None:
    predecessor = node.predecessor
    node = graph.nodes[final_vertice]
    
    distance_predecessor = graph.nodes[predecessor].start_distance if predecessor else 0
    distance = node.start_distance - distance_predecessor
    
    type_path = node.type 
    path[final_vertice] = ({"distance": round(distance, 2), "type": type_path }) 
    final_vertice = predecessor
  
  # Em vez de print(path), coloquei para retornar  
  return path

