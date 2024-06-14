import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from bst2 import Bst, Node


# Test cases for Node class

def test_is_leaf():
    node = Node(5)
    assert node._is_leaf() == True

def test_is_interior():
    node = Node(5)
    node.right = Node(7)
    assert node._is_interior() == False

def test_onlychild():
    node = Node(5)
    node.left = Node(3)
    assert node._onlychild() == 'left'
    node.left = None
    node.right = Node(7)
    assert node._onlychild() == 'right'

def test_side():
    parent = Node(5)
    parent.left = Node(3, parent)
    parent.right = Node(7, parent)
    assert parent.left._side() == 'left'
    assert parent.right._side() == 'right'


# Test cases for Bst class

def test_insert():
    tree = Bst()
    tree.insert(5)
    assert tree.size() == 1
    tree.insert(3)
    tree.insert(7)
    assert tree.size() == 3

def test_search():
    tree = Bst([5, 3, 7])
    assert tree.search(3).val == 3
    assert tree.search(10) == None

def test_size():
    tree = Bst()
    assert tree.size() == 0
    tree.insert(5)
    assert tree.size() == 1

def test_depth():
    tree = Bst([5, 3, 7])
    assert tree.depth() == 2

def test_contains():
    tree = Bst([5, 3, 7])
    assert tree.contains(3) == True
    assert tree.contains(10) == False

def test_balance():
    tree = Bst([5, 3, 7])
    assert tree.balance() == 0

# Additional test cases can be added for the remaining methods.

