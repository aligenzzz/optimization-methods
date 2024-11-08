from methods import find_maximum_graph_matching


if __name__ == "__main__":
    V1 = ['a', 'b', 'c']
    V2 = ['x', 'y', 'z']
    edges = [('a', 'x'), ('b', 'x'), ('b', 'y'), 
             ('c', 'y'), ('c', 'z')]

result = find_maximum_graph_matching(V1, V2, edges)
print(result)
