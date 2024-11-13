#Pyguin test cases converted from find-duplicates/MIO/seed_1706/test_find_duplicates.py
import pytest
import find_duplicates as module_0

def test_case_0():
    bytes_0 = b'\x1dh\x9c\xf0\xd3\xbe\xb7C\x19\xf5\xad\x9a\x81C'
    var_0 = module_0.duplicates_linear(bytes_0, bytes_0)

def test_case_1():
    str_0 = 'Pc=ZM/.\nL0/\r]p]\x0cUyL$'
    dict_0 = {str_0: str_0, str_0: str_0, str_0: str_0}
    var_0 = module_0.duplicates_linear(dict_0, str_0)

def test_case_2():
    bytes_0 = b'\x1dh\x9c\xf0\xd3\xb7C\x19\xf5\xad\x9a\x81C'
    var_0 = module_0.duplicates_pre_sorted(bytes_0, bytes_0)

def test_case_3():
    str_0 = 'kG9*J\t^IG'
    tuple_0 = (str_0, str_0)
    var_0 = module_0.duplicates_pre_sorted(tuple_0, tuple_0)
    var_1 = module_0.duplicates_pre_sorted(tuple_0, str_0)
    var_2 = module_0.duplicates_bin_search(tuple_0, var_1)

def test_case_4():
    str_0 = 'gbCv}'
    var_0 = module_0.duplicates_pre_sorted(str_0, str_0)
    var_1 = module_0.duplicates_bin_search(var_0, var_0)
    var_2 = module_0.duplicates_pre_sorted(var_0, var_1)
    int_0 = -2196

def test_case_5():
    dict_0 = {}
    str_0 = 'A9b?oSSW|&\\mdOuO"'
    var_0 = module_0.duplicates_pre_sorted(str_0, dict_0)
    var_1 = module_0.duplicates_pre_sorted(dict_0, dict_0)
    none_type_0 = None

def test_case_6():
    str_0 = '+'
    var_0 = module_0.duplicates_bin_search(str_0, str_0)
    var_1 = module_0.duplicates_bin_search(var_0, var_0)
    var_2 = module_0.duplicates_pre_sorted(var_0, var_1)

def test_case_7():
    bytes_0 = b'\x1dh\x9c\xf0\xd3\xbe\xb7C\x19\xf5\xad\x9a\x81C'

def test_case_8():
    bool_0 = False
