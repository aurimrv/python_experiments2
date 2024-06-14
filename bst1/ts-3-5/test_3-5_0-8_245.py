import os
import sys

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from binary_search_tree import BinarySearchTree, BinaryTreeNode

import pytest

# Test cases for BinarySearchTree class
class TestBinarySearchTree:

    @pytest.fixture
    def bst(self):
        return BinarySearchTree()
    
    def test_insert(self, bst):
        bst.insert(5)
        assert bst.head.value == 5
        
        bst.insert(3)
        assert bst.head.left.value == 3

        bst.insert(7)
        assert bst.head.right.value == 7

    def test_min(self, bst):
        bst.insert(10)
        bst.insert(5)
        bst.insert(15)
        assert bst.min() == 5

    def test_delete(self, bst):
        bst.insert(10)
        bst.insert(5)
        bst.insert(15)
        bst.delete(10)
        assert bst.head.value == 15

    def test_search(self, bst):
        bst.insert(10)
        bst.insert(5)
        bst.insert(15)
        assert bst.search(5).value == 5
        assert bst.search(20) is None

    def test_in_order_traversal(self, bst):
        bst.insert(10)
        bst.insert(5)
        bst.insert(15)
        bst.insert(2)
        bst.insert(7)
        assert bst.in_order_traversal() == [2, 5, 7, 10, 15]

    def test_merge(self, bst):
        bst1 = BinarySearchTree()
        bst1.insert(5)
        bst1.insert(3)

        bst2 = BinarySearchTree()
        bst2.insert(8)
        bst2.insert(10)

        bst1.merge(bst2)
        
        assert bst1.head.value == 13
        assert bst1.head.left.value == 3
        assert bst1.head.right.value == 10