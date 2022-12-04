from typing import List
from string import ascii_lowercase, ascii_uppercase
from utils.io import read_input
from utils.compare import get_intersection

def get_bag_priority(contents: str) -> int:
    
    global items

    c1, c2 = (
        contents[:len(contents)//2],
        contents[len(contents)//2:],
    )

    return items.index(list(set(c1) & set(c2))[0]) + 1

def get_badge_priority(bags: List[str]) -> int:

    global items

    return items.index(get_intersection(bags)[0]) + 1

items = list(ascii_lowercase) + list(ascii_uppercase)
data = read_input(day=3)

priorities = [get_bag_priority(contents=contents) for contents in data]
print(f"Sum of Bag Priorities: {sum(priorities)}")

bag_groups = [data[i*3:(i+1)*3] for i in range(len(data) // 3)]
priorities = [get_badge_priority(bags=bags) for bags in bag_groups]
print(f"Sum of Badge Priorities: {sum(priorities)}")