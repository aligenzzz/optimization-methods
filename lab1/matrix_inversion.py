import numpy as np


def matrix_with_modified_column_inversion(A: np.ndarray, A_inverted: np.ndarray, 
                                          x: np.ndarray, i: int) -> np.ndarray:
    # Step 0
    n = A.shape[0]
    if i < 0 or i > n:
        raise Exception('Invalid index!')
    i -= 1

    # Step 1
    l = A_inverted.dot(x)
    if l[i] == 0:
        raise Exception('Modified matrix can\'t be inverted!')
    
    # Step 2
    l_copied = np.copy(l)
    l_copied[i] = -1

    # Step 3 
    l_new = (-1 / l[i]) * l_copied

    # Step 4
    Q = np.eye(n)
    Q[:, i] = l_new 

    # Step 5
    A_result = np.zeros((n, n))
    for t in range(n):
        for j in range(n):
            if t != i:
                A_result[t][j] = Q[t][t] * A_inverted[t][j] + Q[t][i] * A_inverted[i][j]
            else:
                A_result[t][j] = Q[t][t] * A_inverted[t][j]

    return A_result
