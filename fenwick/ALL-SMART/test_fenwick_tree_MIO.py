#Pyguin test cases converted from fenwick/MIO/seed_1706/test_fenwick_tree.py
import pytest
import fenwick_tree as module_0

def test_case_0():
    bytes_0 = b'8\x99\x12\xeddT\x99>t\xc92\x9f\x91\x9c\x0c\xe0n\xd8'
    fenwick_tree_0 = module_0.FenwickTree(bytes_0)
    assert f'{type(fenwick_tree_0).__module__}.{type(fenwick_tree_0).__qualname__}' == 'fenwick_tree.FenwickTree'
    assert fenwick_tree_0.nums == [0, 56, 153, 18, 237, 100, 84, 153, 62, 116, 201, 50, 159, 145, 156, 12, 224, 110, 216]
    assert fenwick_tree_0.tree == [0, 56, 209, 18, 464, 100, 184, 153, 863, 116, 317, 50, 526, 145, 301, 12, 1926, 110, 326]

def test_case_1():
    bytes_0 = b'\x92\xb1-\xa2\x0b\xcc\xe3\xaa\x19\x16\xf2K\xf9\xe7'
    fenwick_tree_0 = module_0.FenwickTree(bytes_0)
    assert f'{type(fenwick_tree_0).__module__}.{type(fenwick_tree_0).__qualname__}' == 'fenwick_tree.FenwickTree'
    assert fenwick_tree_0.nums == [0, 146, 177, 45, 162, 11, 204, 227, 170, 25, 22, 242, 75, 249, 231]
    assert fenwick_tree_0.tree == [0, 146, 323, 45, 530, 11, 215, 227, 1142, 25, 47, 242, 364, 249, 480]
    int_0 = 12
    var_0 = fenwick_tree_0.sum_of_n(int_0)
    assert var_0 == 1755

def test_case_2():
    bytes_0 = b'\xe2\xbdbc\xa4\x03\x01\xbb\xdcdW\x84a\xbd\xa1e\n\xba\x19\x8b'
    fenwick_tree_0 = module_0.FenwickTree(bytes_0)
    assert f'{type(fenwick_tree_0).__module__}.{type(fenwick_tree_0).__qualname__}' == 'fenwick_tree.FenwickTree'
    assert fenwick_tree_0.nums == [0, 226, 189, 98, 99, 164, 3, 1, 187, 220, 100, 87, 132, 97, 189, 161, 101, 10, 186, 25, 139]
    assert fenwick_tree_0.tree == [0, 226, 415, 98, 612, 164, 167, 1, 967, 220, 320, 87, 539, 97, 286, 161, 2054, 10, 196, 25, 360]
    bool_0 = True
    var_0 = fenwick_tree_0.sum_of_range(bool_0, bool_0)
    assert var_0 == 189

def test_case_3():
    bytes_0 = b'L\n/\xe8\xfc\xc0\x14q\xa5\x8fp\x08n\xc8.U'
    fenwick_tree_0 = module_0.FenwickTree(bytes_0)
    assert f'{type(fenwick_tree_0).__module__}.{type(fenwick_tree_0).__qualname__}' == 'fenwick_tree.FenwickTree'
    assert fenwick_tree_0.nums == [0, 76, 10, 47, 232, 252, 192, 20, 113, 165, 143, 112, 8, 110, 200, 46, 85]
    assert fenwick_tree_0.tree == [0, 76, 86, 47, 365, 252, 444, 20, 942, 165, 308, 112, 428, 110, 310, 46, 1811]
    int_0 = 461

def test_case_4():
    bytes_0 = b'wC\xcc?O"'
    fenwick_tree_0 = module_0.FenwickTree(bytes_0)
    assert f'{type(fenwick_tree_0).__module__}.{type(fenwick_tree_0).__qualname__}' == 'fenwick_tree.FenwickTree'
    assert fenwick_tree_0.nums == [0, 119, 67, 204, 63, 79, 34]
    assert fenwick_tree_0.tree == [0, 119, 186, 204, 453, 79, 113]
    int_0 = -3263
    var_0 = fenwick_tree_0.sum_of_n(int_0)
    assert var_0 == 0

def test_case_5():
    bytes_0 = b'8\x99\x12\xeddT\x99>t\xc92\x9f\x91\x9c\x0c\xe0n\xd8'
    fenwick_tree_0 = module_0.FenwickTree(bytes_0)
    assert f'{type(fenwick_tree_0).__module__}.{type(fenwick_tree_0).__qualname__}' == 'fenwick_tree.FenwickTree'
    assert fenwick_tree_0.nums == [0, 56, 153, 18, 237, 100, 84, 153, 62, 116, 201, 50, 159, 145, 156, 12, 224, 110, 216]
    assert fenwick_tree_0.tree == [0, 56, 209, 18, 464, 100, 184, 153, 863, 116, 317, 50, 526, 145, 301, 12, 1926, 110, 326]
