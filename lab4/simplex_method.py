import numpy as np

def dual_simplex_method(c: np.ndarray, A: np.ndarray, b: np.ndarray, B: list) -> np.ndarray:
    was = False
    _, n = A.shape
    n_set = set(range(1, n + 1))

    while True:    
        N = list(n_set - set(B))

        # Step 1
        A_B = A[:, np.array(B) - 1] 
        if was:
            A_B_inverted = matrix_with_modified_column_inversion(A_B, A_B_inverted, A[:, j_0 - 1], k + 1)
        else:
            A_B_inverted = np.linalg.inv(A_B)

        # Step 2
        c_B = c[np.array(B) - 1]

        # Step 3
        y_T = c_B.T.dot(A_B_inverted)

        # Step 4
        kappa_B, it = A_B_inverted.dot(b), 0
        kappa = np.zeros(n)
        for i in range(1, n + 1):
            if i in B:
                kappa[B[it] - 1] = kappa_B[it]
                it += 1
        kappa = np.array(kappa)

        # Step 5
        if np.all(kappa >= 0):
            return kappa

        # Step 6
        j_k = np.where(kappa < 0)[0][-1]
        k = B.index(j_k + 1)

        # Step 7
        delta_y = A_B_inverted[k, :]
        mu = [(j, delta_y.T.dot(A[:, j - 1])) for j in N]
        mu = np.array(mu)

        # Step 8
        if np.all(mu >= 0):
            raise Exception('This task is infeasible!!!')

        # Step 9
        sigma = []
        for j, mu_j in mu:
            j = int(j)
            if mu_j < 0:
                sigma.append((j, (c[int(j - 1)] - A[:, int(j - 1)].T.dot(y_T)) / mu_j)) 

        # Step 10
        j_0, _ = min(sigma, key=lambda x: x[1])        

        # Step 11
        B[k] = j_0


# from lab 1
def matrix_with_modified_column_inversion(A: np.ndarray, A_inverted: np.ndarray, 
                                          x: np.ndarray, i: int) -> np.ndarray:
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
