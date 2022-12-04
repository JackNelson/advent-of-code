from typing import Any, List

def get_intersection(l: List[Any]) -> List[Any]:
    return list(set.intersection(*map(set, l)))