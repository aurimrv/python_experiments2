import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from bst2 import Bst, Node

@pytest.fixture
def bst_fixture():
    bst = Bst([5, 3, 8, 2, 4, 7, 9])
    return bst

def test_insert(bst_fixture):
    bst_fixture.insert(6)
    assert bst_fixture.search(6)
    assert bst_fixture.size() == 8

def test_search(bst_fixture):
    assert bst_fixture.search(7).val == 7
    assert bst_fixture.search(10) is None

def test_size(bst_fixture):
    assert bst_fixture.size() == 7

def test_depth(bst_fixture):
    assert bst_fixture.depth() == 3

def test_contains(bst_fixture):
    assert bst_fixture.contains(3)
    assert not bst_fixture.contains(10)

def test_balance(bst_fixture):
    assert bst_fixture.balance() == 0

def test_pre_order(bst_fixture):
    expected_result = [5, 3, 2, 4, 8, 7, 9]
    assert list(bst_fixture.pre_order()) == expected_result

def test_in_order(bst_fixture):
    expected_result = [2, 3, 4, 5, 7, 8, 9]
    assert list(bst_fixture.in_order()) == expected_result

def test_post_order(bst_fixture):
    expected_result = [2, 4, 3, 7, 9, 8, 5]
    assert list(bst_fixture.post_order()) == expected_result

def test_breadth_first(bst_fixture):
    expected_result = [5, 3, 8, 2, 4, 7, 9]
    assert list(bst_fixture.breadth_first()) == expected_result

def test_delete(bst_fixture):
    bst_fixture.delete(7)
    assert not bst_fixture.search(7)
    assert bst_fixture.size() == 6