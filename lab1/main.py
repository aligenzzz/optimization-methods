from matrix_inversion import matrix_with_modified_column_inversion
import numpy as np

if __name__ == '__main__':
    A = np.array([[1, -1, 0],
                  [0, 1, 0],
                  [0, 0, 1]])
    A_inverted = np.array([[1, 1, 0],
                           [0, 1, 0],
                           [0, 0, 1]])
    x = np.array([1, 0, 1]).transpose()
    i = 3

    result = matrix_with_modified_column_inversion(A, A_inverted, x, i)
    print(result)
