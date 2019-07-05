# -*- coding: utf-8 -*-
# @Author: Lucien Zhang
# @Date:   2019-06-02 16:32:28
# @Last Modified by:   Lucien Zhang
# @Last Modified time: 2019-06-02 16:50:56

import collections

# namedtuple()    factory function for creating tuple subclasses with named fields
# collections.namedtuple(typename, field_names, *, rename=False, defaults=None, module=None)
# field_names=['x', 'y']  'x y'  'x, y'
Point = collections.namedtuple('Point', ['x', 'y'])
p = Point(11, y=22)
print('p[0] + p[1] =', p[0] + p[1])
x, y = p
print('x, y:', x, y)
print('p.x + p.y =', p.x + p.y)
print('p is', p)
print('-' * 20)

# deque   list-like container with fast appends and pops on either end
# the name is pronounced “deck” and is short for “double-ended queue”
# class collections.deque([iterable[, maxlen]])
""" Methods:
append(x)
appendleft(x)
clear()
copy()
count(x)
extend(iterable)
extendleft(iterable)
insert(i, x)
pop()
popleft()
remove(value)
reverse()
rotate(n=1): Rotate the deque n steps to the right. If n is negative, rotate to the left.
maxlen: Maximum size of a deque or None if unbounded.
"""
print('-' * 20)

# ChainMap    dict-like class for creating a single view of multiple mappings

print('-' * 20)

# Counter dict subclass for counting hashable objects

print('-' * 20)

# OrderedDict dict subclass that remembers the order entries were added

print('-' * 20)

# defaultdict dict subclass that calls a factory function to supply missing values

print('-' * 20)

# UserDict    wrapper around dictionary objects for easier dict subclassing

print('-' * 20)

# UserList    wrapper around list objects for easier list subclassing

print('-' * 20)

# UserString  wrapper around string objects for easier string subclassing
