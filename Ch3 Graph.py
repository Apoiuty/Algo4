import heapq
from copy import deepcopy
from functools import total_ordering


class V:
    def __init__(self, attr):
        self.nodes = set()
        self.attr = attr

    def add_v(self, *v_list):
        for v in v_list:
            if isinstance(v, V):
                self.nodes.add(v)
            else:
                self.nodes.add(V(v))

    def dfs(self, target=None):
        stack = [self]
        checked = set()
        checked.add(self)
        while stack:
            v = stack.pop()
            print(v.attr)
            if v.attr == target:
                return v
            else:
                for v_adj in v.nodes:
                    if v_adj not in checked:
                        stack.append(v_adj)
                        checked.add(v_adj)
        return False

    def bfs(self, target=None):
        from collections import deque
        checked = set()
        checked.add(self)
        stack = deque()
        stack.append(self)
        while stack:
            v = stack.popleft()
            print(v.attr)
            if v.attr == target:
                return v
            else:
                for v_adj in v.nodes:
                    if v_adj not in checked:
                        checked.add(v_adj)
                        stack.append(v_adj)
        return False

    def __repr__(self):
        return f'{self.attr}'


@total_ordering
class Edge:
    def __init__(self, s, e, w):
        self.s = s
        self.e = e
        self.weight = w

    @property
    def start(self):
        return self.s

    @property
    def end(self):
        return self.e

    @property
    def weight(self):
        return self.weight

    @weight.setter
    def weight(self, value):
        self._weight = value

    def __repr__(self):
        return f'{self.start}-{self.weight}->{self.end}'

    def __eq__(self, other):
        return self.weight == other.weight

    def __lt__(self, other):
        return self.weight < other.weight


class WeightedGraph:
    """
    加权无向图
    """

    def __init__(self):
        from collections import defaultdict
        # 每个顶点的连接的顶点
        self.adj = defaultdict(list)
        self.edge = []

    def add_edge(self, e):
        self.adj[e.start].append(e)
        self.adj[e.end].append(e)
        self.edge.append(e)

    def E(self):
        return len(self.edge)

    def V(self):
        return len(self.adj)

    def prim(self):
        """
        生成最小生成树
        :return: WeightedGraph
        """
        mst = WeightedGraph()
        marked = set()
        v0 = self.edge[0].start
        Queue = self.adj[v0]
        heapq.heapify(Queue)
        marked.add(v0)
        while Queue:
            edge = heapq.heappop(Queue)
            v = edge.start
            e = edge.end
            if v in marked:
                if e in marked:
                    continue
                else:
                    mst.add_edge(edge)
                    marked.add(e)
                    for i in self.adj[e]:
                        if i.start in marked and i.end in marked:
                            continue
                        else:
                            heapq.heappush(Queue, i)
            else:
                mst.add_edge(edge)
                marked.add(v)
                for i in self.adj[v]:
                    if i.start in marked and i.end in marked:
                        continue
                    else:
                        heapq.heappush(Queue, i)

        return mst

    def Kruskal(self):
        mst = WeightedGraph()
        from collections import defaultdict
        union_set = defaultdict(lambda: None)
        n = self.V()
        edges = deepcopy(self.edge)
        heapq.heapify(edges)
        while mst.V() < n:
            edge = heapq.heappop(edges)
            v = edge.start
            w = edge.weight
            if union_set[v] == None and union_set[w] == None:
                union_set[v] = union_set[w] = min(v, w)
            elif union_set[v] == None:
                union_set[v] = union_set[w]
            elif union_set[w] == None:
                union_set[w] = union_set[v]
            elif union_set[w] != union_set[v]:
                union_set[w] = union_set[v]
            else:
                continue

            mst.add_edge(edge)

        return mst


g = WeightedGraph()
