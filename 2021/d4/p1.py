class BingoBoard():
    def __init__(self, board):
        self.rows = [set(row) for row in board]
        self.cols = [set(row) for row in [*zip(*board)]]
        self.allnums = set().union(*board)

    def checknums(self, nums):
        for x in range(len(nums)):
            if any( [(row - set(nums[:x])) == set() for row in self.rows]):
                break
            if any( [(col - set(nums[:x])) == set() for col in self.cols]):
                break
        return x

    def score(self, nums):
        return sum(list(self.allnums - set(nums))) * nums[-1]

class Bingo():
    def __init__(self, path, size):
        self.nums = None
        self.size = size
        self._parse(path)

    def _parse(self, path):
        # reads list of lines, returns set of sets
        lines = [list(map(int, x.strip().replace(',', ' ').split())) for x in open(path).readlines() if len(x.strip())>0]
        self.nums = lines[0]
        numboards = ((len(lines)-1)//self.size)
        self.boards = [lines[x:x+self.size] for x in range(1, numboards*self.size, self.size)]

    def get_scores(self):
        results=[]
        for board in self.boards:
            thisboard = BingoBoard(board)
            num = thisboard.checknums(self.nums)
            results.append([num, thisboard.score(self.nums[:num])])
        return sorted(results, key=lambda x: x[0])

b = Bingo("input.txt", 5)
results = b.get_scores()
print(results[0], results[-1])
