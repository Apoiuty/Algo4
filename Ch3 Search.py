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


print(binary_search([1, 2, 3, -1], -999))
