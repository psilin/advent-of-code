
def read_input():
    data = []
    with open('./input.txt', 'r') as fh:
        for line in fh:
            data.append(line)
    return data 

def count_trees(data):
    p = 0
    cnt = 0
    length = len(data[0]) - 1

    for s in data:
        if s[p] == '#':
            cnt = cnt + 1
        p = (p + 3) % length
    return cnt

def advanced_count_trees(data, right, down):
    pos = 0
    line_num = 0

    cnt = 0
    length = len(data[0]) - 1

    while line_num < len(data):
        if data[line_num][pos] == '#':
            cnt = cnt + 1 
        pos = (pos + right) % length
        line_num = line_num + down
    return cnt

if __name__ == '__main__':
    data = read_input()
    print(count_trees(data))

    advanced_res = 1
    advanced_res *= advanced_count_trees(data, 1, 1)
    advanced_res *= advanced_count_trees(data, 3, 1)
    advanced_res *= advanced_count_trees(data, 5, 1)
    advanced_res *= advanced_count_trees(data, 7, 1)
    advanced_res *= advanced_count_trees(data, 1, 2)
    print(advanced_res)
