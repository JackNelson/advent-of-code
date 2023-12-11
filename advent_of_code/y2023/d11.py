from typing import List, Tuple
import re
import numpy as np
import itertools

from advent_of_code.io import read_input
from advent_of_code.xy import Point2D


def expand_universe(grid: np.array, scale: int) -> np.array:

    dist_grid = np.ones(grid.shape)

    # scale rows
    for i in range(len(grid)):

        if all([x == "." for x in grid[i, :]]):
            dist_grid[i, :] = scale

    # scale columns
    for j in range(len(grid[0])):

        if all([x == "." for x in grid[:, j]]):
            dist_grid[:, j] = scale

    return dist_grid


def get_distance(p1: Point2D, p2: Point2D, grid:np.array) -> int:

    return (
        sum(grid[p1.i, min(p1.j, p2.j):max(p1.j, p2.j)]) +
        sum(grid[min(p1.i, p2.i):max(p1.i, p2.i), p1.j])
    )


def main(test: bool, part: int = None) -> None:

    path = "data/y2023/d11.txt"

    if test:
        path = "tests/" + path

    ans_part1 = "SKIPPED"
    ans_part2 = "SKIPPED"

    grid = read_input(
        path=path,
        parse_func=lambda line: [char for char in line],
        post_parse_func=lambda data: np.array(data)
    )

    galaxies = [
        Point2D(i=i, j=j)
        for i, j in list(zip(*np.where(grid == "#")))
    ]

    pairs = [pair for pair in itertools.combinations(galaxies, 2)]

    if part != "2":

        dist_grid = expand_universe(grid=grid, scale=2)
        ans_part1 = int(sum(
            [
                get_distance(p1=p1, p2=p2, grid=dist_grid) for p1, p2 in pairs
            ]
        ))

    if part != "1":

        if test:
            scale = 100
        else:
            scale = 1000000

        dist_grid = expand_universe(grid=grid, scale=scale)
        ans_part2 = int(sum(
            [
                get_distance(p1=p1, p2=p2, grid=dist_grid) for p1, p2 in pairs
            ]
        ))

    print(f"AOC 2023 - Day 11")
    print(f"    Part 1: {ans_part1}")
    print(f"    Part 2: {ans_part2}")