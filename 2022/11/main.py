
class Monkey:
    def __init__(self, items, op, test):
        self.items = items
        self.op = op
        self.test = test
        self.inspect = 0


def create_initial():
    monkeys = []
    monkey0 = Monkey(
        items=[71, 86],
        op=lambda x: x * 13,
        test=lambda x: 6 if (x % 19) == 0 else 7)
    monkeys.append(monkey0)
    monkey1 = Monkey(
        items=[66, 50, 90, 53, 88, 85],
        op=lambda x: x + 3,
        test=lambda x: 5 if (x % 2) == 0 else 4)
    monkeys.append(monkey1)
    monkey2 = Monkey(
        items=[97, 54, 89, 62, 84, 80, 63],
        op=lambda x: x + 6,
        test=lambda x: 4 if (x % 13) == 0 else 1)
    monkeys.append(monkey2)
    monkey3 = Monkey(
        items=[82, 97, 56, 92],
        op=lambda x: x + 2,
        test=lambda x: 6 if (x % 5) == 0 else 0)
    monkeys.append(monkey3)    
    monkey4 = Monkey(
        items=[50, 99, 67, 61, 86],
        op=lambda x: x * x,
        test=lambda x: 5 if (x % 7) == 0 else 3)
    monkeys.append(monkey4)
    monkey5 = Monkey(
        items=[61, 66, 72, 55, 64, 53, 72, 63],
        op=lambda x: x + 4,
        test=lambda x: 3 if (x % 11) == 0 else 0)
    monkeys.append(monkey5)
    monkey6 = Monkey(
        items=[59, 79, 63],
        op=lambda x: x * 7,
        test=lambda x: 2 if (x % 17) == 0 else 7)
    monkeys.append(monkey6)
    monkey7 = Monkey(
        items=[55,],
        op=lambda x: x + 7,
        test=lambda x: 2 if (x % 3) == 0 else 1)
    monkeys.append(monkey7)
    return monkeys


def play(monkeys, rounds):
    for i in range(rounds):
        for m in monkeys:
            while len(m.items) > 0:
                m.inspect += 1
                stress = m.op(m.items.pop(0)) // 3
                monkeys[m.test(stress)].items.append(stress)

    inspects = []
    for m in monkeys:
        inspects.append(m.inspect)
    inspects.sort(reverse=True)
    print(inspects)
    print(inspects[0] * inspects[1])


def play_stress(monkeys, rounds):
    N = 19 * 2 * 13 * 5 * 7 * 11 * 17 * 3
    for i in range(rounds):
        for m in monkeys:
            while len(m.items) > 0:
                m.inspect += 1
                stress = m.op(m.items.pop(0)) % N
                monkeys[m.test(stress)].items.append(stress)
                
    inspects = []
    for m in monkeys:
        inspects.append(m.inspect)
    inspects.sort(reverse=True)
    print(inspects)
    print(inspects[0] * inspects[1])


def main():
    monkeys = create_initial()
    play(monkeys, 20)

    monkeys = create_initial()
    play_stress(monkeys, 10000)


if __name__ == "__main__":
    main()
