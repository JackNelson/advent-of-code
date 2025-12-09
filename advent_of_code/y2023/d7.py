from __future__ import annotations
from typing import List, Tuple
import re
import itertools

from advent_of_code.io import read_input


class Card:

    l_1 = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]
    l_2 = ["J", "2", "3", "4", "5", "6", "7", "8", "9", "T", "Q", "K", "A"]


    def __init__(self, kind: str) -> None:

        self.kind = kind
        self.card_value = Card.l_1.index(kind)
        self.new_card_value = Card.l_2.index(kind)


    def __str__(self) -> str:
        return f"Card({self.kind}, {self.card_value})"


class Hand:

    l = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "Q", "K", "A"]


    def __init__(self, cards: List[Card], bid: int) -> None:

        self.cards = cards
        self.bid = bid
        self.hand_value = self.get_hand_value()
        self.new_hand_value = self.get_new_hand_value()


    def __str__(self) -> str:
        return f"Hand({''.join([card.kind for card in self.cards])}, {self.hand_value})"


    def card_groups(self) -> List[Tuple[str, int]]:
        return sorted(
            [
                (k, len(list(g)))
                for k, g in itertools.groupby(
                    sorted(self.cards, key=lambda x: x.kind),
                    lambda c: c.kind,
                )
            ],
            key=lambda x: x[1],
            reverse=True,
        )


    def is_five_of_kind(self) -> bool:
        return self.card_groups()[0][1] == 5


    def is_four_of_kind(self) -> bool:
        return self.card_groups()[0][1] == 4


    def is_three_of_kind(self) -> bool:
        return self.card_groups()[0][1] == 3


    def is_full_house(self) -> bool:
        return (
            (self.card_groups()[0][1] == 3)
            and
            (self.card_groups()[1][1] == 2)
        )


    def is_pair(self) -> bool:
        return self.card_groups()[0][1] == 2


    def is_two_pair(self) -> bool:
        return (
            (self.card_groups()[0][1] == 2)
            and
            (self.card_groups()[1][1] == 2)
        )


    def get_hand_value(self) -> int:

        props = [
            self.is_five_of_kind,
            self.is_four_of_kind,
            self.is_full_house,
            self.is_three_of_kind,
            self.is_two_pair,
            self.is_pair,
        ]

        for i, prop in enumerate(props):
            if prop():
                return len(props) - i

        return 0

    def get_new_hand_value(self) -> int:

        hand_values = []

        joker_idx = [
            i
            for i, card in enumerate(self.cards)
            if card.kind == "J"
        ]

        if joker_idx:

            for new_kind in Hand.l:

                for i in joker_idx:
                    self.cards[i] = Card(kind=new_kind)

                hand_values.append(self.get_hand_value())

            for i in joker_idx:
                self.cards[i] = Card(kind="J")

            return max(hand_values)

        else:
            return self.get_hand_value()


def main(test: bool, part: str = None) -> None:

    path = "data/y2023/d7.txt"

    if test:
        path = "tests/" + path

    ans_part1 = "SKIPPED"
    ans_part2 = "SKIPPED"

    hands = read_input(
        path=path,
        parse_func=lambda line: [
            Hand(
                cards=[Card(kind=kind) for kind in hand],
                bid=int(bid),
            )
            for hand, bid in re.findall(r"([0-9TJQKA]{5}) (\d+)", line)
        ][0],
    )

    if part != "2":

        rankded_hands = [
            hand for hand in sorted(
                hands,
                key= lambda hand: (
                    hand.hand_value,
                    hand.cards[0].card_value,
                    hand.cards[1].card_value,
                    hand.cards[2].card_value,
                    hand.cards[3].card_value,
                    hand.cards[4].card_value,
                ),
            )
        ]

        ans_part1 = sum(
            [(i+1)*hand.bid for i, hand in enumerate(rankded_hands)]
        )

    if part != "1":

        new_rankded_hands = [
            hand for hand in sorted(
                hands,
                key= lambda hand: (
                    hand.new_hand_value,
                    hand.cards[0].new_card_value,
                    hand.cards[1].new_card_value,
                    hand.cards[2].new_card_value,
                    hand.cards[3].new_card_value,
                    hand.cards[4].new_card_value,
                ),
            )
        ]

        ans_part2 = sum(
            [(i+1)*hand.bid for i, hand in enumerate(new_rankded_hands)]
        )

    print(f"AOC 2023 - Day 7")
    print(f"    Part 1: {ans_part1}")
    print(f"    Part 2: {ans_part2}")
