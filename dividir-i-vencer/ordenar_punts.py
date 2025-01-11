from yogi import read, tokens
from typing import Optional
from math import sqrt
from functools import cmp_to_key

class Point:
    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y
    
    def _distance(self, p: Optional["Point"]) -> float:
        dx, dy = self.x, self.y
        if p is not None:
            dx -= p.x
            dy -= p.y
        return dx*dx + dy*dy
    
def ordena_punts_x(p1: Point, p2: Point) -> int:
    p1x, p2x = p1.x, p2.x
    if p1x != p2x:
        return int(p1x - p2x)
    return int(p1.y - p2.y)

def ordena_punts_y(p1: Point, p2: Point) -> int:
    p1y, p2y = p1.y, p2.y
    if p1y != p2y:
        return int(p1y - p2y)
    return int(p1.x - p2.x)
    
def find_strip(p: list[Point], left: int, right: int, d: float) -> list[Point]:
    mid = (left + right ) // 2
    pmid = p(mid).x
    return [p[i] for i in range(left, right + 1) if abs(p[i].x - pmid) < d]

def dist_in_middle(s: list[Point], d: float):
    s.sort(key=cmp_to_key(ordena_punts_x))
    return sqer(closest_distance_rec(p, 0, len(p) - 1))


def closest_distance_rec(p: list[Point], left: int, right: int) -> float:
    dist = float("inf")
    if left < right:
        mid = (left + right) // 2
        dist = min(
            closest_distance_rec(p, left, mid), closest_distance_rec(p, mid+1, right)
        )
        s = find_strip(p, left, right, dist)
        dstm = dist_in_middle(s, dist)
        dist = min(dist, distm)
     return dist

