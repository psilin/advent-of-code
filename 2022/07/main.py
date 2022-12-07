

class Node:
    def __init__(self, name, is_dir=True, size=0, parent=None):
        self.name = name
        self.is_dir = is_dir
        self.size = size
        self.parent = parent
        self.children = {}

    def fs_size(self):
        if self.is_dir is False:
            return self.size
        else:
            summ = 0
            for ch in self.children:
                summ += self.children[ch].fs_size()
            return summ


def parse():
    fs = Node("/")
    current = fs
    with open("./input.txt", "r") as fh:
        for line in fh:
            lst = line.rstrip("\n").split()
            if lst[0] == "$":
                if lst[1] == "ls":
                    pass
                elif lst[1] == "cd":
                    if lst[2] == "..":
                        current = current.parent
                    elif lst[2] != "/":
                        current = current.children.get(lst[2], None)
            else:
                if lst[0] == "dir":
                    current.children[lst[1]] = Node(lst[1], True, 0, current)
                else:
                    current.children[lst[1]] = Node(lst[1], False, int(lst[0]), current)
    return fs


def traverse_cnt(node, cnt):
    if node.is_dir is True:
        sz = node.fs_size()
        if sz < 100000:
            cnt[0] += sz
        for ch in node.children:
            traverse_cnt(node.children[ch], cnt)


def traverse_agg(node, lst):
    if node.is_dir is True:
        sz = node.fs_size()
        lst.append(sz)
        for ch in node.children:
            traverse_agg(node.children[ch], lst)


def main():
    fs = parse()
    cnt = [0, ]
    traverse_cnt(fs, cnt)
    print(cnt)
    print()
    lst = []
    traverse_agg(fs, lst)
    lst.sort()
    size = 70000000 - lst[-1]
    need = 30000000 - size
    for l in lst:
        if l > need:
            print(l)
            break


if __name__ == "__main__":
    main()
