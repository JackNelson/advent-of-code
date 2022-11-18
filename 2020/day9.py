def recurse_func(loc, N, n, l, val):
    """
    recursive loop to find see if previous preamble values sum to val
    """

    for i in range(N):

        l.append(data[loc + i])

        if len(l) == n:

            if sum(l) == val:
                return True

            l.pop()
        else:
            res = recurse_func(loc + i + 1, N - i, n, l, val)
            if res:
                return True
            else:
                l.pop()
    return False


def find_contiguous_set(val):
    """find a contiguous set that sums to val given"""

    n = 2
    while len(data) > n:

        for i in range(len(data) - n + 1):

            l = sorted(data[i : i + n])

            if sum(l) == val:
                return l

        n += 1


with open("data/day9.txt", "r") as f:
    data = f.readlines()

data = [int(x) for x in data]

loc = 0
length = 25
n = 2
N = length - n + 1

while loc != (len(data) - length):

    val = data[loc + length]
    checksum = recurse_func(loc, N, n, [], val)

    if not checksum:
        print(f"{val} failed to find sum in preamble")
        l = find_contiguous_set(val)
        print(f"encryption weakness sum: {l[0]+l[-1]}")
        break

    loc += 1
