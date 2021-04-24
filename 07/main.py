
from collections import deque


def parse_input():
    data = {}
    with open('./input.txt', 'r') as fh:
        for line in fh:
            cnt = line.count(',')
            
            l = line.split(' ')
            if l[4] == 'no':
                data[l[0]+' '+l[1]] = []
            else:    
                data[l[0]+' '+l[1]] = [(int(l[4]), l[5]+' '+l[6]),]
            
            if cnt > 0:
                for i in range(cnt):
                    data[l[0]+' '+l[1]].append((int(l[8 + i * 4]), l[8 + i * 4 + 1]+' '+l[8 + i * 4 + 2]))
    return data


def count_contained(data, color):
    res = set()
    dq = deque()
    dq.append(color)
    while len(dq) > 0:
        clr = dq.popleft()
        for k, v in data.items():
            for vv in v:
                if vv[1] == clr:
                    dq.append(k)
                    res.add(k)
                    break
    return len(res)


def count_contains_tree(data, color):
    g_count = 0

    def count_recursive(clr, number):
        for bag in data[clr]:
            nonlocal g_count
            g_count += number * bag[0]
            count_recursive(bag[1], number * bag[0])
    
    count_recursive(color, 1)
    return g_count


if __name__ == '__main__':
    data = parse_input()
    print(count_contained(data, 'shiny gold'))
    print(count_contains_tree(data, 'shiny gold'))
