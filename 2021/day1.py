with open('2021/data/day1.txt') as f:
    l = [int(x) for x in f.readlines()]

ans = sum([n < l[i+1] for i, n in enumerate(l[:-1])])
print(f"Part 1, increases in depth: {ans}")

l2 = [n + l[i+1] + l[i+2] for i, n in enumerate(l[:-2])]
ans2 = sum([n < l2[i+1] for i, n in enumerate(l2[:-1])])
print(f"Part 2, increases in rolling sum depth: {ans2}")