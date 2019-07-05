# -*- coding: utf-8 -*-
# @Author: Lucien Zhang
# @Date:   2019-05-27 15:09:43
# @Last Modified by:   Lucien Zhang
# @Last Modified time: 2019-06-02 16:31:19

""" heapq is the abbreviation of heap queue
    heapq is min heap, to use max heap, use opposite number of the key, i.e. (-key, value)
    heap[k] <= heap[2*k+1] and heap[k] <= heap[2*k+2] for all k
    counting elements from zero. For the sake of comparison
    non-existing elements are considered to be infinite
    The interesting property of a heap is that its smallest element is always the root, heap[0].
"""

import heapq
import random


h = list(range(20, 6, -2))
print(f'original h: {h}')
print('-' * 20)

# Transform list x into a heap, in-place, in linear time
heapq.heapify(h)
print(f'heapified h: {h}')

# Return the minimum value of the heap
print(f'min of the heap, i.e. h[0]: {h[0]}')
print('-' * 20)

# heapq.heappush(heap, item)
# Push the value item onto the heap, maintaining the heap invariant
print('push 3')
heapq.heappush(h, 3)
print(f'h: {h}')

print('push 15')
heapq.heappush(h, 15)
print(f'h: {h}')

print('push 25')
heapq.heappush(h, 25)
print(f'h: {h}')

print('push 10')
heapq.heappush(h, 10)
print(f'h: {h}')

print('push 10')
heapq.heappush(h, 10)
print(f'h: {h}')

print(f'min of the heap, i.e. h[0]: {h[0]}')
print('-' * 20)

# heapq.heappop(heap)
# Pop and return the smallest item from the heap, maintaining the heap invariant.
# If the heap is empty, IndexError is raised.
# To access the smallest item without popping it, use heap[0].
print('pop: {}'.format(heapq.heappop(h)))
print(f'h: {h}')

print('pop: {}'.format(heapq.heappop(h)))
print(f'h: {h}')

print('pop: {}'.format(heapq.heappop(h)))
print(f'h: {h}')

print(f'min of the heap, i.e. h[0]: {h[0]}')
print('-' * 20)

# heapq.heappushpop(heap, item)
# Push item on the heap, then pop and return the smallest item from the heap.
# The combined action runs more efficiently than heappush() followed by a separate call to heappop().
# Note: push, then, pop
print('pushpop 5: {}'.format(heapq.heappushpop(h, 5)))
print(f'h: {h}')

print('pushpop 15: {}'.format(heapq.heappushpop(h, 15)))
print(f'h: {h}')

print(f'min of the heap, i.e. h[0]: {h[0]}')
print('-' * 20)

# heapq.heapreplace(heap, item)
"""
    Pop and return the smallest item from the heap, and also push the new item. The heap size doesn’t change. If the heap is empty, IndexError is raised.
    This one step operation is more efficient than a heappop() followed by heappush() and can be more appropriate when using a fixed-size heap. The pop/push combination always returns an element from the heap and replaces it with item.
    The value returned may be larger than the item added. If that isn’t desired, consider using heappushpop() instead. Its push/pop combination returns the smaller of the two values, leaving the larger value on the heap.
"""
print('replace the minimum by 5: {}'.format(heapq.heapreplace(h, 5)))
print('replace the minimum by 17: {}'.format(heapq.heapreplace(h, 17)))

print(f'min of the heap, i.e. h[0]: {h[0]}')
print('-' * 20)

# heapq.merge(*iterables, key=None, reverse=False)
"""
    Merge multiple sorted inputs into a single sorted output
    Returns an iterator over the sorted values
    Similar to sorted(itertools.chain(*iterables)) but returns an iterable
    Assumes that each of the input streams is already sorted (smallest to largest)
    key and reverse must be specified as keyword arguments, because iterables is variable-length argument
    key specifies a key function of one argument that is used to extract a comparison key from each input element.
    The default value is None (compare the elements directly).
    reverse is a boolean value. If set to True, then the input elements are merged as if each comparison were reversed.
    To achieve behavior similar to sorted(itertools.chain(*iterables), reverse=True), all iterables must be sorted from largest to smallest.
"""

random.seed(42)
a = sorted([random.randrange(100) for _ in range(5)])
b = sorted([random.randrange(100) for _ in range(5)])
print(f'a is {a}')
print(f'b is {b}')
print('merge result is {}'.format(list(heapq.merge(a, b))))

a = sorted([(random.randrange(100), random.randrange(100)) for _ in range(3)], key=lambda x: x[1], reverse=True)
b = sorted([(random.randrange(100), random.randrange(100)) for _ in range(3)], key=lambda x: x[1], reverse=True)
print(f'a is {a}')
print(f'b is {b}')
print('key=lambda x: x[1], reverse=True, merge result is {}'.format(list(heapq.merge(a, b, key=lambda x: x[1], reverse=True))))
print('-' * 20)

# heapq.nlargest(n, iterable, key=None)
"""
    Return a list with the n largest elements from the dataset defined by iterable.
    Equivalent to: sorted(iterable, key=key, reverse=True)[:n].
"""
a = [random.randrange(100) for _ in range(10)]
print(f'a is {a}')
print('3 largest numbers are {}'.format(heapq.nlargest(3, a)))
print('-' * 20)

# heapq.nsmallest(n, iterable, key=None)
"""
    Return a list with the n smallest elements from the dataset defined by iterable.
    Equivalent to: sorted(iterable, key=key)[:n].
"""
a = [random.randrange(100) for _ in range(10)]
print(f'a is {a}')
print('3 smallest numbers are {}'.format(heapq.nsmallest(3, a)))

"""
    The latter two functions perform best for smaller values of n.
    For larger values, it is more efficient to use the sorted() function.
    Also, when n==1, it is more efficient to use the built-in min() and max() functions.
    If repeated usage of these functions is required, consider turning the iterable into an actual heap.
"""
