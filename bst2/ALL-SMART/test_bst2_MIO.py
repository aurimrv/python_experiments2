#Pyguin test cases converted from bst2/MIO/seed_1706/test_bst2.py
import pytest
import bst2 as module_0
import builtins as module_1

def test_case_0():
    bst_0 = module_0.Bst()
    assert f'{type(bst_0).__module__}.{type(bst_0).__qualname__}' == 'bst2.Bst'
    assert bst_0.root is None
    var_0 = bst_0.insert(bst_0)
    assert f'{type(bst_0.root).__module__}.{type(bst_0.root).__qualname__}' == 'bst2.Node'
    var_1 = bst_0.delete(bst_0)
    assert bst_0.root is None

def test_case_1():
    bytes_0 = b'w'
    bst_0 = module_0.Bst(bytes_0)
    assert f'{type(bst_0).__module__}.{type(bst_0).__qualname__}' == 'bst2.Bst'
    assert f'{type(bst_0.root).__module__}.{type(bst_0.root).__qualname__}' == 'bst2.Node'

def test_case_2():
    bytes_0 = b'\xd5>6\xfcS`\xad\xc0'
    bst_0 = module_0.Bst(bytes_0)
    assert f'{type(bst_0).__module__}.{type(bst_0).__qualname__}' == 'bst2.Bst'
    assert f'{type(bst_0.root).__module__}.{type(bst_0.root).__qualname__}' == 'bst2.Node'
    node_0 = module_0.Node()
    assert node_0.height == 1

def test_case_3():
    bst_0 = module_0.Bst()
    assert f'{type(bst_0).__module__}.{type(bst_0).__qualname__}' == 'bst2.Bst'
    assert bst_0.root is None

def test_case_4():
    bytes_0 = b'\x11\xf4e\x91\xd1\x05\x02\xac\xd1'
    bst_0 = module_0.Bst(bytes_0)
    assert f'{type(bst_0).__module__}.{type(bst_0).__qualname__}' == 'bst2.Bst'
    assert f'{type(bst_0.root).__module__}.{type(bst_0.root).__qualname__}' == 'bst2.Node'

def test_case_5():
    bst_0 = module_0.Bst()
    assert f'{type(bst_0).__module__}.{type(bst_0).__qualname__}' == 'bst2.Bst'
    assert bst_0.root is None
    var_0 = bst_0.insert(bst_0)
    assert f'{type(bst_0.root).__module__}.{type(bst_0.root).__qualname__}' == 'bst2.Node'

def test_case_6():
    bool_0 = False
    bytes_0 = b'\xf1\x8co\x80%\x98\x14\xda\xf5qz\x85i'
    bst_0 = module_0.Bst(bytes_0)
    assert f'{type(bst_0).__module__}.{type(bst_0).__qualname__}' == 'bst2.Bst'
    assert f'{type(bst_0.root).__module__}.{type(bst_0.root).__qualname__}' == 'bst2.Node'
    var_0 = bst_0.delete(bool_0)

def test_case_7():
    bst_0 = module_0.Bst()
    assert f'{type(bst_0).__module__}.{type(bst_0).__qualname__}' == 'bst2.Bst'
    assert bst_0.root is None
    var_0 = bst_0.insert(bst_0)
    assert f'{type(bst_0.root).__module__}.{type(bst_0.root).__qualname__}' == 'bst2.Node'

def test_case_8():
    str_0 = 'qS'
    bst_0 = module_0.Bst(str_0)
    assert f'{type(bst_0).__module__}.{type(bst_0).__qualname__}' == 'bst2.Bst'
    assert f'{type(bst_0.root).__module__}.{type(bst_0.root).__qualname__}' == 'bst2.Node'
    var_0 = bst_0.delete(str_0)
    bst_1 = module_0.Bst()
    assert f'{type(bst_1).__module__}.{type(bst_1).__qualname__}' == 'bst2.Bst'
    assert bst_1.root is None

def test_case_9():
    bst_0 = module_0.Bst()
    assert f'{type(bst_0).__module__}.{type(bst_0).__qualname__}' == 'bst2.Bst'
    assert bst_0.root is None
    var_0 = bst_0.contains(bst_0)
    assert var_0 is False

