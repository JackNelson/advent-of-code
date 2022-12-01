from typing import Any, Callable, List

def read_input(
    day: int,
    parse_func: Callable[[str], Any] = None,
) -> List[Any]:

    with open(f'data/day{day}.txt') as f:
        lines = f.read().splitlines()

    if parse_func:
        return [parse_func(line) for line in lines]

    else:
        return lines