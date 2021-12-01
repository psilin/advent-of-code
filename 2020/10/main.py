
import copy


def parse_input():
    res = [0, ]
    with open('./input.txt', 'r') as fh:
        for line in fh:
            line = line.strip('\n')
            res.append(int(line))
    res.sort()
    res.append(res[-1] + 3)
    return res


def count_gaps(arr):
    gap1 = 0
    gap3 = 0
    for i in range(len(arr)-1):
        d = arr[i + 1] - arr[i]
        if d == 1:
            gap1 += 1
        elif d == 3:
            gap3 += 1
    return gap1, gap3, gap1 * gap3


def count_rearrangements(arr):
    res2d = []
    cur = []
    for i in range(len(arr)-1):
        cur.append(arr[i])
        if arr[i + 1] - arr[i] == 3:
            res2d.append(copy.deepcopy(cur))
            cur = []

    # dirty sortcut using the nature of data
    cnt = 1
    for ar in res2d:
        l = len(ar)
        if l == 3:
            cnt *= 2
        elif l == 4:
            cnt *= 4
        elif l == 5:    
            cnt *= 7
    return cnt, res2d


if __name__ == '__main__':
    res = parse_input()
    print(count_gaps(res))
    print(count_rearrangements(res))
