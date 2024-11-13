#Pyguin test cases converted from convert-base/WHOLE_SUITE/seed_1706/test_convert_base.py
import pytest
import convert_base as module_0
import builtins as module_1

def test_case_0():
    str_0 = "I3kZe'xY"
    none_type_0 = None
    var_0 = module_0.convert_digit_to_int(str_0)
    assert var_0 == -1
    object_0 = module_1.object()

def test_case_1():
    str_0 = 'X*(HcG4O'
    var_0 = module_0.convert_digit_to_int(str_0)
    assert var_0 == -1
    var_1 = module_0.convert_digit_to_int(str_0)
    assert var_1 == -1
    var_2 = module_0.convert_digit_to_int(str_0)
    assert var_2 == -1
    var_3 = module_0.convert_base(var_0, var_0)
    assert var_3 == -1
    str_1 = 'A5f}>W_'
    int_0 = -865
    var_4 = module_0.convert_base(str_1, int_0)
    assert var_4 == -1
    list_0 = [var_1, var_3, var_3]
    var_5 = module_0.convert_digit_to_int(list_0)
    assert var_5 == -1
    none_type_0 = None

def test_case_2():
    str_0 = '1'
    bool_0 = True
    var_0 = module_0.convert_base(str_0, bool_0)
    assert var_0 == 1
    var_1 = module_0.convert_digit_to_int(str_0)
    assert var_1 == 1

def test_case_3():
    int_0 = 264
    str_0 = ' ]G\nxS'
    var_0 = module_0.convert_digit_to_int(str_0)
    assert var_0 == -1
    var_1 = module_0.convert_digit_to_int(str_0)
    assert var_1 == -1
    var_2 = module_0.convert_base(var_0, int_0)
    assert var_2 == -1
    bool_0 = True

def test_case_4():
    str_0 = '`/y\\>~!'
    var_0 = module_0.convert_digit_to_int(str_0)
    assert var_0 == -1
    none_type_0 = None

def test_case_5():
    str_0 = "r@V2q';.1[np3\tX8Z4~"
    var_0 = module_0.convert_digit_to_int(str_0)
    assert var_0 == -1

def test_case_6():
    str_0 = '?8t52uAAU0f'
    bool_0 = False

def test_case_7():
    str_0 = "U\tgU;Bh9>p|'uJ5x3R\t{"
    var_0 = module_0.convert_digit_to_int(str_0)
    assert var_0 == -1
    var_1 = module_0.convert_digit_to_int(str_0)
    assert var_1 == -1
    var_2 = module_0.convert_base(str_0, var_0)
    assert var_2 == -1

def test_case_8():
    str_0 = 'D'
    str_1 = '8g'
    bool_0 = True
    var_0 = module_0.convert_base(str_1, bool_0)
    assert var_0 == -1
    int_0 = 10
    var_1 = module_0.convert_base(str_0, int_0)
    assert var_1 == -1
    str_2 = ''
    var_2 = module_0.convert_base(str_2, int_0)
    assert var_2 == 0
    str_3 = 'y7dG"Q$'
    var_3 = module_0.convert_base(str_3, var_2)
    assert var_3 == -1
    str_4 = 'UQ~IZL-cY\t'
    var_4 = module_0.convert_digit_to_int(str_0)
    assert var_4 == 13
    var_5 = module_0.convert_digit_to_int(str_4)
    assert var_5 == -1
    var_6 = module_0.convert_base(var_5, var_4)
    assert var_6 == -1

def test_case_9():
    str_0 = '.R@\n\na:XOD+\r'
    str_1 = 's_'
    var_0 = module_0.convert_digit_to_int(str_1)
    assert var_0 == -1
    str_2 = "H\r'U"
    var_1 = module_0.convert_digit_to_int(str_2)
    assert var_1 == -1
    complex_0 = 625.57366 + 182.93205j

def test_case_10():
    none_type_0 = None
    int_0 = 16
