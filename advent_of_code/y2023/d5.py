from __future__ import annotations
from typing import Any, List
from dataclasses import dataclass
import re
from itertools import groupby
import numpy as np

from advent_of_code.io import read_input


@dataclass
class GardenMapLine:
    to_n: int
    from_n: int
    range_n: int

    def shift_value(self) -> int:
        return self.from_n - self.to_n

    def map_value(self, n: int) -> int:

        if (n >= self.from_n) and (n <= self.from_n + self.range_n):
            return self.to_n + (n - self.from_n)

        else:
            return n


@dataclass
class GardenMap:
    from_cat: str
    to_cat: str
    map_lines: List[GardenMapLine]

    def get_map_line(self, n: int) -> GardenMapLine:

        tmp = self.map_lines[0]

        for map_line in sorted(self.map_lines, key=lambda x: x.from_n):

            if n >= map_line.from_n:
                tmp = map_line
            else:
                break

        return tmp


def parse_line(line: str) -> List[Any]:

    l = re.findall(r"^([a-z]+)-to-([a-z]+) map\:$", line)

    if not l:
        l = [int(x) for x in re.findall(r"\d+", line)]
    else:
        l = l[0]

    return l


def group_lines(lines: List[Any]) -> Any:
    return [
        list(group)
        for key, group in groupby(lines, key=lambda x: x == [])
        if not key
    ]

def get_location_value(
        garden_maps: List[GardenMap],
        n: int,
        from_cat: str = "seed",
    ) -> int:

        v = n

        if from_cat != "location":

            gm = [gm for gm in garden_maps if gm.from_cat == from_cat][0]
            new_n = gm.get_map_line(n=n).map_value(n)

            v = get_location_value(
                garden_maps=garden_maps,
                n=new_n,
                from_cat=gm.to_cat,
            )

        return v


def main(test: bool, part: int = None) -> None:

    path = "data/y2023/d5.txt"

    if test:
        path = "tests/" + path

    ans_part1 = "SKIPPED"
    ans_part2 = "SKIPPED"

    data = read_input(
        path=path,
        parse_func=parse_line,
        post_parse_func=group_lines,
    )

    seeds = data[0][0]

    garden_maps = [
        GardenMap(
            from_cat=group[0][0],
            to_cat=group[0][1],
            map_lines=[
                GardenMapLine(
                    from_n=from_n,
                    to_n=to_n,
                    range_n=range_n
                )
                for to_n, from_n, range_n in group[1:]
            ]
        )
        for group in data[1:]
    ]

    ans_part1 = min([
        get_location_value(garden_maps=garden_maps, n=seed)
        for seed in seeds
    ])

    print(f"AOC 2023 - Day 5")
    print(f"    Part 1: {ans_part1}")
    # print(f"    Part 2: {ans_part2}")

    # for gm in garden_maps:
        # lowest_shift = sorted(gm.map_lines, key=lambda x: x.shift_value())[0].shift_value()
        # print(lowest_shift)

    for start_n, range_n in [(seeds[i], seeds[i+1]) for i in np.arange(0, len(seeds), 2)]:
        print(f"range: {start_n}-{start_n+range_n}")
        tmp = min([
            get_location_value(garden_maps=garden_maps, n=seed)
            for seed in np.arange(start_n, start_n+range_n)
        ])
        print(tmp)
