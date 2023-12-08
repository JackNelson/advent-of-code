import re
import math

from advent_of_code.io import read_input


def main(test: bool, part: int = None) -> None:

    path = "data/y2023/"

    if test:
        if part == "1":
            path = "tests/" + path + "d8a.txt"
        elif part == "2":
            path = "tests/" + path + "d8b.txt"
    else:
        path = path + "d8.txt"

    instructions = read_input(path=path, last_line=1,)[0]
    nodes_dict = read_input(
        path=path,
        parse_func=lambda line: re.findall(r"[A-Z0-9]{3}", line),
        post_parse_func=lambda data: {n: (l, r) for n, l, r in data},
        skip_lines=2,
    )

    direction_dict = {"L": 0, "R": 1}

    ans_part1 = "SKIPPED"
    ans_part2 = "SKIPPED"

    # part 1
    if part != "2":

        i = 0
        current_node = "AAA"

        while current_node != "ZZZ":

            direction = instructions[i%len(instructions)]
            current_node = nodes_dict[current_node][direction_dict[direction]]

            i += 1

        ans_part1 = i

    # part 2
    if part != "1":

        current_nodes = [node for node in nodes_dict.keys() if node.endswith("A")]
        l = []

        for current_node in current_nodes:

            tmp = [[] for _ in instructions]

            for i, direction in enumerate(instructions):

                current_node = nodes_dict[current_node][direction_dict[direction]]
                tmp[i].append(current_node)

            i = len(instructions)

            while True:

                direction = instructions[i%len(instructions)]
                current_node = nodes_dict[current_node][direction_dict[direction]]

                if current_node in tmp[i%len(instructions)]:

                    tmp[i%len(instructions)].append(current_node)
                    break

                else:
                    tmp[i%len(instructions)].append(current_node)

                i += 1

            l.append(
                [
                    j for j in range(i)
                    if tmp[j%len(instructions)][j//len(instructions)].endswith("Z")]
            )

        ans_part2 = math.lcm(*[y+1 for x in l for y in x])

    print(f"AOC 2023 - Day 8")
    print(f"    Part 1: {ans_part1}")
    print(f"    Part 2: {ans_part2}")
