
from enum import IntEnum


def parse_input():
    data = []
    with open('./input.txt', 'r') as fh:
        for line in fh:
            line = line.strip('\n')
            data.append((line[0], int(line[1:])))
    return data


class Direction(IntEnum):
    E = 0,
    S = 1,
    W = 2,
    N = 3


class Ship:
    def __init__(self):
        self.ns = 0
        self.ew = 0
        self.dir = Direction.E

    def __repr__(self):
        return f'({self.dir.name}, {self.ns}, {self.ew})'

    def apply(self, d):
        if d[0] in ('E', 'S', 'W', 'N'):
            self._move_direction(d)
        elif d[0] in ('L', 'R'):
            self._change_direction(d)
        elif d[0] == 'F':
            self._move_forward(d)

    def _change_direction(self, d):
        if d[0] == 'R':
            val = d[1] // 90
        else:
            val = len(Direction) - d[1] // 90
        self.dir = Direction((self.dir.value + val) % len(Direction))

    def _move_forward(self, d):
        if self.dir == Direction.E:
            self.ew += d[1] 
        elif self.dir == Direction.W:
            self.ew -= d[1] 
        elif self.dir == Direction.N:
            self.ns += d[1] 
        elif self.dir == Direction.S:
            self.ns -= d[1]

    def _move_direction(self, d):
        if d[0] == Direction.E.name:
            self.ew += d[1] 
        elif d[0] == Direction.W.name:
            self.ew -= d[1] 
        elif d[0] == Direction.N.name:
            self.ns += d[1] 
        elif d[0] == Direction.S.name:
            self.ns -= d[1]


class ShipWithWaypoint:
    def __init__(self):
        self.ns = 0
        self.ew = 0
        self.nsWP = 1
        self.ewWP = 10

    def __repr__(self):
        return f'S ({self.ns}, {self.ew}) WP ({self.nsWP}, {self.ewWP})'

    def apply(self, d):
        if d[0] in ('E', 'S', 'W', 'N'):
            self._move_direction(d)
        elif d[0] in ('L', 'R'):
            self._change_direction(d)
        elif d[0] == 'F':
            self._move_forward(d)

    def _change_direction(self, d):
        if d[1] == 180:
            self.nsWP, self.ewWP = -self.nsWP, -self.ewWP 
        elif d[0] == 'R' and d[1] == 90 or d[0] == 'L' and d[1] == 270:
            self.nsWP, self.ewWP = -self.ewWP, self.nsWP
        elif d[0] == 'L' and d[1] == 90 or d[0] == 'R' and d[1] == 270:
            self.nsWP, self.ewWP = self.ewWP, -self.nsWP 

    def _move_forward(self, d):
        self.ns += self.nsWP * d[1]
        self.ew += self.ewWP * d[1] 

    def _move_direction(self, d):
        if d[0] == Direction.E.name:
            self.ewWP += d[1] 
        elif d[0] == Direction.W.name:
            self.ewWP -= d[1] 
        elif d[0] == Direction.N.name:
            self.nsWP += d[1] 
        elif d[0] == Direction.S.name:
            self.nsWP -= d[1]


if __name__ == '__main__':
    data = parse_input()
    ship = Ship()
    shipWP = ShipWithWaypoint()
    for d in data:
        ship.apply(d)
        shipWP.apply(d)
    print(abs(ship.ew) + abs(ship.ns))
    print(abs(shipWP.ew) + abs(shipWP.ns))

