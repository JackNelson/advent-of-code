from __future__ import annotations
from typing import Dict, List, Tuple
from dataclasses import dataclass
import numpy as np

from advent_of_code.io import read_input
from advent_of_code.xy import Point2D, get_adjacent_point


class BeamGrid:


    beam_dict = {
        "N": {
            ".": ["N"],
            "-": ["E", "W"],
            "|": ["N"],
            "/": ["E"],
            "\\": ["W"],
        },
        "S": {
            ".": ["S"],
            "-": ["E", "W"],
            "|": ["S"],
            "/": ["W"],
            "\\": ["E"],
        },
        "E": {
            ".": ["E"],
            "-": ["E"],
            "|": ["N", "S"],
            "/": ["N"],
            "\\": ["S"],
        },
        "W": {
            ".": ["W"],
            "-": ["W"],
            "|": ["N", "S"],
            "/": ["S"],
            "\\": ["N"],
        },
    }


    def __init__(self, start_p: Point2D, start_dir: str, grid: np.array):

        self.start_p = start_p
        self.start_dir = start_dir
        self.grid = grid

        self.energized_grid = np.full(shape=grid.shape, fill_value=".")
        self.trace = []


    @property
    def energized_tiles(self) -> int:
        return (self.energized_grid == "#").sum()


    def energize_grid(
        self,
        p: Point2D = None,
        dir: str = None,
    ) -> None:

        if p is None:
            p = self.start_p

        if dir is None:
            dir = self.start_dir

        while (p, dir) not in self.trace:

            self.trace.append((p, dir))

            try:
                self.energized_grid[*p] = "#"
            except:
                break

            dirs = self.beam_dict[dir][self.grid[*p]]

            if len(dirs) > 1:

                for dir in dirs:

                    new_p = get_adjacent_point(p=p, dir=dir, grid=self.grid)

                    if new_p:
                        self.energize_grid(p=new_p, dir=dir)

                break

            else:

                p = get_adjacent_point(p=p, dir=dirs[0], grid=self.grid)
                dir = dirs[0]

                if not p:
                    break


def main(test: bool, part: int = None) -> None:

    path = "data/y2023/d16.txt"

    if test:
        path = "tests/" + path

    ans_part1 = "SKIPPED"
    ans_part2 = "SKIPPED"

    grid = read_input(
        path=path,
        parse_func=lambda line: [char for char in line],
        post_parse_func=lambda data: np.array(data)
    )

    if part != "2":

        beam_grid = BeamGrid(
            start_p=Point2D(i=0, j=0),
            start_dir="E",
            grid=grid,
        )

        beam_grid.energize_grid()

        ans_part1 = beam_grid.energized_tiles

    if part != "1":

        ans_part2 = 0

        for i, dir in zip([0, grid.shape[0]], ["S", "N"]):
            for j in range(grid.shape[1]):

                beam_grid = BeamGrid(
                    start_p=Point2D(i=i, j=j),
                    start_dir=dir,
                    grid=grid,
                )

                beam_grid.energize_grid()

                ans_part2 = max(beam_grid.energized_tiles, ans_part2)

        for j, dir in zip([0, grid.shape[1]], ["E", "W"]):
            for i in range(grid.shape[0]):

                beam_grid = BeamGrid(
                    start_p=Point2D(i=i, j=j),
                    start_dir=dir,
                    grid=grid,
                )

                beam_grid.energize_grid()

                ans_part2 = max(beam_grid.energized_tiles, ans_part2)

    print(f"AOC 2023 - Day 16")
    print(f"    Part 1: {ans_part1}")
    print(f"    Part 2: {ans_part2}")