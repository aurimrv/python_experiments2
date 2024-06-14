import os
import sys

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from bst2 import Bst, Node

import pytest


@pytest.fixture
def sample_tree():
    tree = Bst([8, 3, 10, 1, 6, 4, 7, 14, 13])
    return tree


def test_insert(sample_tree):
    sample_tree.insert(5)
    assert sample_tree.contains(5) == True

    assert sample_tree.size() == 10


def test_search(sample_tree):
    assert sample_tree.search(6).val == 6
    assert sample_tree.search(11) is None


def test_size(sample_tree):
    assert sample_tree.size() == 9


def test_depth(sample_tree):
    assert sample_tree.depth() == 4


def test_contains(sample_tree):
    assert sample_tree.contains(4) == True
    assert sample_tree.contains(12) == False


def test_balance(sample_tree):
    assert sample_tree.balance() == 0


def test_pre_order(sample_tree):
    assert list(sample_tree.pre_order()) == [8, 3, 1, 6, 4, 7, 10, 14, 13]


def test_in_order(sample_tree):
    assert list(sample_tree.in_order()) == [1, 3, 4, 6, 7, 8, 10, 13, 14]


def test_post_order(sample_tree):
    assert list(sample_tree.post_order()) == [1, 4, 7, 6, 3, 13, 14, 10, 8]


def test_breadth_first(sample_tree):
    assert list(sample_tree.breadth_first()) == [8, 3, 10, 1, 6, 14, 4, 7, 13]


def test_delete(sample_tree):
    sample_tree.delete(6)
    assert sample_tree.contains(6) == False

    sample_tree.delete(8)
    assert sample_tree.contains(8) == False