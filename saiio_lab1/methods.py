import numpy as np
from collections import namedtuple
from copy import deepcopy


def dual_simplex_method(c: np.ndarray, A: np.ndarray, b: np.ndarray, B: list) -> np.ndarray:
    _, n = A.shape
    n_set = set(range(1, n + 1))

    while True:    
        N = list(n_set - set(B))
        
        A_B = A[:, np.array(B) - 1] 
        A_B_inverted = np.linalg.inv(A_B)   
        c_B = c[np.array(B) - 1]
        y_T = c_B @ A_B_inverted

        kappa_B, it = A_B_inverted @ b, 0
        kappa = np.zeros(n)
        for i in range(1, n + 1):
            if i in B:
                kappa[B[it] - 1] = kappa_B[it]
                it += 1
        kappa = np.array(kappa)

        if np.all(kappa >= 0):
            return kappa

        j_k = np.where(kappa < 0)[0][-1]
        k = B.index(j_k + 1)

        delta_y = A_B_inverted[k, :]
        mu = [(j, delta_y @ A[:, j - 1]) for j in N]
        mu = np.array(mu)

        if np.all(mu >= 0):
            raise Exception('This problem is infeasible!')

        sigma = []
        for j, mu_j in mu:
            j = int(j)
            if mu_j < 0:
                sigma.append((j, (c[int(j - 1)] - A[:, int(j - 1)] @ y_T) / mu_j)) 

        j_0, _ = min(sigma, key=lambda x: x[1])        
        B[k] = j_0


def branch_and_bound_method(c: np.ndarray, A: np.ndarray, 
                            b: np.ndarray, d_m: np.ndarray, d_p: np.ndarray) -> np.ndarray:
    m, n = A.shape
    Problem = namedtuple('Problem', ['alpha', 'c', 'A', 'b', 'd_m', 'delta'])
    initial_c = deepcopy(c)
    
    # Step 1
    for i in range(len(c)):
        if c[i] > 0:
            c[i] *= -1
            A[:, i] *= -1
            d_m[i] *= -1; d_p[i] *= -1
            d_m[i], d_p[i] = d_p[i], d_m[i]
            
    # Step 2
    alpha = 0 
    c = np.concatenate((c, np.zeros(m + n)))
    A = np.hstack((np.vstack((A, np.eye(n))), np.eye(n + m)))
    b = np.concatenate((b, d_p))
    d_m = np.concatenate((d_m, np.zeros(m + n)))
    
    # Step 3
    x = None
    r = -np.inf
    delta = deepcopy(d_m)
    S = [Problem(alpha=alpha, c=c, A=A, b=b, d_m=d_m, delta=delta)]
    
    # Step 4
    while True:
        if not S:
            if x is None:
                raise Exception('This problem is infeasible!')
            else:
                c = np.concatenate((initial_c, np.array([-1 for _ in range(m + n)])))
                return np.where(c < 0, x, -x)[:n]
            
        else:
            P = S.pop()
            alpha_ = P.alpha + P.c @ P.d_m
            b_ = P.b - P.A @ P.d_m
            
            B = [i + 1 for i in range(n, n * 2 + m)]
            x_ = dual_simplex_method(P.c, P.A, b_, B)
            
            integer_mask = x_ == x_.astype(np.int32)
            temp = P.c @ x_ + alpha_
            
            if all(integer_mask):                
                x_ += P.delta
                if not x or r < temp:
                    x = x_; r = temp 
                       
            else:
                float_index = np.where(integer_mask[:n] == False)[0][-1]
                float_element = x_[float_index]
                
                if x is None or np.floor(temp) > r:
                    new_b = deepcopy(b_)
                    new_b[m + float_index] = np.floor(float_element)
                    S.append(Problem(
                        alpha=deepcopy(alpha_),
                        c=deepcopy(P.c),
                        A=deepcopy(P.A),
                        b=new_b,
                        d_m=np.zeros(2 * n + m),
                        delta=deepcopy(P.delta)
                    ))
                    
                    new_d_m = np.zeros(2 * n + m)
                    new_d_m[float_index] = np.ceil(float_element)
                    S.append(Problem(
                        alpha=deepcopy(alpha_),
                        c=deepcopy(P.c),
                        A=deepcopy(P.A),
                        b=deepcopy(b_),
                        d_m=new_d_m,
                        delta=(P.delta + new_d_m)
                    ))
