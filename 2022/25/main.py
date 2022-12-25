
def to_number(line):
    number = 0
    l = len(line)
    for i in range(len(line)):
        power = 5**(l - 1 - i)
        c = line[i]
        if c == "2":
            number += 2 * power
        elif c == "1":
            number += power
        elif c == "-":
            number -= power
        elif c == "=":
            number -= 2 * power
    return number


def to_snafu(number):
    lst = []
    move_up = False
    while number > 0:
        rel = number % 5
        if move_up is True:
            rel += 1
            move_up = False

        if rel == 0:
            lst.append("0")
        elif rel == 1:
            lst.append("1")
        elif rel == 2:
            lst.append("2")
        elif rel == 3:
            lst.append("=")
            move_up = True
        elif rel == 4:
            lst.append("-")
            move_up = True
        elif rel == 5:
            lst.append("0")
            move_up = True
        number = number // 5
    
    if move_up is True:
        lst.append("1")
    
    lst = list(reversed(lst))
    return "".join(lst)


def parse():
    numbers = []
    with open("./input.txt", "r") as fh:
        for line in fh:
            number = to_number(line.rstrip("\n"))
            print(number)
            numbers.append(number)
    return numbers


def main():
    numbers = parse()
    number = sum(numbers)
    print(to_snafu(number))


if __name__ == "__main__":
    main()
