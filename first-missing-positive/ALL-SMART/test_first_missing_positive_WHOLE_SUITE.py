#Pyguin test cases converted from first-missing-positive/WHOLE_SUITE/seed_1706/test_first_missing_positive.py
import pytest
import first_missing_positive as module_0
import builtins as module_1

def test_case_0():
    float_0 = 408.0
    list_0 = []
    var_0 = module_0.first_missing_positive(list_0)
    assert var_0 == 1

def test_case_1():
    bytes_0 = b'\xe0\xc8"\xefS\x8b\x0b'

def test_case_2():
    bytes_0 = b'\x05\x8b3\xbex\xd6\x82\xb1I;M~\xcf\xbb\xcf)\xf1\xae'

def test_case_3():
    bytes_0 = b'\x05\x8b3\xbex\xd6\x82\xb1I;M~\xcf\xbb\xcf)\xc0\xae'

def test_case_4():
    float_0 = -3237.7
    list_0 = [float_0, float_0, float_0, float_0]
    var_0 = module_0.first_missing_positive(list_0)
    assert var_0 == 1
    list_1 = [var_0, var_0, float_0]
    var_1 = module_0.first_missing_positive(list_1)
    assert var_1 == 2
