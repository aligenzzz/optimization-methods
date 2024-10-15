from methods import solve_knapsack_problem


if __name__ == '__main__':
    v = [6, 3, 4, 2]  # weights
    c = [30, 14, 16, 9]  # prices
    B = 10  # max weight
    
    OPT, result = solve_knapsack_problem(v, c, B)
    print(OPT)
    print(result)
    