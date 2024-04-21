from potentials_method import potentials_method
import numpy as np


if __name__ == '__main__':
    a = np.array([100, 300, 300])
    b = np.array([300, 200, 200])
    c = np.array([[8, 4, 1],
                  [8, 4, 3],
                  [9, 7, 5]])
    
    result = potentials_method(a, b, c)
    
    print(result)
    