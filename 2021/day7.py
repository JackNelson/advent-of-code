import pandas as pd
import re

with open('2021/data/day7.txt') as f:
    positions = [int(i) for i in re.findall(r'\d+', f.read())]

df = pd.DataFrame(positions, columns=['x'])

# part 1
target = df['x'].median()
fuel = int((df['x'] - target).abs().sum())
print(f"Fuel used in initial solution: {fuel}")

# part 2
target = round(df['x'].mean())

def calculate_fuel(v):
    fuel = 0

    for i in range(v):
        fuel += i+1
    
    return fuel

def calculate_total_fuel(df, target):
    return (df['x'] - target).abs().apply(calculate_fuel).sum()

fuel = calculate_total_fuel(df, target)

while (
    (fuel > calculate_total_fuel(df, target+1))
    |
    (fuel > calculate_total_fuel(df, target-1))
):
    if (fuel > calculate_total_fuel(df, target+1)):
        target += 1
    else:
        target -= 1
    
    fuel = calculate_total_fuel(df, target)

print(f"Fuel used in weighted solution: {fuel}")