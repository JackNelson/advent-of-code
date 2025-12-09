from typing import List, Tuple
import re
import numpy as np

from advent_of_code.io import read_input
from advent_of_code.xy import Point2D, get_adjacent_point, get_adjacent_value


pipe_dict = {
    "N": {
        "|": "N",
        "7": "W",
        "F": "E"
    },
    "S": {
        "|": "S",
        "J": "W",
        "L": "E",
    },
    "E": {
        "-": "E",
        "J": "N",
        "7": "S",
    },
    "W": {
        "-": "W",
        "L": "N",
        "F": "S",
    }
}

# def get_adjacent_point(p: Point2D, d: str) -> Point2D:

#     d_dict = {
#         "N": Point2D(i=-1, j=0),
#         "S": Point2D(i=1, j=0),
#         "E": Point2D(i=0, j=1),
#         "W": Point2D(i=0, j=-1),
#     }

#     return p + d_dict[d]


# def get_adjacent_value(grid: np.array, p: Point2D, d: str) -> str:

#     tmp = get_adjacent_point(p=p, d=d)

#     return grid[tmp.i, tmp.j]


def get_starting_directions(grid: np.array, p: Point2D) -> List[str]:

    tmp = ["N", "S", "E", "W"]

    return [
        d for d in tmp
        if get_adjacent_value(p=p, dir=d, grid=grid) in pipe_dict[d].keys()
    ]


def travel_down_pipe(grid: np.array, p: Point2D, d: str) -> Tuple[Point2D, str]:

    new_p = get_adjacent_point(p=p, dir=d)
    new_d = pipe_dict[d][grid[new_p.i, new_p.j]]

    return (new_p, new_d)


def expand_grid(grid: np.array) -> np.array:

    rows, cols = grid.shape

    for i in range(rows-1):

            grid = np.vstack(
                (
                    grid[0:(i*2)+1, :],
                    np.full(grid.shape[1], "."),
                    grid[(i*2)+1:, :],
                )
            )

    for j in range(cols-1):

        grid = np.hstack(
            (
                grid[:, 0:(j*2)+1],
                np.full((grid.shape[0], 1), "."),
                grid[:, (j*2)+1:],
            )
        )

    return grid


def main(test: bool, part: int = None) -> None:

    path = "data/y2023/"

    if test:
        if part == "1":
            path = "tests/" + path + "d10a.txt"
        elif part == "2":
            path = "tests/" + path + "d10b.txt"
    else:
        path = path + "d10.txt"

    ans_part1 = "SKIPPED"
    ans_part2 = "SKIPPED"

    grid = read_input(
        path=path,
        parse_func=lambda line: [char for char in line],
        post_parse_func=lambda data: np.array(data)
    )

    start_point = read_input(
        path=path,
        parse_func=lambda line: re.finditer(r"S", line),
        post_parse_func=lambda data: [
            Point2D(i=i, j=m.start())
            for i, line in enumerate(data)
            for m in line if m
        ][0],
    )

    if part != "2":

        tmp = [
            (start_point, d)
            for d in get_starting_directions(grid=grid, p=start_point,)
        ]

        tmp = [
            travel_down_pipe(grid=grid, p=p, d=d)
            for p, d in tmp
        ]
        steps = 1

        while tmp[0][0] != tmp[1][0]:

            steps += 1

            tmp = [
                travel_down_pipe(grid=grid, p=p, d=d)
                for p, d in tmp
            ]

        ans_part1 = steps

    if part != "1":

        new_grid = expand_grid(grid=grid)
        print(new_grid)

    print(f"AOC 2023 - Day 10")
    print(f"    Part 1: {ans_part1}")
    print(f"    Part 2: {ans_part2}")