from collections import deque
from yogi import read

def bfs(map: list[list[str]], x: int, y: int) -> int:
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    queue = deque([(x, y, 0)])
    visited = [[False] * len(map[0]) for _ in range(len(map))]
    max_steps = -1
    while queue:
        x, y, steps = queue.popleft()
        if map[x][y] == 't':
            max_steps = max(max_steps, steps)
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx >= 0 and ny >= 0 and nx < len(map) and ny < len(map[0]) and not visited[nx][ny] and map[nx][ny] != 'X':
                visited[nx][ny] = True
                queue.append((nx, ny, steps + 1))
    return max_steps

def main():
    n, m = read(int), read(int)
    map = [list(read(str)) for _ in range(n)]
    x, y = read(int), read(int)
    x -= 1
    y -= 1
    steps = bfs(map, x, y)
    if steps != -1:
        print(f"maximum distance: {steps}")
    else:
        print("no treasure can be reached")

main()