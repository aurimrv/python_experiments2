import os
import sys
module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from binary_search_tree import BinarySearchTree, BinaryTreeNode

import pytest

class TestBinarySearchTree:

    def test_insert_one_node(self):
        tree = BinarySearchTree()
        tree.insert(5)
        assert tree.head.value == 5

    def test_insert_multiple_nodes(self):
        tree = BinarySearchTree()
        tree.insert(5)
        tree.insert(3)
        tree.insert(7)
        assert tree.head.value == 5
        assert tree.head.left.value == 3
        assert tree.head.right.value == 7

    def test_min(self):
        tree = BinarySearchTree()
        tree.insert(5)
        tree.insert(3)
        tree.insert(7)
        assert tree.min() == 3

    def test_delete_node(self):
        tree = BinarySearchTree()
        tree.insert(5)
        tree.insert(3)
        tree.insert(7)
        tree.delete(3)
        assert tree.head.left is None

    def test_search_existing_node(self):
        tree = BinarySearchTree()
        tree.insert(5)
        tree.insert(3)
        tree.insert(7)
        assert tree.search(3).value == 3

    def test_search_non_existing_node(self):
        tree = BinarySearchTree()
        tree.insert(5)
        tree.insert(3)
        tree.insert(7)
        assert tree.search(8) is None

    def test_in_order_traversal(self):
        tree = BinarySearchTree()
        tree.insert(5)
        tree.insert(3)
        tree.insert(7)
        assert tree.in_order_traversal() == [3, 5, 7]

    def test_merge_trees(self):
        tree1 = BinarySearchTree()
        tree1.insert(5)
        tree1.insert(3)
        
        tree2 = BinarySearchTree()
        tree2.insert(7)
        tree2.insert(9)

        tree1.merge(tree2)
        assert tree1.head.value == 12
        assert tree1.head.right.value == 9
