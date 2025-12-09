import pandas as pd

df = pd.read_fwf(
    '2021/data/day3.txt',
    widths=[1]*12,
    dtype=str
)

# part 1
def shift_bit(bit, offset=1):
    return str((int(bit)+offset)%2)

bit_num = ''.join(df.mode().values[0])
inv_bit_num = ''.join([shift_bit(i) for i in bit_num])
g_rate = int(bit_num, 2)
e_rate = int(inv_bit_num, 2)

print(f"gamma rate: {g_rate}, epsilon rate: {e_rate}, \
power comsumption: {g_rate*e_rate}")

# part 2
def filter_df(df, offset=0):

    tmp = df.copy()
    i = 0
    cols = tmp.columns

    while len(tmp) > 1:

        val = shift_bit(
            tmp.mode()[cols[i]].sort_values(ascending=False).iloc[0],
            offset=offset 
        )
        tmp = tmp.loc[lambda x: x[cols[i]] == val]

        i += 1

    return tmp

o_rating = int(''.join(filter_df(df).values[0]), 2)
co_rating = int(''.join(filter_df(df, offset=1).values[0]), 2)

print(f"oxygen generator rating: {o_rating}, CO2 scrubber rating: \
{co_rating}, life support rating: {o_rating*co_rating}")