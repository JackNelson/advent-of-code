from __future__ import annotations
from typing import Dict, List, Literal
from dataclasses import dataclass
import re
import operator

from advent_of_code.io import read_input


@dataclass
class Part:
    x: int
    m: int
    a: int
    s: int

    @property
    def total_rating(self) -> int:
        return self.x + self.m + self.a + self.s


@dataclass
class Condition:
    attr: str
    symbol: Literal["<", ">"]
    val: int
    out: str

    def evaluate(self, part: Part) -> str:

        d = {
            ">": operator.gt,
            "<": operator.lt,
        }

        if d[self.symbol](getattr(part, self.attr), int(self.val)):
            return self.out

        return None


@dataclass
class Rule:
    name: str
    conditions: List[Condition]
    else_val: str

    def evaluate(self, part) -> str:

        for condition in self.conditions:
            val = condition.evaluate(part=part)

            if val:
                return val

        return self.else_val


def parse_part(line: str) -> Part:

    if re.findall(r"^\{", line):

        params = {
            k: int(v) for k, v in zip(
                re.findall(r"[xmas]", line),
                re.findall(r"\d+", line)
            )
        }

        return Part(**params)

    else:
        return None


def parse_rule(line: str) -> Rule:

    if re.findall(r"^[a-z]", line):

        name, tmp = re.findall(r"^([a-z]+)\{(.*)\}", line)[0]

        tmp = tmp.split(",")

        else_val = tmp.pop()

        conditions = [
            Condition(*re.findall(r"([xmas])([\<\>])(\d+)\:([a-zAR]+)", s)[0])
            for s in tmp
        ]

        return Rule(name=name, conditions=conditions, else_val=else_val)

    else:
        return None


def evaluate_part(
    part: Part,
    rules_dict: Dict[str, Rule],
) -> Literal["A", "R"]:

    val = "in"

    while val not in ["A", "R"]:

        rule = rules_dict[val]
        val = rule.evaluate(part=part)

    return val


def main(test: bool, part: int = None) -> None:

    path = "data/y2023/d19.txt"

    if test:
        path = "tests/" + path

    ans_part1 = "SKIPPED"
    ans_part2 = "SKIPPED"

    rules_dict = read_input(
        path=path,
        parse_func=parse_rule,
        post_parse_func=lambda data: {
            rule.name: rule for rule in data if rule
        },
    )

    parts = read_input(
        path=path,
        parse_func=parse_part,
        post_parse_func=lambda data: [line for line in data if line],
    )

    if part != "2":

        ans_part1 = sum(
            [
                part.total_rating for part in parts
                if evaluate_part(part=part, rules_dict=rules_dict) == "A"
            ]
        )

    # if part != "1":

    print(f"AOC 2023 - Day 19")
    print(f"    Part 1: {ans_part1}")
    print(f"    Part 2: {ans_part2}")
