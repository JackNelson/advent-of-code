from bidict import bidict
import numpy as np
import re

pattern = r"\w+"

with open('2021/data/day8.txt') as f:
    lines = f.readlines()

inputs = [
    [''.join(sorted(x)) for x in re.findall(r"\w+", line.split('|')[0])]
    for line in lines
]
outputs = [
    [''.join(sorted(x)) for x in re.findall(r"\w+", line.split('|')[1])]
    for line in lines
]
answers = [bidict(dict(zip(range(10), range(10)))) for _ in range(len(lines))]
mapped_output = [[] for _ in range(len(lines))]

def find_str_length(l, length):
    return [x for x in l if len(x) == length]

def find_str_diff(l, string, length, reverse=False):
    
    tmp = zip(np.arange(len(l)), l)
    
    if not reverse:
        tmp = [
            (
                x[0], 
                ''.join([c for c in string if c not in x[1]])
            ) for x in tmp
        ]

    else:
        tmp = [
            (
                x[0],
                ''.join([c for c in x[1] if c not in string])
            ) for x in tmp
        ]

    tmp = [x for x in tmp if len(x[1]) == length]

    return [l[x[0]] for x in tmp]

def calculate_count(l, value):
    return len([x for x in l if x == value])

for i in range(len(lines)):

    answers[i][1] = find_str_length(inputs[i], 2)[0]
    answers[i][7] = find_str_length(inputs[i], 3)[0]
    answers[i][4] = find_str_length(inputs[i], 4)[0]
    answers[i][8] = find_str_length(inputs[i], 7)[0]
    answers[i][2] = find_str_diff(
        find_str_length(inputs[i], 5), 
        answers[i][4], 
        2,
    )[0]
    answers[i][5] = find_str_diff(
        find_str_length(inputs[i], 5), 
        answers[i][2], 
        2,
    )[0]
    answers[i][3] = find_str_diff(
        find_str_length(inputs[i], 5), 
        answers[i][2], 
        1,
    )[0]
    answers[i][9] = find_str_diff(
        find_str_length(inputs[i], 6), 
        answers[i][4], 
        0,
    )[0]
    answers[i][6] = find_str_diff(
        find_str_length(inputs[i], 6), 
        answers[i][1], 
        1,
    )[0]
    answers[i][0] = [x for x in inputs[i] if x not in answers[i].values()][0]

    mapped_output[i] = [answers[i].inverse[x] for x in outputs[i]]

ones = sum([calculate_count(l, 1) for l in mapped_output])
fours = sum([calculate_count(l, 4) for l in mapped_output])
sevens = sum([calculate_count(l, 7) for l in mapped_output])
eights = sum([calculate_count(l, 8) for l in mapped_output])

# part 1
print(f"1,4,7,8 Output Occurrences: {ones+fours+sevens+eights}")

# part 2
output_values = [int(''.join([str(x) for x in l])) for l in mapped_output]
print(f"Total Output Sum: {sum(output_values)}")