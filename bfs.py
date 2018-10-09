# apsp best known alg for unweighted O(VE)
# sssp best known alg for unweighted O(V+E)
def bfs(Adj, start, end):
    level = {start: 0}
    parent = {start: None}
    i = 1
    frontier = [start]

    while frontier:
        next = []
        for u in frontier:
            for v in Adj[u]:
                if v not in level:
                    level[v] = i
                    parent[v] = u
                    if v == end:
                        return parent
                    next.append(v)
        frontier = next
        i += 1
    return parent

Adj = {1: [2], 3: [4], 2: [3, 5], 4: [], 5: []}
print(bfs(Adj, 1, 5))