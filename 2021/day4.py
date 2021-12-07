import numpy as np
import pandas as pd
import re

class BingoCard(object):

    def __init__(self, lines):

        self.card = pd.DataFrame(
            [
                [int(i) for i in re.findall(r'\d+', line)]
                for line in lines
            ]
        )
        self.picked = pd.DataFrame(
            [[False for _ in range(5)] for _ in range(5)]
        )

    def mark_card(self, value):

        for col in self.card.columns:
            idx = self.card.loc[lambda x: x[col] == value].index

            for i in idx:
                self.picked.loc[i,col] = True
                
        self.check_bingo()
            
        if self.won:
            self.score_card()

    def check_bingo(self):

        tmp = False
        
        for col in self.picked:
            if self.picked[col].all():
                tmp = True

        for col in self.picked.T:
            if self.picked.T[col].all():
                tmp = True

        self.won = tmp

    def score_card(self):

        unmarked = 0

        for col in self.card.columns:
            for idx in self.card.index:
                if not self.picked.loc[idx,col]:
                    unmarked += self.card.loc[idx,col]

        self.unmarked = unmarked

def find_winners(bingo_cards):
    return [i for i, card in enumerate(bingo_cards) if card.won]

def find_losers(bingo_cards):
    return [i for i, card in enumerate(bingo_cards) if not card.won]

def print_winner(idx, bingo_card, value):
    print(f"Card #: {idx+1}, Score: {bingo_card.unmarked * value}")


with open('2021/data/day4.txt') as f:
    lines = f.readlines()

values = [int(i) for i in lines[0].split(',')]
n = (len(lines) - 1) // 6
bingo_cards = [BingoCard(lines[i:i+5]) for i in np.arange(2, (6*n)+1, 6)]

first_card_won = False
all_cards_won = False

for v in values:
    for bingo_card in bingo_cards:
        bingo_card.mark_card(v)

    cards_won = [bingo_card.won for bingo_card in bingo_cards]
    
    # part 1
    if not first_card_won:
        if any(cards_won):
            first_card_won = True
            idx = find_winners(bingo_cards)[0]
            print("First Bingo Card Won!")
            print_winner(idx, bingo_cards[idx], v)

    # part 2
    if sum(cards_won) == n-1:
        idx = find_losers(bingo_cards)[0]

    if all(cards_won):
        print("Last Bingo Card Won!")
        print_winner(idx, bingo_cards[idx], v)
        break