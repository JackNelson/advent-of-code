from utils.io import read_input
from typing import List
import numpy as np
from math import prod

data = read_input(day=8, parse_func=lambda x: [int(i) for i in x])

trees = np.array(data)
rows, cols = trees.shape

def is_edge(i:int, j:int) -> bool:

    global rows, cols

    return any(
        [
            i == 0, # top edge
            j == 0, # left edge
            i == rows - 1, # bottom edge
            j == cols - 1, # right edge
        ]
    )

def has_shorter(i:int, j:int) -> bool:

    global trees

    return any(
        [
            max(trees[:i,j]) < trees[i,j], # above
            max(trees[i,:j]) < trees[i,j], # left
            max(trees[i+1:,j]) < trees[i,j], # bottom
            max(trees[i,j+1:]) < trees[i,j], # right
        ]
    )

def is_visible(i:int, j:int) -> bool:

    if is_edge(i=i, j=j):
        return True

    else:
        return has_shorter(i=i, j=j)

def get_visible_trees(tree:int, view_trees:List[int]) -> int:

    l = [view_tree >= tree for view_tree in view_trees]

    if True in l:
        return len(l[:l.index(True) + 1])
    else:
        return len(l)

def get_scenic_score(i:int, j:int) -> int:

    global trees

    return prod(
        [
            get_visible_trees(
                tree=trees[i,j],
                view_trees=trees[:i,j][::-1]
            ), # above
            get_visible_trees(
                tree=trees[i,j],
                view_trees=trees[i,:j][::-1]
            ), # left
            get_visible_trees(
                tree=trees[i,j],
                view_trees=trees[i+1:,j]
            ), # bottom
            get_visible_trees(
                tree=trees[i,j],
                view_trees=trees[i,j+1:]
            ), # right
        ]
    )

visible_grid = [
    [is_visible(i=i, j=j) for j in range(cols)]
    for i in range(rows) 
]
print(f'Visible Trees: {sum([sum(i) for i in visible_grid])}')

scenic_scores = [
    get_scenic_score(i=i, j=j)
    for j in range(cols)
    for i in range(rows) 
]
print(f'Highest Scenic Score: {max(scenic_scores)}')