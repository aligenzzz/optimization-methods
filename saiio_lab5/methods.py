from collections import defaultdict, deque


def find_the_longest_way(V: list[str], 
                         A: list[tuple[str]], 
                         L: list[int]) -> tuple[int, list[str]]:
    V = _topological_sorting(V, A)
    print(f"Topological sorting: {V}")
    
    n = len(V)
    OPT = {V[0]: 0}; x = {V[0]: V[0]}
    
    for i, v in enumerate(V):
        if i == 0:
            continue
        
        options = dict()
        for a, l in zip(A, L):
            if a[1] == v:
                options[a[0]] = OPT[a[0]] + l
                
        max_key, max_value = max(options.items(), 
                                 key=lambda x: x[1])
        OPT[v] = max_value; x[v] = max_key   
        
    length = OPT[V[-1]]; way = [V[-1]]
    while way[0] != V[0]:
        way.insert(0, x[way[0]])
    
    return length, way
    

def _topological_sorting(V: list[str], A: list[tuple[str]]) -> list[str]:
    in_degree = {v: 0 for v in V}
    adj_list = defaultdict(list)
    
    for u, v in A:
        adj_list[u].append(v)
        in_degree[v] += 1

    queue = deque([v for v in V if in_degree[v] == 0])
    sorted_order = []
    
    while queue:
        node = queue.popleft()
        sorted_order.append(node)
        
        for neighbor in adj_list[node]:
            in_degree[neighbor] -= 1
            
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    if len(sorted_order) != len(V):
        raise ValueError("Graph has at least one cycle")
    
    return sorted_order