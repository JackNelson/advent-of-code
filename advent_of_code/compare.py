from typing import Any, List

def get_intersection(l: List[Any]) -> List[Any]:
    return list(set.intersection(*map(set, l)))

def get_x_dist(p1: List[int], p2: List[int]) -> int:
    return p1