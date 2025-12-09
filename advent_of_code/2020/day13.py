with open("data/day13.txt", "r") as f:
    data = [x.replace("\n", "") for x in f.readlines()]


time = int(data.pop(0))
buses = [int(j) for i, j in enumerate(data[0].split(",")) if j != "x"]
locs = [i for i, j in enumerate(data[0].split(",")) if j != "x"]


def find_earliest_bus(time, buses):

    times = [(time // x) * x + x for x in buses]
    min_time_loc = [i for i, j in enumerate(times) if j == min(times)][0]
    bus_id = buses[min_time_loc]

    wait = times[min_time_loc] - val

    print(f"Looking for ")
    print(f"Product of wait({wait}) and bus id ({bus_id}): {bus_id*wait}")
