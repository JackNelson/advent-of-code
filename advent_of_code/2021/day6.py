import re

with open('2021/data/day6.txt') as f:
    fishes = [int(i) for i in re.findall(r'\d+', f.read())]

def calculate_population(fishes, num_days, daily_print=False):

    adult_fish = [0]*7
    child_fish = [0]*9

    for fish in fishes:
        adult_fish[fish] += 1

    for i in range(num_days):

        adult_spawn = adult_fish.pop(0)
        child_spawn = child_fish.pop(0)

        child_fish.append(adult_spawn + child_spawn)
        adult_fish.append(adult_spawn + child_spawn)

        count = sum(adult_fish) + sum(child_fish)
        
        if daily_print:
            print(f"After {i+1} day: {count}")

    print(f"{count} lanternfish after {num_days} days")

calculate_population(fishes, 80)
calculate_population(fishes, 256)