import numpy as np
from pprint import pprint
import re

def show_paper(dots):

    paper = np.full(
        (
            np.max(dots[:,1]) + 1, 
            np.max(dots[:,0]) + 1
        ),
        '.'
    )

    for dot in dots:
        paper[dot[1], dot[0]] = "#"

    pprint(['.'.join(line) for line in paper])

with open('2021/data/day13.txt') as f:
    lines = f.readlines()
    
dots = np.array([
    (int(x[0][0]), int(x[0][1]))
    for x in [re.findall(r'(\d+)\,(\d+)', line) for line in lines] 
    if x
])

folds = [
    (x[0][0], int(x[0][1]))
    for x in [re.findall(r'([xy])\=(\d+)', line) for line in lines]
    if x
]

d = {
    'x':0,
    'y':1
}

# part one
# for fold in [folds[0]]:

# part two
for fold in folds:

    axis = fold[0]
    crease = fold[1]
    tmp = []

    for dot in dots:

        if dot[d[axis]] != crease:

            stay_val = dot[abs(d[axis] - 1)]
            fold_val = dot[d[axis]]

            new_dot = [None, None]

            if dot[d[axis]] > crease:
                new_dot[abs(d[axis] - 1)] = stay_val
                new_dot[d[axis]] = fold_val - (2 * (fold_val - crease))

            else:
                new_dot[abs(d[axis] - 1)] = stay_val
                new_dot[d[axis]] = fold_val

            tmp.append(tuple(new_dot))

    
    dots = np.array(list(set(tmp)))

print(f"Dots showing after folds: {len(dots)}")
show_paper(dots)