# -*- coding: utf-8 -*-
# @Author: Lucien Zhang
# @Date:   2019-05-26 18:32:14
# @Last Modified by:   Lucien Zhang
# @Last Modified time: 2019-05-26 19:11:11

""" merge_sort is for list version
    merge_sort2 is for linked list version
"""

from typing import List


def merge(a: List[int], b: List[int])->List[int]:
    ans = []
    i = 0
    j = 0
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            ans.append(a[i])
            i += 1
        else:
            ans.append(b[j])
            j += 1
    ans += a[i:]
    ans += b[j:]
    return ans


def merge_sort(l: List[int])->List[int]:
    if not l:
        return None
    l = [[e] for e in l]
    m = len(l)
    step = 1
    while step < m:
        i = 0
        while i + step < m:
            l[i] = merge(l[i], l[i + step])
            i += step * 2
        step *= 2
    return l[0]


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def merge2(a: ListNode, b: ListNode)->ListNode:
    root = ListNode(None)
    tail = root
    while a and b:
        if a.val < b.val:
            tail.next = a
            tail = tail.next
            a = a.next
        else:
            tail.next = b
            tail = tail.next
            b = b.next
    if a:
        tail.next = a
    else:
        tail.next = b
    return root.next


def merge_sort2(l: List[int])->ListNode:
    if not l:
        return None
    l = [ListNode(e) for e in l]
    i = 0
    step = 1
    m = len(l)
    while step < m:
        i = 0
        while i + step < m:
            l[i] = merge2(l[i], l[i + step])
            i += step * 2
        step *= 2
    return l[0]


if __name__ == '__main__':
    L = [4, 1, 10, 8, 7, 12, 9, 2, 15]
    print(f'L: {L}')
    print(f'result: {merge_sort(L)}')

    print('-' * 20)

    L = [4, 1, 10, 8, 7, 12, 9, 2, 15]
    ans_node = merge_sort2(L)
    ans = []
    while ans_node:
        ans.append(ans_node.val)
        ans_node = ans_node.next
    print(f'L: {L}')
    print(f'result: {ans}')
