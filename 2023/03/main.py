
def parse():
    matrix = []
    with open("./input.txt", "r") as fh:
        for line in fh:
            matrix.append(line.rstrip("\n"))
    return matrix


def look_around(matrix, x, y, n):
    if (x-1)>= 0 and (str(matrix[y][x-1]).isdigit() or matrix[y][x-1] != '.'):
        return True
    elif (x+len(n)) < len(matrix[y]) and (str(matrix[y][x+len(n)]).isdigit() or matrix[y][x+len(n)] != '.'):
        return True
    
    for i in range(x-1, x+1+len(n)):
        for j in (y-1, y+1):
            if 0 <= i < len(matrix[y]):
                if 0 <= j < len(matrix):
                    if (str(matrix[j][i]).isdigit() or matrix[j][i] != '.') is True:
                        return True    
    return False


def process(matrix):
    summ = 0
    for y in range(len(matrix)):
        x = 0
        while x < len(matrix[y]):
            n = ""
            while str(matrix[y][x]).isdigit(): 
                n += matrix[y][x]
                x += 1
                if x == len(matrix[y]):
                    break
            if len(n) > 0 and look_around(matrix, x - len(n), y, n):
                summ += int(n)
            x += 1
    return summ


def look_around_star(matrix, x, y):
    res = []
    if (x - 1) >= 0 and str(matrix[y][x-1]).isdigit():
        n = str(matrix[y][x-1])
        i = x - 2
        while i >= 0 and str(matrix[y][i]).isdigit():
            n = str(matrix[y][i]) + n
            i -= 1
        res.append(int(n))

    if (x + 1) < len(matrix[y]) and str(matrix[y][x+1]).isdigit():
        n = str(matrix[y][x+1])
        i = x + 2
        while i < len(matrix[y]) and str(matrix[y][i]).isdigit():
            n = n + str(matrix[y][i])
            i += 1
        res.append(int(n))

    if y > 0:
        if str(matrix[y-1][x]).isdigit():
            n = str(matrix[y-1][x])
            i = x - 1
            while i >= 0 and str(matrix[y-1][i]).isdigit():
                n = str(matrix[y-1][i]) + n
                i -= 1
            i = x + 1
            while i < len(matrix[y-1]) and str(matrix[y-1][i]).isdigit():
                n = n + str(matrix[y-1][i])
                i += 1
            res.append(int(n))
        else:
            n = ""
            i = x - 1
            while i >= 0 and str(matrix[y-1][i]).isdigit():
                n = str(matrix[y-1][i]) + n
                i -= 1
            if len(n) > 0:
                res.append(int(n))
            n = ""
            i = x + 1
            while i < len(matrix[y-1]) and str(matrix[y-1][i]).isdigit():
                n = n + str(matrix[y-1][i])
                i += 1
            if len(n) > 0:
                res.append(int(n))
    
    if y < (len(matrix) - 1):
        if str(matrix[y+1][x]).isdigit():
            n = str(matrix[y+1][x])
            i = x - 1
            while i >= 0 and str(matrix[y+1][i]).isdigit():
                n = str(matrix[y+1][i]) + n
                i -= 1
            i = x + 1
            while i < len(matrix[y+1]) and str(matrix[y+1][i]).isdigit():
                n = n + str(matrix[y+1][i])
                i += 1
            res.append(int(n))
        else:
            n = ""
            i = x - 1
            while i >= 0 and str(matrix[y+1][i]).isdigit():
                n = str(matrix[y+1][i]) + n
                i -= 1
            if len(n) > 0:
                res.append(int(n))
            n = ""
            i = x + 1
            while i < len(matrix[y+1]) and str(matrix[y+1][i]).isdigit():
                n = n + str(matrix[y+1][i])
                i += 1
            if len(n) > 0:
                res.append(int(n))


    return res


def process_stars(matrix):
    summ = 0
    for y in range(len(matrix)):
        for x in range(len(matrix[y])):
            if matrix[y][x] == "*":
                lst = look_around_star(matrix, x, y)
                if len(lst) == 2:
                    summ += lst[0]*lst[1]
    return summ


def main():
    matrix = parse()
    print(process(matrix))
    print(process_stars(matrix))


if __name__ == "__main__":
    main()
