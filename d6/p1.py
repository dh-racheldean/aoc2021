class Fish:
    def __init__(self, state = 8):
        self.state = state

    def update(self):
        # define daily rules
        #Each day, a 0 becomes a 6 and adds a new 8 to the end of the list, while each other number decreases by 1 if it was present at the start of the day.
        if self.state == 0:
            self.state = 6
            return Fish()
        else:
            self.state = self.state - 1

    def __str__(self):
        return str(self.state)


class School:
    def __init__(self, filename):
        self.initial_states = self._parse(filename)
        self.fishes = [Fish(state) for state in self.initial_states]

    def _parse(self, filename):
        return list(map(int, open(filename).readlines()[0].strip().split(',')))

    def evolve(self, days: int):
        for x in range(days):
            newborns = []
            newfish = None
            for fish in self.fishes:
                if newfish:=fish.update():
                    newborns.append(newfish)
            self.fishes += newborns

    def __str__(self):
        return ','.join([str(fish) for fish in self.fishes])


school = School('input.txt')
school.evolve(80)
print(len(school.fishes))
