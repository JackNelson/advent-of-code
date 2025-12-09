from typing import List, Tuple
from dataclasses import dataclass
import re
import numpy as np
import itertools

from advent_of_code.io import read_input
from advent_of_code.xy import Point2D


@dataclass
class ConditionRecord:
    partial_record: str
    missing_idx: List[int]
    damaged_values: List[int]


    def is_possible(self, record: str):

        damaged_values = [
            m.end() - m.start() for m in re.finditer(r"\#+", record)
        ]

        return self.damaged_values == damaged_values


    def potential_records(self) -> List[str]:

        records = []

        fill_values = [
            l for l in itertools.product(
                *[["#", "."] for _ in range(len(self.missing_idx))]
            )
        ]

        for l in fill_values:

            record = self.partial_record

            for idx, v in zip(self.missing_idx, l):
                record = (
                    record[:idx] + v + record[idx+1:]
                )

            records.append(record)

        return records


    def possible_records(self) -> List[str]:

        return [
            record for
            record in self.potential_records()
            if self.is_possible(record=record)
        ]


def main(test: bool, part: int = None) -> None:

    path = "data/y2023/d12.txt"

    if test:
        path = "tests/" + path

    ans_part1 = "SKIPPED"
    ans_part2 = "SKIPPED"

    condition_records = read_input(
        path=path,
        parse_func=lambda line: (
            line.split(" ")[0],
            [m.start() for m in re.finditer(r"\?", line.split(" ")[0])],
            [int(v) for v in re.findall(r"\d+", line.split(" ")[1])],
        ),
        post_parse_func=lambda data: [
            ConditionRecord(
                partial_record=partial_record,
                missing_idx=missing_idx,
                damaged_values=damaged_values
            )
            for (partial_record, missing_idx, damaged_values)
            in data
        ],
    )

    if part != "2":

        ans_part1 = sum(
            [
                len(condition_record.possible_records())
                for condition_record in condition_records
            ]
        )

    # # if part != "1":

    print(f"AOC 2023 - Day 12")
    print(f"    Part 1: {ans_part1}")
    print(f"    Part 2: {ans_part2}")