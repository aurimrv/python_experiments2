import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from bst2 import Bst, Node


@pytest.fixture
def sample_tree():
    return Bst([5, 3, 7, 2, 4, 6, 8])


def test_insert(sample_tree):
    assert sample_tree.size() == 7

    # Test inserting existing value
    sample_tree.insert(5)
    assert sample_tree.size() == 7

    # Test inserting new value
    sample_tree.insert(9)
    assert sample_tree.size() == 8
    assert sample_tree.search(9).val == 9


def test_search(sample_tree):
    assert sample_tree.search(3).val == 3
    assert sample_tree.search(10) is None


def test_size(sample_tree):
    assert sample_tree.size() == 7


def test_depth(sample_tree):
    assert sample_tree.depth() == 3


def test_contains(sample_tree):
    assert sample_tree.contains(4) is True
    assert sample_tree.contains(10) is False


def test_balance_empty():
    empty_tree = Bst()
    assert empty_tree.balance() == 0


def test_balance_sample_tree(sample_tree):
    assert sample_tree.balance() == 0


def test_pre_order(sample_tree):
    assert list(sample_tree.pre_order()) == [5, 3, 2, 4, 7, 6, 8]


def test_in_order(sample_tree):
    assert list(sample_tree.in_order()) == [2, 3, 4, 5, 6, 7, 8]


def test_post_order(sample_tree):
    assert list(sample_tree.post_order()) == [2, 4, 3, 6, 8, 7, 5]


def test_breadth_first(sample_tree):
    assert list(sample_tree.breadth_first()) == [5, 3, 7, 2, 4, 6, 8]


def test_delete(sample_tree):
    sample_tree.delete(2)
    assert sample_tree.size() == 6
    assert sample_tree.search(2) is None

    sample_tree.delete(5)
    assert sample_tree.size() == 5
    assert sample_tree.search(5) is None