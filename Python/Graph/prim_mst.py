import heapq

class Graph:
    def __init__(self, graph):
        self.graph = graph

    def prim_mst(self):
        start_node = next(iter(self.graph))  # Starting node (arbitrarily chosen)
        mst = []
        visited = {node: False for node in self.graph}
        priority_queue = [(0, start_node, None)]  # (weight, node, parent) tuples

        while priority_queue:
            weight, current_node, parent_node = heapq.heappop(priority_queue)
            if visited[current_node]:
                continue
            visited[current_node] = True

            if parent_node is not None:
                mst.append((current_node, parent_node, weight))

            for neighbor, edge_weight in self.graph[current_node]:
                if not visited[neighbor]:
                    heapq.heappush(priority_queue, (edge_weight, neighbor, current_node))

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
    mst = graph.prim_mst()

    print("Minimum Spanning Tree:")
    for edge in mst:
        print(f"{edge[0]} - {edge[1]} : {edge[2]}")
