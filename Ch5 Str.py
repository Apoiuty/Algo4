import string


def BM_search(s, p):
    if len(s) < len(p):
        return -1
    from collections import defaultdict
    bad_letter = defaultdict(lambda: -1)
    # 生成坏字符索引
    for i, letter in enumerate(p):
        bad_letter[letter] = i

    good_suffix = dict()
    len_p = len(p)
    cnt = 0
    while p[cnt] == p[len_p - cnt - 1]:
        cnt += 1
    for i in range(len_p - 1, -1, -1):
        if i == len_p - 1:
            good_suffix[i] = -1
        else:
            pass
    i = j = len_p - 1
    while j >= 0 and i < len(s):
        if s[i] == p[j]:
            i -= 1
            j -= 1
        else:
            i += len_p - 1 - j + max(good_suffix[j], j - bad_letter[j])
            j = len_p - 1

        if j == 0:
            return i


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


print(KMP('123456', '90'))
