# -*- coding: utf-8 -*-
# @Author: Lucien Zhang
# @Date:   2019-06-02 14:28:28
# @Last Modified by:   Lucien Zhang
# @Last Modified time: 2019-06-02 15:14:51

from typing import List


def dton(d: int, base: int)->List[int]:
    if base in [-1, 0, 1] or type(base) != int:
        print(f'wrong base {base}')
        return None
    ans = []
    while d != 0:
        r = d % base
        d = (d - r) // base
        if r < 0:
            r -= base
            d += 1
        ans.insert(0, r)
    return ans


def ntod(nums: List[int], base: int)->int:
    ans = 0
    for n in nums:
        ans *= base
        ans += n
    return ans


if __name__ == '__main__':
    print('12345 base=6 is equal to {}'.format(ntod([1, 2, 3, 4, 5], 6)))
    print(1 * 6**4 + 2 * 6**3 + 3 * 6**2 + 4 * 6**1 + 5 * 6**0)
    print('12345 base=-6 is equal to {}'.format(ntod([1, 2, 3, 4, 5], -6)))
    print(1 * (-6)**4 + 2 * (-6)**3 + 3 * (-6)**2 + 4 * (-6)**1 + 5 * (-6)**0)
    print('-' * 20)
    print('1865 base=6 is equal to {}'.format(dton(1865, 6)))
    print('953 base=-6 is equal to {}'.format(dton(953, -6)))
