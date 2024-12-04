from __future__ import annotations
from typing import List, Literal, Tuple
import numpy as np
import re

from advent_of_code.io import read_input


class BroadcastNetwork:

    def __init__(self, modules: List[BaseModule]):

        self.module_dict = {module.name: module for module in modules}
        self.transmissions = []

    def press_button(self) -> None:

        transmission = []
        queue = [("button", "low", "broadcaster")]

        while len(queue) > 0:

            in_module, pulse, module = queue.pop(0)

            transmission.append((in_module, pulse, module))

            if module != "output":
                out_pulse, out_modules = self.module_dict[module].relay_pulse(
                    in_module=in_module,
                    pulse=pulse,
                )

                for out_module in out_modules:
                    queue.append((module, out_pulse, out_module))

        return np.array(transmission)

    def cycle_buttons(self) -> bool:

        self.transmissions = []

        while True:

            transmission = self.press_button()

            for t in self.transmissions:

                if np.array_equiv(t, transmission):
                    if np.all(t==transmission):
                        return True

            self.transmissions.append(transmission)


class BaseModule:

    def __init__(self, name: str, out_modules: List[str]):

        self.name = name
        self.out_modules = out_modules

    def relay_pulse(
        self,
        in_module: BaseModule,
        pulse: Literal["low", "high"]
    ) -> Tuple[Literal["low", "high"], List[str]]:
        return (pulse, self.out_modules)


class FlipFlopModule(BaseModule):

    def __init__(self, name: str, out_modules: List[str]):

        super().__init__(name=name, out_modules=out_modules)
        self.status = "off"

    def relay_pulse(
        self,
        in_module: BaseModule,
        pulse: Literal["low", "high"],
    ) -> Tuple[Literal["low", "high"], List[str]]:

        if pulse == "low":

            if self.status == "off":

                self.status = "on"
                out_pulse = "high"

            else:

                self.status = "off"
                out_pulse = "low"

            return (out_pulse, self.out_modules)

        else:
            return (None, [])


class ConjunctionModule(BaseModule):

    def __init__(self, name: str, out_modules: List[str]):

        super().__init__(name=name, out_modules=out_modules)
        self._in_modules = []
        self.last_transmission = {}

    @property
    def in_modules(self) -> List[str]:
        return self._in_modules

    @in_modules.setter
    def in_modules(self, l: List[str]):

        self._in_modules = l
        self.last_transmission = {in_module: "low" for in_module in l}

    def relay_pulse(
        self,
        in_module: BaseModule,
        pulse: Literal["low", "high"],
    ) -> Tuple[Literal["low", "high"], List[BaseModule]]:

        self.last_transmission[in_module] = pulse

        if all([v=="high" for v in self.last_transmission.values()]):
            return ("low", self.out_modules)

        else:
            return ("high", self.out_modules)


def parse_module(line: str) -> BaseModule:

    module_type, module_name, out_modules = (
        re.findall(r"([\%\&]?)([a-z]+) -> ([a-z\s\,]+)", line)[0]
    )

    out_modules = out_modules.split(", ")

    if module_type == "%":
        return FlipFlopModule(name=module_name, out_modules=out_modules)

    elif module_type == "&":
        return ConjunctionModule(name=module_name, out_modules=out_modules)

    else:
        return BaseModule(name=module_name, out_modules=out_modules)


def main(test: bool, part: int = None) -> None:

    path = "data/y2023/d20.txt"

    if test:
        path = "tests/" + path

    ans_part1 = "SKIPPED"
    ans_part2 = "SKIPPED"

    modules = read_input(
        path=path,
        parse_func=parse_module,
    )

    conjunction_modules = [
        m for m in modules if isinstance(m, ConjunctionModule)
    ]

    for conjunction_module in conjunction_modules:

        conjunction_module.in_modules = [
            m.name for m in modules
            if conjunction_module.name in m.out_modules
        ]

    network = BroadcastNetwork(modules=modules)

    from pprint import pprint
    pprint([(k, type(v), v.out_modules) for k, v in network.module_dict.items()])

    network.cycle_buttons()

    pprint(network.transmissions)

    # if part != "2":

    # if part != "1":

    print(f"AOC 2023 - Day 20")
    print(f"    Part 1: {ans_part1}")
    print(f"    Part 2: {ans_part2}")
