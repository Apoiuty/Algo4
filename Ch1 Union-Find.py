class UnionFind:
    def __init__(self, nodes):
        self.connects = nodes
        self.__cnt = len(nodes)
        self.__tree_size = [1] * len(nodes)

    def quick_find_union(self, p, q):
        """
        将所有连通分量中触点用同一个触点表示，如果在连通时该触点所在连通分量不同则用
        其中一者替换，算法复杂度为平方复杂度
        该union操作的查询操作为find
        :param p:
        :param q:
        :return:
        """
        p_ = self.find(p)
        q_ = self.find(q)
        if p_ == q_:
            return
        else:
            for i, _ in enumerate(self.connects):
                if _ == p_:
                    self.connects[i] = q_

        self.__cnt -= 1

    def quick_union(self, p, q):
        """
        构建树的结构使相同在同一连通分量内的节点具有相同的根节点，该
        union算法的复杂度为线性,但是最坏情况下该算法的最坏复杂度依然是
        线性
        :param p:
        :param q:
        :return:
        """
        p_root = self.quick_union_find(p)
        q_root = self.quick_union_find(q)

        if q_root != p_root:
            self.connects[q_root] = p_root

        self.__cnt -= 1

    def connected(self, p, q):
        return self.find(p) == self.find(q)

    def find(self, p):
        return self.connects[p]

    def quick_union_find(self, p):
        while self.connects[p] != p:
            p = self.connects[self.connects[p]]

        return p

    def union(self, p, q):
        """
        构建平衡树的结构使相同在同一连通分量内的节点具有相同的根节点，该
        union算法的复杂度为对数平方
        :param p:
        :param q:
        :return:
        """
        p_root = self.quick_union_find(p)
        q_root = self.quick_union_find(q)

        if q_root != p_root:
            p_tree_size = self.__tree_size[p_root]
            q_tree_size = self.__tree_size[q_root]
            if p_tree_size > q_tree_size:
                self.connects[q_root] = p_root
                p_tree_size += q_tree_size
            else:
                self.connects[p_root] = q_root
                q_tree_size += p_tree_size

            self.__cnt -= 1

    def count(self):
        return self.__cnt


# 测试
with open('data/tinyUF.txt') as f:
    n = f.readline().strip()
    union_find = UnionFind(list(range(int(n))))
    for line in f:
        union_find.union(*[int(i) for i in line.split()])

print(union_find.connects, union_find.count())
