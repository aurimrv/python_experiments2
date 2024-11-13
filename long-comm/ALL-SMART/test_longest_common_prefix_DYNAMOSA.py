#Pyguin test cases converted from long-comm/DYNAMOSA/seed_1706/test_longest_common_prefix.py
import pytest
import longest_common_prefix as module_0

def test_case_0():
    bytes_0 = b'\xb7;n\x9e\x87\x86\x1f\xd4\x02\x93\xe9\x13\xb9\x94'
    list_0 = [bytes_0, bytes_0]

def test_case_1():
    set_0 = set()
    var_0 = module_0.find_longest_common_prefix_reduce(set_0)
    assert var_0 == ''
    var_1 = module_0.find_longest_common_prefix(var_0)
    assert var_1 == ''

def test_case_2():
    bytes_0 = b'\xb7;n\x9e\x87\x86\x1f\xd4\x02\x93\xe9\x13\xb9\x94'
    list_0 = [bytes_0, bytes_0]
    var_0 = module_0.find_longest_common_prefix_reduce(list_0)
    assert var_0 == b'\xb7;n\x9e\x87\x86\x1f\xd4\x02\x93\xe9\x13\xb9\x94'

def test_case_3():
    bool_0 = True
    str_0 = '67%H+H]R~O0FKk<=p'
    var_0 = module_0.find_longest_common_prefix_reduce(str_0)
    assert var_0 == ''
    list_0 = [bool_0, bool_0, bool_0]

def test_case_4():
    bool_0 = False

def test_case_5():
    set_0 = set()
    list_0 = [set_0, set_0]
    var_0 = module_0.find_longest_common_prefix(list_0)
    assert var_0 == ''
    var_1 = module_0.find_longest_common_prefix_reduce(set_0)
    assert var_1 == ''
    var_2 = module_0.find_longest_common_prefix(var_1)
    assert var_2 == ''

def test_case_6():
    str_0 = 'U'
    var_0 = module_0.find_longest_common_prefix(str_0)
    assert var_0 == 'U'
    list_0 = [str_0, str_0, str_0, str_0]
    var_1 = module_0.find_longest_common_prefix_reduce(list_0)
    assert var_1 == 'U'
    var_2 = module_0.find_longest_common_prefix_reduce(var_1)
    assert var_2 == 'U'
    list_1 = [str_0, list_0, str_0]
    var_3 = module_0.find_longest_common_prefix(list_1)
    assert var_3 == 'U'
    var_4 = module_0.find_longest_common_prefix_reduce(var_1)
    assert var_4 == 'U'
