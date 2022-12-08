
def parse():
    trees = []
    with open("./input.txt", "r") as fh:
        for line in fh:
            line = line.rstrip("\n")
            lst = [int(i) for i in list(line)]
            trees.append(lst)
    return trees


def count_visible(trees):
    cnt = 0
    for y in range(1, len(trees)-1):
        for x in range(1, len(trees[0])-1):
            t = trees[y][x]

            vis = True
            for i in range(0, y):
                if trees[i][x] >= t:
                    vis = False
                    break
            if vis is True:
                cnt += 1
                continue
            
            vis = True
            for i in range(y + 1, len(trees)):
                if trees[i][x] >= t:
                    vis = False
                    break
            if vis is True:
                cnt += 1
                continue

            vis = True
            for j in range(0, x):
                if trees[y][j] >= t:
                    vis = False
                    break
            if vis is True:
                cnt += 1
                continue

            vis = True
            for j in range(x + 1, len(trees[0])):
                if trees[y][j] >= t:
                    vis = False
                    break
            if vis is True:
                cnt += 1

    cnt += 2 * (len(trees) + len(trees[0]) - 2)
    print(cnt)


def count_max_visibility(trees):
    max_vis = 0
    for y in range(1, len(trees)-1):
        for x in range(1, len(trees[0])-1):
            t = trees[y][x]
            
            see_up = 0
            for i in range(y-1, -1, -1):
                see_up += 1
                if trees[i][x] >= t:
                    break

            see_down = 0
            for i in range(y+1, len(trees)):
                see_down += 1
                if trees[i][x] >= t:
                    break

            see_left = 0
            for j in range(x-1,-1, -1):
                see_left += 1
                if trees[y][j] >= t:
                    break

            see_right = 0
            for j in range(x+1,len(trees[0])):
                see_right += 1
                if trees[y][j] >= t:
                    break

            res = see_up * see_down * see_left * see_right
            if res > max_vis:
                max_vis = res
    print(max_vis)


def main():
    trees = parse()
    count_visible(trees)
    count_max_visibility(trees)


if __name__ == "__main__":
    main()
