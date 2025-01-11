from typing import Optional

def average(s: set[float]) -> float:
    """
    Retorna la mitjana dels elements d’un conjunt no buit.
    """
    return sum(s) / len(s)

def different_elements(l1: list[int], l2: list[int]) -> int:
    """
    Donades dues llistes, retorna el nombre d’elements diferents que contenen entre les dues.
    """
    return len(set(l1) | set(l2))

def has_duplicates(L: list[int]) -> bool:
    """
    Donada una llista, indica si aquesta té o no algun elements duplicat.
    """
    return len(L) != len(set(L))

def extraneous(l1: list[str], l2: list[str]) -> str:
    """
    A partir d’una llista l1, s’ha generat una llista l2 permutant a l’atzar els seus elements i afegint un nou element (en alguna posició). Retorna aquest nou element.
    """
    return list(set(l2) - set(l1)).pop()

def extraneous_maybe(l1: list[str], l2: list[str]) -> Optional[str]:
    """
    Retorna el nou element si s’ha afegit o None si n’hi ha cap de nou.
    """
    nou = list(set(l2) - set(l1))
    if nou:
        return nou.pop()

def different_words(s: str) -> int:
    """
    Retorna el nombre total de paraules diferents
    """
    return len(set(s.lower().split()))