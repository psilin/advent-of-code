
def process(num):
    lst = [15,12,0,14,3,1]
    for _ in range(len(lst), num):
        tmp_lst = lst[:len(lst)-1]
        if lst[-1] in tmp_lst:
            lst.append(1 + tmp_lst[::-1].index(lst[-1]))
        else:
            lst.append(0)
    return lst


def process_adv(num):
    lst = [15,12,0,14,3,1]
    mem = {15: 0, 12: 1, 0: 2, 14: 3, 3: 4}
    last = 1
    for i in range(len(lst), num):
        pos = mem.get(last, None)
        if pos is None:
            mem[last] = i - 1
            last = 0
        else:
            mem[last] = i - 1
            last = i - 1 - pos
    return last  


if __name__ == '__main__':
    res = process(2020)
    print(res)
    res = process_adv(30000000)
    print(res)