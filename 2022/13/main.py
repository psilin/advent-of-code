
import ast
import functools


def parse():
    pairs = []
    with open("./input.txt", "r") as fh:
        left = None
        right = None
        for line in fh:
            line = line.rstrip("\n")
            if left is None:
                left = ast.literal_eval(line)
            elif right is None:
                right = ast.literal_eval(line)
            else:
                pairs.append([left, right])
                left = None
                right = None
        pairs.append([left, right])
    return pairs


def compare(left, right):
    for i in range(min(len(left), len(right))):
        if isinstance(left[i], int) and isinstance(right[i], int):
            if left[i] < right[i]:
                return -1
            elif left[i] > right[i]:
                return 1
        elif isinstance(left[i], int):
            res = compare([left[i], ], right[i])
            if res != 0:
                return res
        elif isinstance(right[i], int):
            res = compare(left[i], [right[i], ])
            if res != 0:
                return res
        else:
            res = compare(left[i], right[i])
            if res != 0:
                return res
    if len(left) > len(right):
        return 1
    elif len(left) < len(right):
        return -1
    return 0


def main():
    pairs = parse()
    cnt = 0
    num = 0
    for p in pairs:
        num += 1
        if compare(p[0], p[1]) < 0:
            cnt += num
    print(cnt)

    pairs.append([[[2,],],[[6,],]])
    flat = [item for p in pairs for item in p]
    flat = sorted(flat, key=functools.cmp_to_key(compare))
    
    mult = 1
    for i, f in enumerate(flat):
        if f == [[2,],] or f == [[6,],]:
            mult *= (i + 1)
    print(mult)


if __name__ == "__main__":
    main()
