# Implement a LRU cache
# Least Recently Used

# capacity limit, number of entries
# key: int
# value: str

# two methods
# get(key: int) -> Optional[str]
# put(key: int, value: str) -> None

# functools.lru_cache

from collections import OrderedDict


class Node(object):
    def __init__(self, val: str, key: int):
        self.val = val
        self.key = key
        self.next = None
        self.pre = None


class LRU(object):
    def __init__(self, size):
        assert isinstance(size, int)
        assert size > 0
        self.size = size
        self.nodes = {}
        self.head = None
        self.tail = None

    def _remove_node(self, n):
        if n is None:
            return None
        if n.pre:
            n.pre.next = n.next
        else:
            # first
            self.head = n.next

        if n.next:
            n.next.pre = n.pre
        else:
            # last
            self.tail = n.pre

    def _insert_node_at_head(self, n):
        n.next = self.head
        if self.head:
            self.head.pre = n
        else:
            # empty
            self.tail = n
        self.head = n

    def _hoist(self, key) -> Node:
        # O(1)
        n = self.nodes[key]
        self._remove_node(n)
        self._insert_node_at_head(n)
        return n

    def get(self, key) -> str:
        if key in self.nodes:
            n = self._hoist(key)
            return self.nodes[key].val
        else:
            return None

    def put(self, key, value):
        if key in self.nodes:
            # O(1)
            n = self._hoist(key)
            n.val = value
        else:
            # not full
            if len(self.nodes) < self.size:
                pass
            else:
                # full
                n = self.tail
                self._remove_node(n)
                del self.nodes[n.key]
            new_node = Node(value, key)
            self.nodes[key] = new_node
            # O(1)
            self._insert_node_at_head(new_node)


class LRU2(object):
    def __init__(self, size):
        self._size = size
        self._d = OrderedDict()

    def get(self, key) -> str:
        if key in self._d:
            self._d.move_to_end(key)
            return self._d[key]
        else:
            return None

    def put(self, key, value):
        self._d[key] = value
        if len(self._d) > self._size:
            self._d.popitem(last=False)
