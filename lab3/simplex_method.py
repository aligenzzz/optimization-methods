import numpy as np


def first_phase(c: np.ndarray, A: np.ndarray, b: np.ndarray) -> tuple[np.ndarray, np.ndarray, list]:
    m, n = A.shape
    n_set = set(range(1, n + 1))

    # Step 1
    mask = (b < 0)
    b[mask] *= -1
    A[mask] *= -1

    # Step 2
    c_aux = np.concatenate((np.zeros(n), np.full(m, -1)))
    A_aux = np.concatenate((A, np.eye(m)), axis=1)

    # Step 3
    x_aux = np.concatenate((np.zeros(n), b))
    B_aux = [i + n for i in range(1, m + 1)]

    # Step 4
    x_aux, B_aux = second_phase(A_aux, c_aux, x_aux, B_aux)

    # Step 5
    if np.any(x_aux[-m:] != 0):
        raise Exception('This task is incompatible!!!')

    # Step 6
    x = x_aux[:n]
    B = B_aux

    while True:
        # Step 7
        if set(B).issubset(n_set):
            return x, A, B

        # Step 8
        j_k = max(B)
        k = B.index(j_k)

        # Step 9
        j_list = list(n_set - set(B))
        A_B = A_aux[:, np.array(B) - 1]
        A_B_inverted = np.linalg.inv(A_B)

        l = [(j, A_B_inverted.dot(A_aux[:, j - 1])) for j in j_list]

        # Step 10
        was = False
        for j, l_j in l:
            if l_j[k] != 0:
                B[k] = j
                was = True
                break

        # Step 11
        if not was:
            i = j_k - n - 1

            A_aux = np.delete(A_aux, i, axis=0)
            A = np.delete(A, i, axis=0)

            b = np.delete(b, i)
            B.remove(j_k)


# from lab2
def second_phase(A: np.ndarray, c_T: np.ndarray, x_T: np.ndarray, B: list) -> tuple[np.ndarray, np.ndarray]:
    was = False

    while True:
        # Step 1
        A_B = A[:, np.array(B) - 1]

        if was:
            A_B_inverted = matrix_with_modified_column_inversion(A_B, A_B_inverted, A[:, j0], k + 1)
        else:
            A_B_inverted = np.linalg.inv(A_B)

        # Step 2
        c_B_T = c_T[np.array(B) - 1]

        # Step 3
        u_T = c_B_T.dot(A_B_inverted)

        # Step 4
        delta_T = u_T.dot(A) - c_T

        # Step 5
        if np.all(delta_T >= 0):
            return x_T, B

        # Step 6
        j0 = np.where(delta_T < 0)[0][0]
        delta = delta_T[j0]

        # Step 7
        z = A_B_inverted.dot(A[:, j0])
        
        # Step 8
        theta = np.array([x_T[j - 1] if z[i] > 0 else np.Inf for i, j in enumerate(B)])
        
        # Step 9
        theta0 = np.min(theta)

        # Step 10
        if theta0 == np.Inf:
            raise Exception('The target functionality of the task is not limited from ' \
                            'above on a set of acceptable plans!')
        
        # Step 11
        k = theta.tolist().index(theta0)
        j_k = B[k]
        
        # Step 12
        B[k] = j0 + 1

        # Step 13 
        x_T[j0] = theta0
        for i, j in enumerate(B):
            if j != j0 + 1:
                x_T[j - 1] = x_T[j - 1] - theta0 * z[i]
        x_T[j_k - 1] = 0

        was = True
        


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