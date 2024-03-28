import numpy as np
from simplex_method import dual_simplex_method

if __name__ == '__main__':
    A = np.array([[-2, -1, -4, 1, 0],
                  [-2, -2, -2, 0, 1]])
    c = np.array([-4, -3, -7, 0, 0])
    b = np.array([-1, -1.5])
    B = [4, 5]

    result = dual_simplex_method(c, A, b, B)

    print(result)