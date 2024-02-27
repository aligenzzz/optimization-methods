import numpy as np

def second_phase(A: np.ndarray, c_T: np.ndarray, x_T: np.ndarray, B: list) -> np.ndarray:
    while True:
        # Step 1
        A_B = A[:, np.array(B) - 1]
        A_B_inverted = np.linalg.inv(A_B)

        # Step 2
        c_B_T = c_T[np.array(B) - 1]

        # Step 3
        u_T = c_B_T.dot(A_B_inverted)

        # Step 4
        delta_T = u_T.dot(A) - c_T

        # Step 5
        if np.all(delta_T >= 0):
            return x_T

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
        