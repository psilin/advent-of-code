
NUMBERS = ("one", "two", "three", "four", "five", "six", "seven", "eight", "nine")


def parse():
    lines = []
    with open("./input.txt", "r") as fh:
        for line in fh:
            lines.append(line.rstrip('\n'))
    return lines


def process_line(line):
    first = None
    last = None
    for c in line:
        if str(c).isdigit() is True:
            if first is None:
                first = int(c)
            last = int(c)
    return 10 * first + last


def process_line_advanced(line):
    first = None
    last = None
    i = 0
    while i < len(line):
        c = line[i]
        if str(c).isdigit() is True:
            if first is None:
                first = int(c)
            last = int(c)
        else:
            for j in range(len(NUMBERS)):
                if NUMBERS[j] == line[i: min(len(line), i + len(NUMBERS[j]))]:
                    if first is None:
                        first = j + 1
                    last = j + 1  
                    break
        i += 1
    return 10 * first + last


def main():
    lines = parse()
    print(sum([process_line(l) for l in lines]))
    print(sum([process_line_advanced(l) for l in lines]))


if __name__ == "__main__":
    main()
