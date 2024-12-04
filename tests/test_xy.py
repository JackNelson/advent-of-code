import pytest
import numpy as np

from advent_of_code.xy import (
    Point2D,
    Vector2D,
    get_grid,
    get_grid_datum,
    sum_points,
    get_grid_loc,
    x_distance,
    y_distance,
    manhattan_distance,
    get_adjacent_point,
)


def test_point2d__eq__():

    p1 = Point2D(i=1,j=1)
    p2 = Point2D(i=1,j=1)

    assert p1 == p2


def test_point2d__add__():

    p1 = Point2D(i=1,j=1)
    p2 = Point2D(i=1,j=1)
    ans = Point2D(i=2,j=2)

    assert (p1 + p2) == ans


def test_point2d__sub__():

    p1 = Point2D(i=1,j=1)
    p2 = Point2D(i=1,j=1)
    ans = Point2D(i=0,j=0)

    assert (p1 - p2) == ans


def test_point2d__iter__():

    l = [1,2]
    p = Point2D(i=1,j=2)

    assert all([a == b for a, b in zip(l,p)])

@pytest.mark.parametrize(
    "p, dir, ans",
    [
        (Point2D(i=1,j=1), "N", Point2D(i=0,j=1)),
        (Point2D(i=1,j=1), "S", Point2D(i=2,j=1)),
        (Point2D(i=1,j=1), "E", Point2D(i=1,j=0)),
        (Point2D(i=1,j=1), "W", Point2D(i=1,j=2)),
        (Point2D(i=0,j=2), "N", None),
        (Point2D(i=2,j=0), "S", None),
        (Point2D(i=0,j=2), "E", None),
        (Point2D(i=2,j=0), "W", None),
    ],
)
def test_get_adjacent_point(p, dir, ans):

    grid = np.array([[1,2,3],[4,5,6],[7,8,9],])

    adj_p = get_adjacent_point(p=p, dir=dir, grid=grid)

    adj_p == ans
