from statistics import median
crabs = [int(x) for x in open('input.txt').read().strip().split(',')]
print(sum([abs(x-median(crabs)) for x in crabs]))