# -*- coding: utf-8 -*-
# @Author: Lucien Zhang
# @Date:   2019-05-26 17:37:07
# @Last Modified by:   Lucien Zhang
# @Last Modified time: 2019-08-18 23:24:13

""" binary search
    input A as a increasing list, K is what to find
    return the index if found, else, return -1
"""

from typing import List


def binary_search(A: List[int], K: int)->int:
    if not A:
        return -1
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


def binary_search2(A: List[int], K: int)->int:
    """ find lower bound
    """
    if not A:
        return -1
    left = 0
    right = len(A) - 1
    while left < right:
        mid = (left + right) // 2
        if K > A[mid]:
            left = mid + 1
        else:
            right = mid
    if A[left] != K:
        return -1
    else:
        return left


def binary_search3(A: List[int], K: int)->int:
    """ find upper bound
    """
    if not A:
        return -1
    left = 0
    right = len(A)
    while left < right:
        mid = (left + right) // 2
        if K >= A[mid]:
            left = mid + 1
        else:
            right = mid
    if left == 0 or A[left - 1] != K:
        return -1
    else:
        return left - 1


def binary_search4(A: List[int], K: int)->int:
    """ find i to insert K s.t. A[i-1]<K<=A[i+1]
    """
    if not A:
        return -1
    left = 0
    right = len(A)
    while left < right:
        mid = (left + right) // 2
        if K > A[mid]:
            left = mid + 1
        else:
            right = mid
    else:
        return left


if __name__ == '__main__':
    A = [3, 14, 27, 31, 39, 42, 55, 70, 74, 1, 85, 93, 98]
    print(f'find 31: {binary_search(A,31)}')
    print(f'find 3: {binary_search(A,3)}')
    print(f'find 98: {binary_search(A,98)}')
    print(f'find 50: {binary_search(A,50)}')
    print(f'find 1: {binary_search(A,1)}')
    print(f'find 100: {binary_search(A,100)}')

    print('-' * 20)
    print('find bound')

    B = [1] * 3
    print('B:', B)
    C = [0] + B + [2]
    print('C:', C)

    print('find lower bound of 1 in B: {}'.format(binary_search2(B, 1)))
    print('find lower bound of 1 in C: {}'.format(binary_search2(C, 1)))
    print('find lower bound of 1 in [1]: {}'.format(binary_search2([1], 1)))
    print('find lower bound of 3 in B: {}'.format(binary_search2(B, 3)))
    print('find lower bound of 3 in C: {}'.format(binary_search2(C, 3)))
    print('find lower bound of 3 in [1]: {}'.format(binary_search2([1], 3)))
    print('find lower bound of -1 in B: {}'.format(binary_search2(B, -1)))
    print('find lower bound of -1 in C: {}'.format(binary_search2(C, -1)))
    print('find lower bound of -1 in [1]: {}'.format(binary_search2([1], -1)))
    print('find lower bound of 1 in []: {}'.format(binary_search2([], 1)))

    print('-' * 20)

    print('find upper bound of 1 in B: {}'.format(binary_search3(B, 1)))
    print('find upper bound of 1 in C: {}'.format(binary_search3(C, 1)))
    print('find upper bound of 1 in [1]: {}'.format(binary_search3([1], 1)))
    print('find upper bound of 3 in B: {}'.format(binary_search3(B, 3)))
    print('find upper bound of 3 in C: {}'.format(binary_search3(C, 3)))
    print('find upper bound of 3 in [1]: {}'.format(binary_search3([1], 3)))
    print('find upper bound of -1 in B: {}'.format(binary_search3(B, -1)))
    print('find upper bound of -1 in C: {}'.format(binary_search3(C, -1)))
    print('find upper bound of -1 in [1]: {}'.format(binary_search3([1], -1)))
    print('find upper bound of 1 in []: {}'.format(binary_search3([], 1)))

    print('-' * 20)

    print('find insert index of 1 in B: {}'.format(binary_search4(B, 1)))
    print('find insert index of 1 in C: {}'.format(binary_search4(C, 1)))
    print('find insert index of 1 in [1]: {}'.format(binary_search4([1], 1)))
    print('find insert index of 3 in B: {}'.format(binary_search4(B, 3)))
    print('find insert index of 3 in C: {}'.format(binary_search4(C, 3)))
    print('find insert index of 3 in [1]: {}'.format(binary_search4([1], 3)))
    print('find insert index of -1 in B: {}'.format(binary_search4(B, -1)))
    print('find insert index of -1 in C: {}'.format(binary_search4(C, -1)))
    print('find insert index of -1 in [1]: {}'.format(binary_search4([1], -1)))
    print('find insert index of 1 in []: {}'.format(binary_search4([], 1)))
