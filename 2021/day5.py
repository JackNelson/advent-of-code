import numpy as np
import pandas as pd
import re

def get_steps(axis, row):

    if row[f'{axis}1'] < row[f'{axis}2']:
        return np.arange(row[f'{axis}1'], row[f'{axis}2']+1)
    else:
        return np.arange(row[f'{axis}1'], row[f'{axis}2']-1, -1)

def get_line_points(df):

    points = []

    for idx, row in df.iterrows():

        x_steps = get_steps('x', row)
        y_steps = get_steps('y', row)

        if len(x_steps) <= 1:
            x_steps = [row['x1']] * len(y_steps)

        if len(y_steps) <= 1:
            y_steps = [row['y1']] * len(x_steps)

        points.extend(zip(x_steps, y_steps))
    
    return pd.DataFrame(points, columns=['x','y'])

def get_overlapping_count(df):
    return (
        len(
            get_line_points(df)
            .loc[lambda x: x.duplicated()]
            .drop_duplicates()
        )
    )


with open('2021/data/day5.txt') as f:
    vents = [
        [int(i) for i in re.findall(r"\d+", line)] 
        for line in f.readlines()
    ]

df = pd.DataFrame(vents, columns=['x1','y1','x2','y2'])

tmp = (
    df
    .loc[
        lambda x:
            (x['x1'] == x['x2'])
            |
            (x['y1'] == x['y2'])
    ]
)

# part 1
print(f"Overlapping vents: {get_overlapping_count(tmp)}")

# part 2
print(f"Overlapping vents: {get_overlapping_count(df)}")