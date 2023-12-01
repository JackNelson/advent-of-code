from typing import Any, List, Tuple
import numpy as np
import operator

def get_grid(points: List[Tuple[int, int]], fill_value: Any) -> np.array:

    return np.full(
        shape = (
            points[:,0].max() - points[:,0].min() + 1,
            points[:,1].max() - points[:,1].min() + 1
        ),
        fill_value=fill_value
    )

def get_grid_datum(points: List[Tuple[int, int]]) -> Tuple[int, int]:

    return (
        0 - points[:,0].min(),
        0 - points[:,1].min()
    )

def sum_points(points: List[Tuple[int, int]]) -> Tuple[int, int]:
    return tuple(map(operator.add, *points))

def get_grid_loc(point: Tuple[int, int], datum: Tuple[int, int]) -> Tuple[int, int]:
    return sum_points(points=[point, datum])

def x_distance(point1: Tuple[int, int], point2: Tuple[int, int]) -> int:
    return point2[0] - point1[0]

def y_distance(point1: Tuple[int, int], point2: Tuple[int, int]) -> int:
    return point2[1] - point1[1]

def manhattan_distance(point1: Tuple[int, int], point2: Tuple[int, int]) -> int:
    return (
        abs(x_distance(point1=point1, point2=point2)) +
        abs(y_distance(point1=point1, point2=point2))
    )