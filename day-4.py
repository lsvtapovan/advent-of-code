from typing import Iterable
import numpy as np
import pandas as pd

def format(input: str):
    return np.array([int(x) for x in input.split(' ') if x != ''])

def bingo_test(card: np.array, numbers: Iterable):
    # Returns the score if the card wins at some point.
    # Returns None otherwise.
    def has_won(marked_card: np.array):
        for row in marked_card:
            if all(row == True):
                return True
        
        for row in marked_card.T:
            if all(row == True):
                return True

        return False

    marked_card = card * False
    for ix, number in enumerate(numbers):
        marked_card += (card == number)

        if has_won(marked_card):
            return ix, np.sum((1 - marked_card) * card) * number

    return None, None



numbers = [62, 55, 98, 93, 48, 28, 82, 78, 19, 96, 31, 42, 76, 25, 34, 4, 18, 80, 66, 6, 14, 17, 57,
54, 90, 27, 40, 47, 9, 36, 97, 56, 87, 61, 91, 1, 64, 71, 99, 38, 70, 5, 94, 85, 49, 59, 69, 26, 21,
60, 0, 79, 2, 95, 11, 84, 20, 24, 8, 51, 46, 44, 88, 22, 16, 53, 7, 32, 89, 67, 15, 86, 41, 92, 10, 
77, 68, 63, 43, 75, 33, 30, 81, 37, 83, 3, 39, 65, 12, 45, 23, 73, 72, 29, 52, 58, 35, 50, 13, 74]

dat = pd.read_table('day-4.txt', header=None)
dat = np.array([format(x) for x in dat[0].values])
dat = dat.reshape([int(np.prod(dat.shape)/25), 5, 5])

best_index = 10000
best_score = None
best_card = None

worst_index = -1
worst_score = None
worst_card = None

for icard, card in enumerate(dat):
    ix, score = bingo_test(card, numbers=numbers)
    if ix < best_index:
        best_score = score
        best_index = ix
        best_card = card

    if ix > worst_index:
        worst_score = score
        worst_index = ix
        worst_card = card

pass
