## Topological sorting for Directed Acyclic Graph (DAG) is a linear 
# ordering of vertices such that for every directed edge uv, vertex 
# u comes before v in the ordering. Topological Sorting for a graph 
# is not possible if the graph is not a DAG

from collections import defaultdict

class Graph:
    def __init__(self,vertices):
        self.graph = defaultdict(list) #dictionary containing adjacency List
        self.V = vertices #No. of vertices
 
    def add_edge(self,u,v):
        self.graph[u].append(v)
 
    def topological_sort_util(self,v,visited,stack):
        """ A recursive function used by topological_sort. """
        # mark the current node as visited.
        visited[v] = True
 
        # recur for all the vertices adjacent to this vertex
        for i in self.graph[v]:
            if visited[i] == False:
                self.topological_sort_util(i,visited,stack)
 
        # push current vertex to stack which stores result
        stack.insert(0,v)
 
    # The function to do topological sort. It uses recursive 
    # topological_sort_util()
    def topological_sort(self):
        # Mark all the vertices as not visited
        visited = [False]*self.V
        stack =[]
 
        # Call the recursive helper function to store Topological
        # Sort starting from all vertices one by one
        for i in range(self.V):
            if visited[i] == False:
                self.topological_sort_util(i,visited,stack)
 
        # Print contents of the stack
        print stack
 
g = Graph(6)
g.add_edge(5, 2);
g.add_edge(5, 0);
g.add_edge(4, 0);
g.add_edge(4, 1);
g.add_edge(2, 3);
g.add_edge(3, 1);
 
g.topological_sort()

##### other implementation

def dfs_topsort(graph):         # recursive dfs with 
    L = []                      # additional list for order of nodes
    color = { u : "white" for u in graph }
    found_cycle = False
    for u in graph:
        if color[u] == "white":
            dfs_visit(graph, u, color, L, found_cycle)
        if found_cycle:
            break
 
    if found_cycle:           # if there is a cycle, 
        L = []                   # then return an empty list  
 
    L.reverse()                  # reverse the list
    return L                     # L contains the topological sort
 
 
def dfs_visit(graph, u, color, L, found_cycle):
    if found_cycle:
        return
    color[u] = "gray"
    for v in graph[u]:
        if color[v] == "gray":
            found_cycle = True
            return
        if color[v] == "white":
            dfs_visit(graph, v, color, L, found_cycle)
    color[u] = "black"      # when we're done with u,
    L.append(u)             # add u to list (reverse it later!)


graph_tasks = { "wash the dishes" : ["have lunch"],
                "cook food" : ["have lunch"],
                "have lunch" : [],
                "wash laundry" : ["dry laundry"],
                "dry laundry" : ["fold laundry"],
                "fold laundry" : [] }

order = dfs_topsort(graph_tasks)
 
for task in order:
    print(task)
