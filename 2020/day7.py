import re


def parse_line(line):
    """parses line into list of bag color and list of all its contents"""

    outer_bag, inner_bags = re.findall(r"^(.*)bags contain (.*).", line)[0]

    outer_bag = outer_bag.strip()

    try:
        inner_bags = [
            re.findall(r"(\d+) (.*) bag", x)[0] for x in inner_bags.split(",")
        ]

        inner_bag_list = []
        for bag in inner_bags:
            for i in range(int(bag[0])):
                inner_bag_list.append(bag[1].strip())

    except:
        inner_bag_list = []

    return outer_bag, inner_bag_list


def get_parent_bag_count(bag_color):
    """finds the number of bags a bag color can be found"""

    child_bags = [bag_color]
    parent_bags = []
    while True:

        new_bags = []

        for b in child_bags:
            for bag in bags:

                if b in bag[1]:
                    parent_bags.append(bag[0])
                    new_bags.append(bag[0])

        if len(new_bags) == 0:
            break
        else:
            child_bags = new_bags.copy()

    print(f"Number of bags that have {bag_color}: {len(set(parent_bags))}")


def get_child_bag_count(bag_color):
    """finds the number of bags inside of a bag color"""

    parent_bags = [bag_color]
    child_bags = []
    count = 0
    while True:

        new_bags = []
        for b in parent_bags:
            for bag in bags:
                if b in bag[0]:
                    count += len(bag[1])
                    new_bags.extend(bag[1].copy())

        if len(new_bags) == 0:
            break
        else:
            parent_bags = new_bags.copy()

    print(f"Number of bag inside of {bag_color}: {count}")


with open("data/day7.txt", "r") as f:
    data = f.readlines()

bags = [parse_line(line) for line in data]
bag_color = input("Enter a bag color: ").lower()
direction = input("Which direction to count bags? (up/down) ").lower()

if direction == "up":
    get_parent_bag_count(bag_color)
elif direction == "down":
    get_child_bag_count(bag_color)
else:
    raise TypeError("Incorrect input, enter either 'up' or 'down'")
