from typing import List, Literal, Tuple
from math import sqrt
import operator
import numpy as np

from utils.io import read_input

class Knot(object):

    def __init__(self):
        self.x = 0
        self.y = 0
        self.path = np.array(self.loc)
        self.directions = []

    @property
    def loc(self) -> Tuple[int, int]:
        return (self.x, self.y)
    
    def log_path(self) -> None:
        self.path = np.vstack((self.path, self.loc))


class Rope(object):
    
    def __init__(self, knot_count: int) -> None:

        self.knots = [Knot() for _ in range(knot_count)]

    def get_grid(self) -> np.array:

        rows = (
            max(knot.path[:,0].max() for knot in self.knots) -
            min(knot.path[:,0].min() for knot in self.knots) + 1
        )

        cols = (
            max(knot.path[:,1].max() for knot in self.knots) -
            min(knot.path[:,1].min() for knot in self.knots) + 1
        )

        return np.full((rows, cols), fill_value='.')

    def get_grid_datum(self) -> Tuple[int, int]:
        return (
            0 - min(knot.path[:,0].min() for knot in self.knots),
            0 - min(knot.path[:,1].min() for knot in self.knots)
        )

    def get_new_loc(
        self,
        loc1: Tuple[int, int],
        loc2: Tuple[int, int],
    ) -> Tuple[int, int]:
            return tuple(map(operator.add, loc1, loc2))
    
    def get_x_distance(self, idx: int) -> int:
        return self.knots[idx-1].x - self.knots[idx].x

    def get_y_distance(self, idx: int) -> int:
        return self.knots[idx-1].y - self.knots[idx].y
    
    def get_distance(self, idx: int) -> float:
        return sqrt(
            self.get_x_distance(idx=idx) ** 2 
            + self.get_y_distance(idx=idx) ** 2
        )

    def move_knot(
        self,
        direction: Literal["U","D","L","R"],
        idx: int
    ) -> None:

        if direction == "U":
            self.knots[idx].x -= 1

        elif direction == "D":
            self.knots[idx].x += 1

        elif direction == "L":
            self.knots[idx].y -= 1

        elif direction == "R":
            self.knots[idx].y += 1
    
    def move_first_knot(
        self,
        direction: Literal["U","D","L","R"],
        value: int
    ) -> None:
        
        for _ in range(value):
            self.move_knot(direction=direction, idx=0)
            self.knots[0].log_path()

            for idx in range(len(self.knots[1:])):
                self.move_next_knot(idx=idx+1)

    def move_next_knot(self, idx: int) -> None:

        x_distance = self.get_x_distance(idx=idx)
        y_distance = self.get_y_distance(idx=idx)
        distance = self.get_distance(idx=idx)

        if distance == 2:
            self.knots[idx].x += (x_distance // 2)
            self.knots[idx].y += (y_distance // 2)

        elif distance > 2:
            self.knots[idx].x += (x_distance // abs(x_distance))
            self.knots[idx].y += (y_distance // abs(y_distance))

        self.knots[idx].log_path()
    
    def print_plot(self, grid: np.array) -> None:

        for row in grid.tolist():
            print(''.join(row))
    
    def plot_rope(self, epoch: int) -> None:

        grid = self.get_grid()
        datum = self.get_grid_datum()
        
        for i, knot in enumerate(self.knots[::-1][:-1]):
            grid[self.get_new_loc(datum, knot.path[epoch])] = (
                len(self.knots) - (i+1)
            )

        grid[self.get_new_loc(datum, self.knots[0].path[epoch])] = 'H'

        self.print_plot(grid=grid)

    def get_tail_plot(self, knot_num: int) -> np.array:

        grid = self.get_grid()
        datum = self.get_grid_datum()

        for loc in self.knots[knot_num].path:
            grid[self.get_new_loc(datum, loc)] = '#'

        return grid

    def get_visit_count(self, knot_num: int) -> int:

        grid = self.get_tail_plot(knot_num=knot_num)
        
        return len([i for i in grid.flatten() if i == '#'])

def get_rope_results(data: List[List[str]], knot_count: int) -> Rope:

    rope = Rope(knot_count=knot_count)

    for direction, value in data:
        rope.move_first_knot(direction=direction, value=int(value))

    return rope

data = read_input(day=9, parse_func=lambda x: x.split(' '))

print("Unique tail position counts...")
for i, knot_count in enumerate([2,10]):

    rope = get_rope_results(data=data, knot_count=knot_count)
    tail_visit_count = rope.get_visit_count(knot_num=-1)
    print(f"Part {i+1} - Rope with {knot_count} Knots: {tail_visit_count}")