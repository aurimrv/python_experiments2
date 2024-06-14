import os
import sys
module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from binary_search_tree import BinarySearchTree, BinaryTreeNode

import pytest

# Test cases for BinarySearchTree class
class TestBinarySearchTree:

    def test_insert_single_node(self):
        bst = BinarySearchTree()
        bst.insert(5)
        assert bst.head.value == 5

    def test_insert_multiple_nodes(self):
        bst = BinarySearchTree()
        bst.insert(5)
        bst.insert(3)
        bst.insert(7)
        assert bst.head.value == 5
        assert bst.head.left.value == 3
        assert bst.head.right.value == 7

    def test_min(self):
        bst = BinarySearchTree()
        bst.insert(10)
        bst.insert(5)
        bst.insert(15)
        assert bst.min() == 5

    def test_delete_node(self):
        bst = BinarySearchTree()
        bst.insert(10)
        bst.insert(5)
        bst.insert(15)
        bst.delete(5)
        assert bst.head.left is None

    def test_search_existing_node(self):
        bst = BinarySearchTree()
        bst.insert(10)
        bst.insert(5)
        bst.insert(15)
        result = bst.search(5)
        assert result.value == 5

    def test_search_non_existing_node(self):
        bst = BinarySearchTree()
        bst.insert(10)
        bst.insert(5)
        bst.insert(15)
        result = bst.search(20)
        assert result is None

    def test_in_order_traversal(self):
        bst = BinarySearchTree()
        bst.insert(10)
        bst.insert(5)
        bst.insert(15)
        assert bst.in_order_traversal() == [5, 10, 15]

    def test_merge_empty_trees(self):
        bst1 = BinarySearchTree()
        bst2 = BinarySearchTree()
        bst1.merge(bst2)
        assert bst1.head is None

    def test_merge_non_empty_trees(self):
        bst1 = BinarySearchTree()
        bst1.insert(10)
        bst1.insert(5)
        bst2 = BinarySearchTree()
        bst2.insert(15)
        bst2.insert(20)
        bst1.merge(bst2)
        assert bst1.head.value == 25
        assert bst1.head.left.value == 5
        assert bst1.head.right.value == 20
