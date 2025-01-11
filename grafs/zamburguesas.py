from typing import List, Tuple
from collections import deque
from math import sqrt
from yogi import read

def bfs(n: int, d: float, rocks: List[Tuple[float, float, float]]) -> int:
    graph = [[] for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            xi, yi, ri = rocks[i]
            xj, yj, rj = rocks[j]
            if sqrt((xi - xj) ** 2 + (yi - yj) ** 2) - ri - rj <= d:
                graph[i].append(j)
                graph[j].append(i)
    queue = deque([(0, 0)])
    visited = [False] * n
    while queue:
        node, jumps = queue.popleft()
        if node == n - 1:
            return jumps
        for neighbor in graph[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append((neighbor, jumps + 1))
    return -1

def main():
    while True:
        n = read(int)
        if n is None:
            break
        d = read(float)
        rocks = [tuple(read(float) for _ in range(3)) for _ in range(n)]
        jumps = bfs(n, d, rocks)
        if jumps != -1:
            print(jumps)
        else:
            print("Xof!")


main()