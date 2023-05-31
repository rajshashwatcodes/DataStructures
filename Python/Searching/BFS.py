from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)

    while queue:
        vertex = queue.popleft()
        print(vertex, end=" ")

        for neighbor in graph[vertex]:
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)

# Test the BFS algorithm
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
print("BFS traversal: ", end="")
bfs(graph, start_vertex)
