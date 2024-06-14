import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from bst2 import Bst, Node

@pytest.fixture
def example_bst():
    return Bst([5, 3, 7, 2, 4, 6, 8])

def test_insert(example_bst):
    assert example_bst.size() == 7
    assert example_bst.search(3).val == 3

    example_bst.insert(9)
    assert example_bst.size() == 8
    assert example_bst.search(9).val == 9

def test_search(example_bst):
    assert example_bst.search(6).val == 6
    assert example_bst.search(10) is None

def test_size(example_bst):
    assert example_bst.size() == 7

def test_depth(example_bst):
    assert example_bst.depth() == 3

def test_contains(example_bst):
    assert example_bst.contains(5) is True
    assert example_bst.contains(10) is False

def test_balance(example_bst):
    assert example_bst.balance() == 0

def test_pre_order(example_bst):
    assert list(example_bst.pre_order()) == [5, 3, 2, 4, 7, 6, 8]

def test_in_order(example_bst):
    assert list(example_bst.in_order()) == [2, 3, 4, 5, 6, 7, 8]

def test_post_order(example_bst):
    assert list(example_bst.post_order()) == [2, 4, 3, 6, 8, 7, 5]

def test_breadth_first(example_bst):
    assert list(example_bst.breadth_first()) == [5, 3, 7, 2, 4, 6, 8]

def test_delete(example_bst):
    example_bst.delete(3)
    assert example_bst.size() == 6
    assert example_bst.search(3) is None