from utils.io import read_input

def to_int(s: str) -> int:
    return int(s) if s != '' else None

data = read_input(day=1, parse_func=to_int)

l = []
total_calories = 0

for calories in data:
    
    if calories:
        total_calories += calories

    else:
        l.append(total_calories)
        total_calories = 0

# part 1
print(f"Most calories an elf is carrying: {max(l)}")

# part 2
print(f'Calories the top 3 elves are carrying: {sum(sorted(l)[-3:])}')