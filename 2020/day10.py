import numpy as np
import pandas as pd


def recurse_func(loc, N, n, l, val, count):
    """
    recursive loop to see if
    """

    for i in range(N):

        l.append(data[loc + i])

        if len(l) == n:

            tmp = [x for x in data if x not in l]
            diff = np.diff(tmp)

            if max(diff) <= val:
                if max(tmp) == max(data):
                    count += 1

            l.pop()
        else:
            count = recurse_func(loc + i + 1, N - i, n, l, val, count)

            l.pop()

    return count


def part1():

    diff = np.diff(data)

    df = (
        pd.DataFrame({"adapter": data[1:], "diff": diff})
        .groupby("diff")
        .agg({"adapter": "count"})
    )
    ans = (df.loc[1] * (df.loc[3] + 1)).values[0]

    print(f"Product of 1-jolt and 3-jolt differences: {ans}")


def part2():

    count = 0
    n = 3

    for i in range(n):
        n_hat = i + 1
        N = len(data) - n + 1
        count += recurse_func(0, N, n_hat, [], n, count)

    print(f"Possible combination of adapters: {count}")


with open("data/day10.txt", "r") as f:
    data = f.readlines()

data = [0] + sorted([int(x) for x in data])

part = input("Select which part to answer (1 or 2): ")

if part == "1":
    part1()
elif part == "2":
    part2()
else:
    raise TypeError("Invalid input, please enter '1' or '2'")
