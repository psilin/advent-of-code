
def parse():
    mapp = []
    with open("./input.txt", "r") as fh:    
        for line in fh:
            mapp.append(list(line.rstrip("\n")))

    result = []
    for y in range(len(mapp)):
        line = []
        for x in range(len(mapp[0])):
            if mapp[y][x] == "S":
                start = [x, y]
                line.append(["a", -1])
            elif mapp[y][x] == "E":
                end = [x, y]
                line.append(["z", -1])
            else:
                line.append([mapp[y][x], -1])
        result.append(line)
    return result, start, end


def astar(result, visited, start):
    x, y = start[0], start[1]
    # up
    if y > 0 and (ord(result[y-1][x][0]) - ord(result[y][x][0])) <= 1:
        if result[y-1][x][1] == -1 or result[y-1][x][1] > (result[y][x][1] + 1):
            result[y-1][x][1] = result[y][x][1] + 1
            visited.append([x, y-1])

    # down
    if y < (len(result) - 1) and (ord(result[y+1][x][0]) - ord(result[y][x][0])) <= 1:
        if result[y+1][x][1] == -1 or result[y+1][x][1] > (result[y][x][1] + 1):
            result[y+1][x][1] = result[y][x][1] + 1
            visited.append([x, y+1])

    # left
    if x > 0 and (ord(result[y][x-1][0]) - ord(result[y][x][0])) <= 1:
        if result[y][x-1][1] == -1 or result[y][x-1][1] > (result[y][x][1] + 1):
            result[y][x-1][1] = result[y][x][1] + 1
            visited.append([x-1, y])

    # right
    if x < (len(result[0])-1) and (ord(result[y][x+1][0]) - ord(result[y][x][0])) <= 1:
        if result[y][x+1][1] == -1 or result[y][x+1][1] > (result[y][x][1] + 1):
            result[y][x+1][1] = result[y][x][1] + 1
            visited.append([x+1, y])


def find_path(result, start, end):
    visited = [start, ]
    result[start[1]][start[0]][1] = 0
    while len(visited) > 0:
        pt = visited.pop(0)
        astar(result, visited, pt)
    return result[end[1]][end[0]][1]

def main():
    result, start, end = parse()
    path = find_path(result, start, end)
    
    print(path)
    minn = path
    
    for y in range(len(result)):
        for x in range(len(result[0])):
            if result[y][x][0] == "a":
                res, _, end = parse()
                path_new = find_path(res, [x,y], end)
                if path_new < minn and path_new != -1:
                    minn = path_new
    print(minn)

if __name__ == "__main__":
    main()
