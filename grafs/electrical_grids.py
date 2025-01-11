from yogi import read, scan
from heapq import heapify, heappush, heappop

n: int
m: int
adj: list[list[tuple[int, int]]]
inv_adj: list[list[tuple[int, int]]]
flow: dict[tuple[int, int], int] = {}

def augmenting_path() -> tuple[list[int], int]:
    global n, adj, inv_adj, flow
    pq: list[tuple[int, int]] = [(-1000000000, 0)]
    heapify(pq)
    vis = [True if i == 0 else False for i in range(n)]
    pred = [-1 for i in range(n)]
    last: int = -1
    new_flow: int = 0       

    while len(pq) > 0:
        f, u = heappop(pq)
        if u == n-1 and -f > 0:
            last = u
            new_flow = -f
            break

        for v, c in adj[u]:
            if not vis[v] and c-flow[(u, v)] > 0:
                vis[v] = True
                heappush(pq, (-(min(-f, c - flow[(u, v)])), v))
                pred[v] = u

        for v, c in inv_adj[u]:
            if not vis[v] and flow[(v, u)] > 0:
                vis[v] = True
                heappush(pq, (-(min(-f, flow[(v, u)])), v))
                pred[v] = u

    path: list[int] = []
    while last != -1:
        path.append(last)
        last = pred[last]
    path = list(reversed(path))
    return path, new_flow

def max_flow() -> int:
    aug_path, new_flow = augmenting_path()
    while new_flow > 0:
        for i in range(len(aug_path)-1):
            u = aug_path[i]
            v = aug_path[i+1]
            if (u, v) in flow: flow[(u, v)] += new_flow
            else: flow[(v, u)] -= new_flow
        aug_path, new_flow = augmenting_path()

    max_flow = 0
    for v, c in adj[0]:
        max_flow += flow[(0, v)]
    return max_flow

def main() -> None:
    global n, m, adj, inv_adj, flow

    n, m = scan(int), scan(int)
    while n is not None:
        adj = [[] for i in range(n)]
        inv_adj = [[] for i in range(n)]
        flow = {}

        for i in range(m):
            u, v, c = read(int), read(int), read(int)
            adj[u].append((v, c))
            flow[(u, v)] = 0
            inv_adj[v].append((u, c))
        print(max_flow())

        n, m = scan(int), scan(int)

if __name__ == "__main__":
    main()