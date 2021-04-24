
from string import ascii_lowercase
from copy import deepcopy

class Group:
    def __init__(self):
        self.reset()

    def __repr__(self):
        return f't {self.total} v {self.votes}\n'

    def add_string(self, mystring):
        for c in mystring:
            self.votes[c] += 1
        self.total += 1

    def reset(self):
        self.total = 0

        self.votes = {}
        for c in ascii_lowercase:
            self.votes[c] = 0

    def votes_every(self):
        cnt = 0
        for c in ascii_lowercase:
            if self.votes[c] == self.total:
                cnt += 1
        return cnt

    def votes_any(self):
        cnt = 0
        for c in ascii_lowercase:
            if self.votes[c] > 0:
                cnt += 1
        return cnt


def parse_input():
    data = []
    with open('./input.txt', 'r') as fh:
        grp = Group()
        for line in fh:
            line = line.strip('\n')
            if len(line) == 0:
                data.append(deepcopy(grp))
                grp.reset()
            else:
                grp.add_string(line)
        
        data.append(grp)
        return data


if __name__ == '__main__':
    data = parse_input()
    print(sum([x.votes_any() for x in data]))
    print(sum([x.votes_every() for x in data]))

