from graph import Graph
import numpy as np
import networkx
import matplotlib.pyplot as plt


if __name__ == '__main__':
    g = Graph(3, 4)
    g()
    draw_graw = networkx.Graph()
    draw_graw.add_nodes_from([1, 2, 3])
    for i in g.graph_list:
        draw_graw.add_edge(i[0], i[1])

    networkx.draw_circular(draw_graw, node_color = 'red', node_size=1000,
                           with_labels = True)



