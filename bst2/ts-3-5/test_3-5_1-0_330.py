import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)
from bst2 import Bst, Node

# Test cases for Node class
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

    def test_side_parent_left(self):
        parent = Node(5)
        child = Node(3, parent)
        parent.left = child
        assert child._side() == 'left'

    def test_side_parent_right(self):
        parent = Node(5)
        child = Node(7, parent)
        parent.right = child
        assert child._side() == 'right'

# Test cases for Binary Search Tree class
class TestBst:
    def test_insert_empty_tree(self):
        bst = Bst()
        bst.insert(5)
        assert bst.root.val == 5

    def test_insert_nonempty_tree(self):
        bst = Bst([5, 3, 7])
        bst.insert(4)
        assert bst.root.left.right.val == 4

    def test_search_exists(self):
        bst = Bst([5, 3, 7])
        assert bst.search(3).val == 3

    def test_search_not_exists(self):
        bst = Bst([5, 3, 7])
        assert bst.search(10) is None

    def test_size_empty_tree(self):
        bst = Bst()
        assert bst.size() == 0

    def test_size_nonempty_tree(self):
        bst = Bst([5, 3, 7])
        assert bst.size() == 3

    def test_depth_empty_tree(self):
        bst = Bst()
        assert bst.depth() == 0

    def test_depth_nonempty_tree(self):
        bst = Bst([5, 3, 7])
        assert bst.depth() == 2

    def test_contains_true(self):
        bst = Bst([5, 3, 7])
        assert bst.contains(3) == True

    def test_contains_false(self):
        bst = Bst([5, 3, 7])
        assert bst.contains(10) == False

    def test_balance_balanced_tree(self):
        bst = Bst([3, 2, 4])
        assert bst.balance() == 0

    def test_balance_left_heavy(self):
        bst = Bst([5, 4, 3])
        assert bst.balance() > 0

    def test_balance_right_heavy(self):
        bst = Bst([3, 4, 5])
        assert bst.balance() < 0

    # More test cases can be added for the remaining methods.
