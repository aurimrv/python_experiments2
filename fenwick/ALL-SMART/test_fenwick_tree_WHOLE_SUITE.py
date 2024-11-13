#Pyguin test cases converted from fenwick/WHOLE_SUITE/seed_1706/test_fenwick_tree.py
import pytest
import fenwick_tree as module_0

def test_case_0():
    dict_0 = {}
    str_0 = "'[SMO`~KND1"
    set_0 = {str_0, str_0}
    float_0 = -2637.078006
    fenwick_tree_0 = module_0.FenwickTree(dict_0)
    assert f'{type(fenwick_tree_0).__module__}.{type(fenwick_tree_0).__qualname__}' == 'fenwick_tree.FenwickTree'
    assert fenwick_tree_0.nums == [0]
    assert fenwick_tree_0.tree == [0]
    var_0 = fenwick_tree_0.sum_of_n(float_0)
    assert var_0 == 0

def test_case_1():
    bool_0 = True
    list_0 = [bool_0, bool_0, bool_0, bool_0]
    fenwick_tree_0 = module_0.FenwickTree(list_0)
    assert f'{type(fenwick_tree_0).__module__}.{type(fenwick_tree_0).__qualname__}' == 'fenwick_tree.FenwickTree'
    assert fenwick_tree_0.nums == [0, True, True, True, True]
    assert fenwick_tree_0.tree == [0, 1, 2, 1, 4]
    var_0 = fenwick_tree_0.sum_of_n(bool_0)
    assert var_0 == 2
    fenwick_tree_1 = module_0.FenwickTree(list_0)
    assert fenwick_tree_1.nums == [0, True, True, True, True]
    assert fenwick_tree_1.tree == [0, 1, 2, 1, 4]
    var_1 = fenwick_tree_1.sum_of_range(bool_0, var_0)
    assert var_1 == 2
    tuple_0 = (bool_0, list_0)

def test_case_2():
    bool_0 = False

def test_case_3():
    set_0 = set()
    none_type_0 = None
    fenwick_tree_0 = module_0.FenwickTree(set_0)
    assert f'{type(fenwick_tree_0).__module__}.{type(fenwick_tree_0).__qualname__}' == 'fenwick_tree.FenwickTree'
    assert fenwick_tree_0.nums == [0]
    assert fenwick_tree_0.tree == [0]
