#Pyguin test cases converted from bst2/WHOLE_SUITE/seed_1706/test_bst2.py
import pytest
import bst2 as module_0
import a_queue as module_1

def test_case_0():
    bst_0 = module_0.Bst()
    assert f'{type(bst_0).__module__}.{type(bst_0).__qualname__}' == 'bst2.Bst'
    assert bst_0.root is None
    var_0 = bst_0.size()
    assert var_0 == 0
    var_1 = bst_0.balance()
    assert var_1 == 0
    bst_1 = module_0.Bst()
    none_type_0 = None
    bst_2 = module_0.Bst(none_type_0)
    node_0 = module_0.Node(parent=none_type_0)
    assert node_0.height == 1
    var_2 = bst_2.insert(none_type_0)
    assert f'{type(bst_2.root).__module__}.{type(bst_2.root).__qualname__}' == 'bst2.Node'
    var_3 = bst_1.depth()
    assert var_3 == 0
    var_4 = bst_0.depth()
    assert var_4 == 0
    var_5 = bst_2.contains(none_type_0)
    assert var_5 is True
    var_6 = bst_2.breadth_first()

def test_case_1():
    bytes_0 = b'\xb6\xc6\xa3\x08\xc5\x11\x12\x13'
    bst_0 = module_0.Bst(bytes_0)
    assert f'{type(bst_0).__module__}.{type(bst_0).__qualname__}' == 'bst2.Bst'
    assert f'{type(bst_0.root).__module__}.{type(bst_0.root).__qualname__}' == 'bst2.Node'
    var_0 = bst_0.balance()
    assert var_0 == 3

def test_case_2():
    bst_0 = module_0.Bst()
    assert f'{type(bst_0).__module__}.{type(bst_0).__qualname__}' == 'bst2.Bst'
    assert bst_0.root is None
    bool_0 = True
    set_0 = {bool_0, bool_0, bool_0}
    var_0 = bst_0.depth()
    assert var_0 == 0

def test_case_3():
    none_type_0 = None
    bst_0 = module_0.Bst()
    assert f'{type(bst_0).__module__}.{type(bst_0).__qualname__}' == 'bst2.Bst'
    assert bst_0.root is None
    var_0 = bst_0.balance()
    assert var_0 == 0

def test_case_4():
    str_0 = 'L.:\x0c\x0c!;s.O\x0crP!8'
    node_0 = module_0.Node(parent=str_0)
    assert node_0.height == 1

def test_case_5():
    bst_0 = module_0.Bst()
    assert f'{type(bst_0).__module__}.{type(bst_0).__qualname__}' == 'bst2.Bst'
    assert bst_0.root is None
    var_0 = bst_0.insert(bst_0)
    assert f'{type(bst_0.root).__module__}.{type(bst_0.root).__qualname__}' == 'bst2.Node'
    var_1 = bst_0.balance()
    assert var_1 == 0
    var_2 = bst_0.size()
    assert var_2 == 1
    var_3 = bst_0.pre_order()

def test_case_6():
    str_0 = 'c(5w0:<3y'
    bst_0 = module_0.Bst(str_0)
    assert f'{type(bst_0).__module__}.{type(bst_0).__qualname__}' == 'bst2.Bst'
    assert f'{type(bst_0.root).__module__}.{type(bst_0.root).__qualname__}' == 'bst2.Node'
    var_0 = bst_0.pre_order()
    bst_1 = module_0.Bst(var_0)
    assert f'{type(bst_1).__module__}.{type(bst_1).__qualname__}' == 'bst2.Bst'
    assert f'{type(bst_1.root).__module__}.{type(bst_1.root).__qualname__}' == 'bst2.Node'
    node_0 = module_0.Node()
    assert node_0.height == 1
    var_1 = bst_0.pre_order(var_0)
    var_2 = bst_0.delete(str_0)

def test_case_7():
    str_0 = '$'
    bst_0 = module_0.Bst(str_0)
    assert f'{type(bst_0).__module__}.{type(bst_0).__qualname__}' == 'bst2.Bst'
    assert f'{type(bst_0.root).__module__}.{type(bst_0.root).__qualname__}' == 'bst2.Node'
    var_0 = bst_0.depth()
    assert var_0 == 1
    var_1 = bst_0.delete(str_0)
    assert bst_0.root is None
    var_2 = bst_0.insert(var_0)

def test_case_8():
    bool_0 = True
    bst_0 = module_0.Bst()
    assert f'{type(bst_0).__module__}.{type(bst_0).__qualname__}' == 'bst2.Bst'
    assert bst_0.root is None
    int_0 = 197
    var_0 = bst_0.insert(int_0)
    assert f'{type(bst_0.root).__module__}.{type(bst_0.root).__qualname__}' == 'bst2.Node'
    var_1 = bst_0.post_order()
    var_2 = bst_0.search(bool_0)
    var_3 = bst_0.insert(bool_0)
    bst_1 = module_0.Bst(var_1)
    assert f'{type(bst_1).__module__}.{type(bst_1).__qualname__}' == 'bst2.Bst'
    assert f'{type(bst_1.root).__module__}.{type(bst_1.root).__qualname__}' == 'bst2.Node'

