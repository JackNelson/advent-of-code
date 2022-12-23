from typing import Literal

from utils.io import read_input

def get_pixel(cycle:int, X:int) -> Literal['#','.']:
    return '#' if X-1 <= ((cycle - 1) % 40) <= X+1 else '.'

data = read_input(day=10, parse_func=lambda x: x.split(' '))

X = 1
cycle = 1
pixels = []
register = []

for line in data:
    
    register.append(X)
    pixels.append(get_pixel(cycle=cycle, X=X))

    if line[0] == "addx":
        cycle += 1
        register.append(X)
        pixels.append(get_pixel(cycle=cycle, X=X))
        X += int(line[1])  

    cycle += 1 

signal_strengths = [
    (i+1) * X for i, X, in enumerate(register) if (i+21) % 40 == 0 
]

print("Part 1 - 20th, 60th, 100th, 140th, 180th, 220th Signal Strengths:")
print(f"{sum(signal_strengths)}")

print('\nPart 2 - CRT:')
for line in [''.join(pixels[i*40:(i+1)*40]) for i in range(len(pixels)//40)]:
    print(line)