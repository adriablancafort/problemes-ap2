from heapq import heappop, heappush
from yogi import read

def topological_sort(n: int, edges: list[tuple[int, int]]) -> list[int]:
    indegree = [0] * n
    graph = [[] for _ in range(n)]
    for x, y in edges:
        graph[x].append(y)
        indegree[y] += 1
    heap = [i for i in range(n) if indegree[i] == 0]
    result = []
    while heap:
        node = heappop(heap)
        result.append(node)
        for neighbor in graph[node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                heappush(heap, neighbor)
    return result

def main():
    while True:
        n = read(int)
        if n is None:
            break
        m = read(int)
        edges = [tuple(read(int) for _ in range(2)) for _ in range(m)]
        result = topological_sort(n, edges)
        print(' '.join(map(str, result)))

main()