
def parse_input():
    data = []
    with open('./input.txt', 'r') as fh:
        for line in fh:
            line = line.strip('\n')
            lst = line.split(' ')
            data.append([lst[0], int(lst[1])])
    return data


def calculate_value(data):
    visited = set()
    cnt = 0
    i = 0
    while True:
        if i in visited:
            return False, cnt
        elif i > len(data):
            return False, cnt
        elif i == len(data):
            return True, cnt

        visited.add(i)

        if data[i][0] == 'nop':
            i += 1
        elif data[i][0] == 'acc':
            cnt += data[i][1]
            i += 1
        elif data[i][0] == 'jmp':
            i += data[i][1]


def try_substitutions(data):
    for i in range(len(data)):
        if data[i][0] == 'nop':
            data[i][0] = 'jmp'
            res = calculate_value(data)
            if res[0] is False:
                data[i][0] = 'nop'
            else:
                return res[1]
        elif  data[i][0] == 'jmp':
            data[i][0] = 'nop'
            res = calculate_value(data)
            if res[0] is False:
                data[i][0] = 'jmp'
            else:
                return res[1]

if __name__ == '__main__':
    data = parse_input()
    print(calculate_value(data))
    print(try_substitutions(data))