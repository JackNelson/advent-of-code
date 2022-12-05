from typing import List, Literal
import re
import numpy as np
from utils.io import read_input

def parse_stacks(l: str) -> List[str]:
    return [l[1 + (4 * i)] for i in range(9)]

def parse_line(l: str) -> List[int]:
    return [
        int(group) 
        for group in re.match(r"move (\d+) from (\d+) to (\d+)", l).groups()
    ]

def get_starting_stacks() -> List[str]:

    stack_start = read_input(day=5, parse_func=parse_stacks, last_line=8)

    return [
        [crate for crate in stack if crate != ' ']
        for stack in np.array(stack_start).T.tolist()
    ]

def move_crates(
    qty: int,
    from_stack: int,
    to_stack: int,
    mover: Literal['9000','9001']
) -> None:

    global stacks

    if mover == '9000':
        for crate in range(qty):
            top_crate = stacks[from_stack - 1].pop(0)
            stacks[to_stack - 1].insert(0, top_crate)

    elif mover == '9001':

        substack = stacks[from_stack - 1][:qty]
        del stacks[from_stack - 1][:qty]
        stacks[to_stack - 1] = substack + stacks[to_stack - 1]

data = read_input(day=5, parse_func=parse_line, skip_lines=10)

stacks = get_starting_stacks()
for qty, from_stack, to_stack in data:
    move_crates(qty=qty, from_stack=from_stack, to_stack=to_stack, mover='9000')
print(f"Top Crates using the CrateMover9000: {''.join(stack[0] for stack in stacks)}")

stacks = get_starting_stacks()
for qty, from_stack, to_stack in data:
    move_crates(qty=qty, from_stack=from_stack, to_stack=to_stack, mover='9001')
print(f"Top Crates using the CrateMover9001: {''.join(stack[0] for stack in stacks)}")