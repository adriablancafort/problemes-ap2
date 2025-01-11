from typing import List
from yogi import read


def is_valid(map: List[List[str]], x: int, y: int, visited: List[List[bool]]) -> bool:
    """Retorna cert si la coordenada està a dins del mapa, no està prèviament visitada i no és un obstacle."""
    return 0 <= x < len(map) and 0 <= y < len(map[0]) and not visited[x][y] and map[x][y] != 'X'


def is_treasure(map: List[List[str]], x: int, y: int) -> int:
    """Retorna cert si la coordenada és un tresor."""
    return map[x][y] == 't'


def dfs(map: List[List[str]], x: int, y: int, visited: List[List[bool]]) -> int:
    """Fa un DFS sobre el mapa i compta el nombre de tresors accessibles."""
    if not is_valid(map, x, y, visited): return 0

    visited[x][y] = True
    treasures = 1 if is_treasure(map, x, y) else 0

    # Es crida recursivament avançant una posició en cada una de les 4 direccions permeses
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        treasures += dfs(map, x + dx, y + dy, visited)
    return treasures


def main():
    n, m = read(int), read(int)
    map = [list(read(str)) for _ in range(n)]
    x, y = read(int), read(int)
    visited = [[False] * m for _ in range(n)]
    print(dfs(map, x - 1, y - 1, visited))


main()