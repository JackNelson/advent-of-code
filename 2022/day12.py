from typing import List, Tuple
import numpy as np

from utils.io import read_input

data = read_input(day=12, parse_func=lambda x: x.split(''))

heightmap = np.array(data)

class Route(object):
    def __init__(self, start: List[int], end: List[int]):

        self.heightmap = heightmap
        
        self.start = self.get_start()
        self.end = self.get_end()

        self.heightmap[self.start] = 'a'
        self.heightmap[self.end] = 'z'


        self.location = start
        self.route = []
        decision_points = []

    def get_start(self) -> Tuple[int, int]:
        return list(zip(*np.where(self.heightmap == "S")))

    def get_end(self) -> Tuple[int, int]:
        return list(zip(*np.where(self.heightmap == "E")))