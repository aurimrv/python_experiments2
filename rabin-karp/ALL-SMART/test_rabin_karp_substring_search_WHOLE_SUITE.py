#Pyguin test cases converted from rabin-karp/WHOLE_SUITE/seed_1706/test_rabin_karp_substring_search.py
import pytest
import rabin_karp_substring_search as module_0
import builtins as module_1

def test_case_0():
    bool_0 = False
    none_type_0 = None

def test_case_1():
    set_0 = set()
    var_0 = module_0.rabin_karp_find_substring(set_0, set_0)
    assert var_0 == 0
    object_0 = module_1.object()

def test_case_2():
    dict_0 = {}
    object_0 = module_1.object(**dict_0)

def test_case_3():
    bool_0 = True
    none_type_0 = None

def test_case_4():
    str_0 = '\n*;<]6GDhuf'
    var_0 = module_0.rabin_karp_find_substring(str_0, str_0)
    assert var_0 == 0

def test_case_5():
    bytes_0 = b'\x15\x92v+\xbb\xb9\xc2\xde\x1d\xfd\x83`\x1aU\x81{\xa1'
    none_type_0 = None

def test_case_6():
    int_0 = 1454
    list_0 = [int_0, int_0, int_0]

def test_case_7():
    str_0 = '{p21'
    str_1 = '\\}Lh5MUf1;DhOC>N'
    var_0 = module_0.rabin_karp_find_substring(str_1, str_0)
    assert var_0 == -1
    bytes_0 = b'\xe6l\x1f\xff\xcfA\x87N,n\xec'

def test_case_8():
    str_0 = '{p2'
    str_1 = '\\}Lh5MUf1\rDhOCx7>N'
    var_0 = module_0.rabin_karp_find_substring(str_1, str_0)
    assert var_0 == -1
