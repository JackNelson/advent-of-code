import itertools

with open("data/day6.txt", "r") as f:
    data = f.read().split("\n\n")

data = [[list(y) for y in x.split("\n")] for x in data]

# use for part a
# data = [set(list(itertools.chain(*x))) for x in data]

# use for part b
data = [set.intersection(*map(set, x)) for x in data]

counts = [len(x) for x in data]
print(f"Sum of yes answers: {sum(counts)}")