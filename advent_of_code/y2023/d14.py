from __future__ import annotations
from typing import List
from dataclasses import dataclass
import numpy as np

from advent_of_code.io import read_input
from advent_of_code.xy import Point2D


@dataclass
class RoundedRock:
    p: Point2D

    def load(self, grid: np.array) -> int:

        rows = grid.shape[0]

        return rows - self.p.i


def get_rounded_rocks(grid: np.array) -> List[RoundedRock]:

    return [
            RoundedRock(p=Point2D(i=i, j=j))
            for i, j in zip(*np.where(grid == "O"))
        ]


def move_up(grid: np.array, rounded_rock: RoundedRock) -> np.array:

    if rounded_rock.p.i == 0:
        return grid

    elif grid[rounded_rock.p.i-1, rounded_rock.p.j] != ".":
        return grid

    else:
        grid[*rounded_rock.p] = "."
        rounded_rock.p.i -= 1
        grid[*rounded_rock.p] = "O"

        return move_up(grid=grid, rounded_rock=rounded_rock)


def spin_cycle(grid: np.array) -> np.array:

    for _ in range(4):

        rounded_rocks = [
            RoundedRock(p=Point2D(i=i, j=j))
            for i, j in zip(*np.where(grid == "O"))
        ]

        for rounded_rock in rounded_rocks:
            grid = move_up(grid=grid, rounded_rock=rounded_rock)

        grid = np.rot90(grid, -1)

    return grid


def get_pattern_start(l: List[int], min_pattern_length: int = 3) -> int:

    if len(l) // min_pattern_length > 2:

        for j in range((len(l) // min_pattern_length) - 2):

                    tmp = np.reshape(l[-(9 + j*3):], (3, j+3))

                    if (
                        np.array_equal(tmp[0,:], tmp[1,:])
                        and np.array_equal(tmp[0,:], tmp[2,:])
                    ):
                        return len(l) - ((j+3) * 3)

    return None


def main(test: bool, part: str = None) -> None:

    path = "data/y2023/d14.txt"

    if test:
        path = "tests/" + path

    ans_part1 = "SKIPPED"
    ans_part2 = "SKIPPED"

    grid = (
        read_input(
            path=path,
            parse_func=lambda line: [char for char in line],
            post_parse_func=lambda data: np.array(data),
        )
    )

    if part != "2":

        rounded_rocks = get_rounded_rocks(grid=grid)

        for rounded_rock in rounded_rocks:

            grid = move_up(grid=grid, rounded_rock=rounded_rock)

        ans_part1 = sum([r.load(grid) for r in rounded_rocks])

    if part != "1":

        l = []
        for _ in range(1000000000):

            grid = spin_cycle(grid=grid)

            rounded_rocks = get_rounded_rocks(grid=grid)
            l.append(sum([r.load(grid) for r in rounded_rocks]))

            pattern_start = get_pattern_start(l=l)

            if pattern_start:
                break

        pattern_idx = int((1000000000 - pattern_start) % (len(l[pattern_start:]) / 3) - 1)

        ans_part2 = l[pattern_start+pattern_idx]

    print(f"AOC 2023 - Day 14")
    print(f"    Part 1: {ans_part1}")
    print(f"    Part 2: {ans_part2}")
