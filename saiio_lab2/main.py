from methods import homori_method
import numpy as np


if __name__ == '__main__':
    c = np.array([0, 1, 0, 0])
    A = np.array([[3, 2, 1, 0], 
                  [-3, 2, 0, 1]])
    b = np.array([6, 0])
    
    result = homori_method(c, A, b)
    
    print(result)
     