class Graph:
    def __init__(self, graph):
        self.graph = graph

    def find_parent(self, parent, node):
        if parent[node] == node:
            return node
        return self.find_parent(parent, parent[node])

    def union(self, parent, rank, x, y):
        x_root = self.find_parent(parent, x)
        y_root = self.find_parent(parent, y)
        if rank[x_root] < rank[y_root]:
            parent[x_root] = y_root
        elif rank[x_root] > rank[y_root]:
            parent[y_root] = x_root
        else:
            parent[y_root] = x_root
            rank[x_root] += 1

    def kruskal_mst(self):
        mst = []
        edges = []

        for node, neighbors in self.graph.items():
            for neighbor, weight in neighbors:
                edges.append((node, neighbor, weight))

        edges.sort(key=lambda edge: edge[2])
        parent = {node: node for node in self.graph}
        rank = {node: 0 for node in self.graph}

        for edge in edges:
            source, destination, weight = edge
            if self.find_parent(parent, source) != self.find_parent(parent, destination):
                mst.append(edge)
                self.union(parent, rank, source, destination)

        return mst

if __name__ == "__main__":
    data = {
        'A': [('B', 3), ('D', 4), ('E', 4)],
        'B': [('A', 3), ('C', 10), ('E', 2), ('F', 3)],
        'C': [('B', 10), ('F', 6), ('G', 1)],
        'D': [('A', 4), ('E', 5), ('H', 6)],
        'E': [('A', 4), ('B', 2), ('D', 5), ('F', 11), ('H', 2), ('I', 1)],
        'F': [('B', 3), ('C', 6), ('E', 11), ('G', 2), ('I', 3), ('J', 11)],
        'G': [('C', 1), ('F', 2), ('J', 8)],
        'H': [('D', 6), ('E', 2), ('I', 4)],
        'I': [('E', 1), ('F', 3), ('H', 4), ('J', 7)],
        'J': [('F', 11), ('G', 8), ('I', 7)]
    }

    graph = Graph(data)
    mst = graph.kruskal_mst()

    print("Minimum Spanning Tree:")
    for edge in mst:
        print(f"{edge[0]} - {edge[1]} : {edge[2]}")
