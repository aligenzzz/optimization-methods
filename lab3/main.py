from simplex_method import first_phase, second_phase
import numpy as np

if __name__ == '__main__':
    A = np.array([[1, 1, 1],
                  [2, 2, 2]])
    c = np.array([1, 0, 0])
    b = np.array([0, 0])

    result = first_phase(c, A, b)

    print(result)
    
    # example from the last lab
    A = np.array([[-1, 1, 1, 0, 0],
                  [1, 0, 0, 1, 0],
                  [0, 1, 0, 0, 1]])
    c = np.array([1, 1, 0, 0, 0])
    b = np.array([1, 3, 2])

    result = first_phase(c, A, b)

    print(result)
