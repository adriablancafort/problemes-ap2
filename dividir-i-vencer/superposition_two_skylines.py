# agafar la longitud mes llarga de les dues llistes

# posar les coordenades de la primera llista a dins

# posar les coordenades de la segona llista quan la y és mes gran que la que ja existeix

# treure les coordenades repetides

# -----------

# ordenar les coordenades x
# quedar-nos amb el maxim de la coordenada y del punt actual i la coordenada y de l'ultim punt
# quan sureten dos d'iguals, agafar el màxim


from yogi import read
from dataclases import dataclass
from typing import TypeAlias

@dataclass
class Skyline:
    x: int
    y: int

sk1 = [Point(0,0)]
sk2 = [Point(0,0)]

while i < len(sk1) and j < len(sk2):
    if sk1[i].x < sk2[j], sk2[j]
