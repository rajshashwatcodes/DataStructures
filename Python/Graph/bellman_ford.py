class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def add_edge(self, u, v, weight):
        self.graph.append((u, v, weight))

    def bellman_ford(self, source):
        distances = [float('inf')] * self.V
        distances[source] = 0

        for _ in range(self.V - 1):
            for u, v, weight in self.graph:
                if distances[u] != float('inf') and distances[u] + weight < distances[v]:
                    distances[v] = distances[u] + weight

        # Check for negative weight cycles
        for u, v, weight in self.graph:
            if distances[u] != float('inf') and distances[u] + weight < distances[v]:
                raise ValueError("Graph contains negative weight cycle")

        return distances

# Example usage:
if __name__ == "__main__":
    # Create a graph with 5 vertices
    graph = Graph(5)
    
    # Add edges to the graph (u, v, weight)
    graph.add_edge(0, 1, 6)
    graph.add_edge(0, 3, 7)
    graph.add_edge(1, 2, 5)
    graph.add_edge(1, 3, 8)
    graph.add_edge(1, 4, -4)
    graph.add_edge(2, 1, -2)
    graph.add_edge(3, 2, -3)
    graph.add_edge(3, 4, 9)
    graph.add_edge(4, 0, 2)
    graph.add_edge(4, 2, 7)

    source_vertex = 0
    distances = graph.bellman_ford(source_vertex)

    print(f"Shortest distances from vertex {source_vertex} to all other vertices:")
    for vertex, distance in enumerate(distances):
        print(f"Vertex {vertex}: {distance}")
