import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from bst2 import Node, Bst

@pytest.fixture
def sample_bst():
    bst = Bst([10, 5, 15, 2, 7, 12, 20, 1, 3, 6, 8, 11, 14, 18, 25])
    return bst

def test_insert(sample_bst):
    sample_bst.insert(9)
    assert sample_bst.size() == 16
    assert sample_bst.search(9) is not None

def test_search(sample_bst):
    assert sample_bst.search(7).val == 7
    assert sample_bst.search(100) is None

def test_size(sample_bst):
    assert sample_bst.size() == 15

def test_depth(sample_bst):
    assert sample_bst.depth() == 4

def test_contains(sample_bst):
    assert sample_bst.contains(7) is True
    assert sample_bst.contains(100) is False

def test_balance(sample_bst):
    assert sample_bst.balance() == 0

def test_pre_order(sample_bst):
    assert list(sample_bst.pre_order()) == [10, 5, 2, 1, 3, 7, 6, 8, 15, 12, 11, 14, 20, 18, 25]

def test_in_order(sample_bst):
    assert list(sample_bst.in_order()) == [1, 2, 3, 5, 6, 7, 8, 10, 11, 12, 14, 15, 18, 20, 25]

def test_post_order(sample_bst):
    assert list(sample_bst.post_order()) == [1, 3, 2, 6, 8, 7, 5, 11, 14, 12, 18, 25, 20, 15, 10]

def test_breadth_first(sample_bst):
    assert list(sample_bst.breadth_first()) == [10, 5, 15, 2, 7, 12, 20, 1, 3, 6, 8, 11, 14, 18, 25]

def test_delete(sample_bst):
    sample_bst.delete(7)
    assert sample_bst.size() == 14
    assert sample_bst.search(7) is None