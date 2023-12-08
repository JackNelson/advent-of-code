from __future__ import annotations
from typing import Literal, List
import re

from advent_of_code.io import read_input


def get_calibration_value(string: str, word2number: bool = False) -> int:

    d = {
        "one": "o1e",
        "two": "t2o",
        "three": "t3e",
        "four": "f4r",
        "five": "f5e",
        "six": "s6x",
        "seven": "s7n",
        "eight": "e8t",
        "nine": "n9e",
    }

    if word2number:

        for k,v in d.items():
            string = string.replace(k, str(v))

    tmp = re.findall("\d", string)

    return int(tmp[0] + tmp[-1])


def get_calibration_values_sum(strings: List[str], part: Literal["1", "2"]) -> int:

    if part == "1":
        word2number = False

    elif part == "2":
        word2number = True

    else:
        raise ValueError("incorrect part input")

    return sum([get_calibration_value(string=string, word2number=word2number) for string in strings])


def main(test: bool, part: str = None) -> None:

    path = "data/y2023/"

    if test:
        if part == "1":
            path = "tests/" + path + "d1a.txt"
        elif part == "2":
            path = "tests/" + path + "d1b.txt"
    else:
        path = path + "d1.txt"

    ans_part1 = "SKIPPED"
    ans_part2 = "SKIPPED"

    strings = read_input(path=path)

    if part != "2":
        ans_part1 = get_calibration_values_sum(strings=strings, part="1")

    if part != "1":
        ans_part2 = get_calibration_values_sum(strings=strings, part="2")

    print(f"AOC 2023 - Day 1")
    print(f"    Part 1: {ans_part1}")
    print(f"    Part 2: {ans_part2}")
