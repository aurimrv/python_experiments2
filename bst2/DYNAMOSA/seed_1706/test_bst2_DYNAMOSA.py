#Pyguin test cases converted from bst2/DYNAMOSA/seed_1706/test_bst2.py
import pytest
import bst2 as module_0
import builtins as module_1

def test_case_0():
    none_type_0 = None
    bst_0 = module_0.Bst()
    assert f'{type(bst_0).__module__}.{type(bst_0).__qualname__}' == 'bst2.Bst'
    assert bst_0.root is None
    var_0 = bst_0.delete(none_type_0)
    var_1 = bst_0.post_order()
    bst_1 = module_0.Bst(var_1)
    assert f'{type(bst_1).__module__}.{type(bst_1).__qualname__}' == 'bst2.Bst'
    assert bst_1.root is None

def test_case_1():
    bst_0 = module_0.Bst()
    assert f'{type(bst_0).__module__}.{type(bst_0).__qualname__}' == 'bst2.Bst'
    assert bst_0.root is None

def test_case_2():
    bool_0 = False
    int_0 = -3745
    dict_0 = {bool_0: bool_0, bool_0: int_0, int_0: int_0, int_0: int_0}
    bst_0 = module_0.Bst(dict_0)
    assert f'{type(bst_0).__module__}.{type(bst_0).__qualname__}' == 'bst2.Bst'
    assert f'{type(bst_0.root).__module__}.{type(bst_0.root).__qualname__}' == 'bst2.Node'
    var_0 = bst_0.delete(bool_0)

def test_case_3():
    bst_0 = module_0.Bst()
    assert f'{type(bst_0).__module__}.{type(bst_0).__qualname__}' == 'bst2.Bst'
    assert bst_0.root is None
    none_type_0 = None
    var_0 = bst_0.insert(none_type_0)
    assert f'{type(bst_0.root).__module__}.{type(bst_0.root).__qualname__}' == 'bst2.Node'

def test_case_4():
    bool_0 = False
    int_0 = 3347
    dict_0 = {bool_0: bool_0, bool_0: int_0, int_0: int_0, int_0: int_0}
    bst_0 = module_0.Bst(dict_0)
    assert f'{type(bst_0).__module__}.{type(bst_0).__qualname__}' == 'bst2.Bst'
    assert f'{type(bst_0.root).__module__}.{type(bst_0.root).__qualname__}' == 'bst2.Node'
    var_0 = bst_0.delete(bool_0)

def test_case_5():
    bool_0 = False
    int_0 = 3347
    dict_0 = {bool_0: bool_0, bool_0: int_0, int_0: int_0, int_0: int_0}
    bst_0 = module_0.Bst(dict_0)
    assert f'{type(bst_0).__module__}.{type(bst_0).__qualname__}' == 'bst2.Bst'
    assert f'{type(bst_0.root).__module__}.{type(bst_0.root).__qualname__}' == 'bst2.Node'
    var_0 = bst_0.insert(int_0)
    var_1 = bst_0.delete(bool_0)

def test_case_6():
    bst_0 = module_0.Bst()
    assert f'{type(bst_0).__module__}.{type(bst_0).__qualname__}' == 'bst2.Bst'
    assert bst_0.root is None
    var_0 = bst_0.search(bst_0)

def test_case_7():
    bst_0 = module_0.Bst()
    assert f'{type(bst_0).__module__}.{type(bst_0).__qualname__}' == 'bst2.Bst'
    assert bst_0.root is None
    node_0 = module_0.Node()
    assert node_0.height == 1
    var_0 = bst_0.pre_order()
    node_1 = module_0.Node()
    assert node_1.height == 1
    var_1 = bst_0.depth()
    assert var_1 == 0

def test_case_8():
    int_0 = 501
    bst_0 = module_0.Bst()
    assert f'{type(bst_0).__module__}.{type(bst_0).__qualname__}' == 'bst2.Bst'
    assert bst_0.root is None
    var_0 = bst_0.insert(int_0)
    assert f'{type(bst_0.root).__module__}.{type(bst_0.root).__qualname__}' == 'bst2.Node'
    var_1 = bst_0.breadth_first()

