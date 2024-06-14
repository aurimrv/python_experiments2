import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from bst2 import Node, Bst

@pytest.fixture
def sample_bst():
    return Bst([8, 3, 10, 1, 6, 14, 4, 7, 13])

def test_node_is_leaf():
    node = Node(5)
    assert node._is_leaf() == True

def test_node_is_interior():
    node = Node(5)
    node.left = Node(3)
    node.right = Node(7)
    assert node._is_interior() == True

def test_node_onlychild():
    node = Node(5)
    node.left = Node(3)
    assert node._onlychild() == 'left'

def test_node_side():
    parent = Node(5)
    left_child = Node(3, parent)
    parent.left = left_child
    assert left_child._side() == 'left'

def test_bst_insert(sample_bst):
    sample_bst.insert(5)
    assert sample_bst.size() == 10

def test_bst_search(sample_bst):
    assert sample_bst.search(6).val == 6

def test_bst_size(sample_bst):
    assert sample_bst.size() == 9

def test_bst_depth(sample_bst):
    assert sample_bst.depth() == 4

def test_bst_contains(sample_bst):
    assert sample_bst.contains(14) == True
    assert sample_bst.contains(2) == False

def test_bst_balance(sample_bst):
    assert sample_bst.balance() == 0

def test_bst_pre_order(sample_bst):
    assert list(sample_bst.pre_order()) == [8, 3, 1, 6, 4, 7, 10, 14, 13]

def test_bst_in_order(sample_bst):
    assert list(sample_bst.in_order()) == [1, 3, 4, 6, 7, 8, 10, 13, 14]

def test_bst_post_order(sample_bst):
    assert list(sample_bst.post_order()) == [1, 4, 7, 6, 3, 13, 14, 10, 8]

def test_bst_breadth_first(sample_bst):
    assert list(sample_bst.breadth_first()) == [8, 3, 10, 1, 6, 14, 4, 7, 13]

def test_bst_delete(sample_bst):
    sample_bst.delete(6)
    assert sample_bst.size() == 8