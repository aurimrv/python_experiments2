import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from bst2 import Node, Bst

# Test Cases for Node Class Methods
def test_node_is_leaf():
    n = Node(5)
    assert n._is_leaf() == True

def test_node_is_interior():
    n = Node(5)
    n.left = Node(3)
    n.right = Node(7)
    assert n._is_interior() == True

def test_node_onlychild():
    n = Node(5)
    n.left = Node(3)
    assert n._onlychild() == 'left'

def test_node_side():
    parent = Node(5)
    child = Node(3, parent)
    parent.left = child
    assert child._side() == 'left'

# Test Cases for Bst Class Methods
def test_bst_insert():
    bst = Bst()
    bst.insert(5)
    assert bst.size() == 1
    bst.insert(3)
    bst.insert(7)
    assert bst.size() == 3

def test_bst_search():
    bst = Bst([5, 3, 7])
    assert bst.search(3).val == 3
    assert bst.search(10) == None

def test_bst_depth():
    bst = Bst([5, 3, 7, 1, 4])
    assert bst.depth() == 3

def test_bst_contains():
    bst = Bst([5, 3, 7])
    assert bst.contains(3) == True
    assert bst.contains(10) == False

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
    assert list(bst.in_order()) == [5, 7]
    assert bst.size() == 2
    bst.delete(10)
    assert list(bst.in_order()) == [5, 7]
    assert bst.size() == 2