def test_case_9():
    bool_0 = True
    bst_0 = module_0.Bst()
    assert f'{type(bst_0).__module__}.{type(bst_0).__qualname__}' == 'bst2.Bst'
    assert bst_0.root is None
    var_0 = bst_0.delete(bool_0)
    var_1 = bst_0.insert(var_0)
    assert f'{type(bst_0.root).__module__}.{type(bst_0.root).__qualname__}' == 'bst2.Node'
    var_2 = bst_0.delete(var_1)
    assert bst_0.root is None
    var_3 = bst_0.balance()
    assert var_3 == 0
    var_4 = bst_0.search(bst_0)

def test_case_10():
    bst_0 = module_0.Bst()
    assert f'{type(bst_0).__module__}.{type(bst_0).__qualname__}' == 'bst2.Bst'
    assert bst_0.root is None
    var_0 = bst_0.delete(bst_0)
    var_1 = bst_0.insert(var_0)
    assert f'{type(bst_0.root).__module__}.{type(bst_0.root).__qualname__}' == 'bst2.Node'
    var_2 = bst_0.delete(var_1)
    assert bst_0.root is None
    var_3 = bst_0.insert(var_1)

def test_case_11():
    node_0 = module_0.Node()
    assert node_0.height == 1

def test_case_12():
    bst_0 = module_0.Bst()
    assert f'{type(bst_0).__module__}.{type(bst_0).__qualname__}' == 'bst2.Bst'
    assert bst_0.root is None
    var_0 = bst_0.size()
    assert var_0 == 0

def test_case_13():
    bst_0 = module_0.Bst()
    assert f'{type(bst_0).__module__}.{type(bst_0).__qualname__}' == 'bst2.Bst'
    assert bst_0.root is None
    var_0 = bst_0.insert(bst_0)
    assert f'{type(bst_0.root).__module__}.{type(bst_0.root).__qualname__}' == 'bst2.Node'
    var_1 = bst_0.delete(bst_0)
    assert bst_0.root is None

def test_case_14():
    bytes_0 = b'\xe0<Q0\x8afG>'
    bst_0 = module_0.Bst(bytes_0)
    assert f'{type(bst_0).__module__}.{type(bst_0).__qualname__}' == 'bst2.Bst'
    assert f'{type(bst_0.root).__module__}.{type(bst_0.root).__qualname__}' == 'bst2.Node'
    var_0 = bst_0.breadth_first()

def test_case_15():
    bool_0 = False
    int_0 = -3745
    dict_0 = {int_0: int_0, int_0: bool_0, bool_0: int_0}
    bst_0 = module_0.Bst(dict_0)
    assert f'{type(bst_0).__module__}.{type(bst_0).__qualname__}' == 'bst2.Bst'
    assert f'{type(bst_0.root).__module__}.{type(bst_0.root).__qualname__}' == 'bst2.Node'
    var_0 = bst_0.delete(bool_0)

def test_case_16():
    bool_0 = True
    bst_0 = module_0.Bst()
    assert f'{type(bst_0).__module__}.{type(bst_0).__qualname__}' == 'bst2.Bst'
    assert bst_0.root is None
    var_0 = bst_0.delete(bool_0)
    var_1 = bst_0.insert(var_0)
    assert f'{type(bst_0.root).__module__}.{type(bst_0.root).__qualname__}' == 'bst2.Node'
    int_0 = 1238
    var_2 = bst_0.delete(var_1)
    assert bst_0.root is None
    var_3 = bst_0.insert(int_0)
    var_4 = bst_0.balance()
    assert var_4 == 0

def test_case_17():
    bytes_0 = b'\xe0<QM\x8afG>'
    bst_0 = module_0.Bst(bytes_0)
    assert f'{type(bst_0).__module__}.{type(bst_0).__qualname__}' == 'bst2.Bst'
    assert f'{type(bst_0.root).__module__}.{type(bst_0.root).__qualname__}' == 'bst2.Node'
    var_0 = bst_0.breadth_first()
    var_1 = bst_0.depth()
    assert var_1 == 6
    bst_1 = module_0.Bst(var_0)
    assert f'{type(bst_1).__module__}.{type(bst_1).__qualname__}' == 'bst2.Bst'
    assert f'{type(bst_1.root).__module__}.{type(bst_1.root).__qualname__}' == 'bst2.Node'
    var_2 = bst_0.delete(var_1)
    var_3 = bst_0.insert(var_1)

