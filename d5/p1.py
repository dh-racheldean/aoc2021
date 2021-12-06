class Matrix:
    maxx = 0
    maxy = 0
    matrix = {}

    def update_matrix(self, x,y):
        self.maxx = max(x, self.maxx)
        self.maxy = max(y, self.maxy)
        if x not in self.matrix:
            self.matrix[x] = {y: 1}
        else:
            if y not in self.matrix[x]:
                self.matrix[x][y] = 1
            else:
                self.matrix[x][y] += 1

    @staticmethod
    def parse_input(line):
        return [[int(j) for j in x.split(',')] for x in line.strip().split(' -> ')]

    def add_line(self, c):
        st, en = c
        if st[0] == en[0] or st[1] == en[1]:
            for x in range(min(st[0], en[0]), max(st[0], en[0])+1):
                for y in range(min(st[1], en[1]), max(st[1], en[1])+1):
                    self.update_matrix(x, y)
        if abs(st[0]-en[0]) == abs(st[1]-en[1]):
            for q in range(abs(st[1]-en[1])+1):
                a = st[0] + (q * (-1 if (st[0] > en[0]) else 1))
                b = st[1] + (q * (-1 if (st[1] > en[1]) else 1))
                self.update_matrix(a,b)

    def dump_matrix(self):
        print(self.maxx, self.maxy, self.matrix)
        for x in range(self.maxx+1):
            if x in self.matrix:
                line = [str(self.matrix[x].get(y, '.')) for y in range(self.maxy+1)]
                print(''.join(line))
            else:
                print('.'*self.maxy)

    def __init__(self, path):
        for line in open(path):
            coords = self.parse_input(line)
            self.add_line(coords)


bob = Matrix('input.txt')
bob.dump_matrix()

tot = 0
for x, ys in bob.matrix.items():
    for y, val in ys.items():
        if val>1:
            tot=tot+1
print(tot)