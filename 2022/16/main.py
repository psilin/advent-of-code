
import copy
import itertools
import matplotlib.pyplot as plt
import networkx as nx


class Node:
    def __init__(self, strr, name = "", value=0, children=[]):
        if strr is not None:
            self.name, self.value, self.children = self.from_string(strr)
        else:
            self.name = name
            self.value = value
            self.children = children

    def from_string(self, strr):
        lst = strr.split(" ")
        name = lst[1]
        value = int(lst[4].rstrip(";").lstrip("rate="))
        children = []
        for i in range(9, len(lst), 1):
            children.append(lst[i].rstrip(","))
        return name, value, children

    def __repr__(self):
        return f"Name: {self.name} Value: {self.value} Children: {self.children}"


def parse():
    nodes = {}
    with open("./input.txt", "r") as fh:
        for line in fh:
            line = line.rstrip("\n")
            n = Node(line)
            nodes[n.name] = n
    return nodes


def visualize(nodes):
    G = nx.Graph()
    edges = []
    for i in nodes:
        n = nodes[i]
        name = n.name
        if n.value > 0:
            name = f"{n.name}-{n.value}"
        
        for c in n.children:
            nn = nodes[c[0]]
            nname = nn.name
            if nn.value > 0:
                nname = f"{nn.name}-{nn.value}"
        
            edges.append([name, nname])
    G.add_edges_from(edges)
    nx.draw_networkx(G)
    plt.show()


def optimize(nodes):
    opt_nodes = {}
    nodes["AA"].value = 1
    
    for i in nodes:
        n = nodes[i]
        if n.value == 0:
            continue

        new_node = Node(None, n.name, n.value, [])
        for c in n.children:
            prev = n.name
            cur = c
            path = 0
            while True:
                path += 1
                nn = nodes[cur]
                if len(nn.children) == 2 and nn.value == 0:
                    if nn.children[0] == prev:
                        prev = cur
                        cur = nn.children[1]
                    elif nn.children[1] == prev:
                        prev = cur
                        cur = nn.children[0]
                else:
                    new_node.children.append([nn.name, path])
                    break
        opt_nodes[new_node.name] = new_node
    
    nodes["AA"].value = 0
    opt_nodes["AA"].value = 0
    return opt_nodes


def shortest_path(opt_nodes):
    g = nx.Graph()
    for i in opt_nodes:
        n = opt_nodes[i]
        for ch in n.children:
            g.add_edge(n.name, ch[0], weight=ch[1])
    pth = nx.shortest_path_length(g, weight="weight")
    return {p[0]: p[1] for p in pth}    


def random_walk(paths, opt_nodes, time_left, good_nodes):
    best = [time_left, 0, ["AA",]]
    current = [[time_left, 0, ["AA",]],]
    while len(current) > 0:
        new_current = []
        for cur in current:
            for node in opt_nodes:
                n = opt_nodes[node]
                if n.name not in cur[2] and (dst := paths[cur[2][-1]][n.name] + 1) <= cur[0]:
                    if (good_nodes is not None and n.name in good_nodes) or good_nodes is None:
                        c = copy.deepcopy(cur)
                        c[0] -= dst
                        c[1] += c[0] * n.value
                        c[2].append(n.name)
                        new_current.append(c)
            if cur[1] > best[1]:
                best = cur
        current = new_current
    return best


def divide_graph(paths):
    # max path length between components
    dist = 10
    graph = set([k for k in paths if k != "AA"])
    # divide into 2 subsets of 8 and 9 elements exactly (almost equal in number of elements)
    subsets = [set(subset) for subset in itertools.combinations(graph, 8)]
    good_subsets = []
    for s in subsets:
        res = False
        for i in s:
            for j in s:
                if paths[i][j] > dist:
                    res = True
                    break
        if res is False:
            c = graph - s
            print(s, c)
            for i in c:
                for j in c:
                    if paths[i][j] > dist:
                        res = True
                        break
        if res is False:
            good_subsets.append([s, c])
    return good_subsets


def random_walk_together(good_subsets, paths, opt_nodes):
    maxx = 0
    for gs in good_subsets:
        best1 = random_walk(paths, opt_nodes, 26, gs[0])
        best2 = random_walk(paths, opt_nodes, 26, gs[1])
        if (best1[1] + best2[1]) > maxx:
            maxx = best1[1] + best2[1]
            print(maxx, best1, best2)


def main():
    nodes = parse()
    for i in nodes:
        print(nodes[i])
    print()
    
    opt_nodes = optimize(nodes)
    for i in opt_nodes:
        print(opt_nodes[i])
    print()
    
    #visualize(opt_nodes)
    paths = shortest_path(opt_nodes)
    for k,v in paths.items():
        print(f"{k}: {v}")
    print()

    best = random_walk(paths, opt_nodes, 30, None)
    print(best)

    good_subsets = divide_graph(paths)
    random_walk_together(good_subsets, paths, opt_nodes)


if __name__ == "__main__":
    main()