def test_case_18():
    bool_0 = False
    int_0 = 3347
    dict_0 = {int_0: int_0, bool_0: bool_0, int_0: int_0}
    bst_0 = module_0.Bst(dict_0)
    assert f'{type(bst_0).__module__}.{type(bst_0).__qualname__}' == 'bst2.Bst'
    assert f'{type(bst_0.root).__module__}.{type(bst_0.root).__qualname__}' == 'bst2.Node'
    var_0 = bst_0.delete(bool_0)
    var_1 = bst_0.insert(int_0)

def test_case_19():
    str_0 = 'iJF\rkS'
    bst_0 = module_0.Bst(str_0)
    assert f'{type(bst_0).__module__}.{type(bst_0).__qualname__}' == 'bst2.Bst'
    assert f'{type(bst_0.root).__module__}.{type(bst_0.root).__qualname__}' == 'bst2.Node'
    var_0 = bst_0.balance()
    assert var_0 == 2

def test_case_20():
    bytes_0 = b'\xe0<Q0\x8afG>'
    bst_0 = module_0.Bst(bytes_0)
    assert f'{type(bst_0).__module__}.{type(bst_0).__qualname__}' == 'bst2.Bst'
    assert f'{type(bst_0.root).__module__}.{type(bst_0.root).__qualname__}' == 'bst2.Node'
    var_0 = bst_0.size()
    assert var_0 == 8
    var_1 = bst_0.breadth_first()
    var_2 = bst_0.depth()
    assert var_2 == 5
    bst_1 = module_0.Bst(var_1)
    assert f'{type(bst_1).__module__}.{type(bst_1).__qualname__}' == 'bst2.Bst'
    assert f'{type(bst_1.root).__module__}.{type(bst_1.root).__qualname__}' == 'bst2.Node'
    var_3 = bst_0.delete(var_2)
    var_4 = bst_0.insert(var_2)
    var_5 = bst_0.balance()
    assert var_5 == 4
    bst_2 = module_0.Bst()
    assert f'{type(bst_2).__module__}.{type(bst_2).__qualname__}' == 'bst2.Bst'
    assert bst_2.root is None

def test_case_21():
    bytes_0 = b'\xe0<QM\x8afG>'
    bst_0 = module_0.Bst(bytes_0)
    assert f'{type(bst_0).__module__}.{type(bst_0).__qualname__}' == 'bst2.Bst'
    assert f'{type(bst_0.root).__module__}.{type(bst_0.root).__qualname__}' == 'bst2.Node'
    var_0 = bst_0.pre_order(bytes_0)
    var_1 = bst_0.post_order()
    var_2 = bst_0.depth()
    assert var_2 == 6
    bst_1 = module_0.Bst(var_1)
    assert f'{type(bst_1).__module__}.{type(bst_1).__qualname__}' == 'bst2.Bst'
    assert f'{type(bst_1.root).__module__}.{type(bst_1.root).__qualname__}' == 'bst2.Node'
    var_3 = bst_0.insert(var_2)
    var_4 = bst_0.balance()
    assert var_4 == 5

def test_case_22():
    bytes_0 = b'\xe0HQ0\x8afG>'
    bst_0 = module_0.Bst(bytes_0)
    assert f'{type(bst_0).__module__}.{type(bst_0).__qualname__}' == 'bst2.Bst'
    assert f'{type(bst_0.root).__module__}.{type(bst_0.root).__qualname__}' == 'bst2.Node'
    var_0 = bst_0.in_order(bst_0)
    var_1 = bst_0.depth()
    assert var_1 == 5

