mat = [[int(z) for z in x.strip()] for x in open('input.txt').readlines()]
w = len(mat[0])
h = len(mat)
low = 0
for x in range(h):
    for y in range(w):
        if ((x == 0 or mat[x][y] < mat[x-1][y]) and
            (x == h-1 or mat[x][y] < mat[x+1][y]) and
            (y == 0 or mat[x][y] < mat[x][y-1]) and
            (y == w-1 or mat[x][y] < mat[x][y+1])):
            low+=mat[x][y]+1
print(low)