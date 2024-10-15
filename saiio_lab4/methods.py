def solve_knapsack_problem(v: list[int], c: list[int], B: int):
    N = len(v)

    OPT = [[0 for _ in range(B + 1)] for _ in range(N + 1)]

    for k in range(N + 1):
        for b in range(B + 1):
            if k == 0 or b == 0:
                OPT[k][b] = 0
            else:
                if v[k - 1] <= b:
                    OPT[k][b] = max(OPT[k - 1][b], OPT[k - 1][b - v[k - 1]] + c[k - 1])
                else:
                    OPT[k][b] = OPT[k - 1][b]         

    return OPT, _get_result(OPT, v, k, b)


def _get_result(OPT, v, k, b):
    if OPT[k][b] == 0:
        return []
    elif OPT[k - 1][b] == OPT[k][b]:
        return _get_result(OPT, v, k - 1, b)
    else:
        sub_result = _get_result(OPT, v, k - 1, b - v[k - 1])
        sub_result.append(k)
        return sub_result
    