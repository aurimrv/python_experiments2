import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from bst2 import Bst, Node

@pytest.fixture
def bst_instance():
    return Bst([5, 3, 7, 2, 4, 6, 8])

def test_insert(bst_instance):
    bst_instance.insert(9)
    assert bst_instance.size() == 8
    assert bst_instance.search(9).val == 9

def test_search(bst_instance):
    assert bst_instance.search(7).val == 7
    assert bst_instance.search(10) is None

def test_size(bst_instance):
    assert bst_instance.size() == 7

def test_depth(bst_instance):
    assert bst_instance.depth() == 3

def test_contains(bst_instance):
    assert bst_instance.contains(2) is True
    assert bst_instance.contains(10) is False

def test_balance(bst_instance):
    assert bst_instance.balance() == 0

def test_pre_order(bst_instance):
    assert list(bst_instance.pre_order()) == [5, 3, 2, 4, 7, 6, 8]

def test_in_order(bst_instance):
    assert list(bst_instance.in_order()) == [2, 3, 4, 5, 6, 7, 8]

def test_post_order(bst_instance):
    assert list(bst_instance.post_order()) == [2, 4, 3, 6, 8, 7, 5]

def test_breadth_first(bst_instance):
    assert list(bst_instance.breadth_first()) == [5, 3, 7, 2, 4, 6, 8]

def test_delete(bst_instance):
    bst_instance.delete(2)
    assert bst_instance.size() == 6
    assert bst_instance.contains(2) is False