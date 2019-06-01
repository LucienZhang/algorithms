# -*- coding: utf-8 -*-
# @Author: Lucien Zhang
# @Date:   2019-03-31 16:39:53
# @Last Modified by:   Lucien Zhang
# @Last Modified time: 2019-06-01 21:54:27


class UnionFind(object):
    def __init__(self, size):
        self.size = size
        self.forest = list(range(size))

    def find(self, element):
        root = element
        while self.forest[root] != root:
            root = self.forest[root]
        # path compression
        while self.forest[element] != root:
            self.forest[element], element = root, self.forest[element]
        return root

    def union(self, x, y):
        rx = self.find(x)
        ry = self.find(y)
        if rx == ry:
            return
        self.forest[rx] = ry
        self.size -= 1

    def get_sets(self):
        for _ in range(len(self.forest)):
            self.find(_)
        roots = {root: index for index, root in enumerate(set(self.forest))}
        sets = []
        for _ in range(len(roots)):
            sets.append([])
        for node, root in enumerate(self.forest):
            sets[roots[root]].append(node)
        return sets


class UnionFind2(object):
    def __init__(self):
        self.forest = {}
        self.size = 0

    def find(self, element):
        if element not in self.forest:
            return None
        root = element
        while self.forest[root] != root:
            root = self.forest[root]
        while self.forest[element] != root:
            self.forest[element], element = root, self.forest[element]
        return root

    def union(self, x, y):
        rx = self.find(x)
        ry = self.find(y)
        if rx == ry:
            return
        self.forest[ry] = rx
        self.size -= 1

    def add(self, x):
        self.forest[x] = x
        self.size += 1

    def get_sets(self):
        sets = {}
        for k in self.forest.keys():
            root = self.find(k)
            if root == k and root not in sets:
                sets[root] = [root]
            elif root in sets:
                sets[root].append(k)
            else:
                sets[root] = [root, k]
        return list(sets.values())


if __name__ == "__main__":
    """
    0-1  4-5
    |    |
    2-3  6
    """
    G = [[1, 1, 1, 0, 0, 0, 0],
         [1, 1, 0, 0, 0, 0, 0],
         [1, 0, 1, 1, 0, 0, 0],
         [0, 0, 1, 1, 0, 0, 0],
         [0, 0, 0, 0, 1, 1, 1],
         [0, 0, 0, 0, 1, 1, 0],
         [0, 0, 0, 0, 1, 0, 1]]

    ufs = [UnionFind(len(G)), UnionFind2()]
    for i in range(len(G)):
        ufs[1].add(i)
    for uf in ufs:
        # consider upper triangle
        for i in range(len(G) - 1):
            for j in range(i + 1, len(G)):
                if G[i][j] == 1:
                    uf.union(i, j)
        print("sets count:", uf.size)
        sets = uf.get_sets()
        for i in range(len(sets)):
            print("{}-th set is".format(i))
            print(sets[i])
        print('-' * 20)
