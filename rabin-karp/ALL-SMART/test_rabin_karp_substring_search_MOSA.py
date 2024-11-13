#Pyguin test cases converted from rabin-karp/MOSA/seed_1706/test_rabin_karp_substring_search.py
import pytest
import rabin_karp_substring_search as module_0

def test_case_0():
    str_0 = '\tdw$K6e9hR()_Q'
    var_0 = module_0.rabin_karp_find_substring(str_0, str_0)
    assert var_0 == 0

def test_case_1():
    set_0 = set()
    var_0 = module_0.rabin_karp_find_substring(set_0, set_0)
    assert var_0 == 0

def test_case_2():
    none_type_0 = None

def test_case_3():
    str_0 = "*Q~z'&KS/5aMcsX\th0#S"
    str_1 = "*Q~z'&1S/5aMcsX\th0#S"
    var_0 = module_0.rabin_karp_find_substring(str_1, str_0)
    assert var_0 == -1

def test_case_4():
    str_0 = '\tdw$K6e9hR()_6Q'
    str_1 = 'a|U`G'
    var_0 = module_0.rabin_karp_find_substring(str_0, str_1)
    assert var_0 == -1
    none_type_0 = None

def test_case_5():
    str_0 = "*Q~z'&KS/5aMcsX\th0#S"
    str_1 = "*Q~z'&1S/5aMcsX\th0#S"
    bool_0 = False
    var_0 = module_0.rabin_karp_find_substring(str_1, str_0, bool_0)
    assert var_0 == -1
    var_1 = module_0.rabin_karp_find_substring(str_1, str_0)
    assert var_1 == -1
