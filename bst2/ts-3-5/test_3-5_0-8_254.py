import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from bst2 import Bst, Node

# Test cases for Node class
def test_node_is_leaf():
    node = Node(10)
    assert node._is_leaf() == True

def test_node_is_interior():
    node = Node(10)
    node.left = Node(5)
    node.right = Node(15)
    assert node._is_interior() == True

def test_node_onlychild_left():
    node = Node(10)
    node.left = Node(5)
    assert node._onlychild() == 'left'

def test_node_onlychild_right():
    node = Node(10)
    node.right = Node(15)
    assert node._onlychild() == 'right'

def test_node_side_left():
    parent = Node(10)
    node = Node(5, parent)
    parent.left = node
    assert node._side() == 'left'

def test_node_side_right():
    parent = Node(10)
    node = Node(15, parent)
    parent.right = node
    assert node._side() == 'right'


# Test cases for Bst class
@pytest.fixture
def sample_tree():
    return Bst([10, 5, 15, 3, 7, 12, 17])

def test_bst_insert(sample_tree):
    sample_tree.insert(20)
    assert sample_tree.size() == 8

def test_bst_search(sample_tree):
    assert sample_tree.search(5).val == 5

def test_bst_size(sample_tree):
    assert sample_tree.size() == 7

def test_bst_depth(sample_tree):
    assert sample_tree.depth() == 3

def test_bst_contains(sample_tree):
    assert sample_tree.contains(12) == True

def test_bst_balance(sample_tree):
    assert sample_tree.balance() == 0

def test_bst_pre_order(sample_tree):
    assert list(sample_tree.pre_order()) == [10, 5, 3, 7, 15, 12, 17]

def test_bst_in_order(sample_tree):
    assert list(sample_tree.in_order()) == [3, 5, 7, 10, 12, 15, 17]

def test_bst_post_order(sample_tree):
    assert list(sample_tree.post_order()) == [3, 7, 5, 12, 17, 15, 10]

def test_bst_breadth_first(sample_tree):
    assert list(sample_tree.breadth_first()) == [10, 5, 15, 3, 7, 12, 17]

def test_bst_delete(sample_tree):
    sample_tree.delete(7)
    assert sample_tree.size() == 6