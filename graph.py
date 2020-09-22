import numpy


class Graph:
    def __init__(self, v, e):
        self.number_of_v = v
        self.number_of_e = e
        self.graph_list = self.get_list()
        self.matrix_incidence = self.get_matrix_incidence()
        self.matrix_adjacency = self.get_matrix_adjacency()
        self.semi_exodus = self.get_semi_exodus()
        self.half_degree_of_approach = self.get_half_degree_of_approach()

    def get_list(self):
        buf = []
        for i in range(self.number_of_e):
            pair = input('Пара вершин: ')
            buf.append([int(pair.split()[0])-1, int(pair.split()[1])-1])
        return buf

    def get_matrix_adjacency(self):
        gl = self.graph_list
        matrix = numpy.array([[0]*self.number_of_v]*self.number_of_v)
        for i in range(self.number_of_e):
            matrix[gl[i][0]][gl[i][1]] = 1
        return matrix

    def get_matrix_incidence(self):
        gl = self.graph_list
        matrix = numpy.array([[0] * self.number_of_e] * self.number_of_v)
        for i in range(self.number_of_e):
            if gl[i][0] != gl[i][1]:
                matrix[gl[i][0]][i] = -1
                matrix[gl[i][1]][i] = 1
        return matrix

    def print_matrix(self, mas):
        for i in mas:
            for j in i:
                print(j, end='\t')
            print()
        print()

    def __call__(self, *args, **kwargs):
        self.print_matrix(self.get_matrix_adjacency())
        self.print_matrix(self.get_matrix_incidence())
        print(self.semi_exodus)
        print(self.half_degree_of_approach)

    # Получение полустепени исхода
    def get_semi_exodus(self):
        semi_exodus = []
        for i in self.matrix_incidence:
            semi_exodus.append(numpy.count_nonzero(-1 == i))
        return semi_exodus

    # Получение полустепени захода
    def get_half_degree_of_approach(self):
        half_degree_of_approach = []
        for i in self.matrix_incidence:
            half_degree_of_approach.append(numpy.count_nonzero(1 == i))
        return half_degree_of_approach

    # определяет число маршрутов заданной длины
    def number_of_routes(self, length, v1, v2):
        matrix = numpy.linalg.matrix_power(self.matrix_adjacency, length)
        return matrix[v1][v2]
