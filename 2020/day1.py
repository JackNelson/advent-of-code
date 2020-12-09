import pandas as pd
import numpy as np

vals = pd.read_csv("data/day1.csv", header=None)[0].values.tolist()

n = int(input("Amount of numbers that sum to 2020: "))
N = len(vals) - n + 1


def recurse_func(loc, N, n, l):

    for i in range(N):

        l.append(vals[loc + i])

        if len(l) == n:

            if sum(l) == 2020:
                print(f"values: {l}")
                print(f"answer: {np.product(l)}")
                exit()

            l.pop()
        else:
            recurse_func(loc + i + 1, N - i, n, l)
            l.pop()


recurse_func(0, N, n, [])
