from __future__ import annotations
from typing import Dict, List, Tuple
import re
from dataclasses import dataclass
import numpy as np

from advent_of_code.io import read_input

@dataclass
class CubeSet:
    qty: int
    color: str

@dataclass
class Handful:
    cube_sets: List[CubeSet]

@dataclass
class Game:
    game_id: int
    handfuls: List[Handful]

    def flatten(self) -> List[CubeSet]:
        return [
            cube_set
            for handful in self.handfuls
            for cube_set in handful.cube_sets
        ]

    def max_cube_sets(self) -> Dict[str, CubeSet]:

        d = {}

        for cube_set in self.flatten():

            if cube_set.color not in d.keys():
                d[cube_set.color] = cube_set

            elif d[cube_set.color].qty < cube_set.qty:
                d[cube_set.color] = cube_set

        return d

    def power(self) -> int:

        return np.prod(
            [cube_set.qty for color, cube_set in self.max_cube_sets().items()]
        )

    def possible_game(self, other: Game) -> bool:

        for color, cube_set in self.max_cube_sets().items():

            if color not in other.max_cube_sets().keys():
                print(color)
                print(other.max_cube_sets())
                print("color")
                return False

            elif cube_set.qty > other.max_cube_sets()[color].qty:
                return False

        return True

def parse_game(string: str) -> List[List[Tuple[str, str]]]:

    game_id = re.findall(r"\d+", string.split(":")[0])[0]
    game = string.split(":")[1].split(";")

    return Game(
        game_id=int(game_id),
        handfuls=[
            Handful(
                cube_sets=[
                    CubeSet(qty=int(qty), color=color)
                    for qty, color in
                    zip(
                        re.findall(r"\d+", handful),
                        re.findall(r"[a-z]+", handful),
                    )
                ]
            )
            for handful in game
        ]
    )

def get_possible_ids_sum(games: List[Game], limit: Game) -> int:

    return sum([game.game_id for game in games if game.possible_game(other=limit)])

def get_power_sum(games: List[Game]) -> int:

    return sum([game.power() for game in games])


def main(test: bool, part: str = None) -> None:

    path = "data/y2023/d2.txt"
    limit_path = "data/y2023/d2_limit.txt"

    if test:
        path = "tests/" + path

    ans_part1 = "SKIPPED"
    ans_part2 = "SKIPPED"

    games = read_input(path=path, parse_func=parse_game)
    limit = read_input(path=limit_path, parse_func=parse_game)[0]

    if part != "2":
        ans_part1 = get_possible_ids_sum(games=games, limit=limit)

    if part != "1":
        ans_part2 = get_power_sum(games=games)

    print(f"AOC 2023 - Day 2")
    print(f"    Part 1: {ans_part1}")
    print(f"    Part 2: {ans_part2}")
