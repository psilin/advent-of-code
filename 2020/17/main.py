

def parse_input():
    cubes = []
    cubes4 = []
    y = 0
    with open('./input.txt', 'r') as fh:
        for line in fh:
            line = line.strip('\n')
            for i in range(len(line)):
                if line[i] == '#':
                    cubes.append((i, y, 0))
                    cubes4.append((i, y, 0, 0))
            y -= 1
    return cubes, cubes4


def _get_neighbors(p):
    return [(x, y, z) for x in (p[0]-1, p[0], p[0]+1) for y in (p[1]-1, p[1], p[1]+1) for z in (p[2]-1, p[2], p[2]+1)]


def _count_status(p, cubes):
    nbrs = _get_neighbors(p)
    cnt = 0
    for n in nbrs:
        if p != n and n in cubes:
            cnt += 1
    active = p in cubes
    return active, cnt


def step(cubes):
    new_cubes = []
    for cb in cubes:
        for n in _get_neighbors(cb):
            act, cnt = _count_status(n, cubes)
            if act is True and cnt == 2 or cnt == 3:
                new_cubes.append(n)
    return list(set(new_cubes))


def _get_neighbors4(p):
    return [(x, y, z, w) for x in (p[0]-1, p[0], p[0]+1) for y in (p[1]-1, p[1], p[1]+1) for z in (p[2]-1, p[2], p[2]+1) for w in (p[3]-1, p[3], p[3]+1)]


def _count_status4(p, cubes):
    nbrs = _get_neighbors4(p)
    cnt = 0
    for n in nbrs:
        if p != n and n in cubes:
            cnt += 1
    active = p in cubes
    return active, cnt


def step4(cubes):
    new_cubes = []
    for cb in cubes:
        for n in _get_neighbors4(cb):
            act, cnt = _count_status4(n, cubes)
            if act is True and cnt == 2 or cnt == 3:
                new_cubes.append(n)
    return list(set(new_cubes))


if __name__ == '__main__':
    cubes, cubes4 = parse_input()
    for i in range(6):
        cubes = step(cubes)
        print(i, len(cubes))
    
    for i in range(6):
        cubes4 = step4(cubes4)
        print(i, len(cubes4))
    