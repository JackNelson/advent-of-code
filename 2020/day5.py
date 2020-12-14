import os
import numpy as np

with open("data/day5.txt", "r") as f:
    data = [x.strip() for x in f.readlines()]


def __find_middle(string, length, lower_char, upper_char):

    l = np.arange(length)

    for i in string:
        if i == lower_char:
            l = [x for x in l if x < sum(l) / len(l)]
        elif i == upper_char:
            l = [x for x in l if x >= sum(l) / len(l)]
        else:
            raise NameError()

    return l[0]


def find_row(string):
    return __find_middle(string, 128, "F", "B")


def find_col(string):
    return __find_middle(string, 8, "L", "R")


def find_seat_id(row, col):
    return row * 8 + col


rows = [find_row(x[:7]) for x in data]
cols = [find_col(x[7:]) for x in data]
seats = [find_seat_id(x[0], x[1]) for x in zip(rows, cols)]

# use for part a
print(f"Highest seat ID: {max(seats)}")

available_seats = np.arange(127 * 8 + 8)
available_seats = [x for x in available_seats if x not in seats]
diff = np.diff(available_seats)

my_seat = [x[0] for x in list(zip(available_seats, diff)) if x[1] > 1][-1]

# use for part b
print(f"My seat: {my_seat}")
