crabs = [int(x) for x in open('input.txt').read().strip().split(',')]
print(min([sum([(abs(y-x)*(abs(y-x)+1))/2 for y in crabs]) for x in range(min(crabs), max(crabs))]))
