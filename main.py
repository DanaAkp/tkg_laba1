from graph import Graph
import numpy
import networkx
import matplotlib.pyplot as plt

#
# def laba1():
#     graph_list = [[0, 1],
#                   [0, 2],
#                   [1, 1],
#                   [1, 4],
#                   [3, 2],
#                   [4, 3],
#                   [5, 4],
#                   [4, 0],
#                   [5, 0],
#                   [5, 5]]
#     g = Graph(6, 10, graph_list)
#     g()
#     g.print_matrix(g.number_of_routes(4, 12, 2))
#
#
# def laba2():
#     gl1 = [[0, 3],
#            [3, 0],
#            [3, 1],
#            [2, 3],
#            [3, 2],
#            [2, 1],
#            [1, 2],
#            [0, 0],
#            [1, 1]]
#     gl2 = [[0, 2], [2, 1], [1, 0]]
#     g1 = Graph(4, 9, gl1)
#     g2 = Graph(3, 3, gl2)
#     g1()
#     g2()


def extend_matrix(matrix, v):
    ext_matrix = numpy.array([[0] * v] * v)
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            ext_matrix[i][j] = matrix[i][j]
    return ext_matrix


def obedinen(g1: Graph, g2: Graph):
    if g1.number_of_v > g2.number_of_v:
        g2.matrix_adjacency = extend_matrix(g2.matrix_adjacency, g1.number_of_v)

    if g1.number_of_v < g2.number_of_v:
        g1.matrix_adjacency = extend_matrix(g1.matrix_adjacency, g2.number_of_v)
# какая-то хрень
    # martix = numpy.array([[0] * g1.number_of_v] * g1.number_of_v)
    #
    # for i in range(len(g1.matrix_adjacency)):
    #     for j in range(len(g1.matrix_adjacency)):
    #         ext_matrix[i][j] = matrix[i][j]




if __name__ == '__main__':
    gl1 = [[0, 3],
           [3, 0],
           [3, 1],
           [2, 3],
           [3, 2],
           [2, 1],
           [1, 2],
           [0, 0],
           [1, 1]]
    gl2 = [[0, 2], [2, 1], [1, 0]]
    g1 = Graph(4, 9, gl1)
    g2 = Graph(3, 3, gl2)
    g1()
    g2()
