import os
import sys

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from bst2 import Bst, Node

# Test cases for Node class
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
    parent = Node(10)
    n = Node(5, parent)
    parent.left = n
    assert n._side() == 'left'


# Test cases for Bst class
def test_bst_insert():
    bst = Bst()
    bst.insert(5)
    assert bst.size() == 1

def test_bst_search():
    bst = Bst([5, 3, 7, 1, 4])
    assert bst.search(4).val == 4

def test_bst_depth():
    bst = Bst([5, 3, 7, 1, 4])
    assert bst.depth() == 3

def test_bst_contains():
    bst = Bst([5, 3, 7, 1, 4])
    assert bst.contains(7) == True

def test_bst_balance():
    bst = Bst([5, 3, 7, 1, 4])
    assert bst.balance() == 1

def test_bst_pre_order():
    bst = Bst([5, 3, 7, 1, 4])
    assert list(bst.pre_order()) == [5, 3, 1, 4, 7]

def test_bst_in_order():
    bst = Bst([5, 3, 7, 1, 4])
    assert list(bst.in_order()) == [1, 3, 4, 5, 7]

def test_bst_post_order():
    bst = Bst([5, 3, 7, 1, 4])
    assert list(bst.post_order()) == [1, 4, 3, 7, 5]

def test_bst_breadth_first():
    bst = Bst([5, 3, 7, 1, 4])
    assert list(bst.breadth_first()) == [5, 3, 7, 1, 4]

def test_bst_delete():
    bst = Bst([5, 3, 7, 1, 4])
    bst.delete(3)
    assert bst.size() == 4