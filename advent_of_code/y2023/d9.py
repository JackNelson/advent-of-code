from typing import List
import re

from advent_of_code.io import read_input


def extrapolate_out(l: List[int]) -> int:

    tmp = [l]

    for _ in range(len(l)-1):

        l = [l[i+1] - v for i, v in enumerate(l[:-1])]
        tmp.append(l)

        if all([v==0 for v in l]):
            return sum([vals[-1] for vals in tmp])

def extrapolate_in(l: List[int]) -> int:

    tmp = [l]

    for _ in range(len(l)-1):

        l = [l[i+1] - v for i, v in enumerate(l[:-1])]
        tmp.append(l)

        if all([v==0 for v in l]):

            val = 0

            for vals in tmp[:-1][::-1]:
                val = vals[0] - val

            return val


def main(test: bool, part: int = None) -> None:

    path = "data/y2023/d9.txt"

    if test:
        path = "tests/" + path

    data = read_input(
        path=path,
        parse_func=lambda line: re.findall(r"\-?\d+", line),
        post_parse_func=lambda data: [[int(v) for v in line] for line in data]
    )

    ans_part1 = "SKIPPED"
    ans_part2 = "SKIPPED"

    if part != "2":
        ans_part1 = sum([extrapolate_out(l=l) for l in data])

    if part != "1":
        ans_part2 = sum([extrapolate_in(l=l) for l in data])

    print(f"AOC 2023 - Day 9")
    print(f"    Part 1: {ans_part1}")
    print(f"    Part 2: {ans_part2}")

