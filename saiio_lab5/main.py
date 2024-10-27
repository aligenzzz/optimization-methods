from methods import find_the_longest_way

if __name__ == "__main__":
    V = ['s', 'a', 'b', 'c', 'd', 't']
    A = [('s', 'a'), ('s', 'c'), 
         ('a', 'b'), ('b', 'd'), 
         ('b', 't'), ('c', 'a'), 
         ('c', 'd'), ('d', 't')]
    L = [3, 2, 4, 1, 2, 2, 2, 1]
    
    result = find_the_longest_way(V, A, L)
    print("Result:", result)
    