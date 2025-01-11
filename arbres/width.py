from __future__ import annotations
from dataclasses import dataclass
from typing import TypeAlias, Optional
from yogi import read


@dataclass
class Node:
    elem: int
    fe: Arbin
    fd: Arbin


Arbin: TypeAlias = None | Node

def read_tree() -> Optional[Arbin]:
    x = read(int)
    if x == -1:
        return None
    return Node(x, read_tree(), read_tree())


def width(a: Arbin) -> int:
    levels: list[list[int]] = []

    def dfs(node: Arbin, depth: int = 0):
        if node:
            if len(levels) <= depth:
                levels.append([])
            levels[depth].append(node.elem)
            dfs(node.fe, depth + 1)
            dfs(node.fd, depth + 1)
    dfs(a)
    return max(len(level) for level in levels) if levels else 0



def main() -> None:
    m = read(int)
    for _ in range(m):
        a = read_tree()
        print(width(a))

main()
