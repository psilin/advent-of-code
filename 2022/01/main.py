

def parse():
    elves = []
    with open("./input.txt", "r") as fh:
        elf = []
        for line in fh:
            line = line.rstrip("\n")
            if len(line) == 0:
                elves.append(elf)
                elf = []
            else:
                elf.append(int(line))
    elves.append(elf)
    return elves    

def max_elf(elves):
    maxx = 0
    max_num = 0
    for n, e in enumerate(elves):
        s = sum(e)
        if s > maxx:
            maxx = s
            max_num = n
    return maxx, max_num

def main():
    elves = parse()
    maxers = []
    for _ in range(3):
        maxx, max_num = max_elf(elves)
        print(maxx, max_num)
        maxers.append(maxx)
        del elves[max_num]

    print(sum(maxers))

if __name__ == "__main__":
    main()