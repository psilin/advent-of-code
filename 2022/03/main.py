
def parse():
    backpacks = []
    with open("./input.txt", "r") as fh:
        for line in fh:
            line = line.rstrip("\n")
            backpacks.append([set(line[:len(line)//2]),set(line[len(line)//2:])])
        return backpacks


def char_to_prio(c):
    if ord(c) > ord('Z'):
        prio = ord(c) - ord('a') + 1
    else:
        prio = ord(c) - ord('A') + 27
    return prio


def compute_priority(backpacks):
    summ = 0
    for b in backpacks:
        for c in b[0].intersection(b[1]):
            summ += char_to_prio(c)
    print(summ)


def compute_badges(backpacks):
    summ = 0
    while len(backpacks) > 0:
        e1 = backpacks.pop(0)
        e2 = backpacks.pop(0)
        e3 = backpacks.pop(0)

        s1 = e1[0].union(e1[1])
        s2 = e2[0].union(e2[1])
        s3 = e3[0].union(e3[1])

        s = s1.intersection(s2).intersection(s3)
        for c in s:
            summ += char_to_prio(c)
    print(summ)


def main():
    backpacks = parse()
    compute_priority(backpacks)
    compute_badges(backpacks)


if __name__ == "__main__":
    main()
