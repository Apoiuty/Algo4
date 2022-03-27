import string


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


print(BM_search('123456', '5600'))
