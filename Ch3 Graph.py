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


v0 = V(0)
v1 = V(1)
v2 = V(2)
v3 = V(3)
v4 = V(4)
v5 = V(5)
v1.add_v(v0, v2, )
v0.add_v(v1, v2, v5)
v2.add_v(v0, v1, v3, v5)
v3.add_v(v2, v5, v4)
v4.add_v(v2, v3)
v5.add_v(v0, v3)
v0.bfs(90)
