import networkx as nx
import matplotlib.pyplot as plt
from classes.Vertice import Vertice

seed = 20532
G = nx.Graph(seed=seed)

def show_all_graph(key, node, marked):
  pointers = node.pointers
  for pointer_key in pointers.keys():
    if pointer_key not in marked:
      G.add_node(pointer_key)
      marked.append(key)

    distance = f"{pointers[pointer_key]['type']} {pointers[pointer_key]['distance']}"
    G.add_edge(key, pointer_key, label = distance)
  return marked

def show_path(nodes, marked, node, i, key):
  if i < len(nodes.keys()) - 1:
    pointer_key = list(nodes.keys())[i+1]
    
    G.add_node(pointer_key)
    marked.append(pointer_key)
    
    distance = f"{node['type']} {node['distance']}" 
    G.add_edge(key, pointer_key, label = distance)
  return marked

def config_graph(nx):
  pos = nx.spring_layout(G, seed=seed) 
  edge_labels = nx.get_edge_attributes(G, 'label')
  
  nx.draw_networkx_nodes(G, pos, node_color = 'skyblue', node_size = 150)
  nx.draw_networkx_edges(G, pos, edge_color = 'k')
  nx.draw_networkx_edge_labels(G, pos, edge_labels = edge_labels, font_size = 6 )
  nx.draw_networkx_labels(G, pos, font_color = 'black', font_size = 6)

  ax = plt.gca()
  ax.margins(0)
  plt.axis("off")
  plt.show()

def show_graph(nodes):
  marked = []
  
  for i, key in enumerate(nodes.keys()):
    node = nodes[key]
    
    if key not in marked:
      G.add_node(key)
      marked.append(key)
    
    if isinstance(node, Vertice): marked = show_all_graph(key, node, marked)
    else: marked = show_path(nodes, marked, node, i, key)

  config_graph(nx)