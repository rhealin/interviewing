def dfs(s):
	stack = [s]
	visited = []
	while stack:
		node = stack.pop()
		visited.append(node)
		for child in node.children:
			if child not in visited:
				stack.append(child)
	return visited

def dfs(Adj):
	parent = {}
	for s in Adj:
		if s not in parent:
			parent[s] = None
			parent = dfs_visit(Adj, parent, s)
	return parent

def dfs_visit(Adj, parent, s):
	for v in Adj[s]:
		if v not in parent:
			parent[v] = s
			parent = dfs_visit(Adj, parent, v)
	return parent

# Adj = {1: [2], 3: [4], 2: [3, 5], 4: [], 5: []}
# print(dfs(Adj))

