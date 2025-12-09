import copy
import pprint


def check_aisle(seat):
    """checks if seat is an aisle"""

    if seat == ".":
        return True
    else:
        return False


def check_occupied(seat):
    """checks if seat is occupied"""

    if seat == "#":
        return True
    else:
        return False


def check_empty(seat):
    """checks if seat is empty"""

    if seat == "L":
        return True
    else:
        return False


def char_split(seat_chart):
    return [[y for y in x] for x in seat_chart]


def char_join(seat_chart):
    return ["".join(x) for x in seat_chart]


def get_col_length(seat_chart):
    """returns the columns in the seat chart"""
    return len(seat_chart[0])


def get_row_length(seat_chart):
    """returns the rows in the seat chart"""
    return len(seat_chart)


def check_seat_in_range(loc, seat_chart):
    """checks if location is in the seat chart"""

    rows = get_row_length(seat_chart)
    cols = get_col_length(seat_chart)

    row = loc[0]
    col = loc[1]

    if (row >= 0) and (col >= 0) and (row < rows) and (col < cols):
        return True
    else:
        return False


def scan_direction(loc, direction, seat_chart):
    """scans a direction to see if an occupied seat in that direction"""

    row = loc[0] + direction[0]
    col = loc[1] + direction[1]

    while check_seat_in_range((row, col), seat_chart):

        seat = seat_chart[row][col]

        if not check_aisle(seat):

            if check_occupied(seat):
                return True

            else:
                return False

        row += direction[0]
        col += direction[1]

    return False


def check_direction(loc, direction, seat_chart):
    """checks if seat in an adjacent direction is occupied"""

    row = loc[0] + direction[0]
    col = loc[1] + direction[1]

    if check_seat_in_range((row, col), seat_chart):

        seat = seat_chart[row][col]

        if check_occupied(seat):
            return True
    else:
        return False


def scan_adj_seats(loc, seat_chart):
    """scans the adjacent directions to see how many seats are occupied"""

    adj_row = (-1, 0, 1)
    adj_col = (-1, 0, 1)

    count = 0

    for i in adj_row:
        for j in adj_col:
            if not ((i == 0) and (j == 0)):

                direction = (i, j)

                if scan_direction(loc, direction, seat_chart):
                    count += 1

    return count


def check_adj_seats(loc, seat_chart):
    """checks the adjacent seats to see how many seats are occupied"""

    adj_row = (-1, 0, 1)
    adj_col = (-1, 0, 1)

    count = 0

    for i in adj_row:
        for j in adj_col:
            if not ((i == 0) and (j == 0)):

                direction = (i, j)

                if check_direction(loc, direction, seat_chart):
                    count += 1

    return count


def get_seat_count(seat_chart):
    """"""

    count = 0

    for rows in seat_chart:
        for seat in rows:
            if check_occupied(seat):
                count += 1

    return count


def step1(seat_chart, func, thresh):
    """"""

    tmp = copy.deepcopy(seat_chart)

    for row in range(len(seat_chart)):
        for col in range(len(seat_chart[row])):

            loc = (row, col)
            seat = seat_chart[row][col]

            if check_empty(seat):

                adj_count = func(loc, seat_chart)

                if adj_count <= thresh:
                    tmp[row][col] = "#"

    return tmp


def step2(seat_chart, func, thresh):
    """"""

    tmp = copy.deepcopy(seat_chart)

    for row in range(len(seat_chart)):
        for col in range(len(seat_chart[row])):

            loc = (row, col)
            seat = seat_chart[row][col]

            if check_occupied(seat):

                adj_count = check_adj_seats(loc, seat_chart)

                if adj_count >= thresh:
                    tmp[row][col] = "L"

    return tmp


with open("data/day11.txt", "r") as f:
    data = [x.replace("\n", "") for x in f.readlines()]

seat_chart = char_split(data)

part = input("What part to solve for? (a or b): ")

d = {"a": (check_adj_seats, 0, 4), "b": (scan_adj_seats, 0, 5)}
params = d[part]

i = 0
while True:
    # i = 0
    # while i < 4:

    pprint.pprint(char_join(seat_chart))
    new_seat_chart = step1(seat_chart, params[0], params[1])
    pprint.pprint(char_join(new_seat_chart))
    new_seat_chart = step2(new_seat_chart, params[0], params[2])
    # pprint.pprint(char_join(new_seat_chart))

    if seat_chart == new_seat_chart:
        print(f"Number of occupied seats: {get_seat_count(new_seat_chart)}")
        print(i)
        break
    else:
        seat_chart = copy.deepcopy(new_seat_chart)

    i += 1
