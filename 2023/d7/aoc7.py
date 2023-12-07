# aoc 7
from collections import Counter


SORT_ORDER = {x: idx for idx, x in enumerate("J23456789TQKA")}
hands = [line.split(" ") for line in open('aoc7.input').readlines()]


def hand_type(hand: str) -> int:
    handset = Counter(hand).most_common()
    handset_noj = Counter(hand.replace("J", "")).most_common()
    jokers = hand.count("J")
    if len(handset) == 1 or (handset_noj[0][1] + jokers == 5):
        return 7  # 5k ###
    if (
        handset[0][1] == 4
        or (handset_noj[0][1] + jokers == 4)
    ):
        return 6  # 4k ###
    if (handset[0][1] == 3 and handset[1][1] == 2) or (
        handset_noj[0][1] == 2 and handset_noj[1][1] == 2 and jokers == 1
    ):
        return 5  # fh ###
    if (
        (handset_noj[0][1] == 3 and handset_noj[1][1] == 1)
        or (handset_noj[0][1] == 2 and handset_noj[1][1] == 1 and jokers == 1)
        or jokers == 2
    ):
        return 4  # 3k
    if handset_noj[0][1] == 2 and handset_noj[1][1] == 2:
        return 3  # 2p ##
    if (handset_noj[0][1] == 2 and handset_noj[1][1] == 1) or jokers == 1:
        return 2  # 1p ##
    return 1


bids_sorted = sorted(
    [
        ([hand_type(hand)] + [SORT_ORDER[card] for card in hand], bid)
        for hand, bid in hands
    ],
    key=lambda x: x[0],
)

print(sum([(idx + 1) * int(x[1]) for idx, x in enumerate(bids_sorted)]))
