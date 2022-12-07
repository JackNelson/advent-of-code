from typing import Dict, List, Literal
import re
import os

from utils.io import read_input

def process_line(line: List[str]) -> None:

    global filesystem
    global cursor

    if line[0] == '$': # is a command
        
        if line[1] == 'cd': # is cd

            if line[2] != '..': # move down tree
                cursor.append(line[2])

            elif line[2] == '..': # move up tree
                cursor.pop(-1)

        elif line[1] == 'ls': # is ls
        
            path = os.path.join(*cursor)

            if path not in filesystem.keys():
                filesystem[path] = 0

    else:

        if re.match(r"\d+", line[0]): # is a file

            for i in range(len(cursor)):
                path = os.path.join(*cursor[:i+1])
                filesystem[path] += int(line[0])

def get_dirs(
    size_threshold: int,
    direction: Literal['above','below']
) -> Dict[str, int]:

    global filesystem

    if direction == 'above':
        return {k:v for k,v in filesystem.items() if v >= size_threshold}

    elif direction == 'below':
        return {k:v for k,v in filesystem.items() if v <= size_threshold}

def get_dir_to_delete(available_space: int, needed_space: int) -> Dict[str, int]:

    tmp = get_dirs(
        size_threshold=needed_space-available_space,
        direction='above',
    )

    return {k:v for k,v in tmp.items() if v == min(tmp.values())}

data = read_input(day=7, parse_func=lambda x: x.split(' '))

# build filesystem data
filesystem = {}
cursor = []

for line in data:
    process_line(line=line)

# answers
size = int(1e5)
undersize_dirs = get_dirs(size_threshold=size, direction='below')
print(f"Sum of dirs under {str(size)}: {sum(undersize_dirs.values())}")

available_space = 7e7
needed_space = 3e7
dir_to_delete = get_dir_to_delete(
    available_space=available_space - filesystem['/'],
    needed_space=needed_space,
)
print(f'Size of dir to delete: {list(dir_to_delete.values())[0]}')