def knapsack_problem(v, w, W):
    from collections import defaultdict
    dp = defaultdict(int)
    nv = len(v)
    for i in range(nv):
        for j in range(W, w[i] - 1, -1):
            # j为不加i，j-w[i]为加i物品
            dp[j] = max(dp[j], dp[j - w[i]] + v[i])

    return dp[W]


def unbounded_knapsack_problem(v, w, W):
    from collections import defaultdict
    dp = defaultdict(int)
    nv = len(v)
    for i in range(nv):
        for j in range(w[i], W + 1):
            # j为不加i，j-w[i]为加i物品
            dp[j] = max(dp[j], dp[j - w[i]] + v[i])

    return dp[W]


def bounded_knapsack_problem(v, w, n, W):
    from collections import defaultdict
    dp = defaultdict(int)
    nv = len(v)
    for i in range(nv):
        for j in range(W, w[i] - 1, -1):
            # j为不加i，j-w[i]为加i物品
            dp[j] = max(dp[j - k * w[i]] for k in range(1, min(n[i], j // w[i]) + 1))

    return dp[W]


print(knapsack_problem([0, 4, 5, 6], [0, 3, 4, 5], 10))
