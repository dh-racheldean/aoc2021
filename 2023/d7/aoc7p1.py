# aoc 7
from collections import Counter
import pprint
SORT_ORDER = {x: idx for idx, x in enumerate("J23456789TQKA")}
src = """32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483"""


def hand_type(hand: str) -> int:
    handset = Counter(hand).most_common()
    jokers = hand.count("J")
    if len(handset) == 1 or (handset[0][0] != "J" and handset[0][1] + jokers == 5):
        return 7
    if handset[0][1] == 4:
        return 6
    if handset[0][1] == 3 and handset[1][1] == 2:
        return 5
    if handset[0][1] == 3 and handset[1][1] == 1:
        return 4
    if handset[0][1] == 2 and handset[1][1] == 2:
        return 3
    if handset[0][1] == 2 and handset[1][1] == 1:
        return 2
    else:
        return 1


hands = [a.split(" ") for a in src.split("\n")]
pprint([(hand_type(hand), hand) for hand in hands])
bids_sorted = sorted([
    ([hand_type(hand)] + [SORT_ORDER[card] for card in hand], bid)
    for hand, bid in hands
], key=lambda x: x[0])

print(sum([(idx + 1) * int(x[1]) for idx, x in enumerate(bids_sorted)]))
