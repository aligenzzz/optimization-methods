import numpy as np


def first_phase(a: np.ndarray, b: np.ndarray) -> tuple[np.ndarray, list]:
    n, m = a.shape[0], b.shape[0]

    # the balance condition
    if np.sum(a) != np.sum(b):
        difference = np.sum(a) - np.sum(b)
        if difference > 0:
            b = np.append(b, difference)
            c = np.hstack((c, np.zeros((len(b), 1))))
        else:
            a = np.append(a, -difference)
            c = np.vstack((c, np.zeros((len(a), 1))))

    X = np.zeros((n, m))
    i, j = 0, 0
    B = list()

    while True:
        if b[j] - a[i]  > 0:
            count = a[i]; b[j] -= count; a[i] = 0
        else:
            count = b[j]; a[i] -= count; b[j] = 0

        X[i, j] = count
        B.append((i, j))
        
        if a[i] == 0:
            i += 1
        if b[j] == 0:
            j += 1

        if np.all(a == 0) and np.all(b == 0):
            break

    return X, B


def potentials_method(a: np.ndarray, b: np.ndarray, c: np.ndarray) -> np.ndarray:
    # Step 0
    X, B = first_phase(a, b)
    n, m = a.shape[0], b.shape[0]

    while True:
        # Step 1
        x, y = [], []
        
        for i, j in B:
            u, v = [0] * n, [0] * m
            u[i] = 1; v[j] = 1

            x.append(u + v)
            y.append(c[i, j])

        u_1 = [0] * (n + m); u_1[0] = 1
        x.append(u_1); y.append(0)

        result = np.linalg.solve(x, y)
        u, v = result[:len(a)], result[len(b):]
        
        # Step 2
        new_position, was = None, False
        for i in range(n):
            if was:
                break
            for j in range(m):
                if (i, j) not in B:
                    if u[i] + v[j] > c[i][j]:
                        new_position = (i, j)
                        was = True
                        break
        
        if new_position is None:
            return X  
        else:
            B.append(new_position) 
            
        # Step 3
        corner_B = B.copy()
        
        for i in range(n):
            counter = 0
            for j in range(m):
                if (i, j) in corner_B:
                    counter += 1
            if counter <= 1:
                for j in range(m):
                    if (i, j) in corner_B:
                        corner_B.remove((i, j))

        for j in range(m):
            counter = 0
            for i in range(n):
                if (i, j) in corner_B:
                    counter += 1
            if counter <= 1:
                for i in range(n):
                    if (i, j) in corner_B:
                        corner_B.remove((i, j))
                        
        # Step 4
        marked_B = {position: None for position in corner_B}
        marked_B[new_position] = True
        add_plus_or_minus(new_position, marked_B)
        
        # Step 5
        theta, min_i, min_j = np.inf, -1, -1
        for i in range(n):
            for j in range(m):
                if (i, j) in marked_B and marked_B[(i, j)] is False:
                    if theta > X[i, j]:
                        theta, min_i, min_j = X[i, j], i, j
                    
        # Step 6
        for (i, j) in marked_B.keys():
            if marked_B[(i, j)]:
                X[i, j] += theta
            else:
                X[i, j] -= theta
        
        B.remove((min_i, min_j))


def add_plus_or_minus(position: tuple[int, int], B: dict) -> None:   
    for i, j in B.keys():
        if position[0] == i:
            if B[(i, j)] is None:
                B[(i, j)] = not B[position]
                add_plus_or_minus((i, j), B)
        if position[1] == j:
            if B[(i, j)] is None:
                B[(i, j)] = not B[position]
                add_plus_or_minus((i, j), B)
                