
def parse_data():
    with open('./input.txt', 'r') as fh:
        arrival = int(fh.readline().strip('\n'))
        buses = fh.readline().strip('\n').split(',')
    return arrival, buses


def process_fastest(arrival, buses):
    res = []
    for bus in buses:
        if bus != 'x':
            num = int(bus)
            d = arrival % num
            if d > 0:
                d = num - d
            res.append([d, num])
    res.sort()
    return res


def chinese_theorem(buses):
    data = []
    for i in range(len(buses)):
        if buses[i] != 'x':
            b = int(buses[i])
            data.append([b, (b - i) % b])

    M = 1
    for d in data:
        M *= d[0]
    
    S = 0
    for d in data:
        S += d[1] * pow(M // d[0], d[0] - 1)
    return S % M


if __name__ == '__main__':
    arrival, buses = parse_data()
    res = process_fastest(arrival, buses)
    print(res[0][0] * res[0][1])
    print(chinese_theorem(buses))
