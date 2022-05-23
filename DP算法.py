from collections import defaultdict


def LCS(s1, s2):
    """
    返回s1和s2的最长公共子序列
    :param s1:
    :param s2:
    :return:
    """
    m, n = len(s1), len(s2)
    dp = defaultdict(int)
    for i in range(m):
        for j in range(n):
            if s1[i] == s2[j]:
                dp[(i, j)] = dp[(i - 1, j - 1)] + 1
            else:
                dp[(i, j)] = max(dp[(i - 1, j)], dp[(i, j - 1)])

    return dp[(m - 1, n - 1)]


def optimal_SBT(p, q):
    """
    最优二叉搜索树构建
    :param p: p1-pn,每个有效节点检索概率
    :param q: q0-qn，每个无效节点的检索概率
    :return: 每个子序列的期望搜索代价和最优根节点
    """
    # eij是pi,pj的期望搜索
    e = defaultdict(int)
    # wij是pi,pj的概率之和(也包含无效检索)
    w = defaultdict(int)
    n = len(p)
    for i in range(1, n + 2):
        # 单个节点的期望搜索概率
        e[i, i - 1] = q[i - 1]
        # 单个节点的概率之和
        w[i, i - 1] = q[i - 1]

    for l in range(1, n + 1):
        for i in range(1, n - l + 2):
            j = i + l - 1
            w[i, j] = w[i, j - 1] + p[j - 1] + q[j]
            # i,j的期望等于左子树的期望加上右子树的期望加上该节点增加的期望
            e[i, j] = min(e[i, r - 1] + w[i, j] + e[r + 1, j] for r in range(i, j + 1))

    return e[1, n]


print(optimal_SBT([0.15, 0.10, 0.05, 0.1, .2], [0.05, 0.10, 0.05, 0.05, 0.05, .1]))

print(LCS([1, 1, 1], [1, 2, 1, 2, 1]))
