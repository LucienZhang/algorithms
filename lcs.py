# -*- coding: utf-8 -*-
# @Author: Lucien Zhang
# @Date:   2019-09-10 15:15:21
# @Last Modified by:   Lucien Zhang
# @Last Modified time: 2019-09-10 16:21:31

""" longest common subsequence
Input: x = "abcde", y = "ace"
Output: 3,"ace"
Explanation: The longest common subsequence is "ace" and its length is 3.

DP[i][j] indicates the length of lcs of x[:i+1] and y[:j+1]
the lcs does not need to be ended with x[i] or y[j]
"""


def lcs(x: str, y: str)->(int, str):
    m = len(x)
    n = len(y)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    direction = [[None] * (n + 1) for _ in range(m + 1)]
    UP = 0
    LEFT = 1
    UP_LEFT = 2
    for i in range(m):
        for j in range(n):
            if x[i] == y[j]:
                dp[i + 1][j + 1] = dp[i][j] + 1
                direction[i + 1][j + 1] = UP_LEFT
            elif dp[i + 1][j] > dp[i][j + 1]:
                dp[i + 1][j + 1] = dp[i + 1][j]
                direction[i + 1][j + 1] = LEFT
            else:
                dp[i + 1][j + 1] = dp[i][j + 1]
                direction[i + 1][j + 1] = UP

    ans_len = dp[-1][-1]
    ans_str = ""
    i = m
    j = n
    while direction[i][j] is not None:
        if direction[i][j] == UP_LEFT:
            i -= 1
            j -= 1
            ans_str = x[i] + ans_str
        elif direction[i][j] == UP:
            i -= 1
        else:
            j -= 1
    return ans_len, ans_str


def lcs2(x: str, y: str)->int:
    # input length only
    # time complexity O(N^2)
    # space somplexity O(N^2)
    m = len(x)
    n = len(y)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(m):
        for j in range(n):
            if x[i] == y[j]:
                dp[i + 1][j + 1] = dp[i][j] + 1
            else:
                dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j])
    return dp[-1][-1]


def lcs3(x: str, y: str)->int:
    # compress space complexity to O(N)
    # time complexity O(N^2)
    # space somplexity O(N)
    m = len(x)
    n = len(y)
    dp = [0] * (n + 1)
    for i in range(m):
        ul = 0  # up_left
        for j in range(n):
            if x[i] == y[j]:
                dp[j + 1], ul = ul + 1, dp[j + 1]
            else:
                ul = dp[j + 1]
                dp[j + 1] = max(dp[j], dp[j + 1])
    return dp[-1]


if __name__ == '__main__':
    x = "abcde"
    y = "ace"
    print("x={},y={},answer is {}".format(x, y, lcs(x, y)))
    print("x={},y={},answer is {}".format(x, y, lcs2(x, y)))
    print("x={},y={},answer is {}".format(x, y, lcs3(x, y)))
    x = "abc"
    y = "abc"
    print("x={},y={},answer is {}".format(x, y, lcs(x, y)))
    print("x={},y={},answer is {}".format(x, y, lcs2(x, y)))
    print("x={},y={},answer is {}".format(x, y, lcs3(x, y)))
    x = "abcd"
    y = "efgh"
    print("x={},y={},answer is {}".format(x, y, lcs(x, y)))
    print("x={},y={},answer is {}".format(x, y, lcs2(x, y)))
    print("x={},y={},answer is {}".format(x, y, lcs3(x, y)))
    x = ""
    y = ""
    print("x={},y={},answer is {}".format(x, y, lcs(x, y)))
    print("x={},y={},answer is {}".format(x, y, lcs2(x, y)))
    print("x={},y={},answer is {}".format(x, y, lcs3(x, y)))
    x = "mhunuzqrkzsnidwbun"
    y = "szulspmhwpazoxijwbq"
    print("x={},y={},answer is {}".format(x, y, lcs(x, y)))
    print("x={},y={},answer is {}".format(x, y, lcs2(x, y)))
    print("x={},y={},answer is {}".format(x, y, lcs3(x, y)))
