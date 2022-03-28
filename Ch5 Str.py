import string
from collections import defaultdict


class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = defaultdict(lambda: None)


class LZW:
    pass


class TierTree:
    def __init__(self):
        self.root = Node()
        self.cnt = 0

    def get_string(self, node, s, d):
        if node == None:
            return
        elif len(s) == d:
            return node
        else:
            char = s[d]
            return self.get_string(node.next[char], s, d + 1)

    def get(self, s):
        node = self.get_string(self.root, s, 0)
        if node == None:
            return None
        else:
            return node.val

    def put_string(self, node, s, d):
        if node == None:
            node = Node()
        if d == len(s):
            node.val = s
            return node
        else:
            char = s[d]
            node.next[char] = self.put_string(node.next[char], s, d + 1)
            return node

    def put(self, s):
        self.root = self.put_string(self.root, s, 0)

    def prefix_with(self, s):
        queue = []
        self.__prefix_with(self.root, s, 0, queue)
        return queue

    def __prefix_with(self, node, s, d, queue):
        if node == None:
            return
        elif len(s) > d:
            self.__prefix_with(node.next[s[d]], s, d + 1, queue)
        elif len(s) <= d:
            if node.val:
                queue.append(node.val)
            for c in node.next:
                self.__prefix_with(node.next[c], s, d + 1, queue)

    def delete(self, s):
        self.root = self.__delete(self.root, s, 0)

    def long_prefix(self, s):
        return self.__long_prefix(self.root, s, 0, '')

    def __long_prefix(self, node, s, d, pre):
        if node == None:
            return pre
        if node.val == s[:d]:
            pre = node.val
        if d < len(s):
            return self.__long_prefix(node.next[s[d]], s, d + 1, pre)
        else:
            return pre

    def __delete(self, node, s, d):
        if node == None:
            return None
        if d == len(s):
            node.val = None
        else:
            node.next[s[d]] = self.__delete(node.next[s[d]], s, d + 1)

        if node.val:
            return node
        else:
            if any(node.next[c] for c in node.next):
                return node
            else:
                return None


def BM_search(s, p):
    if len(s) < len(p):
        return -1
    from collections import defaultdict
    bad_letter = defaultdict(lambda: -1)
    # 生成坏字符索引
    for i, letter in enumerate(p):
        bad_letter[letter] = i

    i = 0
    j = len(p) - 1
    while j >= 0 and i <= len(s) - len(p):
        if p[j] == s[i + j]:
            j -= 1
        else:
            if s[i + j] not in bad_letter:
                i += j + 1
            else:
                if j - bad_letter[s[i + j]] <= 0:
                    i += j - bad_letter[s[i + j]] + 1
                else:
                    i += j - bad_letter[s[i + j]]
            j = len(p) - 1

        if j == -1:
            return i

    return -1


from functools import total_ordering


@total_ordering
class Huffman_node:
    def __init__(self, freq, char, left=None, right=None):
        self.freq = freq
        self.char = char
        self.left = left
        self.right = right

    def is_leaf(self):
        return self.right is None and self.left is None

    def __eq__(self, other):
        return self.freq == other.freq

    def __lt__(self, other):
        return self.freq < other.freq

    def __repr__(self):
        return f'{self.char} with {self.freq}s'


class Huffman:
    def __init__(self, s):
        self.s = s
        self.root = self.build_tree()
        self.mp = {}
        self.build_mp(self.root, '')

    def build_tree(self):
        queue = []
        from collections import Counter
        import heapq
        cnt = Counter(self.s)
        for key, freq in cnt.items():
            heapq.heappush(queue, (freq, Huffman_node(freq, key)))

        while len(queue) > 1:
            x = heapq.heappop(queue)[1]
            y = heapq.heappop(queue)[1]
            node = Huffman_node(x.freq + y.freq, None, x, y)
            heapq.heappush(queue, (node.freq, node))

        return queue[0][1]

    def encode(self):
        result = ''
        s = self.s
        for letter in s:
            result += self.mp[letter]

        return result

    def build_mp(self, node, s):
        if node.is_leaf():
            self.mp[node.char] = s
        else:
            self.build_mp(node.left, s + '0')
            self.build_mp(node.right, s + '1')

    def decode(self, codes):

        i = 0
        result = ''
        while i < len(codes):
            root = self.root
            while not root.is_leaf():
                if codes[i] == '1':
                    root = root.right
                else:
                    root = root.left
                i += 1

            result += root.char

        return result


def KMP(s, p):
    from collections import defaultdict
    dfa = defaultdict(int)
    X = 0
    dfa[(p[0], 0)] = 1
    for j in range(1, len(p)):
        for letter in string.ascii_letters:
            dfa[(letter, j)] = dfa[(letter, X)]
        dfa[(p[j], j)] = j + 1
        X = dfa[(p[j], X)]

    i = j = 0
    while i < len(s) and j < len(p):
        j = dfa[(s[i], j)]
        i += 1
    if j == len(p):
        return i - len(p)
    else:
        return -1


class LZW:
    def encode(self, s):
        Tree = TierTree()
        mp = {}
        max_code = 0
        for i in string.ascii_letters:
            mp[i] = ord(i)
            Tree.put(i)
            max_code = max(max_code, ord(i))

        max_code += 1

        i = 0
        codes = []
        while i < len(s):
            long_prefix = Tree.long_prefix(s[i:])
            codes.append(mp[long_prefix])
            if i + len(long_prefix) >= len(s):
                break
            prefix_char = long_prefix + s[i + len(long_prefix)]
            mp[prefix_char] = max_code
            max_code += 1
            Tree.put(prefix_char)
            i += len(long_prefix)

        return codes

    def decode(self, codes):
        Tree = TierTree()
        mp = {}
        max_code = 0
        for i in string.ascii_letters:
            mp[ord(i)] = i
            Tree.put(i)
            max_code = max(max_code, ord(i))

        max_code += 1

        i = 0
        s = ''
        while i < len(codes):
            if i == len(codes) - 1:
                s += mp[codes[i]]
                break
            try:
                next_pre = mp[codes[i + 1]][0]
            except KeyError:
                next_pre = mp[codes[i]][0]
            s += mp[codes[i]]
            mp[max_code] = mp[codes[i]] + next_pre
            max_code += 1
            i += 1

        return s


t = Huffman('ABRACADABRA!')
print(t.decode(t.encode()))
