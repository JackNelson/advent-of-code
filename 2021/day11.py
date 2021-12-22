import numpy as np
import re

class OctopiGrid:

    def __init__(self, grid):
        self.grid = grid
        self.flashes = 0

    def increment_grid(self):
        self.grid = np.array([[j+1 for j in i] for i in self.grid])

    def reset_values(self):

        indexes = zip(*np.where(self.grid > 9))

        for idx in indexes:
            for i in np.arange(-1,2):
                for j in np.arange(-1,2):
                    array = self.increment_value(idx[0]+i, idx[1]+j)

            self.grid[idx[0], idx[1]] = 0
            self.flashes += 1

    def increment_value(self, i, j):

        if (
            (i < 10) and (i > -1)
            and 
            (j < 10) and (j > -1)
            and
            (self.grid[i,j] != 0) and (self.grid[i,j] < 10)
        ):
            self.grid[i,j] += 1

    def increment_steps(self, steps, print_grid=False):

        for i in range(steps):
            self.increment_grid()

            while len(np.where(self.grid > 9)[0]) > 0: 
                self.reset_values()

        if print_grid:
            print(i)
            print(self.grid)

    def find_synchronization(self):

        step_count = 0
        
        while len(np.where(self.grid == 0)[0]) != 100:
            self.increment_grid()

            while len(np.where(self.grid > 9)[0]) > 0: 
                self.reset_values()

            step_count += 1

        return step_count


with open('2021/data/day11.txt') as f:
    data = np.array(
        [
            [int(x) for x in re.findall(r'\d', line)]
            for line in f.readlines()
        ]
    )

# step 1
steps = 100
octopi_grid = OctopiGrid(data)
octopi_grid.increment_steps(steps)
print(f"Flashes after {steps} steps: {octopi_grid.flashes}")

# step 2
octopi_grid = OctopiGrid(data)
step_count = octopi_grid.find_synchronization()
print(f"Flashes sunchronize at step: {step_count}")