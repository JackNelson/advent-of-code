import re
# import pandas as pd

with open('2021/data/day9.txt') as f:
    data = [
        [int(x) for x in re.findall('\d', line)]
        for line in f.readlines()
    ]

def islower(i, j, dir):

    global data

    shift_i = i
    shift_j = j

    if dir == 'up':
        shift_i -= 1
    elif dir == 'down':
        shift_i += 1
    elif dir == 'left':
        shift_j -= 1
    elif dir == 'right':
        shift_j += 1

    if (
        (shift_i >= 0) and (shift_i < len(data))
        and
        (shift_j >= 0) and (shift_j < len(data[i]))
    ):
        return data[i][j] < data[shift_i][shift_j]

    else:
        return True

lowpoints = []
# res = []
for i, row in enumerate(data):

    # tmp = []
    for j, col in enumerate(row):
        
        # tmp.append(
        #     all(
        #         [
        #             islower(i, j, 'up'),
        #             islower(i, j, 'down'),
        #             islower(i, j, 'left'),
        #             islower(i, j, 'right'),
        #         ]
        #     )
        # )

        if (
                all(
                    [
                        islower(i, j, 'left'),
                        islower(i, j, 'up'),
                        islower(i, j, 'right'),
                        islower(i, j, 'down'),
                    ]
                )
            ):

                lowpoints.append(data[i][j])

    # res.append(tmp)

# print(pd.DataFrame(data))
# print(pd.DataFrame(res))

risk_level = sum([x+1 for x in lowpoints])

print(f"Overall risk level for {len(lowpoints)} low points: {risk_level}")