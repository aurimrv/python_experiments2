import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from bst2 import Node, Bst

@pytest.fixture
def sample_bst():
    bst = Bst([8, 3, 10, 1, 6, 14, 4, 7, 13])
    return bst

def test_insert(sample_bst):
    assert sample_bst.size() == 9
    sample_bst.insert(5)
    assert sample_bst.size() == 10

def test_search(sample_bst):
    assert sample_bst.search(6).val == 6
    assert sample_bst.search(11) is None

def test_size(sample_bst):
    assert sample_bst.size() == 9
    sample_bst.insert(20)
    assert sample_bst.size() == 10

def test_depth(sample_bst):
    assert sample_bst.depth() == 4

def test_contains(sample_bst):
    assert sample_bst.contains(8) is True
    assert sample_bst.contains(15) is False

def test_balance(sample_bst):
    assert sample_bst.balance() == 0

def test_pre_order_traversal(sample_bst):
    assert list(sample_bst.pre_order()) == [8, 3, 1, 6, 4, 7, 10, 14, 13]

def test_in_order_traversal(sample_bst):
    assert list(sample_bst.in_order()) == [1, 3, 4, 6, 7, 8, 10, 13, 14]

def test_post_order_traversal(sample_bst):
    assert list(sample_bst.post_order()) == [1, 4, 7, 6, 3, 13, 14, 10, 8]

def test_breadth_first_traversal(sample_bst):
    assert list(sample_bst.breadth_first()) == [8, 3, 10, 1, 6, 14, 4, 7, 13]

def test_delete(sample_bst):
    sample_bst.delete(6)
    assert sample_bst.size() == 8
    assert sample_bst.search(6) is None