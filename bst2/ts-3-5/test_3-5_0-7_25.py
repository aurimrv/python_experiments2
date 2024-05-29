import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from bst2 import Bst, Node

# Test Node class methods
def test_node_is_leaf():
    node = Node(5)
    assert node._is_leaf() == True

def test_node_is_interior():
    node = Node(5)
    assert node._is_interior() == False

def test_node_onlychild():
    node = Node(5)
    assert node._onlychild() == None

def test_node_side():
    parent_node = Node(10)
    child_node = Node(5, parent_node)
    parent_node.left = child_node
    assert child_node._side() == 'left'

# Test Bst class methods
def test_bst_insert():
    bst = Bst()
    bst.insert(5)
    assert bst.size() == 1
    assert bst.root.val == 5

def test_bst_search():
    bst = Bst([5, 10, 15])
    assert bst.search(10).val == 10

def test_bst_depth():
    bst = Bst([5, 3, 7, 2, 4, 6, 8])
    assert bst.depth() == 4

def test_bst_contains():
    bst = Bst([5, 10, 15])
    assert bst.contains(10) == True
    assert bst.contains(20) == False

def test_bst_balance():
    bst = Bst([5, 3, 7, 2, 4, 6, 8])
    assert bst.balance() == 0

def test_bst_pre_order():
    bst = Bst([5, 3, 7, 2, 4, 6, 8])
    assert list(bst.pre_order()) == [5, 3, 2, 4, 7, 6, 8]

def test_bst_in_order():
    bst = Bst([5, 3, 7, 2, 4, 6, 8])
    assert list(bst.in_order()) == [2, 3, 4, 5, 6, 7, 8]

def test_bst_post_order():
    bst = Bst([5, 3, 7, 2, 4, 6, 8])
    assert list(bst.post_order()) == [2, 4, 3, 6, 8, 7, 5]

def test_bst_breadth_first():
    bst = Bst([5, 3, 7, 2, 4, 6, 8])
    assert list(bst.breadth_first()) == [5, 3, 7, 2, 4, 6, 8]