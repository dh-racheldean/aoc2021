from collections import Counter
base_map = {
    0: "abcefg",
    1: "cf",
    2: "acdeg",
    3: "acdfg",
    4: "bcdf",
    5: "abdfg",
    6: "abdefg",
    7: "acf",
    8: "abcdefg",
    9: "abcdfg"
}
ns = {}
segs = {}
cnt = 0
for line in open("input.txt"):
    a = line.strip().split()
    clue = [set(x) for x in sorted(a[:10], key=lambda x: len(x))]
    q = a[11:]
    ns[1] = clue[0]
    ns[7] = clue[1]
    ns[4] = clue[2]
    ns[8] = clue[9]
    segs['a'], = ns[7]-ns[1]
    for x in clue[6:9]:
        if len(x-clue[2]-clue[1]) == 1:
            ns[9] = x
            segs['g'], = ns[9] - ns[7] - ns[4]
            break
    counts = dict(Counter([y for x in clue for y in x]))
    counts.pop(segs['a'])
    counts.pop(segs['g'])
    def bycnt(q):
        return [k for k, v in counts.items() if v == q][0]
    segs['e'] = bycnt(4)
    segs['b'] = bycnt(6)
    segs['d'] = bycnt(7)
    segs['c'] = bycnt(8)
    segs['f'] = bycnt(9)
    fixed_map = {"".join(sorted(map(lambda x: segs[x], set(ss)))):n for n, ss in base_map.items()}
    cnt+=sum(([10**(3-i)*fixed_map["".join(sorted(x))] for i, x in enumerate(q)]))
print(cnt)
