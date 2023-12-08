import numpy as np
import pandas as pd
from pprint import pprint
import re

with open('2021/data/test.txt') as f:
    grid = np.array([re.findall('\d',line) for line in f.readlines()])

pprint(grid)

class PathFinder:

    def __init__(self, grid):

        self.grid = grid
        self.loc = (0,0)
        self.prev = None

    def get_risk_level(self, loc):
        return self.grid[loc[1], loc[0]]

    def get_distance(self, loc):
        return (np.array(self.grid.shape) - np.array(loc)).sum()

    def calculate(self, loc):
        return (loc, self.get_risk_level(loc), self.get_distance(loc))

    def get_options(self, loc):

        d = {
            'left': (loc[1]-1, loc[0]),
            'right': (loc[1]+1, loc[0]),
            'up': (loc[1], loc[0]-1),
            'down': (loc[1], loc[0]+1),
        }

        tmp = []

        for k,v in d.items():
            if (self.prev != k) and (v[1] >= 0) and (v[0] >= 0):
                try:
                    self.grid[loc[1], loc[0]]
                    tmp.append(v)

                except:
                    pass

        return tmp

path_finder = PathFinder(grid)
print(path_finder.calculate((1,2)))
print(path_finder.get_options((0,0)))


