import pandas as pd
inp = [x.strip() for x in open('input3.txt').readlines()]
df1 = pd.DataFrame([[int(x) for x in y ] for y in inp])
df2 = df1.copy()
def x(d, c, f): return d[d[c]==((f(d[c].sum()/len(d)))*1)]
def bc2i(col): return int("".join([str(x) for x in col]),2)
for c in range(len(inp[0])):
    if len(df1)>1: df1 = x(df1, c, lambda x: x>=0.5)
    if len(df2)>1: df2 = x(df2, c, lambda x: x<0.5)
bc2i(df1.iloc[0])*bc2i(df2.iloc[0])
