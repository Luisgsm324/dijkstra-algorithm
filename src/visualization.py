import networkx as nx
import matplotlib.pyplot as plt

seed = 20532
G = nx.Graph(seed=seed)

marked = []

def show_graph(nodes):
  for key in nodes.keys():
    if key not in marked:
      G.add_node(key)
      marked.append(key)
    
    pointers = nodes[key].pointers
    for pointer_key in pointers.keys():
      if pointer_key not in marked:
        G.add_node(pointer_key)
      
      distance = pointers[pointer_key]["distance"]
      G.add_edge(key, pointer_key, weight = distance)
  
  pos = nx.spring_layout(G, seed=seed) 
  edge_labels = nx.get_edge_attributes(G, 'weight')
  
  nx.draw_networkx_nodes(G, pos, node_color = 'skyblue', node_size = 100)
  nx.draw_networkx_edges(G, pos, edge_color = 'k')
  nx.draw_networkx_edge_labels(G, pos, edge_labels = edge_labels, font_size = 5 )
  nx.draw_networkx_labels(G, pos, font_color = 'black', font_size = 6)

  ax = plt.gca()
  ax.margins(0)
  plt.axis("off")
  plt.show()