def test_case_9():
    bool_0 = False
    bst_0 = module_0.Bst()
    assert f'{type(bst_0).__module__}.{type(bst_0).__qualname__}' == 'bst2.Bst'
    assert bst_0.root is None
    var_0 = bst_0.in_order()
    var_1 = bst_0.search(bool_0)
    var_2 = bst_0.insert(bool_0)
    assert f'{type(bst_0.root).__module__}.{type(bst_0.root).__qualname__}' == 'bst2.Node'
    bst_1 = module_0.Bst(var_0)
    assert f'{type(bst_1).__module__}.{type(bst_1).__qualname__}' == 'bst2.Bst'
    assert f'{type(bst_1.root).__module__}.{type(bst_1.root).__qualname__}' == 'bst2.Node'

def test_case_10():
    bool_0 = False
    bst_0 = module_0.Bst()
    assert f'{type(bst_0).__module__}.{type(bst_0).__qualname__}' == 'bst2.Bst'
    assert bst_0.root is None
    var_0 = bst_0.in_order()
    var_1 = bst_0.search(bool_0)
    var_2 = bst_0.insert(bool_0)
    assert f'{type(bst_0.root).__module__}.{type(bst_0.root).__qualname__}' == 'bst2.Node'
    bst_1 = module_0.Bst(var_0)
    assert f'{type(bst_1).__module__}.{type(bst_1).__qualname__}' == 'bst2.Bst'
    assert f'{type(bst_1.root).__module__}.{type(bst_1.root).__qualname__}' == 'bst2.Node'

def test_case_11():
    node_0 = module_0.Node()
    assert node_0.height == 1

def test_case_12():
    bool_0 = False
    list_0 = [bool_0, bool_0]
    bst_0 = module_0.Bst(list_0)
    assert f'{type(bst_0).__module__}.{type(bst_0).__qualname__}' == 'bst2.Bst'
    assert f'{type(bst_0.root).__module__}.{type(bst_0.root).__qualname__}' == 'bst2.Node'
    var_0 = bst_0.pre_order()
    var_1 = bst_0.breadth_first()

def test_case_13():
    str_0 = "Ws?(\\|xHo'd"
    bst_0 = module_0.Bst(str_0)
    assert f'{type(bst_0).__module__}.{type(bst_0).__qualname__}' == 'bst2.Bst'
    assert f'{type(bst_0.root).__module__}.{type(bst_0.root).__qualname__}' == 'bst2.Node'
    var_0 = bst_0.in_order()
    var_1 = bst_0.contains(str_0)
    assert var_1 is False

def test_case_14():
    bst_0 = module_0.Bst()
    assert f'{type(bst_0).__module__}.{type(bst_0).__qualname__}' == 'bst2.Bst'
    assert bst_0.root is None
    var_0 = bst_0.insert(bst_0)
    assert f'{type(bst_0.root).__module__}.{type(bst_0.root).__qualname__}' == 'bst2.Node'
    var_1 = bst_0.delete(bst_0)
    assert bst_0.root is None
    var_2 = bst_0.delete(bst_0)
    var_3 = bst_0.contains(var_1)
    assert var_3 is False
    var_4 = bst_0.pre_order()
    bool_0 = False
    queue_0 = module_1.Queue(bool_0)

def test_case_15():
    bst_0 = module_0.Bst()
    assert f'{type(bst_0).__module__}.{type(bst_0).__qualname__}' == 'bst2.Bst'
    assert bst_0.root is None
    var_0 = bst_0.breadth_first()
    bst_1 = module_0.Bst(var_0)
    assert f'{type(bst_1).__module__}.{type(bst_1).__qualname__}' == 'bst2.Bst'
    assert bst_1.root is None

def test_case_16():
    node_0 = module_0.Node()
    assert node_0.height == 1
    dict_0 = {node_0: node_0}
    bst_0 = module_0.Bst()
    assert f'{type(bst_0).__module__}.{type(bst_0).__qualname__}' == 'bst2.Bst'
    assert bst_0.root is None
    var_0 = bst_0.breadth_first()
    var_1 = bst_0.insert(dict_0)
    assert f'{type(bst_0.root).__module__}.{type(bst_0.root).__qualname__}' == 'bst2.Node'
    bst_1 = module_0.Bst(var_0)
    assert f'{type(bst_1).__module__}.{type(bst_1).__qualname__}' == 'bst2.Bst'
    assert f'{type(bst_1.root).__module__}.{type(bst_1.root).__qualname__}' == 'bst2.Node'

def test_case_17():
    node_0 = module_0.Node()
    assert node_0.height == 1
    dict_0 = {}
    bst_0 = module_0.Bst()
    assert f'{type(bst_0).__module__}.{type(bst_0).__qualname__}' == 'bst2.Bst'
    assert bst_0.root is None
    var_0 = bst_0.breadth_first()
    var_1 = bst_0.insert(dict_0)
    assert f'{type(bst_0.root).__module__}.{type(bst_0.root).__qualname__}' == 'bst2.Node'
    bst_1 = module_0.Bst(var_0)
    assert f'{type(bst_1).__module__}.{type(bst_1).__qualname__}' == 'bst2.Bst'
    assert f'{type(bst_1.root).__module__}.{type(bst_1.root).__qualname__}' == 'bst2.Node'
    var_2 = bst_0.balance()
    assert var_2 == 0
    var_3 = bst_0.depth()
    assert var_3 == 1

def test_case_18():
    none_type_0 = None
    bst_0 = module_0.Bst()
    assert f'{type(bst_0).__module__}.{type(bst_0).__qualname__}' == 'bst2.Bst'
    assert bst_0.root is None
    queue_0 = module_1.Queue()
    var_0 = bst_0.contains(none_type_0)
    assert var_0 is False
