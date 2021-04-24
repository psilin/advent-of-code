
import re


def get_processor():
    mem = re.compile('^mem\[(\d+)\] = (\d+)')
    mask = re.compile('^mask = (\w+)')
    def process_line(line):
        nonlocal mem
        nonlocal mask
        m = mem.match(line)
        if m is not None:
            return [0, int(m.group(1)), int(m.group(2))]

        m = mask.match(line)
        if m is not None:
            s = str(m.group(1))
            multip = int(s.replace('1', '0').replace('X', '1'), 2)
            addit = int(s.replace('X', '0'), 2)
            return [1, multip, addit, s.replace('1', '0').replace('X', '1')]
    return process_line


def parse_input():
    process_line = get_processor()
    data = []
    with open('./input.txt', 'r') as fh:
        for line in fh:
            data.append(process_line(line))
    return data


def process_mem(data):
    memory = dict()
    multip = None
    addit = None

    for d in data:
        if d[0] == 1:
            multip = d[1]
            addit = d[2]
        elif d[0] == 0:
            memory[d[1]] = (d[2] & multip) + addit
    
    return sum(memory.values())


def process_mem_adv(data):
    memory = dict()
    multip = None
    addit = None
    mem_lst = []

    for d in data:
        if d[0] == 1:
            multip = d[1]
            addit = d[2]
            one_pos = []
            mem_lst = []
            for i in range(len(d[3])):
                if d[3][i] == '1':
                    one_pos.append(len(d[3]) - 1 - i)
            for i in range(2**d[3].count('1')):
                mem = 0
                for j in range(d[3].count('1')):
                    mem += ((i & (1 << j)) >> j) * (2**one_pos[j])
                mem_lst.append(mem)

        elif d[0] == 0:
            mem_base = (d[1] | addit) & ~multip
            for m in mem_lst:
                memory[mem_base + m] = d[2]

    return sum(memory.values())


if __name__ == '__main__':
    data = parse_input()
    print(process_mem(data))
    print(process_mem_adv(data))
