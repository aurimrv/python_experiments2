import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from bst2 import Node, Bst

# Test cases for Node class
def test_node_is_leaf():
    node = Node(10)
    assert node._is_leaf() == True

def test_node_is_interior():
    node = Node(10)
    node.left = Node(5)
    node.right = Node(15)
    assert node._is_interior() == True

# Test cases for Bst class
def test_insert():
    bst = Bst()
    bst.insert(10)
    bst.insert(5)
    assert bst.size() == 2
    assert bst.root.val == 10
    assert bst.root.left.val == 5

def test_search():
    bst = Bst([10, 5, 15])
    assert bst.search(15).val == 15
    assert bst.search(20) == None

def test_depth():
    bst = Bst([10, 5, 15])
    assert bst.depth() == 2

def test_contains():
    bst = Bst([10, 5, 15])
    assert bst.contains(5) == True
    assert bst.contains(12) == False

def test_balance():
    bst = Bst([10, 5, 15])
    assert bst.balance() == 0

# Add more test cases for other methods as needed