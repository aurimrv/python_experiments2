#Pyguin test cases converted from first-missing-positive/DYNAMOSA/seed_1706/test_first_missing_positive.py
import pytest
import first_missing_positive as module_0
import builtins as module_1

def test_case_0():
    bytes_0 = b'4\xd9\xd9\x89|\xdcR2\xb5P\x8c\x1f\xa2^\x1e{\t'

def test_case_1():
    bytes_0 = b''
    var_0 = module_0.first_missing_positive(bytes_0)
    assert var_0 == 1

def test_case_2():
    float_0 = -335.788283

def test_case_3():
    float_0 = -1790.62168
    list_0 = [float_0]
    list_1 = [float_0, list_0, float_0]

def test_case_4():
    bool_0 = True
    tuple_0 = (bool_0,)
    var_0 = module_0.first_missing_positive(tuple_0)
    assert var_0 == 2

def test_case_5():
    bool_0 = True
    int_0 = -283
    dict_0 = {int_0: bool_0}
    bool_1 = True
    str_0 = '07Tcqx_]=g'
    tuple_0 = (bool_0, dict_0, bool_1, str_0)

def test_case_6():
    bytes_0 = b'\x0f{\xc3\x19S\xb2\x07\x04&\\v \xf5\x92\xfb'

def test_case_7():
    bool_0 = True
    bool_1 = True
    list_0 = [bool_0, bool_0, bool_1, bool_0]
    var_0 = module_0.first_missing_positive(list_0)
    assert var_0 == 2
    bytes_0 = b'\x0f{\xc3\x19S\xb2\x07\x04&\\v \xf5\x92\x01'
