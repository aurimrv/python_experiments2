import os
import sys
module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from naive_tree import NaiveBinaryTree

import pytest

@pytest.fixture
def sample_tree():
    # Create a sample binary tree for testing
    tree = NaiveBinaryTree()
    class Node:
        def __init__(self, value):
            self.value = value
            self.left = None
            self.right = None
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    tree.head = root
    return tree

def test_pre_order_traversal(sample_tree):
    expected_output = [1, 2, 4, 5, 3, 6, 7]
    assert sample_tree.pre_order_traversal() == expected_output

def test_in_order_traversal(sample_tree):
    expected_output = [4, 2, 5, 1, 6, 3, 7]
    assert sample_tree.in_order_traversal() == expected_output

def test_post_order_traversal(sample_tree):
    expected_output = [4, 5, 2, 6, 7, 3, 1]
    assert sample_tree.post_order_traversal() == expected_output

def test_level_order_traversal(sample_tree):
    expected_output = [1, 2, 3, 4, 5, 6, 7]
    assert sample_tree.level_order_traversal() == expected_output