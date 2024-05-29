import os
import sys
import pytest

# Add project directory to the sys path for correct imports
module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

# Import the module to be tested
from bst2 import Bst, Node


@pytest.fixture
def bst_empty():
    return Bst()


@pytest.fixture
def bst_filled():
    return Bst([5, 3, 8, 2, 4, 7, 9])


def test_insert(bst_empty):
    bst_empty.insert(5)
    assert bst_empty.size() == 1
    bst_empty.insert(3)
    assert bst_empty.size() == 2
    bst_empty.insert(8)
    assert bst_empty.size() == 3


def test_search(bst_filled):
    assert bst_filled.search(5).val == 5
    assert bst_filled.search(3).val == 3
    assert bst_filled.search(8).val == 8
    assert bst_filled.search(10) is None


def test_size(bst_empty, bst_filled):
    assert bst_empty.size() == 0
    assert bst_filled.size() == 7


def test_depth(bst_empty, bst_filled):
    assert bst_empty.depth() == 0
    assert bst_filled.depth() == 3


def test_contains(bst_filled):
    assert bst_filled.contains(5) is True
    assert bst_filled.contains(10) is False


def test_balance(bst_filled):
    assert bst_filled.balance() == 0


def test_pre_order(bst_filled):
    assert list(bst_filled.pre_order()) == [5, 3, 2, 4, 8, 7, 9]


def test_in_order(bst_filled):
    assert list(bst_filled.in_order()) == [2, 3, 4, 5, 7, 8, 9]


def test_post_order(bst_filled):
    assert list(bst_filled.post_order()) == [2, 4, 3, 7, 9, 8, 5]


def test_breadth_first(bst_filled):
    assert list(bst_filled.breadth_first()) == [5, 3, 8, 2, 4, 7, 9]