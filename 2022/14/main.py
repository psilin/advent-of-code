

def parse():
    maze = set()
    with open("./input.txt", "r") as fh:
        for line in fh:
            lst = line.rstrip("\n").split(" -> ")
            lst = [tuple(map(int, l.split(","))) for l in lst]
            for i in range(len(lst)-1):
                if lst[i][1] == lst[i+1][1]:
                    for j in range(min(lst[i][0], lst[i+1][0]), max(lst[i][0], lst[i+1][0])+1, 1):
                        maze.add((j, lst[i][1]))
                elif lst[i][0] == lst[i+1][0]:
                    for j in range(min(lst[i][1], lst[i+1][1]), max(lst[i][1], lst[i+1][1])+1, 1):
                        maze.add((lst[i][0],j))
    
    maxy = 0
    for m in maze:
        if m[1] > maxy:
            maxy = m[1]
    return maze, maxy


def simulate(maze, maxy):    
    cnt = 0
    while True:
        p = (500, 0)
        while True:
            if p[1] > maxy:
                return cnt

            if (p[0], p[1]+1) not in maze:
                p = (p[0], p[1]+1)
                continue
            elif (p[0]-1, p[1]+1) not in maze:
                p = (p[0]-1, p[1]+1)
                continue
            elif (p[0]+1, p[1]+1) not in maze:
                p = (p[0]+1, p[1]+1)
                continue
            else:
                maze.add(p)
                cnt += 1
                break


def upd_simulate(maze):
    cnt = 0
    while True:
        p = (500, 0)
        while True:
            if (p[0], p[1]+1) not in maze:
                p = (p[0], p[1]+1)
                continue
            elif (p[0]-1, p[1]+1) not in maze:
                p = (p[0]-1, p[1]+1)
                continue
            elif (p[0]+1, p[1]+1) not in maze:
                p = (p[0]+1, p[1]+1)
                continue
            else:
                maze.add(p)
                cnt += 1
                if p == (500, 0):
                    return cnt
                break


def main():
    maze, maxy = parse()
    cnt = simulate(maze, maxy)
    print(cnt)

    upd_maze, _ = parse()
    for i in range(1001):
        upd_maze.add((i, maxy+2))
    upd_cnt = upd_simulate(upd_maze)
    print(upd_cnt)


if __name__ == "__main__":
    main()
