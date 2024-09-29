from methods import solve
import numpy as np


if __name__ == '__main__':
    P = 3; Q = 3
    A = np.array([[0, 1, 2, 3], 
                  [0, 0, 1, 2],
                  [0, 2, 2, 3]], dtype=np.int32)
    
    B, C, result = solve(A, P, Q)
    
    print(B)
    print(C)
    print(result)
     