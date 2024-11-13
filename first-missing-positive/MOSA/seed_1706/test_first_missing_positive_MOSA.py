#Pyguin test cases converted from first-missing-positive/MOSA/seed_1706/test_first_missing_positive.py
import pytest
import first_missing_positive as module_0
import builtins as module_1

def test_case_0():
    bytes_0 = b'\xde\xf3\xb1;s\x97\xc0\x12\x05'

def test_case_1():
    bool_0 = True
    int_0 = -283
    dict_0 = {int_0: bool_0}
    bool_1 = True
    str_0 = '07Tcqx_]=g'
    tuple_0 = (bool_0, dict_0, bool_1, str_0)

def test_case_2():
    bool_0 = True
    tuple_0 = (bool_0,)
    var_0 = module_0.first_missing_positive(tuple_0)
    assert var_0 == 2
    int_0 = 11

def test_case_3():
    bool_0 = False
    dict_0 = {bool_0: bool_0}
    var_0 = module_0.first_missing_positive(dict_0)
    assert var_0 == 1
    none_type_0 = None

def test_case_4():
    set_0 = set()
    var_0 = module_0.first_missing_positive(set_0)
    assert var_0 == 1
    none_type_0 = None
    var_1 = module_0.first_missing_positive(set_0)
    assert var_1 == 1

def test_case_5():
    float_0 = -335.788283

def test_case_6():
    bool_0 = True
    list_0 = [bool_0, bool_0]
    var_0 = module_0.first_missing_positive(list_0)
    assert var_0 == 2
    tuple_0 = ()
    object_0 = module_1.object(*tuple_0)

def test_case_7():
    bool_0 = True
    list_0 = [bool_0, bool_0]
    var_0 = module_0.first_missing_positive(list_0)
    assert var_0 == 2
    bool_1 = False
    dict_0 = {var_0: var_0, bool_0: bool_1, bool_1: bool_1}
    var_1 = module_0.first_missing_positive(dict_0)
    assert var_1 == 1
    tuple_0 = ()
    var_2 = module_0.first_missing_positive(tuple_0)
    assert var_2 == 1
    object_0 = module_1.object()
