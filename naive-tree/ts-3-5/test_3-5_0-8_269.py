import os
import sys
module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from naive_tree import NaiveBinaryTree

import pytest

@pytest.fixture
def sample_binary_tree():
    # Create a sample binary tree for testing
    tree = NaiveBinaryTree()
    class Node:
        def __init__(self, value):
            self.value = value
            self.left = None
            self.right = None
    
    tree.head = Node(1)
    tree.head.left = Node(2)
    tree.head.right = Node(3)
    tree.head.left.left = Node(4)
    tree.head.left.right = Node(5)
    tree.head.right.left = Node(6)
    tree.head.right.right = Node(7)
    
    return tree

def test_pre_order_traversal(sample_binary_tree):
    assert sample_binary_tree.pre_order_traversal() == [1, 2, 4, 5, 3, 6, 7]
    # Additional test
    assert sample_binary_tree.pre_order_traversal() != [1, 2, 3, 4, 5, 6, 7]

def test_in_order_traversal(sample_binary_tree):
    assert sample_binary_tree.in_order_traversal() == [4, 2, 5, 1, 6, 3, 7]
    # Additional test
    assert sample_binary_tree.in_order_traversal() != [4, 2, 1, 5, 6, 3, 7]

def test_post_order_traversal(sample_binary_tree):
    assert sample_binary_tree.post_order_traversal() == [4, 5, 2, 6, 7, 3, 1]
    # Additional test
    assert sample_binary_tree.post_order_traversal() != [4, 2, 5, 1, 6, 7, 3]

def test_level_order_traversal(sample_binary_tree):
    assert sample_binary_tree.level_order_traversal() == [1, 2, 3, 4, 5, 6, 7]
    # Additional test
    assert sample_binary_tree.level_order_traversal() != [1, 3, 2, 7, 6, 5, 4]