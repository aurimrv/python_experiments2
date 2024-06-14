import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from bst2 import Bst, Node

@pytest.fixture
def sample_tree():
    data = [5, 3, 7, 2, 4, 6, 8]
    return Bst(data)

def test_node_is_leaf():
    node = Node(10)
    assert node._is_leaf() == True

def test_node_is_interior():
    node = Node(10)
    node.left = Node(5)
    node.right = Node(15)
    assert node._is_interior() == True

def test_node_onlychild():
    node = Node(10)
    node.left = Node(5)
    assert node._onlychild() == 'left'

def test_node_side():
    parent = Node(10)
    node_left = Node(5, parent)
    parent.left = node_left
    assert node_left._side() == 'left'

def test_insert(sample_tree):
    sample_tree.insert(9)
    assert sample_tree.size() == 8

def test_search(sample_tree):
    assert sample_tree.search(7).val == 7

def test_size(sample_tree):
    assert sample_tree.size() == 7

def test_depth(sample_tree):
    assert sample_tree.depth() == 3

def test_contains(sample_tree):
    assert sample_tree.contains(4) == True

def test_balance(sample_tree):
    assert sample_tree.balance() == 0

def test_pre_order(sample_tree):
    expected = [5, 3, 2, 4, 7, 6, 8]
    assert list(sample_tree.pre_order()) == expected

def test_in_order(sample_tree):
    expected = [2, 3, 4, 5, 6, 7, 8]
    assert list(sample_tree.in_order()) == expected

def test_post_order(sample_tree):
    expected = [2, 4, 3, 6, 8, 7, 5]
    assert list(sample_tree.post_order()) == expected

def test_breadth_first(sample_tree):
    expected = [5, 3, 7, 2, 4, 6, 8]
    assert list(sample_tree.breadth_first()) == expected

def test_delete(sample_tree):
    sample_tree.delete(3)
    assert sample_tree.size() == 6
    assert sample_tree.contains(3) == False