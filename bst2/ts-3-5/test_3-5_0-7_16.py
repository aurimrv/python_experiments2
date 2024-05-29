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
        n = Node(5)
        assert n._is_leaf() == True

    def test_is_interior(self):
        n = Node(5)
        assert n._is_interior() == False

    def test_onlychild_left(self):
        n = Node(5)
        n.left = Node(3)
        assert n._onlychild() == 'left'

    def test_onlychild_right(self):
        n = Node(5)
        n.right = Node(7)
        assert n._onlychild() == 'right'

    def test_side_left(self):
        parent = Node(5)
        child = Node(3, parent)
        parent.left = child
        assert child._side() == 'left'

# Test cases for Bst class
class TestBst:
    def test_insert(self):
        b = Bst()
        b.insert(5)
        assert b.root.val == 5

    def test_search_found(self):
        b = Bst([5, 3, 7])
        assert b.search(3).val == 3

    def test_search_not_found(self):
        b = Bst([5, 3, 7])
        assert b.search(10) is None

    def test_size(self):
        b = Bst([5, 3, 7])
        assert b.size() == 3

    def test_depth(self):
        b = Bst([5, 3, 7])
        assert b.depth() == 2

    def test_contains_true(self):
        b = Bst([5, 3, 7])
        assert b.contains(3) == True

    def test_contains_false(self):
        b = Bst([5, 3, 7])
        assert b.contains(10) == False

    def test_balance_positive(self):
        b = Bst([5, 3, 2])
        assert b.balance() > 0

    def test_balance_negative(self):
        b = Bst([5, 7, 9])
        assert b.balance() < 0

    def test_pre_order(self):
        b = Bst([5, 3, 7, 2, 4, 6, 8])
        assert list(b.pre_order()) == [5, 3, 2, 4, 7, 6, 8]

    def test_in_order(self):
        b = Bst([5, 3, 7, 2, 4, 6, 8])
        assert list(b.in_order()) == [2, 3, 4, 5, 6, 7, 8]

    def test_post_order(self):
        b = Bst([5, 3, 7, 2, 4, 6, 8])
        assert list(b.post_order()) == [2, 4, 3, 6, 8, 7, 5]

    def test_breadth_first(self):
        b = Bst([5, 3, 7, 2, 4, 6, 8])
        assert list(b.breadth_first()) == [5, 3, 7, 2, 4, 6, 8]

    def test_delete_leaf(self):
        b = Bst([5, 3, 7])
        b.delete(3)
        assert b.size() == 2

    def test_delete_interior(self):
        b = Bst([5, 3, 7, 4])
        b.delete(3)
        assert b.size() == 3
        assert b.contains(4) == True

    def test_delete_one_child(self):
        b = Bst([5, 3, 7])
        b.delete(3)
        assert b.size() == 2
        assert b.contains(4) == False

    def test_delete_root(self):
        b = Bst([5, 3, 7])
        b.delete(5)
        assert b.size() == 2
        assert b.root.val == 7

    def test_delete_not_found(self):
        b = Bst([5, 3, 7])
        b.delete(10)
        assert b.size() == 3

    def test_find_replacement(self):
        b = Bst([5, 3, 7, 4])
        node = b.search(3)
        replacement = b._find_replacement(node)
        assert replacement.val == 4

    def test_findmin(self):
        b = Bst([5, 3, 7, 4])
        assert b._findmin(b.root).val == 3