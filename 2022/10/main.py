
CYCLES = (20, 60, 100, 140, 180, 220)


def parse():
    steps = []
    with open("./input.txt", "r") as fh:
        for line in fh:
            lst = line.rstrip("\n").split(" ")
            if lst[0] == "noop":
                steps.append(0)
            elif lst[0] == "addx":
                steps.append(int(lst[1]))
    return steps


def compute_cycles(steps):
    signal = 1
    cycles = []
    for s in steps:
        if s == 0:
            cycles.append(signal)
        else:
            cycles.append(signal)
            cycles.append(signal)
            signal += s

    return cycles


def compute_signal(cycles):
    summ = 0
    for c in CYCLES:
        summ += cycles[c - 1] * c
    print(summ)


def compute_pixels(cycles):
    pixels = []
    for i, c in enumerate(cycles):
        j = i % 40
        if abs(c - j) <= 1:
            pixels.append("#")
        else:
            pixels.append(".")

    for i, p in enumerate(pixels):
        if (i % 40) == 0:
            print()
        print(p, end="")
    print()


def main():
    steps = parse()
    cycles = compute_cycles(steps)
    print(cycles)
    compute_signal(cycles)
    compute_pixels(cycles)


if __name__ == "__main__":
    main()
