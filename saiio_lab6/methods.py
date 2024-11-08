import networkx as nx


def find_maximum_graph_matching(
    V1: list[str], 
    V2: list[str], 
    edges: list[tuple[str, str]]
) -> set[tuple[str, str]]:
    # Step 1
    G = nx.DiGraph()
    G.add_nodes_from(V1, bipartite=0) 
    G.add_nodes_from(V2, bipartite=1) 
    G.add_edges_from(edges)

    # Step 2
    s, t = 's', 't'
    G.add_nodes_from([s, t])    
    for u in V1:
        G.add_edge(s, u)
    for v in V2:
        G.add_edge(v, t)

    while True:
        # Step 3
        try:
            path = nx.shortest_path(G, s, t)
            path_edges = list(zip(path, path[1:]))
        except nx.NetworkXNoPath:
            break
        
        # Step 5
        for edge in path_edges:
            G.remove_edge(*edge)
            if edge[0] != s and edge[1] != t:
                G.add_edge(*edge[::-1])

    # Step 4
    M = set()
    for v in V2:
        for u in G.successors(v):
            if u in V1:
                M.add((u, v))

    return M
