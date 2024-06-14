import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from bst2 import Bst, Node

@pytest.fixture
def sample_bst():
    return Bst([5, 3, 8, 2, 4, 7, 9])

def test_node_init():
    node = Node(10)
    assert node.val == 10
    assert node.right is None
    assert node.left is None
    assert node.parent is None
    assert node.height == 1

def test_node_is_leaf():
    node = Node(5)
    assert node._is_leaf() == True

def test_node_is_interior():
    node = Node(5)
    node.left = Node(3)
    node.right = Node(8)
    assert node._is_interior() == True

def test_node_onlychild():
    node = Node(5)
    node.left = Node(3)
    assert node._onlychild() == 'left'

def test_node_side():
    parent = Node(5)
    child = Node(3, parent)
    parent.left = child
    assert child._side() == 'left'

def test_bst_insert(sample_bst):
    sample_bst.insert(6)
    assert sample_bst.size() == 8

def test_bst_search(sample_bst):
    assert sample_bst.search(3).val == 3
    assert sample_bst.search(10) is None

def test_bst_size(sample_bst):
    assert sample_bst.size() == 7

def test_bst_depth(sample_bst):
    assert sample_bst.depth() == 3

def test_bst_contains(sample_bst):
    assert sample_bst.contains(3) == True
    assert sample_bst.contains(10) == False

def test_bst_balance(sample_bst):
    assert sample_bst.balance() == 0

def test_bst_pre_order(sample_bst):
    assert list(sample_bst.pre_order()) == [5, 3, 2, 4, 8, 7, 9]

def test_bst_in_order(sample_bst):
    assert list(sample_bst.in_order()) == [2, 3, 4, 5, 7, 8, 9]

def test_bst_post_order(sample_bst):
    assert list(sample_bst.post_order()) == [2, 4, 3, 7, 9, 8, 5]

def test_bst_breadth_first(sample_bst):
    assert list(sample_bst.breadth_first()) == [5, 3, 8, 2, 4, 7, 9]

def test_bst_delete(sample_bst):
    sample_bst.delete(3)
    assert sample_bst.size() == 6
    assert sample_bst.search(3) is None