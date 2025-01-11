from typing import List
from yogi import read

AdjacencyList = List[int]
Graph = List[AdjacencyList]


def dfs(G: Graph, u: int, vis: List[bool]):
    if not vis[u]:
        vis[u] = True
        for v in G[u]:
            dfs(G, v, vis)


def reachable(G: Graph, x: int, y: int) -> bool:
    n = len(G)
    vis = [False for _ in range(n)]
    dfs(G, x, vis)
    return vis[y]


def main():
    n = read(int)
    names = [read(str) for _ in range(n)]
    name_to_index = {name: index for index, name in enumerate(names)}
    m = read(int)
    G: Graph = [[] for _ in range(n)]
    for _ in range(m):
        u, v = read(str), read(str)
        G[name_to_index[u]].append(name_to_index[v])
    x, y = read(str), read(str)
    print("yes" if reachable(G, name_to_index[x], name_to_index[y]) else "no")


main()
