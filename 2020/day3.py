import os
import numpy as np

with open("data/day3.txt", "r") as f:
    data = [x.replace(os.linesep, "") for x in f.readlines()]

ans = []

while True:

    count = 0
    shift = int(input("How many spaces to the right on slope? "))
    drop = int(input("How many spaces down on slope? "))

    lines = list(np.arange(0, len(data), drop))

    for i in range(len(data)):
        line = data[i]

        if i in lines:

            j = lines.index(i)
            loc = j * shift % (len(line) - 1)
            print(loc)
            print(j)
            print(i)

            if line[loc] == "#":
                line = line[:loc] + "X" + line[loc + 1 :]
                count += 1
            else:
                line = line[:loc] + "O" + line[loc + 1 :]
        print(line)

    ans.append(count)
    again = input("Go down the slope again (Y/N)? ").lower()
    print(lines)

    if again == "n":
        break

print(f"Number of trees encountered: {ans}")
print(f"Product of the encountered trees: {np.prod(ans, dtype=float)}")
