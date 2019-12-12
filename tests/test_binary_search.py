import sys
from pathlib import Path
import pytest

base_dir = Path(__file__).resolve().parent.parent
sys.path.append(str(base_dir))


def base_binary_search(func):
    assert func([], 1) == -1
    assert func([1], -1) == -1
    assert func([1], 1) == 0
    assert func([1], 2) == -1
    assert func([1, 2], -1) == -1
    assert func([1, 2], 1) == 0
    assert func([1, 2], 2) == 1
    assert func([1, 2], 3) == -1
    assert func([1, 2, 2, 2, 3], -1) == -1
    assert func([1, 2, 2, 2, 3], 1) == 0
    assert func([1, 2, 2, 2, 3], 2) in [1, 2, 3]
    assert func([1, 2, 2, 2, 3], 3) == 4
    assert func([1, 2, 2, 2, 3], 4) == -1


@pytest.mark.sample
def test_binary_search():
    from algorithms.binary_search import binary_search as bs_sample
    base_binary_search(bs_sample)
