#Pyguin test cases converted from first-missing-positive/MIO/seed_1706/test_first_missing_positive.py
import pytest
import first_missing_positive as module_0

def test_case_0():
    bytes_0 = b'\x11\xb5\x95Gh;\x14\x8f\xdb^\x99\xc1\xd8\x99*L'

def test_case_1():
    bytes_0 = b'\x11\xb5\x95\x00GK;\x14\x8f\xb6^\x99\xc1\xd8\x90\x99*L'

def test_case_2():
    bool_0 = True
    bytes_0 = b'\x8f\\\t\x19\x1d*V9\xd7'
    tuple_0 = (bool_0, bool_0, bool_0, bytes_0)

def test_case_3():
    bool_0 = False
    list_0 = [bool_0, bool_0, bool_0, bool_0]
    var_0 = module_0.first_missing_positive(list_0)
    assert var_0 == 1

def test_case_4():
    bool_0 = False
    bool_1 = True
    list_0 = [bool_0, bool_0, bool_1, bool_0]
    var_0 = module_0.first_missing_positive(list_0)
    assert var_0 == 2

def test_case_5():
    bytes_0 = b''
    var_0 = module_0.first_missing_positive(bytes_0)
    assert var_0 == 1
