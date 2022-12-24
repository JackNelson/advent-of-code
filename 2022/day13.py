from typing import List, Union
from copy import copy
from math import prod

from utils.io import read_input


def compare_pair(left: int, right: int) -> bool:
    
    if left > right:
        return False
    elif left < right:
        return True
    else:
        return None

def right_order(
    left: Union[int, List[int]],
    right: Union[int, List[int]]
) -> bool:

    for l, r in list(zip(left, right)):
        if isinstance(l, list) or isinstance(r, list):

            if isinstance(l, int):
                l = [l]
            elif isinstance(r, int):
                r = [r]

            is_in_right_order = right_order(left=l, right=r)

        else:
            is_in_right_order = compare_pair(left=l, right=r)

        if is_in_right_order != None:
            return is_in_right_order

    if len(left) != len(right):
        return len(left) < len(right)
    else:
        return None

data = read_input(day=13)

packets = []

for line in data:
    if len(line) > 0:
        exec(f'packets.append({line})')

correct_order_idx = [
    i+1 
    for i, (left, right) 
    in enumerate([packets[j:j+2] for j in range(0, len(packets), 2)])
    if right_order(left=left, right=right)
]

print(f"Sum of correct order pair indices: {sum(correct_order_idx)}")

divider_packets = [[[2]],[[6]]] 
ordered_packets = copy(divider_packets)

for packet in packets:

    inserted = False
    
    for i, p in enumerate(ordered_packets):

        if right_order(left=packet, right=p):
            ordered_packets.insert(i, packet)
            break

    if not inserted:
        ordered_packets.append(packet)

divider_packet_idx = [
    i+1 for i, packet in enumerate(ordered_packets)
    if packet in divider_packets
]

print(f'Decoder key for distress signal: {prod(divider_packet_idx)}')