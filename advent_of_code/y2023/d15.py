from __future__ import annotations
from typing import Dict, List
import re

from advent_of_code.io import read_input


def hash_algorithm(step: str, v: int = 0) -> int:

    v = ((ord(step[0]) + v) * 17) % 256

    if len(step) > 1:
        v = hash_algorithm(step=step[1:], v=v)

    return v


def place_lenses(steps: List[str]) -> Dict[int, Dict[str, int]]:

    boxes = {}

    for step in steps:

        label = re.findall(r"[a-zA-Z]+", step)[0]
        val = hash_algorithm(step=label)
        operation = re.findall(r"[\-\=]", step)[0]

        if "=" in step:
                focal_length = int(step[-1])

        if operation == "=":

            if val not in boxes.keys():
                boxes[val] = {}

            boxes[val][label] = focal_length

        elif operation == "-":
            if val in boxes.keys() and label in boxes[val].keys():
                del boxes[val][label]

    return {box: labels for box, labels in boxes.items() if labels}


def get_focusing_power(box: int, labels: Dict[str, int]) -> int:

    return sum([(box+1) * (i+1) * v for i, v in enumerate(labels.values())])


def main(test: bool, part: int = None) -> None:

    path = "data/y2023/d15.txt"

    if test:
        path = "tests/" + path

    ans_part1 = "SKIPPED"
    ans_part2 = "SKIPPED"

    steps = read_input(
        path=path,
        parse_func=lambda line: line.split(","),
        post_parse_func=lambda data: data[0],
    )

    if part != "2":
        ans_part1 = sum([hash_algorithm(step=step) for step in steps])

    if part != "1":

        boxes = place_lenses(steps=steps)

        ans_part2 = sum([
            get_focusing_power(box=box, labels=labels)
            for box, labels in boxes.items()
        ])

    print(f"AOC 2023 - Day 15")
    print(f"    Part 1: {ans_part1}")
    print(f"    Part 2: {ans_part2}")
