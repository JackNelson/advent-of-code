import re

with open('2021/data/day2.txt') as f:
    l = f.readlines()

# print(l)
horz = 0
depth = 0

def read_command(line):

    global horz
    global depth

    m = re.findall(r"(\w+) (\d+)", line)[0]

    if m[0] == 'forward':
        horz += int(m[1])
    elif m[0] == 'down':
        depth += int(m[1])
    else:
        depth -= int(m[1])

for i in l:
    read_command(i)

print(f"horz: {horz}, depth: {depth}, ans: {horz*depth}")

horz = 0
depth = 0
aim = 0

def read_command2(line):

    global horz
    global depth
    global aim

    m = re.findall(r"(\w+) (\d+)", line)[0]

    if m[0] == 'up':
        aim -= int(m[1])
    elif m[0] == 'down':
        aim += int(m[1])
    else:
        horz += int(m[1])
        depth += int(m[1])*aim

for i in l:
    read_command2(i)

print(f"horz: {horz}, depth: {depth}, ans: {horz*depth}")