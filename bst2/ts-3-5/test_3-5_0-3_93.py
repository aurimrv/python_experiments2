import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from bst2 import Bst, Node

@pytest.fixture
def sample_bst():
    return Bst([5, 3, 7, 2, 4, 6, 8])

def test_insert(sample_bst):
    sample_bst.insert(1)
    assert sample_bst.size() == 8
    assert sample_bst.search(1).val == 1

def test_search(sample_bst):
    assert sample_bst.search(5).val == 5
    assert sample_bst.search(10) is None

def test_size(sample_bst):
    assert sample_bst.size() == 7

def test_depth(sample_bst):
    assert sample_bst.depth() == 3

def test_contains(sample_bst):
    assert sample_bst.contains(7) is True
    assert sample_bst.contains(10) is False

def test_balance(sample_bst):
    assert sample_bst.balance() == 0

def test_pre_order(sample_bst):
    assert list(sample_bst.pre_order()) == [5, 3, 2, 4, 7, 6, 8]

def test_in_order(sample_bst):
    assert list(sample_bst.in_order()) == [2, 3, 4, 5, 6, 7, 8]

def test_post_order(sample_bst):
    assert list(sample_bst.post_order()) == [2, 4, 3, 6, 8, 7, 5]

def test_breadth_first(sample_bst):
    assert list(sample_bst.breadth_first()) == [5, 3, 7, 2, 4, 6, 8]

def test_delete(sample_bst):
    sample_bst.delete(2)
    assert sample_bst.size() == 6
    assert sample_bst.search(2) is None