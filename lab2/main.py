from simplex_method import second_phase
import numpy as np

if __name__ == '__main__':
    A = np.array([[-1, 1, 1, 0, 0],
                  [1, 0, 0, 1, 0],
                  [0, 1, 0, 0, 1]])
    c_T = np.array([1, 1, 0, 0, 0])
    x_T = np.array([0, 0, 1, 3, 2])
    B = [3, 4, 5]

    result = second_phase(A, c_T, x_T, B)

    print(result)
