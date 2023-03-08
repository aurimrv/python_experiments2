import pytest
from fenwick_tree import FenwickTree

def test_basic_sum():
    lst = [1,5,7,6,4]
    sums = [1,6,13,19,23]
    tree = FenwickTree(lst)

    for i in range(len(lst)):
        assert sums[i] == tree.sum_of_n(i)

def test_sum_range():
    lst = [1,3,8,2,10,6]

    tree = FenwickTree(lst)

    assert 11 == tree.sum_of_range(1,2)
    assert 20 == tree.sum_of_range(2,4)
    assert 30 == tree.sum_of_range(0,5)

def test_modified_tree():
    lst = [1,2,3,4,5]
    sums = [1,3,6,10,15]

    tree = FenwickTree(lst)

    for i in range(len(lst)):
        assert sums[i] == tree.sum_of_n(i)

    tree.update(1,10)
    tree.update(3,1)

    sums = [1,11,14,15,20]

    for i in range(len(lst)):
        assert sums[i] == tree.sum_of_n(i)

