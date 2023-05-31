def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start, end=" ")

    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

# Test the DFS algorithm
graph = {}

# Reading input graph
edges = input("Enter the edges of the graph in the form (v1,v2), (v2,v3): ").split(", ")
for edge in edges:
    v1, v2 = edge.strip("()").split(",")
    if v1 not in graph:
        graph[v1] = []
    if v2 not in graph:
        graph[v2] = []
    graph[v1].append(v2)
    graph[v2].append(v1)

start_vertex = input("Enter the starting vertex: ")
print("DFS traversal: ", end="")
dfs(graph, start_vertex)
