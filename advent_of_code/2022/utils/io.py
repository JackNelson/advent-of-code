from typing import Any, Callable, List

def read_input(
    day: int,
    parse_func: Callable[[str], Any] = None,
    skip_lines: int = 0,
    last_line: int = None,
) -> List[Any]:
    
    with open(f'data/day{day}.txt') as f:
        
        lines = f.read().splitlines()
        
        if last_line == None:
            lines = lines[skip_lines:]
        else:
            lines = lines[skip_lines:last_line]

    if parse_func:
        return [parse_func(line) for line in lines]
    else:
        return lines