#Pyguin test cases converted from find-duplicates/DYNAMOSA/seed_1706/test_find_duplicates.py
import pytest
import find_duplicates as module_0
import builtins as module_1
import binary_search as module_2

def test_case_0():
    int_0 = 91
    bool_0 = False
    bytes_0 = b'\x80'
    tuple_0 = (int_0, bool_0, bytes_0)
    var_0 = module_0.duplicates_linear(tuple_0, bytes_0)

def test_case_1():
    str_0 = 'kFWlt8d>XU'
    var_0 = module_0.duplicates_pre_sorted(str_0, str_0)

def test_case_2():
    none_type_0 = None
    set_0 = set()
    complex_0 = -418.17 - 2728.1j
    var_0 = module_0.duplicates_pre_sorted(set_0, complex_0)

def test_case_3():
    str_0 = 'V'
    var_0 = module_0.duplicates_pre_sorted(str_0, str_0)
    var_1 = module_0.duplicates_linear(str_0, str_0)
    var_2 = module_0.duplicates_linear(var_1, str_0)
    var_3 = module_0.duplicates_bin_search(var_1, var_0)

def test_case_4():
    str_0 = 'kFWlt8d>XU'
    var_0 = module_0.duplicates_pre_sorted(str_0, str_0)
    var_1 = module_0.duplicates_linear(str_0, str_0)
    tuple_0 = (var_1, var_0, var_0)

def test_case_5():
    str_0 = 'kFWlt8d>XU'
    var_0 = module_0.duplicates_pre_sorted(str_0, str_0)
    var_1 = module_0.duplicates_linear(str_0, str_0)
    var_2 = module_0.duplicates_pre_sorted(var_0, var_0)
    var_3 = module_1.object()

def test_case_6():
    str_0 = 'cR=7. ]V)zlZ:J\x0ct'
    var_0 = module_0.duplicates_pre_sorted(str_0, str_0)

def test_case_7():
    str_0 = '_'
    list_0 = [str_0, str_0, str_0]
    var_0 = module_0.duplicates_pre_sorted(list_0, str_0)
    str_1 = 'cR=7. ]V)zlZ:J\x0ct'
    var_1 = module_0.duplicates_pre_sorted(str_1, str_1)

def test_case_8():
    bytes_0 = b']?6\xda\x83'
    dict_0 = {}
    var_0 = module_0.duplicates_linear(dict_0, dict_0)
    tuple_0 = (dict_0,)
    var_1 = module_0.duplicates_bin_search(dict_0, dict_0)
    var_2 = module_0.duplicates_linear(bytes_0, var_1)
    var_3 = module_0.duplicates_bin_search(var_1, tuple_0)
    var_4 = module_0.duplicates_pre_sorted(var_1, bytes_0)
    var_5 = module_0.duplicates_bin_search(tuple_0, var_1)
    var_6 = module_0.duplicates_pre_sorted(tuple_0, var_3)
    var_7 = module_0.duplicates_bin_search(dict_0, var_1)
    var_8 = module_0.duplicates_pre_sorted(var_3, var_0)
    var_9 = module_0.duplicates_bin_search(var_0, dict_0)

def test_case_9():
    str_0 = 'V'
    var_0 = module_0.duplicates_pre_sorted(str_0, str_0)
    var_1 = module_0.duplicates_linear(str_0, str_0)
    bytes_0 = b'\xab</\xa7\xa2\xce|\x1de\x1d\xe7'

def test_case_10():
    str_0 = 'j{_'
    list_0 = [str_0, str_0, str_0]
    var_0 = module_0.duplicates_pre_sorted(list_0, str_0)
    str_1 = 'cR=7. ]V)zZ:J\x0ct'
