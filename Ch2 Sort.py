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


print(downtop_merge_sort([1, 4, 5, 2, 3, 2], 0, 6))
