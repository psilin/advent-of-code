import re


def parse():
    pairs = []
    with open("./input.txt", "r") as fh:
        for line in fh:
            coords = re.split(",|-", line.rstrip("\n"))
            coords = [int(i) for i in coords]
            pairs.append(coords)
    return pairs


def compute_inclusive(pairs):
    count = 0
    for p in pairs:
        if (p[0] <= p[2] and p[3] <= p[1]) or (p[2] <= p[0] and p[1] <= p[3]):
            count += 1
    print(count)


def compute_overlap(pairs):
    count = 0
    for p in pairs:
        if p[2] <= p[1] and p[0] <= p[3]:
            count += 1
    print(count)


def main():
    pairs = parse()
    compute_inclusive(pairs)
    compute_overlap(pairs)


if __name__ == "__main__":
    main()
