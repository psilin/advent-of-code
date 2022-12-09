
import math


def parse():
    steps = []
    with open("./input.txt", "r") as fh:
        for line in fh:
            lst = line.rstrip("\n").split(" ")
            steps.append((lst[0], int(lst[1])))
    return steps


def move(head, dir):
    if dir == "U":
        head[1] += 1
    elif dir == "D":
        head[1] -= 1
    elif dir == "L":
        head[0] -= 1
    elif dir == "R":
        head[0] += 1
    return head


sign = lambda x: int(math.copysign(1, x))


def react(head, tail):
    if abs(head[0] - tail[0]) <= 1 and abs(head[1] - tail[1]) <= 1:
        pass
    elif head[0] == tail[0]:
        tail[1] += sign(head[1] - tail[1])
    elif head[1] == tail[1]:
        tail[0] += sign(head[0] - tail[0])
    else:
        tail[0] += sign(head[0] - tail[0])
        tail[1] += sign(head[1] - tail[1])
    return tail


def compute(steps):
    head = [0, 0]
    tail = [0, 0]
    tail_visits = set()
    for s in steps:
        for _ in range(s[1]):
            head = move(head, s[0])
            tail = react(head, tail)
            tail_visits.add(tuple(tail))
    print(len(tail_visits))


def compute_long(steps):
    head = [0, 0]
    tail = [[0, 0],[0, 0],[0, 0],[0, 0],[0, 0],[0, 0],[0, 0],[0, 0],[0, 0]]
    tail_visits = set()
    for s in steps:
        for _ in range(s[1]):
            head = move(head, s[0])
            tail[0] = react(head, tail[0])
            for i in range(1,9):
                tail[i] = react(tail[i-1], tail[i])
            tail_visits.add(tuple(tail[8]))
    print(len(tail_visits))


def main():
    steps = parse()
    compute(steps)
    compute_long(steps)


if __name__ == "__main__":
    main()
