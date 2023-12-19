from __future__ import annotations
from typing import Dict, List
import re
import numpy as np
import itertools

from advent_of_code.io import read_input


def is_mirror(grid: np.array, cut_val: int, axis: int = 0) -> bool:

    if axis == 1:
        grid = np.transpose(grid)

    length = grid.shape[0]

    a_idx = np.arange(cut_val, -1, -1)
    b_idx = np.arange(cut_val+1, length)

    for a, b in zip(a_idx, b_idx):

        if not np.array_equiv(grid[a,:], grid[b,:]):
            return False

    return True


def is_smudge(grid: np.array, cut_val: int, axis: int = 0) -> bool:

    if axis == 1:
        grid = np.transpose(grid)

    length = grid.shape[0]

    a_idx = np.arange(cut_val, -1, -1)
    b_idx = np.arange(cut_val+1, length)

    mismatches = 0

    for a, b in zip(a_idx, b_idx):

        mismatches += sum([v1!=v2 for v1, v2 in zip(grid[a,:], grid[b,:])])

    return mismatches == 1


def main(test: bool, part: int = None) -> None:

    path = "data/y2023/d13.txt"

    if test:
        path = "tests/" + path

    ans_part1 = "SKIPPED"
    ans_part2 = "SKIPPED"

    data = read_input(
        path=path,
        parse_func=lambda line: [c for c in line],
        post_parse_func=lambda data: [
            np.array(list(group))
            for k, group in itertools.groupby(data, key=lambda line: line != [])
            if k
        ]
    )

    if part != "2":

        ans_part1 = 0

        for grid in data:
            rows, cols = grid.shape

            for i in range(rows-1):

                if is_mirror(grid=grid, cut_val=i):
                    ans_part1 += 100 * (i+1)
                    break

            for j in range(cols-1):

                if is_mirror(grid=grid, cut_val=j, axis=1):
                    ans_part1 += j+1
                    break

    if part != "1":

        ans_part2 = 0

        for grid in data:
            rows, cols = grid.shape

            for i in range(rows-1):

                if is_smudge(grid=grid, cut_val=i):
                    ans_part2 += 100 * (i+1)
                    break

            for j in range(cols-1):

                if is_smudge(grid=grid, cut_val=j, axis=1):
                    ans_part2 += j+1
                    break

    print(f"AOC 2023 - Day 13")
    print(f"    Part 1: {ans_part1}")
    print(f"    Part 2: {ans_part2}")
