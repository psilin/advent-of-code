
def parse():
    with open("./input.txt", "r") as fh:
        res = fh.read()
        return res.rstrip("\n")


def check(lst, num):
    return len(set(lst)) == num


def get_first(string, num):
    lst = []
    for i, ch in enumerate(string):
        lst.append(ch)
        if len(lst) > num:
            lst.pop(0)
        if check(lst, num) is True:
            return i + 1
    return 0


def main():
    string = parse()
    print(get_first(string, 4))
    print(get_first(string, 14))


if __name__ == "__main__":
    main()
