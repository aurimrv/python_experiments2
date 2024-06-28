import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from naive_tree import NaiveBinaryTree

@pytest.fixture
def sample_binary_tree():
    binary_tree = NaiveBinaryTree()
    # Create a sample binary tree for testing
    class Node:
        def __init__(self, value):
            self.value = value
            self.left = None
            self.right = None
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)
    n5 = Node(5)
    n6 = Node(6)
    n7 = Node(7)
    binary_tree.head = n1
    n1.left = n2
    n1.right = n3
    n2.left = n4
    n2.right = n5
    n3.left = n6
    n3.right = n7
    return binary_tree

def test_pre_order_traversal(sample_binary_tree):
    assert sample_binary_tree.pre_order_traversal() == [1, 2, 4, 5, 3, 6, 7]

def test_in_order_traversal(sample_binary_tree):
    assert sample_binary_tree.in_order_traversal() == [4, 2, 5, 1, 6, 3, 7]

def test_post_order_traversal(sample_binary_tree):
    assert sample_binary_tree.post_order_traversal() == [4, 5, 2, 6, 7, 3, 1]

def test_level_order_traversal(sample_binary_tree):
    assert sample_binary_tree.level_order_traversal() == [1, 2, 3, 4, 5, 6, 7]