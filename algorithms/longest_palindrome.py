# -*- coding: utf-8 -*-
# @Author: Lucien Zhang
# @Date:   2019-09-10 16:43:37
# @Last Modified by:   Lucien Zhang
# @Last Modified time: 2019-09-10 18:08:53

"""
Manacher's Algorithm is for Longest Palindromic Substring
"""


def lp_subsequence(x: str)->int:
    # longest palindromic subsequence
    # dp[i][j] indicates the length of palindrome from i to j
    # time complexity O(N^2)
    # space somplexity O(N^2)
    if not x:
        return 0
    n = len(x)
    dp = [[0] * n for _ in range(n)]
    for i in range(n - 1, -1, -1):
        for j in range(i, n):
            if i == j:
                dp[i][j] = 1
            elif i + 1 == j and x[i] == x[j]:
                dp[i][j] = 2
            elif x[i] == x[j]:
                dp[i][j] = dp[i + 1][j - 1] + 2
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
    return dp[0][-1]


def lp_subsequence2(x: str)->int:
    # longest palindromic subsequence
    # dp[i][j] indicates the length of palindrome from i to j
    # compress space complexity to O(N)
    # time complexity O(N^2)
    # space somplexity O(N)
    if not x:
        return 0
    n = len(x)
    dp = [0] * n

    for i in range(n - 1, -1, -1):
        dl = 0   # down left
        for j in range(i, n):
            if i == j:
                dl = dp[j]
                dp[j] = 1
            elif i + 1 == j and x[i] == x[j]:
                dl = dp[j]
                dp[j] = 2
            elif x[i] == x[j]:
                dp[j], dl = dl + 2, dp[j]
            else:
                dl = dp[j]
                dp[j] = max(dp[j], dp[j - 1])
    return dp[-1]


def lp_substring(x: str)->(int, str):
    # longest palindromic substring
    # dp[i][j] indicates the length of palindrome from i to j
    # time complexity O(N^2)
    # space somplexity O(N^2)
    if not x:
        return 0, ""
    n = len(x)
    dp = [[0] * n for _ in range(n)]
    ans_len = 0
    ans_str = ""
    for i in range(n - 1, -1, -1):
        for j in range(i, n):
            if i == j:
                dp[i][j] = 1
                if dp[i][j] > ans_len:
                    ans_len = dp[i][j]
                    ans_str = x[i:j + 1]
            elif i + 1 == j and x[i] == x[j]:
                dp[i][j] = 2
                if dp[i][j] > ans_len:
                    ans_len = dp[i][j]
                    ans_str = x[i:j + 1]
            elif x[i] == x[j] and dp[i + 1][j - 1] != 0:
                dp[i][j] = dp[i + 1][j - 1] + 2
                if dp[i][j] > ans_len:
                    ans_len = dp[i][j]
                    ans_str = x[i:j + 1]
            else:
                dp[i][j] = 0
    return ans_len, ans_str


def lp_substring2(x: str)->(int, str):
    # longest palindromic substring
    # dp[i][j] indicates the length of palindrome from i to j
    # compress space complexity to O(N)
    # time complexity O(N^2)
    # space somplexity O(N)

    if not x:
        return 0, ""
    n = len(x)
    dp = [0] * n
    ans_len = 0
    ans_str = ""
    for i in range(n - 1, -1, -1):
        dl = 0  # down left
        for j in range(i, n):
            if i == j:
                dl = dp[j]
                dp[j] = 1
                if dp[j] > ans_len:
                    ans_len = dp[j]
                    ans_str = x[i:j + 1]
            elif i + 1 == j and x[i] == x[j]:
                dl = dp[j]
                dp[j] = 2
                if dp[j] > ans_len:
                    ans_len = dp[j]
                    ans_str = x[i:j + 1]
            elif x[i] == x[j] and dl != 0:
                dp[j], dl = dl + 2, dp[j]
                if dp[j] > ans_len:
                    ans_len = dp[j]
                    ans_str = x[i:j + 1]
            else:
                dl = dp[j]
                dp[j] = 0
    return ans_len, ans_str


def manacher(s: str)->(int, str):
    # longest palindromic substring
    # manacher's algorithm
    # time complexity O(N)
    # space somplexity O(N)
    # the string does not contain # ^ $
    # ^ start, $ end, # medium
    if not x:
        return 0, ""
    center = 0
    max_right = 0
    ss = '^#' + '#'.join(list(s)) + '#$'
    radius = [0] * len(ss)
    for i in range(len(ss)):
        r = 0
        if i < max_right:
            r = min(radius[2 * center - i], max_right - i)
        while ss[i + r] != '$' and ss[i - r] != '^' and ss[i + r + 1] == ss[i - r - 1]:
            r += 1
        radius[i] = r
        if i + r > max_right:
            max_right = i + r
            center = i
    r = max(radius)
    c = radius.index(r)
    sub = ss[c - r:c + r + 1]
    ans_str = sub.replace('#', '')
    return len(ans_str), ans_str


if __name__ == '__main__':
    x = "bbbab"
    print("x={},length of longest palindromic subsequence is {}".format(x, lp_subsequence(x)))
    print("x={},length of longest palindromic subsequence is {}".format(x, lp_subsequence2(x)))
    x = "cbbd"
    print("x={},length of longest palindromic subsequence is {}".format(x, lp_subsequence(x)))
    print("x={},length of longest palindromic subsequence is {}".format(x, lp_subsequence2(x)))
    x = "a"
    print("x={},length of longest palindromic subsequence is {}".format(x, lp_subsequence(x)))
    print("x={},length of longest palindromic subsequence is {}".format(x, lp_subsequence2(x)))
    x = ""
    print("x={},length of longest palindromic subsequence is {}".format(x, lp_subsequence(x)))
    print("x={},length of longest palindromic subsequence is {}".format(x, lp_subsequence2(x)))
    x = "aabaa"
    print("x={},length of longest palindromic subsequence is {}".format(x, lp_subsequence(x)))
    print("x={},length of longest palindromic subsequence is {}".format(x, lp_subsequence2(x)))

    print("longest palindromic substring")

    x = "babad"
    print("x={},length of longest palindromic substring is {}".format(x, lp_substring(x)))
    print("x={},length of longest palindromic substring is {}".format(x, lp_substring2(x)))
    print("x={},length of longest palindromic substring is {}".format(x, manacher(x)))
    x = "cbbd"
    print("x={},length of longest palindromic substring is {}".format(x, lp_substring(x)))
    print("x={},length of longest palindromic substring is {}".format(x, lp_substring2(x)))
    print("x={},length of longest palindromic substring is {}".format(x, manacher(x)))
    x = "a"
    print("x={},length of longest palindromic substring is {}".format(x, lp_substring(x)))
    print("x={},length of longest palindromic substring is {}".format(x, lp_substring2(x)))
    print("x={},length of longest palindromic substring is {}".format(x, manacher(x)))
    x = ""
    print("x={},length of longest palindromic substring is {}".format(x, lp_substring(x)))
    print("x={},length of longest palindromic substring is {}".format(x, lp_substring2(x)))
    print("x={},length of longest palindromic substring is {}".format(x, manacher(x)))
