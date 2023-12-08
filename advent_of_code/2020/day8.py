import re
import pprint


def get_new_loc(op, val, loc, acc):
    """updates accumulator and finds next line location"""

    if op == "jmp":
        loc += int(val)
    elif op == "acc":
        acc += int(val)
        loc += 1
    else:
        loc += 1

    return loc, acc


def flip_op(op):
    """flips a jmp operation to nop and vice versa"""

    if op == "jmp":
        return "nop"
    elif op == "nop":
        return "jmp"
    else:
        return op


def execute(loc, locs, acc, data, debug=False):
    """executes the commands in data"""

    while loc != (len(data) - 1):

        locs.append(loc)
        op, val = data[loc]

        loc, acc = get_new_loc(op, val, loc, acc)

        if loc in locs:

            if not debug:
                print(f"Infinite loop happens to {locs[-2]} to {loc}")
                print(f"Value of accumulator before infinite loop: {acc}")

            return (False, acc)

    print(f"Value of accumulator at completion: {acc}")
    return (True, acc)


def debug(loc, locs, acc, data):
    """debugs the data to find infinite loop root cause"""

    while True:

        op, val = data[loc]
        new_op = flip_op(op)

        if new_op in ["nop", "jmp"]:

            tmp = data.copy()
            tmp[loc][0] = new_op

            res = execute(loc, locs, acc, data, True)
            if res[0]:
                break

        loc, acc = get_new_loc(op, val, loc, acc)

    print(f"Bug located at: {loc}")


with open("data/day8.txt", "r") as f:
    data = f.readlines()

data = [list(re.findall("^([a-z]+) ([\+\-]\d+)$", x)[0]) for x in data]

locs = []
loc = 0
acc = 0
count = 0

mode = input("What mode to run boot code? 'normal' or debug ").lower()

if mode == "normal":
    res = execute(loc, locs, acc, data)
elif mode == "debug":
    debug(loc, locs, acc, data)
else:
    raise TypeError("Incorrect input, enter either 'normal' or 'debug'")
