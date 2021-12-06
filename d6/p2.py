from collections import Counter

days = 256
fishes = dict(Counter(list(map(int, open("input.txt").readlines()[0].strip().split(',')))))
for x in range(days):
    fishes[9] = fishes.get(0, 0)
    fishes[7] = fishes.get(7, 0)+fishes.get(0, 0)
    for y in range(9):
        fishes[y] = fishes.get(y+1, 0)
    fishes[9] = 0
print(sum([y for _, y in fishes.items()]))
