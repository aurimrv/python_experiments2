import os
import sys
import pytest

# Setting up sys path to import bst2.py modules
module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from bst2 import Node, Bst

# Test Cases for Node class methods
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
    node = Node(3, parent)
    parent.left = node
    assert node._side() == 'left'

# Test Cases for Bst class methods
def test_insert_single_value():
    bst = Bst()
    bst.insert(5)
    assert bst.size() == 1

def test_insert_multiple_values():
    bst = Bst()
    values = [5, 3, 7, 2, 4, 6, 8]
    for value in values:
        bst.insert(value)
    assert bst.size() == len(values)

def test_search_found():
    bst = Bst([5, 3, 7, 2, 4, 6, 8])
    node = bst.search(4)
    assert node.val == 4

def test_search_not_found():
    bst = Bst([5, 3, 7, 2, 4, 6, 8])
    node = bst.search(9)
    assert node == None

def test_depth():
    bst = Bst([5, 3, 7])
    assert bst.depth() == 2

def test_contains_true():
    bst = Bst([5, 3, 7])
    assert bst.contains(3) == True

def test_contains_false():
    bst = Bst([5, 3, 7])
    assert bst.contains(8) == False

def test_balance():
    bst = Bst([5, 3, 7])
    assert bst.balance() == 0

# Additional Test Cases for Bst class methods can be added similarly
