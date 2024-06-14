import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from bst2 import Bst, Node

@pytest.fixture
def sample_bst():
    bst = Bst([5, 3, 8, 2, 4, 7, 9, 1, 6])
    return bst

def test_insert(sample_bst):
    sample_bst.insert(10)
    assert sample_bst.contains(10) == True

def test_search(sample_bst):
    assert sample_bst.search(4).val == 4

def test_size(sample_bst):
    assert sample_bst.size() == 9

def test_depth(sample_bst):
    assert sample_bst.depth() == 4

def test_contains(sample_bst):
    assert sample_bst.contains(9) == True

def test_balance(sample_bst):
    assert sample_bst.balance() == 0

def test_pre_order(sample_bst):
    assert list(sample_bst.pre_order()) == [5, 3, 2, 1, 4, 8, 7, 6, 9]

def test_in_order(sample_bst):
    assert list(sample_bst.in_order()) == [1, 2, 3, 4, 5, 6, 7, 8, 9]

def test_post_order(sample_bst):
    assert list(sample_bst.post_order()) == [1, 2, 4, 3, 6, 7, 9, 8, 5]

def test_breadth_first(sample_bst):
    assert list(sample_bst.breadth_first()) == [5, 3, 8, 2, 4, 7, 9, 1, 6]

def test_delete(sample_bst):
    sample_bst.delete(2)
    assert sample_bst.contains(2) == False