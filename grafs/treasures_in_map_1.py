from typing import List
from yogi import read

def is_valid(map: List[List[str]], x: int, y: int, visited: List[List[bool]]) -> bool:
    """Returns True if the coordinate is within the map, not previously visited, and not an obstacle."""
    return 0 <= x < len(map) and 0 <= y < len(map[0]) and not visited[x][y] and map[x][y] != 'X'

def is_treasure(map: List[List[str]], x: int, y: int) -> bool:
    """Returns True if the coordinate is a treasure."""
    return map[x][y] == 't'

def dfs(map: List[List[str]], x: int, y: int, visited: List[List[bool]]) -> bool:
    """Performs a DFS on the map and checks if a treasure is reachable."""
    if not is_valid(map, x, y, visited):
        return False

    visited[x][y] = True
    if is_treasure(map, x, y):
        return True

    # Call dfs recursively for each direction
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        if dfs(map, x + dx, y + dy, visited):
            return True

    return False


def main():
    n, m = read(int), read(int)
    map = [list(read(str)) for _ in range(n)]
    x, y = read(int), read(int)
    visited = [[False] * m for _ in range(n)]
    print("yes") if dfs(map, x - 1, y - 1, visited) else print("no")


main()