from typing import List
from utils.io import read_input
from utils.compare import get_intersection

def parse_line(line: str) -> List[List[str]]:

    def range2list(start: str, end: str) -> List[int]:
        return list(range(int(start), int(end)+1))

    return [
        range2list(*ids.split('-'))
        for ids in line.split(',')
    ]

def is_complete_overlap(l: List[List[int]]) -> bool:

    common_search_ids = get_intersection(l=l)

    return any(
        [
            len(common_search_ids) == len(search_ids)
            for search_ids in l
        ]
    )

def any_overlap(l: List[List[int]]) -> bool:
    return bool(get_intersection(l=l))

data = read_input(day=4, parse_func=parse_line)

complete_overlap_count = sum([is_complete_overlap(l) for l in data])
print(f"Complete Overlap Count: {complete_overlap_count}")

partial_overlap_count = sum([any_overlap(l=l) for l in data])
print(f"Partial Overlap Count: {partial_overlap_count}")