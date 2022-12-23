from __future__ import annotations
from typing import List
import re
from math import prod

from utils.io import read_input

class Item(object):
    def __init__(self, worry_level: int):
        self.worry_level = worry_level

class Monkey(object):
    def __init__(
        self,
        number: int,
        items: List[Item],
        operation_str: str,
        test_value: int,
        true_pass_number: int,
        false_pass_number: int,
        monkeys: List[Monkey],
        relief: bool = True,
    ):
        self.number = number
        self.items = items
        self.operation_str = operation_str
        self.test_value = test_value
        self.true_pass_number = true_pass_number
        self.false_pass_number = false_pass_number
        self.monkeys = monkeys
        self.relief = relief

        self.inspections = 0
        self.inspecting_item = None

    @property
    def gcd(self) -> int:
        return prod([monkey.test_value for monkey in self.monkeys])
    
    def add_true_monkey(self, monkey: Monkey):
        self.true_monkey = monkey

    def add_false_monkey(self, monkey: Monkey):
        self.false_monkey = monkey
    
    def operation(self) -> None:

        d = {}
        d['old'] = self.inspecting_item.worry_level
        exec(self.operation_str, d)
        self.inspecting_item.worry_level = d['new']

    def bored(self) -> None:
        self.inspecting_item.worry_level = (
            self.inspecting_item.worry_level // 3
        )

    def reduce_worry(self) -> None:
        
        self.inspecting_item.worry_level = (
            self.inspecting_item.worry_level % self.gcd
        )

    def test(self) -> bool:
        remainder = self.inspecting_item.worry_level % self.test_value
        return remainder == 0

    def pass_item(self, monkey_number: int) -> None:
        
        monkey = [
            monkey
            for monkey in self.monkeys
            if monkey.number == monkey_number
        ][0]

        monkey.items.append(self.inspecting_item)
    
    def inspect_item(self) -> None:

        self.inspecting_item = self.items.pop(0)
        self.operation()

        if self.relief:
            self.bored()
        else:
            self.reduce_worry()

        if self.test():
            self.pass_item(monkey_number=self.true_pass_number)
        else:
            self.pass_item(monkey_number=self.false_pass_number)

        self.inspections += 1

    def inspect_items(self) -> None:

        for _ in range(len(self.items)):
            self.inspect_item()

def extract_ints(string: str) -> List[int]:
    return [int(i) for i in re.findall(r"(\d+)", string)]

def create_monkeys(
    monkey_params: List[List[str]],
    relief: bool = True,
) -> List[Monkey]:

    monkeys = []

    for monkey_param in monkey_params:

        monkeys.append(
            Monkey(
                number = extract_ints(monkey_param[0])[0],
                items = [
                    Item(worry_level=worry_level) 
                    for worry_level in extract_ints(monkey_param[1])
                ],
                operation_str = re.findall(r": (.*)", monkey_param[2])[0],
                test_value = extract_ints(monkey_param[3])[0],
                true_pass_number = extract_ints(monkey_param[4])[0],
                false_pass_number = extract_ints(monkey_param[5])[0],
                monkeys=monkeys,
                relief=relief,
            )
        )

    return monkeys

def play_monkey_in_middle(monkeys: List[Monkey], rounds: int) -> List[Monkey]:
    
    for _ in range(rounds):
        
        for monkey in monkeys:
            monkey.inspect_items()

    return monkeys

def get_monkey_business(monkeys: List[Monkey]) -> int:
    
    monkeys.sort(key=lambda x: -x.inspections)

    return prod([monkey.inspections for monkey in monkeys[:2]])

data = read_input(day=11)
monkey_params = [data[i:i+7] for i in range(0, len(data), 7)]

monkeys = create_monkeys(monkey_params=monkey_params)
monkeys = play_monkey_in_middle(monkeys=monkeys, rounds=20)
monkey_business = get_monkey_business(monkeys=monkeys)
print(f"Monkey Business after 20 rounds: {monkey_business}")

monkeys = create_monkeys(monkey_params=monkey_params, relief=False)
relief_value = prod([monkey.test_value for monkey in monkeys])
monkeys = play_monkey_in_middle(monkeys=monkeys, rounds=10000)
monkey_business = get_monkey_business(monkeys=monkeys)
print(f"Monkey Business after 10000 rounds without relief: {monkey_business}")