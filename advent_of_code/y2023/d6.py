import re
from dataclasses import dataclass
import math
import numpy as np

from advent_of_code.io import read_input


@dataclass
class BoatRace:
    time: int
    distance: int

    def count_above_distance(self) -> int:

        max_intercept = math.floor(
            (self.time + math.sqrt(self.time**2 - 4*self.distance)) / 2 - 0.0001
        )

        min_intercept = math.ceil(
            (self.time - math.sqrt(self.time**2 - 4*self.distance)) / 2 + 0.0001
        )

        return max_intercept - min_intercept + 1


def main(test: bool, part: str = None) -> None:

    path = "data/y2023/d6.txt"

    if test:
        path = "tests/" + path

    ans_part1 = "SKIPPED"
    ans_part2 = "SKIPPED"

    boat_races = read_input(
        path=path,
        parse_func=lambda line: re.findall(r"\d+", line),
        post_parse_func=lambda data: [
            BoatRace(time=int(time), distance=int(distance),)
            for time, distance in list(zip(data[0], data[1]))
        ],
    )

    long_boat_race = read_input(
        path=path,
        parse_func=lambda line: re.findall(r"\d+", line),
        post_parse_func=lambda data: (
            BoatRace(
                time=int("".join(data[0])),
                distance=int("".join(data[1])),
            )
        )
    )

    if part != "2":
        ans_part1 = np.prod(
            [boat_race.count_above_distance() for boat_race in boat_races]
        )

    if part != "1":
        ans_part2 = long_boat_race.count_above_distance()

    print(f"AOC 2023 - Day 6")
    print(f"    Part 1: {ans_part1}")
    print(f"    Part 2: {ans_part2}")
