
import copy


class Board:
    def __init__(self):
        self.brd = []

    def __repr__(self):
        return '\n'.join(self.brd)

    def _equals(self, board):
        if len(self.brd) != len(board):
            return False

        for i in range(len(self.brd)):
            if self.brd[i] != board[i]:
                return False

        return True

    def add_line(self, line):
        self.brd.append(line)

    def count_occupied(self):
        cnt = 0
        for i in self.brd:
            cnt += i.count('#')
        return cnt

    def step(self, advanced=False):
        new_brd = []
        for i in range(len(self.brd)):
            cur = ""
            for j in range(len(self.brd[i])):
                if advanced is True:
                    cur += str(self._change_sit_state_advanced(i, j))
                else:
                    cur += str(self._change_sit_state(i, j))
            new_brd.append(copy.deepcopy(cur))
        
        res = self._equals(new_brd)
        self.brd = new_brd
        return res

    def _change_sit_state(self, i, j):
        if self.brd[i][j] == '.':
            return '.'

        # corner sits always occupied if sit is there    
        if i == 0 and j == 0 or\
           i == 0 and j == len(self.brd[i]) - 1 or\
           i == len(self.brd) - 1 and j == 0 or\
           i == len(self.brd) - 1 and j == len(self.brd[i]) - 1:
            return '#'

        nbrs = []
        if i == 0:
            nbrs.append(self.brd[i][j-1])
            nbrs.append(self.brd[i][j+1])
            nbrs.append(self.brd[i+1][j-1])
            nbrs.append(self.brd[i+1][j])
            nbrs.append(self.brd[i+1][j+1])
        elif i == len(self.brd) - 1:
            nbrs.append(self.brd[i-1][j-1])
            nbrs.append(self.brd[i-1][j])
            nbrs.append(self.brd[i-1][j+1])
            nbrs.append(self.brd[i][j-1])
            nbrs.append(self.brd[i][j+1])
        elif j == 0:
            nbrs.append(self.brd[i-1][j])
            nbrs.append(self.brd[i+1][j])
            nbrs.append(self.brd[i-1][j+1])
            nbrs.append(self.brd[i][j+1])
            nbrs.append(self.brd[i+1][j+1])
        elif j == len(self.brd[i]) - 1:
            nbrs.append(self.brd[i-1][j-1])
            nbrs.append(self.brd[i][j-1])
            nbrs.append(self.brd[i+1][j-1])
            nbrs.append(self.brd[i-1][j])
            nbrs.append(self.brd[i+1][j])
        else:
            nbrs.append(self.brd[i-1][j-1])
            nbrs.append(self.brd[i-1][j])
            nbrs.append(self.brd[i-1][j+1])
            nbrs.append(self.brd[i][j-1])
            nbrs.append(self.brd[i][j+1])
            nbrs.append(self.brd[i+1][j-1])
            nbrs.append(self.brd[i+1][j])
            nbrs.append(self.brd[i+1][j+1])

        if self.brd[i][j] == 'L' and nbrs.count('#') == 0:
            return '#'
        elif self.brd[i][j] == '#' and nbrs.count('#') >= 4:
            return 'L'
        else:
            return self.brd[i][j]

    def _change_sit_state_advanced(self, i, j):
        if self.brd[i][j] == '.':
            return '.'

        nbrs = []
        
        cur = '.'
        ki = i
        while ki > 0 and cur == '.':
            ki -= 1
            cur = self.brd[ki][j]
        nbrs.append(cur)

        cur = '.'
        ki = i
        while ki < len(self.brd) - 1 and cur == '.':
            ki += 1
            cur = self.brd[ki][j]
        nbrs.append(cur)

        cur = '.'
        kj = j
        while kj > 0 and cur == '.':
            kj -= 1
            cur = self.brd[i][kj]
        nbrs.append(cur)
        
        cur = '.'
        kj = j
        while kj < len(self.brd[i]) - 1 and cur == '.':
            kj += 1
            cur = self.brd[i][kj]
        nbrs.append(cur)

        cur = '.'
        ki = i
        kj = j
        while ki > 0 and kj > 0 and cur == '.':
            ki -= 1
            kj -= 1
            cur = self.brd[ki][kj]
        nbrs.append(cur)

        cur = '.'
        ki = i
        kj = j
        while ki > 0 and kj < len(self.brd[i]) - 1 and cur == '.':
            ki -= 1
            kj += 1
            cur = self.brd[ki][kj]
        nbrs.append(cur)

        cur = '.'
        ki = i
        kj = j
        while ki < len(self.brd) - 1 and kj > 0 and cur == '.':
            ki += 1
            kj -= 1
            cur = self.brd[ki][kj]
        nbrs.append(cur)

        cur = '.'
        ki = i
        kj = j
        while ki < len(self.brd) - 1 and kj < len(self.brd[i]) - 1 and cur == '.':
            ki += 1
            kj += 1
            cur = self.brd[ki][kj]
        nbrs.append(cur)

        if self.brd[i][j] == 'L' and nbrs.count('#') == 0:
            return '#'
        elif self.brd[i][j] == '#' and nbrs.count('#') >= 5:
            return 'L'
        else:
            return self.brd[i][j]


def parse_input():
    res = Board()
    with open('./input.txt', 'r') as fh:
        for line in fh:
            res.add_line(line.strip('\n'))
    return res


if __name__ == '__main__':
    res = parse_input()
    while res.step() is False:
        print(res.count_occupied())
    print(res.count_occupied())

    print('------------------')
    res = parse_input()
    while res.step(advanced=True) is False:
        print(res.count_occupied())
    print(res.count_occupied())
