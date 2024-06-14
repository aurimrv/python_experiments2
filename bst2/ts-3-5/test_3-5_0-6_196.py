import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from bst2 import Bst, Node

@pytest.fixture
def sample_tree():
    return Bst([5, 3, 7, 2, 4, 6, 8])

def test_node_is_leaf():
    node = Node(5)
    assert node._is_leaf() == True

def test_node_is_interior():
    node = Node(5)
    node.left = Node(3)
    node.right = Node(7)
    assert node._is_interior() == True

def test_node_onlychild_left():
    node = Node(5)
    node.left = Node(3)
    assert node._onlychild() == 'left'

def test_node_onlychild_right():
    node = Node(5)
    node.right = Node(7)
    assert node._onlychild() == 'right'

def test_node_side_left():
    node_parent = Node(5)
    node_child = Node(3, node_parent)
    node_parent.left = node_child
    assert node_child._side() == 'left'

def test_node_side_right():
    node_parent = Node(5)
    node_child = Node(7, node_parent)
    node_parent.right = node_child
    assert node_child._side() == 'right'

def test_insert_and_search(sample_tree):
    sample_tree.insert(9)
    assert sample_tree.search(9).val == 9

def test_size(sample_tree):
    assert sample_tree.size() == 7

def test_depth(sample_tree):
    assert sample_tree.depth() == 3

def test_contains(sample_tree):
    assert sample_tree.contains(6) == True

def test_balance(sample_tree):
    assert sample_tree.balance() == 0

def test_pre_order(sample_tree):
    assert list(sample_tree.pre_order()) == [5, 3, 2, 4, 7, 6, 8]

def test_in_order(sample_tree):
    assert list(sample_tree.in_order()) == [2, 3, 4, 5, 6, 7, 8]

def test_post_order(sample_tree):
    assert list(sample_tree.post_order()) == [2, 4, 3, 6, 8, 7, 5]

def test_breadth_first(sample_tree):
    assert list(sample_tree.breadth_first()) == [5, 3, 7, 2, 4, 6, 8]

def test_delete(sample_tree):
    sample_tree.delete(3)
    assert sample_tree.search(3) is None