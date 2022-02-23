def exchange(a, b):
    """
    交换两个元素的值
    :param a:
    :param b:
    :return:
    """
    return b, a


def selection_sort(a):
    """
    选择排序
    :param a: 列表
    :return:
    """
    for i, _ in enumerate(a):
        min_index = i
        for j, _ in enumerate(a[i + 1:], i + 1):
            if a[j] < a[min_index]:
                min_index = j
        a[i], a[min_index] = exchange(a[i], a[min_index])

    return a


def insert_sort(a):
    """
    同上
    :param a:
    :return:
    """

    n = len(a)
    for i in range(1, n):
        for j in range(i, 0, -1):
            if a[j - 1] > a[j]:
                a[j - 1], a[j] = exchange(a[j - 1], a[j])

    return a


def shell_sort(a):
    """
    pass
    :param a:
    :return:
    """
    n = len(a)
    h = 1
    while h <= n // 3:
        h = 3 * h + 1

    while h >= 1:
        for i in range(h, n):
            for j in range(i, h - 1, -h):
                if a[j - h] > a[j]:
                    a[j - h], a[j] = a[j], a[j - h]
        h //= 3

    return a


def merge(nums, lo, mid, hi):
    aux = []
    i = lo
    j = mid
    for k in range(lo, hi):
        if i >= mid:
            aux.append(nums[j])
            j += 1
        elif j >= hi:
            aux.append(nums[i])
            i += 1
        elif nums[i] < nums[j]:
            aux.append(nums[i])
            i += 1
        else:
            aux.append(nums[j])
            j += 1
    nums[lo:hi] = aux


def topdown_merge_sort(nums, lo, hi):
    """
    自顶向下的归并排序
    :param nums:
    :param lo:
    :param hi:
    :return:
    """
    if hi <= lo + 1:
        return

    mid = lo + (hi - lo) // 2
    topdown_merge_sort(nums, lo, mid)
    topdown_merge_sort(nums, mid, hi)
    merge(nums, lo, mid, hi)
    return nums


def downtop_merge_sort(nums, lo, hi):
    """
    自底向上的归并排序
    :param nums:
    :param lo:
    :param hi:
    :return:
    """
    sz = 1
    while sz < hi:
        i = lo
        while i < hi - sz:
            merge(nums, i, i + sz, min(hi, i + 2 * sz))
            i += 2 * sz
        sz *= 2
    return nums


def quick_sort(a, lo, hi):
    """
    快速排序
    :param a:
    :param lo:
    :param hi:
    :return:
    """
    random.shuffle(a)
    if hi <= lo:
        return
    lt = lo
    i = lo
    gt = hi - 1
    v = a[lo]
    # 三分
    while i <= gt:
        if a[i] < v:
            a[lt], a[i] = a[i], a[lt]
            lt += 1
            i += 1
        elif a[i] > v:
            a[i], a[gt] = a[gt], a[i]
            gt -= 1
        else:
            i += 1

    quick_sort(a, lo, lt)
    quick_sort(a, gt + 1, hi)
    return a


class Heap:
    def __init__(self):
        self.__a = [None]
        self.__n = 0

    def swim(self, k):
        while k > 1 and self.__a[k // 2] < self.__a[k]:
            self.__a[k // 2], self.__a[k] = self.__a[k], self.__a[k // 2]
            k //= 2

    def sink(self, k):
        while 2 * k <= self.__n:
            j = 2 * k
            if j < self.__n and self.__a[j] < self.__a[j + 1]:
                j += 1
            if not self.__a[k] < self.__a[j]:
                break
            else:
                self.__a[k], self.__a[j] = self.__a[j], self.__a[k]
            k = j

    def insert(self, item):
        self.__a.append(item)
        self.__n += 1
        self.swim(self.__n)

    def pop(self):
        item = self.__a[1]
        self.__a[1] = self.__a[-1]
        self.__a.pop()
        self.__n -= 1
        self.sink(1)
        return item


def swim(a, k):
    while k > 1 and a[k // 2] < a[k]:
        a[k // 2], a[k] = a[k], a[k // 2]
        k //= 2


def sink(a, k, n):
    while 2 * k <= n:
        j = 2 * k
        if j < n and a[j] < a[j + 1]:
            j += 1
        if not a[k] < a[j]:
            break
        else:
            a[k], a[j] = a[j], a[k]
        k = j


def heap_sort(a):
    n = len(a)
    a.insert(0, None)
    k = n // 2
    while k >= 1:
        sink(a, k, n)
        k -= 1

    while n > 1:
        a[n], a[1] = a[1], a[n]
        n -= 1
        sink(a, 1, n)

    return a[1:]


import random

heap = Heap()

nums = []
for i in range(10):
    nums.append(random.randint(0, 100))

print(heap_sort(nums))
