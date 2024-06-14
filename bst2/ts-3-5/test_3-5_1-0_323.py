import os
import sys

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from bst2 import Bst, Node


def test_insert():
    bst = Bst()
    bst.insert(5)
    assert bst.size() == 1
    assert bst.search(5).val == 5

    bst.insert(3)
    assert bst.size() == 2
    assert bst.search(3).val == 3

def test_search():
    bst = Bst([5, 3, 7, 1, 4])
    assert bst.search(7).val == 7
    assert bst.search(2) is None

def test_size():
    bst = Bst([1, 2, 3, 4, 5])
    assert bst.size() == 5

def test_depth():
    bst = Bst([6, 3, 9, 1])
    assert bst.depth() == 3

def test_contains():
    bst = Bst([10, 7, 15, 3])
    assert bst.contains(7) is True
    assert bst.contains(12) is False

def test_balance():
    bst = Bst([5, 3, 8, 2, 4, 7, 9])
    assert bst.balance() == 0

def test_pre_order():
    bst = Bst([5, 3, 7, 2, 4, 6, 8])
    assert list(bst.pre_order()) == [5, 3, 2, 4, 7, 6, 8]

def test_in_order():
    bst = Bst([5, 3, 7, 2, 4, 6, 8])
    assert list(bst.in_order()) == [2, 3, 4, 5, 6, 7, 8]

def test_post_order():
    bst = Bst([5, 3, 7, 2, 4, 6, 8])
    assert list(bst.post_order()) == [2, 4, 3, 6, 8, 7, 5]


def test_breadth_first():
    bst = Bst([5, 3, 7, 2, 4, 6, 8])
    assert list(bst.breadth_first()) == [5, 3, 7, 2, 4, 6, 8]

def test_delete():
    bst = Bst([5, 3, 7, 2, 4, 6, 8])
    bst.delete(3)
    assert bst.size() == 6
    assert list(bst.in_order()) == [2, 4, 5, 6, 7, 8]