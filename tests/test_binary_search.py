import sys
from pathlib import Path

base_dir = Path(__file__).resolve().parent.parent
sys.path.append(str(base_dir))
from algorithms.binary_search import binary_search


def test_binary_search():
    assert binary_search([], 1) == -1
    assert binary_search([1], -1) == -1
    assert binary_search([1], 1) == 0
    assert binary_search([1], 2) == -1
    assert binary_search([1, 2], -1) == -1
    assert binary_search([1, 2], 1) == 0
    assert binary_search([1, 2], 2) == 1
    assert binary_search([1, 2], 3) == -1
    assert binary_search([1, 2, 2, 2, 3], -1) == -1
    assert binary_search([1, 2, 2, 2, 3], 1) == 0
    assert binary_search([1, 2, 2, 2, 3], 2) in [1, 2, 3]
    assert binary_search([1, 2, 2, 2, 3], 3) == 4
    assert binary_search([1, 2, 2, 2, 3], 4) == -1
