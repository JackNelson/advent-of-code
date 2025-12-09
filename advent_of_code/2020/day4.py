import os
import numpy as np
import re

with open("data/day4.txt", "r") as f:
    data = f.read().split("\n\n")


def __check_int(val, min_int, max_int):
    """check if value falls between specified minimum amd maximum values"""

    try:
        val = int(val)

        if (val >= min_int) and (val <= max_int):
            return True

        else:
            return False

    except:
        return False


def check_byr(val):
    """verify birth year is between 1920 and 2002"""
    return __check_int(val, 1920, 2002)


def check_iyr(val):
    """verify issue year is between 2010 and 2020"""
    return __check_int(val, 2010, 2020)


def check_eyr(val):
    """verify expiration year is between 2020 and 2030"""
    return __check_int(val, 2020, 2030)


def check_hgt(val):
    """verify height falls between valid height ranges and correct units"""
    match = re.findall(r"^(\d+)(cm|in)$", val)

    if len(match) > 0:
        if match[0][1] == "cm":
            return __check_int(match[0][0], 150, 193)
        elif match[0][1] == "in":
            return __check_int(match[0][0], 59, 76)
        else:
            return False
    else:
        return False


def check_hcl(val):
    """verify hair color matches the required alphanumeric pattern"""
    match = re.findall(r"^(\#[a-f0-9]{6})$", val)

    if len(match) > 0:
        return True
    else:
        return False


def check_ecl(val):
    """verify eye color matches one of the required color abbreviations"""
    colors = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

    if val in colors:
        return True
    else:
        return False


def check_pid(val):
    """verify passport id follows required alphanumeric pattern"""
    match = re.findall(r"^([0-9]{9})$", val)

    if len(match) > 0:
        return True
    else:
        return False


verify_func = {
    "byr": check_byr,
    "iyr": check_iyr,
    "eyr": check_eyr,
    "hgt": check_hgt,
    "hcl": check_hcl,
    "ecl": check_ecl,
    "pid": check_pid,
}

data = [x.replace(" ", ",").replace("\n", ",") for x in data]
data = [dict(tuple(y.split(":")) for y in x.split(",")) for x in data]

count = 0

for i in data:

    fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

    for k, v in i.items():
        if k in fields:

            # use for part a
            # fields.remove(k)

            # use for part b
            if verify_func[k](v):
                fields.remove(k)

    if len(fields) == 0:
        count += 1

print(f"Number of valid passports: {count}")
