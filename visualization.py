import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

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
        
  pos = nx.spring_layout(G)
  edge_labels = nx.get_edge_attributes(G, 'weight')

  nx.draw_networkx_nodes(G, pos, node_color='skyblue')
  nx.draw_networkx_edges(G, pos, edge_color='k')
  nx.draw_networkx_edge_labels(G, pos, edge_labels = edge_labels, font_size = 5 )
  nx.draw_networkx_labels(G, pos, font_color='black', font_size= 8)

  plt.show()