def test_case_10():
    bst_0 = module_0.Bst()
    assert f'{type(bst_0).__module__}.{type(bst_0).__qualname__}' == 'bst2.Bst'
    assert bst_0.root is None
    var_0 = bst_0.insert(bst_0)
    assert f'{type(bst_0.root).__module__}.{type(bst_0.root).__qualname__}' == 'bst2.Node'
    var_1 = bst_0.depth()
    assert var_1 == 1

def test_case_11():
    bst_0 = module_0.Bst()
    assert f'{type(bst_0).__module__}.{type(bst_0).__qualname__}' == 'bst2.Bst'
    assert bst_0.root is None
    var_0 = bst_0.depth()
    assert var_0 == 0

def test_case_12():
    bytes_0 = b'\x9eR\xc1\xfb\x9a\xa3\x16\x9e\x9bl\xb1\xdb$\x91*$8\x9f\xdf\xf1'
    bst_0 = module_0.Bst(bytes_0)
    assert f'{type(bst_0).__module__}.{type(bst_0).__qualname__}' == 'bst2.Bst'
    assert f'{type(bst_0.root).__module__}.{type(bst_0.root).__qualname__}' == 'bst2.Node'
    var_0 = bst_0.balance()
    assert var_0 == 0

def test_case_13():
    bst_0 = module_0.Bst()
    assert f'{type(bst_0).__module__}.{type(bst_0).__qualname__}' == 'bst2.Bst'
    assert bst_0.root is None
    var_0 = bst_0.insert(bst_0)
    assert f'{type(bst_0.root).__module__}.{type(bst_0.root).__qualname__}' == 'bst2.Node'
    var_1 = bst_0.balance()
    assert var_1 == 0

def test_case_14():
    bst_0 = module_0.Bst()
    assert f'{type(bst_0).__module__}.{type(bst_0).__qualname__}' == 'bst2.Bst'
    assert bst_0.root is None
    var_0 = bst_0.balance()
    assert var_0 == 0

def test_case_15():
    bst_0 = module_0.Bst()
    assert f'{type(bst_0).__module__}.{type(bst_0).__qualname__}' == 'bst2.Bst'
    assert bst_0.root is None

def test_case_16():
    bst_0 = module_0.Bst()
    assert f'{type(bst_0).__module__}.{type(bst_0).__qualname__}' == 'bst2.Bst'
    assert bst_0.root is None
    var_0 = bst_0.pre_order(bst_0)
    var_1 = bst_0.insert(var_0)
    assert f'{type(bst_0.root).__module__}.{type(bst_0.root).__qualname__}' == 'bst2.Node'

def test_case_17():
    bst_0 = module_0.Bst()
    assert f'{type(bst_0).__module__}.{type(bst_0).__qualname__}' == 'bst2.Bst'
    assert bst_0.root is None
    var_0 = bst_0.pre_order()
    bst_1 = module_0.Bst(var_0)
    assert f'{type(bst_1).__module__}.{type(bst_1).__qualname__}' == 'bst2.Bst'
    assert bst_1.root is None

def test_case_18():
    bytes_0 = b'\xfd'
    bst_0 = module_0.Bst(bytes_0)
    assert f'{type(bst_0).__module__}.{type(bst_0).__qualname__}' == 'bst2.Bst'
    assert f'{type(bst_0.root).__module__}.{type(bst_0.root).__qualname__}' == 'bst2.Node'
    var_0 = bst_0.pre_order()
    bst_1 = module_0.Bst(var_0)
    assert f'{type(bst_1).__module__}.{type(bst_1).__qualname__}' == 'bst2.Bst'
    assert f'{type(bst_1.root).__module__}.{type(bst_1.root).__qualname__}' == 'bst2.Node'

def test_case_19():
    bst_0 = module_0.Bst()
    assert f'{type(bst_0).__module__}.{type(bst_0).__qualname__}' == 'bst2.Bst'
    assert bst_0.root is None
    none_type_0 = None
    var_0 = bst_0.pre_order(none_type_0)
    var_1 = bst_0.balance()
    assert var_1 == 0
    bst_1 = module_0.Bst(var_0)
    assert f'{type(bst_1).__module__}.{type(bst_1).__qualname__}' == 'bst2.Bst'
    assert bst_1.root is None

