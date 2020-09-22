from graph import Graph
import numpy as np


if __name__ == '__main__':
    # g = Graph(3, 4)
    # g()
    a = np.arange(4).reshape((2, 2))
    # b = np.arange(4).reshape((2, 2))
    # print(a, b)
    # c = a.dot(b)
    # print(c)
    print(np.linalg.matrix_power(a, 3))
