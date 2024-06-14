import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from bst2 import Bst, Node

# Test Cases for Bst Class
class TestBst:
    @pytest.fixture
    def bst_instance(self):
        return Bst([5, 3, 8, 1, 4, 7, 9])

    def test_insert(self, bst_instance):
        bst_instance.insert(10)
        assert bst_instance.size() == 8
        assert bst_instance.search(10).val == 10

    def test_search(self, bst_instance):
        assert bst_instance.search(4).val == 4
        assert bst_instance.search(6) is None

    def test_size(self, bst_instance):
        assert bst_instance.size() == 7

    def test_depth(self, bst_instance):
        assert bst_instance.depth() == 3

    def test_contains(self, bst_instance):
        assert bst_instance.contains(7) is True
        assert bst_instance.contains(2) is False

    def test_balance(self, bst_instance):
        assert bst_instance.balance() == 0

    def test_pre_order(self, bst_instance):
        assert list(bst_instance.pre_order()) == [5, 3, 1, 4, 8, 7, 9]

    def test_in_order(self, bst_instance):
        assert list(bst_instance.in_order()) == [1, 3, 4, 5, 7, 8, 9]

    def test_post_order(self, bst_instance):
        assert list(bst_instance.post_order()) == [1, 4, 3, 7, 9, 8, 5]

    def test_breadth_first(self, bst_instance):
        assert list(bst_instance.breadth_first()) == [5, 3, 8, 1, 4, 7, 9]

    def test_delete(self, bst_instance):
        bst_instance.delete(1)
        assert bst_instance.size() == 6
        assert bst_instance.search(1) is None

# Test Cases for Node Class
class TestNode:
    def test_is_leaf(self):
        node = Node(5)
        assert node._is_leaf() is True

    def test_is_interior(self):
        node = Node(5)
        assert node._is_interior() is False

    def test_onlychild(self):
        node = Node(5)
        node.left = Node(3)
        assert node._onlychild() == 'left'

    def test_side(self):
        parent = Node(5)
        node = Node(3, parent)
        parent.left = node
        assert node._side() == 'left'
