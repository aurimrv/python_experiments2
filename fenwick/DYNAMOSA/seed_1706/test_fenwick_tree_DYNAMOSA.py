#Pyguin test cases converted from fenwick/DYNAMOSA/seed_1706/test_fenwick_tree.py
import pytest
import fenwick_tree as module_0

def test_case_0():
    bytes_0 = b'\xf1\xd15\xe2 \xcb\xff\xc3\xa9\xd1J'
    fenwick_tree_0 = module_0.FenwickTree(bytes_0)
    assert f'{type(fenwick_tree_0).__module__}.{type(fenwick_tree_0).__qualname__}' == 'fenwick_tree.FenwickTree'
    assert fenwick_tree_0.nums == [0, 241, 209, 53, 226, 32, 203, 255, 195, 169, 209, 74]
    assert fenwick_tree_0.tree == [0, 241, 450, 53, 729, 32, 235, 255, 1414, 169, 378, 74]

def test_case_1():
    none_type_0 = None
    int_0 = -1409
    int_1 = -2021
    list_0 = [int_1, int_1, int_1, int_1]
    fenwick_tree_0 = module_0.FenwickTree(list_0)
    assert f'{type(fenwick_tree_0).__module__}.{type(fenwick_tree_0).__qualname__}' == 'fenwick_tree.FenwickTree'
    assert fenwick_tree_0.nums == [0, -2021, -2021, -2021, -2021]
    assert fenwick_tree_0.tree == [0, -2021, -4042, -2021, -8084]
    var_0 = fenwick_tree_0.sum_of_n(int_0)
    assert var_0 == 0

def test_case_2():
    none_type_0 = None

def test_case_3():
    bytes_0 = b'\xf1\xd15\xe2 \xcb\xff\xc3\xa9\xd1J'
    fenwick_tree_0 = module_0.FenwickTree(bytes_0)
    assert f'{type(fenwick_tree_0).__module__}.{type(fenwick_tree_0).__qualname__}' == 'fenwick_tree.FenwickTree'
    assert fenwick_tree_0.nums == [0, 241, 209, 53, 226, 32, 203, 255, 195, 169, 209, 74]
    assert fenwick_tree_0.tree == [0, 241, 450, 53, 729, 32, 235, 255, 1414, 169, 378, 74]

def test_case_4():
    int_0 = 12
    list_0 = [int_0, int_0, int_0, int_0]
    fenwick_tree_0 = module_0.FenwickTree(list_0)
    assert f'{type(fenwick_tree_0).__module__}.{type(fenwick_tree_0).__qualname__}' == 'fenwick_tree.FenwickTree'
    assert fenwick_tree_0.nums == [0, 12, 12, 12, 12]
    assert fenwick_tree_0.tree == [0, 12, 24, 12, 48]

def test_case_5():
    float_0 = -1000.3163
    int_0 = -1409
    list_0 = [int_0, int_0, int_0, int_0]
    fenwick_tree_0 = module_0.FenwickTree(list_0)
    assert f'{type(fenwick_tree_0).__module__}.{type(fenwick_tree_0).__qualname__}' == 'fenwick_tree.FenwickTree'
    assert fenwick_tree_0.nums == [0, -1409, -1409, -1409, -1409]
    assert fenwick_tree_0.tree == [0, -1409, -2818, -1409, -5636]
    var_0 = fenwick_tree_0.sum_of_range(float_0, int_0)
    assert var_0 == 0
    var_1 = fenwick_tree_0.sum_of_range(var_0, var_0)
    assert var_1 == -1409

def test_case_6():
    float_0 = -1000.3163
    int_0 = 2
    int_1 = -2021
    list_0 = [int_1, int_1, int_1, int_1]
    fenwick_tree_0 = module_0.FenwickTree(list_0)
    assert f'{type(fenwick_tree_0).__module__}.{type(fenwick_tree_0).__qualname__}' == 'fenwick_tree.FenwickTree'
    assert fenwick_tree_0.nums == [0, -2021, -2021, -2021, -2021]
    assert fenwick_tree_0.tree == [0, -2021, -4042, -2021, -8084]
    var_0 = fenwick_tree_0.sum_of_range(float_0, int_0)
    assert var_0 == -6063
    bool_0 = True
    var_1 = fenwick_tree_0.sum_of_range(bool_0, bool_0)
    assert var_1 == -2021
