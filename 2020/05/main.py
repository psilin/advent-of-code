
def parse_input():
    data = []
    with open('./input.txt', 'r') as fh:
        for line in fh:
            line.strip('\n')
            line = line.replace('B', '1').replace('F', '0').replace('R', '1').replace('L', '0')
            data.append(int(line, 2))
    return data


def process(data):
    data.sort()
    cur = data[0]
    for i in range(1,len(data)):
        if data[i] - cur == 2:
            return cur + 1, data[len(data)-1]
        cur = data[i]


if __name__ == '__main__':
    data = parse_input()
    print(process(data))
    