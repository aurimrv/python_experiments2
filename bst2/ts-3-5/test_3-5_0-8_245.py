import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from bst2 import Bst, Node

@pytest.fixture
def sample_bst():
    bst = Bst()
    bst.insert(5)
    bst.insert(3)
    bst.insert(7)
    bst.insert(2)
    bst.insert(4)
    bst.insert(6)
    bst.insert(8)
    return bst

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
    parent.left = Node(3, parent)
    child = parent.left
    assert child._side() == 'left'

def test_insert(sample_bst):
    assert sample_bst.size() == 7

def test_search(sample_bst):
    assert sample_bst.search(3).val == 3

def test_size(sample_bst):
    assert sample_bst.size() == 7

def test_depth(sample_bst):
    assert sample_bst.depth() == 3

def test_contains(sample_bst):
    assert sample_bst.contains(7) == True

def test_balance(sample_bst):
    assert sample_bst.balance() == 0

def test_pre_order(sample_bst):
    result = [val for val in sample_bst.pre_order()]
    assert result == [5, 3, 2, 4, 7, 6, 8]

def test_in_order(sample_bst):
    result = [val for val in sample_bst.in_order()]
    assert result == [2, 3, 4, 5, 6, 7, 8]

def test_post_order(sample_bst):
    result = [val for val in sample_bst.post_order()]
    assert result == [2, 4, 3, 6, 8, 7, 5]

def test_breadth_first(sample_bst):
    result = [val for val in sample_bst.breadth_first()]
    assert result == [5, 3, 7, 2, 4, 6, 8]

def test_delete(sample_bst):
    sample_bst.delete(3)
    assert sample_bst.size() == 6
    assert sample_bst.search(3) == None