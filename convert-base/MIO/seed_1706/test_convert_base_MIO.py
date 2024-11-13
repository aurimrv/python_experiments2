#Pyguin test cases converted from convert-base/MIO/seed_1706/test_convert_base.py
import pytest
import convert_base as module_0

def test_case_0():
    str_0 = '\n^4IE'
    int_0 = 4607
    var_0 = module_0.convert_base(str_0, int_0)
    assert var_0 == -1

def test_case_1():
    int_0 = 16

def test_case_2():
    str_0 = 'n)TrOb^{;5@vuXfV=9^'
    bool_0 = True
    var_0 = module_0.convert_base(str_0, bool_0)
    assert var_0 == -1

def test_case_3():
    str_0 = '0?(6L4'
    bool_0 = True

def test_case_4():
    list_0 = []
    bool_0 = False
    var_0 = module_0.convert_base(list_0, bool_0)
    assert var_0 == 0
    str_0 = '2`#cRIl_(/,\\37'
    var_1 = module_0.convert_base(str_0, bool_0)
    assert var_1 == -1
    var_2 = module_0.convert_base(str_0, bool_0)
    assert var_2 == -1
    int_0 = -1844
    var_3 = module_0.convert_base(bool_0, int_0)
    assert var_3 == -1

def test_case_5():
    str_0 = '2`#cRIl_(/,\\37'
    bool_0 = True
    var_0 = module_0.convert_base(str_0, bool_0)
    assert var_0 == -1

def test_case_6():
    str_0 = '2`#cRIl_(/,\\37'
    bool_0 = True
    int_0 = -198
    var_0 = module_0.convert_base(str_0, int_0)
    assert var_0 == -1
    var_1 = module_0.convert_base(str_0, bool_0)
    assert var_1 == -1

def test_case_7():
    str_0 = 'X\r]\rH?x>Qc]'
    var_0 = module_0.convert_digit_to_int(str_0)
    assert var_0 == -1