def test_case_20():
    bst_0 = module_0.Bst()
    assert f'{type(bst_0).__module__}.{type(bst_0).__qualname__}' == 'bst2.Bst'
    assert bst_0.root is None
    none_type_0 = None
    var_0 = bst_0.insert(none_type_0)
    assert f'{type(bst_0.root).__module__}.{type(bst_0.root).__qualname__}' == 'bst2.Node'
    var_1 = bst_0.in_order()
    bst_1 = module_0.Bst(var_1)
    assert f'{type(bst_1).__module__}.{type(bst_1).__qualname__}' == 'bst2.Bst'
    assert f'{type(bst_1.root).__module__}.{type(bst_1.root).__qualname__}' == 'bst2.Node'

def test_case_21():
    bst_0 = module_0.Bst()
    assert f'{type(bst_0).__module__}.{type(bst_0).__qualname__}' == 'bst2.Bst'
    assert bst_0.root is None
    var_0 = bst_0.in_order()
    bst_1 = module_0.Bst(var_0)
    assert f'{type(bst_1).__module__}.{type(bst_1).__qualname__}' == 'bst2.Bst'
    assert bst_1.root is None

def test_case_22():
    bytes_0 = b'"\x7flyV 6\x9a`\xa46\xaa\x13'
    bst_0 = module_0.Bst(bytes_0)
    assert f'{type(bst_0).__module__}.{type(bst_0).__qualname__}' == 'bst2.Bst'
    assert f'{type(bst_0.root).__module__}.{type(bst_0.root).__qualname__}' == 'bst2.Node'
    var_0 = bst_0.post_order()
    bst_1 = module_0.Bst(var_0)
    assert f'{type(bst_1).__module__}.{type(bst_1).__qualname__}' == 'bst2.Bst'
    assert f'{type(bst_1.root).__module__}.{type(bst_1.root).__qualname__}' == 'bst2.Node'

def test_case_23():
    bst_0 = module_0.Bst()
    assert f'{type(bst_0).__module__}.{type(bst_0).__qualname__}' == 'bst2.Bst'
    assert bst_0.root is None
    var_0 = bst_0.post_order()
    bst_1 = module_0.Bst(var_0)
    assert f'{type(bst_1).__module__}.{type(bst_1).__qualname__}' == 'bst2.Bst'
    assert bst_1.root is None

def test_case_24():
    bytes_0 = b'\x8c\x19\x0e\xcdh6vK\x0f\xe7\xbdb\x03\x96\x02'
    bst_0 = module_0.Bst(bytes_0)
    assert f'{type(bst_0).__module__}.{type(bst_0).__qualname__}' == 'bst2.Bst'
    assert f'{type(bst_0.root).__module__}.{type(bst_0.root).__qualname__}' == 'bst2.Node'
    var_0 = bst_0.breadth_first()

def test_case_25():
    bytes_0 = b'j'
    bst_0 = module_0.Bst(bytes_0)
    assert f'{type(bst_0).__module__}.{type(bst_0).__qualname__}' == 'bst2.Bst'
    assert f'{type(bst_0.root).__module__}.{type(bst_0.root).__qualname__}' == 'bst2.Node'
    var_0 = bst_0.breadth_first()
    bst_1 = module_0.Bst(var_0)
    assert f'{type(bst_1).__module__}.{type(bst_1).__qualname__}' == 'bst2.Bst'
    assert f'{type(bst_1.root).__module__}.{type(bst_1.root).__qualname__}' == 'bst2.Node'

def test_case_26():
    bst_0 = module_0.Bst()
    assert f'{type(bst_0).__module__}.{type(bst_0).__qualname__}' == 'bst2.Bst'
    assert bst_0.root is None
    var_0 = bst_0.breadth_first()
    bst_1 = module_0.Bst(var_0)
    assert f'{type(bst_1).__module__}.{type(bst_1).__qualname__}' == 'bst2.Bst'
    assert bst_1.root is None

def test_case_27():
    bst_0 = module_0.Bst()
    assert f'{type(bst_0).__module__}.{type(bst_0).__qualname__}' == 'bst2.Bst'
    assert bst_0.root is None
    var_0 = bst_0.delete(bst_0)

def test_case_28():
    node_0 = module_0.Node()
    assert node_0.height == 1

def test_case_29():
    bst_0 = module_0.Bst()
    assert f'{type(bst_0).__module__}.{type(bst_0).__qualname__}' == 'bst2.Bst'
    assert bst_0.root is None
    var_0 = bst_0.size()
    assert var_0 == 0
