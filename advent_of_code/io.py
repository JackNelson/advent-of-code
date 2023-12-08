from typing import Any, Callable, List

def read_input(
    path: str,
    parse_func: Callable[[str], Any] = None,
    post_parse_func: Callable[[Any], Any] = None,
    skip_lines: int = 0,
    last_line: int = None,
) -> List[Any]:

    with open(path) as f:

        lines = f.read().splitlines()

        if last_line == None:
            lines = lines[skip_lines:]
        else:
            lines = lines[skip_lines:last_line]

    if parse_func:
        data = [parse_func(line) for line in lines]
    else:
        data = lines

    if post_parse_func:
        return post_parse_func(data)
    else:
        return data
