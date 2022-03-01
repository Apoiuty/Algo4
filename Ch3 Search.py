def binary_search(a, item):
    """
    二分查找
    :param a:
    :param item:
    :return:
    """
    lo = 0
    hi = len(a) - 1
    a.sort()
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        if a[mid] > item:
            hi = mid - 1
        elif a[mid] < item:
            lo = mid + 1
        else:
            return True
    return False


class RB_tree:
    """
    红色树
    """

    def __init__(self):
        # 0为黑色，1为红色
        self.head = None

    def rotate_left(self, h):
        x = h.right
        h.right = x.left
        x.left = h
        x.color = h.color
        h.color = 1
        return x

    def rotate_right(self, h):
        x = h.left
        h.left = x.right
        x.right = h
        x.color = h.color
        h.color = 1
        return x

    def flip_color(self, h):
        h.color = 1
        h.left.color = 0
        h.right.color = 0

    def is_red(self, node):
        if not node:
            return False
        else:
            return bool(node.color)

    def put(self, node, val):
        if not node:
            return Node(val, None, None, 1)

        if val < node.val:
            node.left = self.put(node.left, val)
        elif val > node.val:
            node.right = self.put(node.right, val)
        else:
            return node

        if not self.is_red(node.left) and self.is_red(node.right):
            node = self.rotate_left(node)

        if self.is_red(node.left) and self.is_red(node.left.left):
            node = self.rotate_right(node)

        if self.is_red(node.right) and self.is_red(node.left):
            self.flip_color(node)
        return node

    def insert(self, val):
        self.head = self.put(self.head, val)
        self.head.color = 0

    def preorder_travel(self):
        """
        前向遍历
        :return:
        """
        head = self.head
        heap = []
        while head or heap:
            if head:
                print(head.val, end=' ')
                heap.append(head)
                head = head.left
            else:
                head = heap.pop().right

    def midorder_travel(self):
        stack = []
        head = self.head
        while head or stack:
            if head:
                stack.append(head)
                head = head.left
            else:
                head = stack.pop()
                print(head, end=' ')
                head = head.right

    def postorder_travel(self):
        last_node = None
        stack = []
        head = self.head
        while head or stack:
            if head:
                stack.append(head)
                head = head.left
            else:
                head = stack[-1]
                if not head.right or head.right == last_node:
                    print(head, end=' ')
                    stack.pop()
                    last_node = head
                    head = None
                else:
                    head = head.right

    def levelorder_travel(self):
        from collections import deque
        q = deque()
        q.append((1, self.head))
        level = 1
        while q:
            item = q.popleft()
            level = item[0]
            head = item[1]
            if head:
                level += 1
                q.append((level, head.left))
                q.append((level, head.right))
                print(head, level - 1, end=' ')


class Node:
    def __init__(self, val, left, right, color):
        self.val = val
        self.color = color
        self.left = left
        self.right = right

    def __repr__(self):
        return str(self.val)


tree = RB_tree()
for i in sorted('SEARCHXMPL'):
    tree.insert(i)

tree.preorder_travel()
print()

tree.levelorder_travel()
