
def parse():
    draws = []
    with open("./input.txt", "r") as fh:
        for line in fh:
            line = line.rstrip("\n")
            draws.append(line.split(" "))
    return draws


def compute_strategy1(draws):
    summ = 0
    for d in draws:
        if d[1] == "X":
            summ += 1
            if d[0] == "A":
                summ += 3
            elif d[0] == "C":
                summ += 6
        elif d[1] == "Y":
            summ += 2
            if d[0] == "B":
                summ += 3
            elif d[0] == "A":
                summ += 6
        elif d[1] == "Z":
            summ += 3
            if d[0] == "C":
                summ += 3
            elif d[0] == "B":
                summ += 6
    print(summ)


def compute_strategy2(draws):
    summ = 0
    for d in draws:
        if d[1] == "X":
            summ += 0
            if d[0] == "A":
                summ += 3
            elif d[0] == "B":
                summ += 1
            elif d[0] == "C":
                summ += 2
        elif d[1] == "Y":
            summ += 3
            if d[0] == "A":
                summ += 1
            elif d[0] == "B":
                summ += 2
            elif d[0] == "C":
                summ += 3
        elif d[1] == "Z":
            summ += 6
            if d[0] == "A":
                summ += 2
            elif d[0] == "B":
                summ += 3
            elif d[0] == "C":
                summ += 1
    print(summ)


def main():
    draws = parse()
    compute_strategy1(draws)
    compute_strategy2(draws)


if __name__ == "__main__":
    main()   
