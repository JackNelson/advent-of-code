from __future__ import annotations
from typing import List
from dataclasses import dataclass
import re

from advent_of_code.io import read_input


@dataclass
class ScratchCard:
    numbers: List[str]
    winning_numbers: List[str]

    def matches(self):
        return [
            n for n in self.numbers
            if n in self.winning_numbers
        ]

    def points(self):
        if self.matches():
            return 2 ** (len(self.matches()) - 1)
        else:
            return 0


def parse_line(line: str) -> ScratchCard:

    tmp = line.split(":")[1].split("|")

    return ScratchCard(
        numbers=re.findall(r"\d+", tmp[1]),
        winning_numbers=re.findall(r"\d+", tmp[0]),
    )


def get_scratchcard_counts(scratch_cards: List[ScratchCard]) -> List[int]:

    counts = [0 for _ in scratch_cards]

    for i, sc in enumerate(scratch_cards):
        counts[i] += 1

        for j in range(len(sc.matches())):
            try:
                counts[i+j+1] += counts[i]

            except:
                pass

    return counts


def main(test: bool, part: str = None) -> None:

    path = "data/y2023/d4.txt"

    if test:
        path = "tests/" + path

    ans_part1 = "SKIPPED"
    ans_part2 = "SKIPPED"

    scratch_cards = read_input(
        path=path,
        parse_func=parse_line,
    )

    if part != "2":
        ans_part1 = sum([sc.points() for sc in scratch_cards])

    if part !="1":
        ans_part2 = sum(get_scratchcard_counts(scratch_cards=scratch_cards))

    print(f"AOC 2023 - Day 4")
    print(f"    Part 1: {ans_part1}")
    print(f"    Part 2: {ans_part2}")
