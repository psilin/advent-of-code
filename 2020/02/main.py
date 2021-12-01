
import re


def get_processor():
    g_prog = re.compile('(\d+)-(\d+) (\w): (\w+)')
    def process_line(line):
        nonlocal g_prog
        m = g_prog.match(line)
        return int(m.group(1)), int(m.group(2)), m.group(3), m.group(4)
    return process_line


def read_input(process_line):
    data = []
    with open('./input.txt', 'r') as fh:
        for line in fh:
            data.append(process_line(line))
    return data 


def check_pass(min_num, max_num, c, line):
    return min_num <= line.count(c) <= max_num

def check_pass2(min_num, max_num, c, line):
    A = (line[min_num - 1] == c)
    B = (line[max_num - 1] == c)
    return ((A and B) is False) and ((A or B) is True)

if __name__ == '__main__':
    processor = get_processor()
    data = read_input(processor)
    n = 0
    n2 = 0
    for d in data:
        if check_pass(*d) is True:
            n = n + 1
        
        if check_pass2(*d) is True:
            n2 = n2 + 1

    print(n, n2)
    
