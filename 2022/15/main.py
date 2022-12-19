

def parse():
    pairs = []
    with open("./input.txt", "r") as fh:
        for line in fh:
            lst = line.split()
            s = (int(lst[2].rstrip(",").lstrip("x=")), int(lst[3].rstrip(":").lstrip("y=")))
            b = (int(lst[8].rstrip(",").lstrip("x=")), int(lst[9].lstrip("y=")))
            pairs.append((s,b))
    return pairs


def find_row(pairs, rowy):
    covered = set()
    for p in pairs:
        d = abs(p[0][0] - p[1][0]) + abs(p[0][1] - p[1][1])
        a = abs(rowy - p[0][1])
        for x in range(p[0][0] - d, p[0][0] + d + 1, 1):
            if abs(x - p[0][0]) + a <= d:
                    covered.add((x,rowy))
    beacons = {p[1] for p in pairs}
    covered = covered - beacons
    print(len(covered))


def find_point(pairs, r):
    initial = set()
    for p in pairs:
        print(p)
        d = abs(p[0][0] - p[1][0]) + abs(p[0][1] - p[1][1]) + 1
        for x in range(p[0][0] - d, p[0][0] + d + 1, 1):
            y1 = p[0][1] - (d - abs(x - p[0][0]))
            y2 = p[0][1] + (d - abs(x - p[0][0]))
            if (0 <= x <= r) and (0 <= y1 <= r):
                initial.add((x,y1))
            if (0 <= x <= r) and (0 <= y2 <= r):
                initial.add((x,y2))
    print(len(initial))
    for p in pairs:
        print(p)
        d = abs(p[0][0] - p[1][0]) + abs(p[0][1] - p[1][1])
        minus = set()
        for pt in initial:
            if abs(pt[0] - p[0][0]) + abs(pt[1] - p[0][1]) <= d:
                minus.add(pt)
        initial = initial - minus
    print(len(initial))
    print(initial)
    for i in initial:
        print(i[0] * r + i[1])   


def main():
    pairs = parse()
    find_row(pairs, 2000000)
    find_point(pairs, 4000000)


if __name__ == "__main__":
    main()
