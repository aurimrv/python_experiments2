import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from bst2 import Node, Bst

@pytest.fixture
def sample_tree():
    tree = Bst([5, 3, 7, 2, 4, 6, 8])
    return tree

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

def test_bst_init():
    tree = Bst([5, 3, 7, 2, 4, 6, 8])
    assert tree.size() == 7

def test_bst_insert(sample_tree):
    sample_tree.insert(9)
    assert sample_tree.size() == 8

def test_bst_search(sample_tree):
    node = sample_tree.search(4)
    assert node.val == 4

def test_bst_size(sample_tree):
    assert sample_tree.size() == 7

def test_bst_depth(sample_tree):
    assert sample_tree.depth() == 3

def test_bst_contains(sample_tree):
    assert sample_tree.contains(6) == True

def test_bst_balance(sample_tree):
    assert sample_tree.balance() == 0

def test_bst_pre_order(sample_tree):
    result = list(sample_tree.pre_order())
    assert result == [5, 3, 2, 4, 7, 6, 8]

def test_bst_in_order(sample_tree):
    result = list(sample_tree.in_order())
    assert result == [2, 3, 4, 5, 6, 7, 8]

def test_bst_post_order(sample_tree):
    result = list(sample_tree.post_order())
    assert result == [2, 4, 3, 6, 8, 7, 5]

def test_bst_breadth_first(sample_tree):
    result = list(sample_tree.breadth_first())
    assert result == [5, 3, 7, 2, 4, 6, 8]

def test_bst_delete(sample_tree):
    sample_tree.delete(4)
    assert sample_tree.size() == 6
    assert sample_tree.contains(4) == False