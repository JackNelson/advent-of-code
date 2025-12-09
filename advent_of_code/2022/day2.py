from typing import List, Literal
import pandas as pd
import os

from utils.io import read_input

res_map = pd.DataFrame(
    {
        'opp': ['A','B','C'],
        'key': ['X','Y','Z'],
        'pick': ['rock','paper','scissors'],
        'value': [1,2,3],
        'result': [0,3,6],
    }
)

def parse_line(line: str) -> List[str]:
    return line.split(' ')

"""
PART A 
              Y O U
       | X=1 | Y=2 | Z=3 |
       |-----|-----|-----|
   A=1 |  3  |  6  |  0  |
O  ----|-----|-----|-----|
P  B=2 |  0  |  3  |  6  |
P  ----|-----|-----|-----|
   C=3 |  6  |  0  |  3  |

   RESULT = 3 * ((YOU + 4 - OPP) % 3)
"""
def get_result_a(
    opp: Literal['A','B','C'],
    you: Literal['X','Y','Z']
) -> int:

    global res_map

    opp_v = res_map.set_index('opp').loc[opp, 'value']
    you_v = res_map.set_index('key').loc[you, 'value']

    return 3 * ((you_v + 4 - opp_v) % 3) + you_v

"""
PART B 

           R E S U L T
       | X=0 | Y=3 | Z=6 |
       |-----|-----|-----|
   A=1 |  3  |  1  |  2  |
O  ----|-----|-----|-----|
P  B=2 |  1  |  2  |  3  |
P  ----|-----|-----|-----|
   C=3 |  2  |  3  |  1  |

   YOU = ((OPP + 1) + (RESULT / 3)) % 3 + 1
"""
def get_result_b(
    opp: Literal['A','B','C'],
    result: Literal['X','Y','Z'],
) -> int:

    global res_map

    opp_v = res_map.set_index('opp').loc[opp, 'value']
    result_v = res_map.set_index('key').loc[result, 'result']
    
    return int((opp_v + 1) + (result_v / 3)) % 3 + 1 + result_v

data = read_input(day=2, parse_func=parse_line)

res_a = sum([get_result_a(opp=opp, you=you) for opp, you in data])
print(f"Part A Score: {res_a}")

res_b = sum([get_result_b(opp=opp, result=result) for opp, result in data])
print(f'Part B Score: {res_b}')