import pandas as pd
inp = [x.strip() for x in open('input3.txt').readlines()]
h = int("".join(((pd.DataFrame(list(map(lambda x: list(map(int, list(x))), inp))).sum()/len(inp)>0.5)*1).astype(str)),2)
h * (~h & ((1 << len(inp[0])) - 1))

