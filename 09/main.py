
import copy

def parse_input():
    data = []
    with open('./input.txt', 'r') as fh:
        for line in fh:
            line = line.strip('\n')
            data.append(int(line))
    return data


def process_numbers(data):
    for i in range(25, len(data)):
        found = False
        for j in range(i - 25, i):
            for k in range(i - 25, i):
                if j != k and data[j] + data[k] == data[i]:
                    found = True
                    break
            if found is True:
                break

        if found is False:
            return data[i]


def find_contiguous_sum(data, num):
    for i in range(len(data)):
        for j in range(len(data)):
            if i < j and num == sum(data[i:j+1]):
                return min(data[i:j+1]) + max(data[i:j+1])


if __name__ == '__main__':
    data = parse_input()
    res = process_numbers(data)
    print(res)
    print(find_contiguous_sum(data, res))