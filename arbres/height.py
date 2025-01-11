from typing import Optional, TypeAlias
from dataclasses import dataclass
from yogi import read


@dataclass
class Node:
    elem: int
    fe: 'Arbin'
    fd: 'Arbin'


Arbin: TypeAlias = Optional[Node]


def height(a: Arbin) -> int:
    if a is None:
        return 0

    return max(height(a.fe), height(a.fd)) + 1


def read_tree() -> Optional[Arbin]:
    elem = read(int)
    if elem == -1:
        return None
    else:
        fe = read_tree()
        fd = read_tree()
        return Node(elem, fe, fd)

def main() -> None:
    m = read(int)
    for _ in range(m):
        a = read_tree()
        print(height(a))

main()