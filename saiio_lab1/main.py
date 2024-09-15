from methods import branch_and_bound_method
import numpy as np


if __name__ == '__main__':
    c = np.array([1, 1])
    A = np.array([[5, 9], [9, 5]])
    b = np.array([63, 63])
    d_m = np.array([1, 1])
    d_p = np.array([6, 6])
    
    result = branch_and_bound_method(c, A, b, d_m, d_p)
    
    print(result)
    