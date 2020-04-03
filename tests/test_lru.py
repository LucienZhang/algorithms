import sys
from pathlib import Path
import pytest

base_dir = Path(__file__).resolve().parent.parent
sys.path.append(str(base_dir))


@pytest.mark.sample
def test_lru():
    from data_structure.lru import LRU, LRU2
    check(LRU)
    check(LRU2)


def check(implementation):
    lru = implementation(5)
    assert lru.get(3) is None
    lru.put(0, 'a')
    assert lru.get(0) == 'a'
    for i in range(1, 5):
        lru.put(i, chr(ord('a') + i))
    for i in range(5):
        assert lru.get(i) == chr(ord('a') + i)
    lru.put(5, 'f')
    assert lru.get(0) is None
    for i in range(5, 0, -1):
        assert lru.get(i) == chr(ord('a') + i)
    # get function also change the order, so now node with key=5 is at the tail
    lru.put(0, 'a')
    assert lru.get(5) is None
    for i in range(5):
        assert lru.get(i) == chr(ord('a') + i)
