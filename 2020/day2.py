import os
import re


def __parse_line(line):
    group = re.match(r"(\d+)-(\d+)\s([a-zA-z0-9]):\s(.*)", line)
    return group.groups()


def test_password(line):
    """
    parses password and password rule and tests if rule is followed, rule is
    letter mush occur between min/max count
    """

    min_count, max_count, letter, password = __parse_line(line)
    count = len(re.findall(f"{letter}", password))

    if (count >= int(min_count)) and (count <= int(max_count)):
        return True
    else:
        return False


def test_password_new(line):
    """parses password and new password rule and tests if rule is followed,
    rule is letter must appear between min/max locations"""

    min_loc, max_loc, letter, password = __parse_line(line)

    if (password[int(min_loc) - 1] == letter) and (
        password[int(max_loc) - 1] != letter
    ):
        return True
    elif (password[int(min_loc) - 1] != letter) and (
        password[int(max_loc) - 1] == letter
    ):
        return True
    return False


with open("data/day2.txt", "r") as f:
    data = [x.replace(os.linesep, "") for x in f.readlines()]

policy = input("type policy rule to follow {old or new}: ")

policy_dict = {"old": test_password, "new": test_password_new}

correct = 0

for line in data:
    if policy_dict[policy](line):
        correct += 1

print(f"Number of valid passwords: {correct}")
