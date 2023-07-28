def dijkstra(graph, source):

    distances = [float("inf") for _ in range(len(graph))]
    distances[source] = 0
    visited = set()

    pq = []
    heapq.heappush(pq, (0, source))

    while not pq.empty():
        d, u = heapq.heappop(pq)

        if u in visited:
            continue

        visited.add(u)

        for v, w in graph[u]:
            if distances[v] > distances[u] + w:
                distances[v] = distances[u] + w
                heapq.heappush(pq, (distances[v], v))

    return distances


def main():
    graph = [[(1, 1), (2, 5)], [(0, 1), (3, 2)], [(0, 5), (2, 3)], [(1, 2), (3, 1)]]
    source = 0
    distances = dijkstra(graph, source)
    print(distances)


if __name__ == "__main__":
    main()
