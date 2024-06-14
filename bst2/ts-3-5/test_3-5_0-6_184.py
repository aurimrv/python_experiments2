import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from bst2 import Node, Bst

@pytest.fixture
def sample_bst():
    return Bst([10, 5, 15, 3, 8, 12, 18])

def test_insert(sample_bst):
    sample_bst.insert(20)
    assert sample_bst.size() == 8
    assert sample_bst.contains(20) == True

def test_search(sample_bst):
    assert sample_bst.search(5).val == 5
    assert sample_bst.search(100) == None

def test_size(sample_bst):
    assert sample_bst.size() == 7

def test_depth(sample_bst):
    assert sample_bst.depth() == 3

def test_contains(sample_bst):
    assert sample_bst.contains(12) == True
    assert sample_bst.contains(7) == False

def test_balance(sample_bst):
    assert sample_bst.balance() == 0

def test_pre_order(sample_bst):
    assert list(sample_bst.pre_order()) == [10, 5, 3, 8, 15, 12, 18]

def test_in_order(sample_bst):
    assert list(sample_bst.in_order()) == [3, 5, 8, 10, 12, 15, 18]

def test_post_order(sample_bst):
    assert list(sample_bst.post_order()) == [3, 8, 5, 12, 18, 15, 10]

def test_breadth_first(sample_bst):
    assert list(sample_bst.breadth_first()) == [10, 5, 15, 3, 8, 12, 18]

def test_delete(sample_bst):
    sample_bst.delete(3)
    assert sample_bst.size() == 6
    assert sample_bst.contains(3) == False