
def prepare_initial_state():
    lst = []
    lst.append(list("DLJRVGF"))
    lst.append(list("TPMBVHJS"))
    lst.append(list("VHMFDGPC"))
    lst.append(list("MDPNGQ"))
    lst.append(list("JLHNF"))
    lst.append(list("NFVQDGTZ"))
    lst.append(list("FDBL"))
    lst.append(list("MJBSVDN"))
    lst.append(list("GLD"))
    return lst


def parse():
    steps = []
    with open("./input.txt", "r") as fh:
        for line in fh:
            lst = line.rstrip("\n").split(" ")
            if lst[0] == "move":
                steps.append([int(lst[1]), int(lst[3]), int(lst[5])])
    return steps


def compute(state, steps):
    for s in steps:
        for _ in range(s[0]):
            e = state[s[1]-1].pop(-1)
            state[s[2]-1].append(e)


def compute_advanced(state, steps):
    for s in steps:
        lst = []
        for _ in range(s[0]):
            lst.append(state[s[1]-1].pop(-1))
        for _ in range(s[0]):
            state[s[2]-1].append(lst.pop(-1))


def main():
    steps = parse()

    state = prepare_initial_state()
    compute(state, steps)
    print(state)

    state = prepare_initial_state()
    compute_advanced(state, steps)
    print(state)


if __name__ == "__main__":
    main()
