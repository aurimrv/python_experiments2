import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from bst2 import Bst, Node

# Test cases for Node class methods
class TestNode:
    def test_is_leaf(self):
        node = Node(5)
        assert node._is_leaf() == True

    def test_is_interior(self):
        node = Node(5)
        assert node._is_interior() == False

    def test_onlychild_left(self):
        node = Node(5)
        node.left = Node(3)
        assert node._onlychild() == 'left'

    def test_onlychild_right(self):
        node = Node(5)
        node.right = Node(7)
        assert node._onlychild() == 'right'

    def test_side_left(self):
        parent = Node(5)
        node = Node(3, parent)
        parent.left = node
        assert node._side() == 'left'

# Test cases for Bst class methods
class TestBst:
    def test_insert_single_value(self):
        bst = Bst()
        bst.insert(5)
        assert bst.size() == 1

    def test_insert_duplicate_value(self):
        bst = Bst([5, 3, 7])
        bst.insert(5)
        assert bst.size() == 3

    def test_search_existing_value(self):
        bst = Bst([5, 3, 7])
        assert bst.search(3).val == 3

    def test_search_non_existing_value(self):
        bst = Bst([5, 3, 7])
        assert bst.search(10) == None

    def test_size_empty_tree(self):
        bst = Bst()
        assert bst.size() == 0

    def test_depth_single_node(self):
        bst = Bst([5])
        assert bst.depth() == 1

    def test_depth_multiple_nodes(self):
        bst = Bst([5, 3, 7])
        assert bst.depth() == 2

    def test_contains_existing_value(self):
        bst = Bst([5, 3, 7])
        assert bst.contains(3) == True

    def test_contains_non_existing_value(self):
        bst = Bst([5, 3, 7])
        assert bst.contains(10) == False

    def test_balance_empty_tree(self):
        bst = Bst()
        assert bst.balance() == 0

    def test_pre_order_traversal(self):
        bst = Bst([5, 3, 7])
        assert list(bst.pre_order()) == [5, 3, 7]

    def test_in_order_traversal(self):
        bst = Bst([5, 3, 7])
        assert list(bst.in_order()) == [3, 5, 7]

    def test_post_order_traversal(self):
        bst = Bst([5, 3, 7])
        assert list(bst.post_order()) == [3, 7, 5]

    def test_breadth_first_traversal(self):
        bst = Bst([5, 3, 7, 2, 4, 6, 8])
        assert list(bst.breadth_first()) == [5, 3, 7, 2, 4, 6, 8]

    def test_delete_leaf_node(self):
        bst = Bst([5, 3, 7])
        bst.delete(3)
        assert bst.size() == 2

    def test_delete_interior_node(self):
        bst = Bst([5, 3, 7, 2, 4, 6, 8])
        bst.delete(7)
        assert bst.size() == 6

    def test_delete_root_node(self):
        bst = Bst([5, 3, 7])
        bst.delete(5)
        assert bst.size() == 2