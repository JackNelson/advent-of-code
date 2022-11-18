import re
from types import ClassMethodDescriptorType

with open('2021/data/test.txt') as f:
    lines = f.readlines()
    
polymer = lines[0][:-1]

decipher = {
    x[0][0]:x[0][1]
    for x in [re.findall(r'(\w+) \-\> (\w+)', line) for line in lines] 
    if x
}

def grow_polymer(polymer):
    
    global decipher
    tmp = ''
    
    for i in range(len(polymer)-1):
        insertion = decipher[polymer[i:i+2]]
        tmp += polymer[i] + insertion

    tmp += polymer[-1]

    return tmp

# part 1
# print(f"Template: {polymer}")
for i in range(10):
    polymer = grow_polymer(polymer)
    # print(f"After step {i+1}: {polymer}")

char_counts = {
    char: polymer.count(char) 
    for char in polymer
}

# print(char_counts)
score = sorted(char_counts.values())[-1] - sorted(char_counts.values())[0]

print("10 Steps...")
print(f"Most common element minus least common element count: {score}")

# part 2
for i in range(30):
    polymer = grow_polymer(polymer)
    # print(f"After step {i+1}: {polymer}")

char_counts = {
    char: polymer.count(char) 
    for char in polymer
}

# print(char_counts)
score = sorted(char_counts.values())[-1] - sorted(char_counts.values())[0]

print("40 Steps...")
print(f"Most common element minus least common element count: {score}")

# TODO use pandas to vectorize 
# print(polymer)
# print(decipher)