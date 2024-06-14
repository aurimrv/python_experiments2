import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from bst2 import Bst, Node

# Test cases for Node class methods

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
    child = Node(3, parent)
    parent.left = child
    assert child._side() == 'left'

# Test cases for Bst class methods

def test_bst_insert():
    bst = Bst()
    bst.insert(5)
    assert bst.size() == 1

def test_bst_search():
    bst = Bst([5, 3, 7])
    assert bst.search(3).val == 3

def test_bst_size():
    bst = Bst([5, 3, 7])
    assert bst.size() == 3

def test_bst_depth():
    bst = Bst([5, 3, 7])
    assert bst.depth() == 2

def test_bst_contains():
    bst = Bst([5, 3, 7])
    assert bst.contains(7) == True

def test_bst_balance():
    bst = Bst([5, 3, 7])
    assert bst.balance() == 0

def test_bst_pre_order():
    bst = Bst([5, 3, 7])
    assert list(bst.pre_order()) == [5, 3, 7]

def test_bst_in_order():
    bst = Bst([5, 3, 7])
    assert list(bst.in_order()) == [3, 5, 7]

def test_bst_post_order():
    bst = Bst([5, 3, 7])
    assert list(bst.post_order()) == [3, 7, 5]

def test_bst_breadth_first():
    bst = Bst([5, 3, 7])
    assert list(bst.breadth_first()) == [5, 3, 7]

def test_bst_delete():
    bst = Bst([5, 3, 7])
    bst.delete(3)
    assert bst.size() == 2