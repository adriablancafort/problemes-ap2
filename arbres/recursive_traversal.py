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

def llegir_preordre() -> Arbin:
    x = read(int)
    if x == -1:
        return None
    else:
        return Node(x, llegir_preordre(), llegir_preordre())


def escriure_postordre(a: Optional[Node]) -> None:
    if a is not None:
        escriure_postordre(a.fe)
        escriure_postordre(a.fd)
        print("", end=" ")
        print(a.elem, end="")


def escriure_inordre(a: Optional[Node]) -> None:
    if a is not None:
        escriure_inordre(a.fe)
        print("", end=" ")
        print(a.elem, end="")
        escriure_inordre(a.fd)

def main() -> None:
    a = llegir_preordre()
    print("pos:", end="")
    escriure_postordre(a)
    print("")
    print("ino:", end="")
    escriure_inordre(a)
    print("")

main()