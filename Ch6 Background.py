import bisect
import math


class B_node:
    def __init__(self, M, is_leaf):
        self.M = M
        # 初始化时就把最小键放入
        self.keys = []
        self.is_leaf = is_leaf
        self.links = []

    def add(self, key):
        if self.isExternal():
            bisect.insort(self.keys, key)
        else:
            next = self.next(key)
            next.add(key)
            if next.isFull():
                left, right = next.split()
                self.add_leaf(left)
                self.add_leaf(right)

    def find(self, key):
        if self.isExternal():
            return key in self.keys
        else:
            return self.next(key).find(key)

    def delete(self, key):
        pass
        # todo

    def split(self):
        left = B_node(self.M, self.is_leaf)
        right = B_node(self.M, self.is_leaf)
        n = self.M
        left.links = self.links[:n // 2]
        right.links = self.links[n // 2:]
        left.keys = self.keys[:n // 2]
        right.keys = self.keys[n // 2:]

        return left, right

    def isExternal(self):
        return self.is_leaf

    def add_leaf(self, leaf):
        leaf_key = leaf.keys[0]
        left_index = bisect.bisect_left(self.keys, leaf_key)
        if left_index < len(self.keys) and self.keys[left_index] == leaf_key:
            self.links[left_index] = leaf
        else:
            bisect.insort_left(self.keys, leaf_key)
            self.links.insert(left_index, leaf)

    def isFull(self):
        return len(self.keys) == self.M

    def __contains__(self, item):
        return self.find(item)

    def next(self, key):
        left_index = bisect.bisect_left(self.keys, key)
        if left_index < len(self.keys) and self.keys[left_index] == key:
            return self.links[left_index]
        else:
            return self.links[left_index - 1]

    def __repr__(self):
        return str(self.keys) + f' {self.is_leaf}'


class BTree:
    def __init__(self, M):
        self.M = M
        self.root = B_node(self.M, True)
        self.add(-math.inf)

    def __contains__(self, item):
        return item in self.root

    def add(self, key):
        self.root.add(key)
        if self.root.isFull():
            left, right = self.root.split()
            self.root = B_node(self.M, False)
            self.root.add_leaf(left)
            self.root.add_leaf(right)


t = BTree(4)
for i in [1, 2, 5, 6, 7, 16, 9, 12, 18, 21]:
    t.add(i)

for i in [1, 2, 5, 6, 7, 16, 9, 12, 18, 21]:
    print(i in t)

