import os
import sys

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from binary_search_tree import BinarySearchTree

import pytest
from tree_node import BinaryTreeNode

@pytest.fixture
def binary_search_tree():
    return BinarySearchTree()

def test_insert_single_node(binary_search_tree):
    binary_search_tree.insert(5)
    assert binary_search_tree.head.value == 5

def test_insert_multiple_nodes(binary_search_tree):
    binary_search_tree.insert(5)
    binary_search_tree.insert(3)
    binary_search_tree.insert(7)
    assert binary_search_tree.head.left.value == 3
    assert binary_search_tree.head.right.value == 7

def test_min(binary_search_tree):
    binary_search_tree.insert(5)
    binary_search_tree.insert(3)
    binary_search_tree.insert(7)
    assert binary_search_tree.min() == 3

def test_delete(binary_search_tree):
    binary_search_tree.insert(5)
    binary_search_tree.insert(3)
    binary_search_tree.insert(7)
    binary_search_tree.delete(5)
    assert binary_search_tree.head.value == 7

def test_search(binary_search_tree):
    binary_search_tree.insert(5)
    binary_search_tree.insert(3)
    binary_search_tree.insert(7)
    assert binary_search_tree.search(3).value == 3

def test_in_order_traversal(binary_search_tree):
    binary_search_tree.insert(5)
    binary_search_tree.insert(3)
    binary_search_tree.insert(7)
    assert binary_search_tree.in_order_traversal() == [3, 5, 7]

def test_merge(binary_search_tree):
    binary_search_tree.insert(5)
    binary_search_tree.insert(3)
    
    tree_to_merge = BinarySearchTree()
    tree_to_merge.insert(7)
    
    binary_search_tree.merge(tree_to_merge)
    
    assert binary_search_tree.head.value == 12