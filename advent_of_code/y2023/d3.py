from __future__ import annotations
from typing import Any, List
from dataclasses import dataclass
import itertools
import re
import numpy as np

from advent_of_code.io import read_input
from advent_of_code.xy import Point2D, Vector2D


@dataclass
class Part:
    p: Point2D
    isgear: bool


@dataclass
class PartNumber:
    v: Vector2D
    value: int


def get_part_numbers(grid: List[List[Any]], point: Point2D) -> List[int]:

    l = []

    for i_shift, j_shift in itertools.product([-1,0,1], [-1,0,1]):

        try:
            target = int(grid[point.i + i_shift][point.j + j_shift])
            l.append(target)

        except:
            pass

    return list(set(l))


def main(test: bool, part: str = None) -> None:

    path = "data/y2023/d3.txt"

    if test:
        path = "tests/" + path

    ans_part1 = "SKIPPED"
    ans_part2 = "SKIPPED"

    # make grid of values
    grid = (
        read_input(
            path=path,
            parse_func=lambda line: [char for char in line],
        )
    )

    # extract parts
    parts = (
        read_input(
            path=path,
            parse_func=lambda line: (
                [m for m in re.finditer(r"[^\.0-9]", line)]
            ),
            post_parse_func=lambda data: (
                [
                    Part(
                        p=Point2D(i=i, j=m.start()),
                        isgear="*" == m.group(),
                    )
                    for i, row in enumerate(data)
                    for m in row
                ]
            ),
        )
    )

    # extract part_numbers
    part_numbers = (
        read_input(
            path=path,
            parse_func=lambda line: (
                [m for m in re.finditer(r"[0-9]+", line)]
            ),
            post_parse_func=lambda data: (
                [
                    PartNumber(
                        v=Vector2D(
                            a=Point2D(i=i, j=m.start()),
                            b=Point2D(i=i, j=m.end()),
                        ),
                        value=int(m.group()),
                    )
                    for i, row in enumerate(data)
                    for m in row
                ]
            ),
        )
    )

    # impute part_numbers at their locations
    for part_number in part_numbers:
        for j_shift in range(part_number.v.b.j - part_number.v.a.j):
            grid[part_number.v.a.i][part_number.v.a.j + j_shift] = part_number.value

    pairs = [
        (part, get_part_numbers(grid=grid, point=part.p))
        for part in parts
    ]

    if part != "2":
        ans_part1 = sum([sum(y) for _, y in pairs])

    if part != "1":
        ans_part2 = sum(np.prod(y) for x, y in pairs if x.isgear and len(y) > 1)

    print(f"AOC 2023 - Day 3")
    print(f"    Part 1: {ans_part1}")
    print(f"    Part 2: {ans_part2}")