def test_case_23():
    bytes_0 = b'\xe0<Q0\x8afG>'
    none_type_0 = None
    bst_0 = module_0.Bst(none_type_0)
    assert f'{type(bst_0).__module__}.{type(bst_0).__qualname__}' == 'bst2.Bst'
    assert bst_0.root is None
    var_0 = bst_0.size()
    assert var_0 == 0
    bool_0 = False
    var_1 = bst_0.breadth_first()
    var_2 = bst_0.depth()
    assert var_2 == 0
    bst_1 = module_0.Bst(var_1)
    assert f'{type(bst_1).__module__}.{type(bst_1).__qualname__}' == 'bst2.Bst'
    assert bst_1.root is None
    var_3 = bst_0.delete(bool_0)
    var_4 = bst_0.insert(var_2)
    assert f'{type(bst_0.root).__module__}.{type(bst_0.root).__qualname__}' == 'bst2.Node'
    var_5 = bst_0.balance()
    assert var_5 == 0

def test_case_24():
    bytes_0 = b'\xe0<QM\x8afG>'
    bst_0 = module_0.Bst(bytes_0)
    assert f'{type(bst_0).__module__}.{type(bst_0).__qualname__}' == 'bst2.Bst'
    assert f'{type(bst_0.root).__module__}.{type(bst_0.root).__qualname__}' == 'bst2.Node'
    var_0 = bst_0.pre_order()
    var_1 = bst_0.breadth_first()
    var_2 = bst_0.depth()
    assert var_2 == 6
    bst_1 = module_0.Bst(var_0)
    assert f'{type(bst_1).__module__}.{type(bst_1).__qualname__}' == 'bst2.Bst'
    assert f'{type(bst_1.root).__module__}.{type(bst_1.root).__qualname__}' == 'bst2.Node'
    str_0 = ''

def test_case_25():
    bytes_0 = b'\xe0<QM\x8afG>'
    bst_0 = module_0.Bst(bytes_0)
    assert f'{type(bst_0).__module__}.{type(bst_0).__qualname__}' == 'bst2.Bst'
    assert f'{type(bst_0.root).__module__}.{type(bst_0.root).__qualname__}' == 'bst2.Node'
    bool_0 = False
    var_0 = bst_0.in_order()
    var_1 = bst_0.depth()
    assert var_1 == 6
    bst_1 = module_0.Bst(var_0)
    assert f'{type(bst_1).__module__}.{type(bst_1).__qualname__}' == 'bst2.Bst'
    assert f'{type(bst_1.root).__module__}.{type(bst_1.root).__qualname__}' == 'bst2.Node'
    var_2 = bst_0.delete(bool_0)
    var_3 = bst_0.insert(var_1)
    var_4 = bst_0.balance()
    assert var_4 == 5
    bst_2 = module_0.Bst()
    assert f'{type(bst_2).__module__}.{type(bst_2).__qualname__}' == 'bst2.Bst'
    assert bst_2.root is None

def test_case_26():
    bool_0 = False
    node_0 = module_0.Node()
    assert node_0.height == 1
    int_0 = 3347
    dict_0 = {bool_0: bool_0, bool_0: int_0, int_0: int_0, int_0: int_0}
    bst_0 = module_0.Bst(dict_0)
    assert f'{type(bst_0).__module__}.{type(bst_0).__qualname__}' == 'bst2.Bst'
    assert f'{type(bst_0.root).__module__}.{type(bst_0.root).__qualname__}' == 'bst2.Node'
    var_0 = bst_0.delete(bool_0)
    var_1 = bst_0.size()
    assert var_1 == 1
    var_2 = bst_0.insert(var_1)
    var_3 = bst_0.delete(int_0)

def test_case_27():
    bool_0 = True
    node_0 = module_0.Node()
    assert node_0.height == 1
    int_0 = 3347
    bst_0 = module_0.Bst()
    assert f'{type(bst_0).__module__}.{type(bst_0).__qualname__}' == 'bst2.Bst'
    assert bst_0.root is None
    var_0 = bst_0.depth()
    assert var_0 == 0
    dict_0 = {bool_0: bool_0, var_0: bst_0, int_0: int_0, bool_0: bool_0}
    bst_1 = module_0.Bst(dict_0)
    assert f'{type(bst_1).__module__}.{type(bst_1).__qualname__}' == 'bst2.Bst'
    assert f'{type(bst_1.root).__module__}.{type(bst_1.root).__qualname__}' == 'bst2.Node'
    var_1 = bst_1.delete(bool_0)
    var_2 = bst_1.delete(int_0)
