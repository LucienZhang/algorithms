# -*- coding: utf-8 -*-
# @Author: Lucien Zhang
# @Date:   2019-05-26 17:37:07
# @Last Modified by:   Lucien Zhang
# @Last Modified time: 2019-05-26 17:56:27

""" binary search
    input A as a increasing list, K is what to find
    return the index if found, else, return -1
"""

from typing import List


def binary_search(A: List[int], K: int)->int:
    left = 0
    right = len(A) - 1
    while left <= right:
        mid = (left + right) // 2
        if K == A[mid]:
            return mid
        elif K < A[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return -1


if __name__ == '__main__':
    A = [3, 14, 27, 31, 39, 42, 55, 70, 74, 1, 85, 93, 98]
    print(f'find 31: {binary_search(A,31)}')
    print(f'find 3: {binary_search(A,3)}')
    print(f'find 98: {binary_search(A,98)}')
    print(f'find 50: {binary_search(A,50)}')
    print(f'find 1: {binary_search(A,1)}')
    print(f'find 100: {binary_search(A,100)}')
