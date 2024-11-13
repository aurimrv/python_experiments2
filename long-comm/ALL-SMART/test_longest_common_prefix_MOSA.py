#Pyguin test cases converted from long-comm/MOSA/seed_1706/test_longest_common_prefix.py
import pytest
import longest_common_prefix as module_0

def test_case_0():
    bytes_0 = b'\x0f'
    list_0 = [bytes_0, bytes_0, bytes_0, bytes_0]

def test_case_1():
    bytes_0 = b''
    list_0 = [bytes_0, bytes_0, bytes_0, bytes_0]
    var_0 = module_0.find_longest_common_prefix(list_0)
    assert var_0 == ''

def test_case_2():
    bool_0 = False
    tuple_0 = (bool_0, bool_0)
    tuple_1 = (tuple_0,)

def test_case_3():
    set_0 = set()
    var_0 = module_0.find_longest_common_prefix_reduce(set_0)
    assert var_0 == ''
    var_1 = module_0.find_longest_common_prefix(var_0)
    assert var_1 == ''

def test_case_4():
    bytes_0 = b'\xee\x8d\xac\xd0\xbb\xde\x1d\x17\x05['

def test_case_5():
    bytes_0 = b'.\xbc\xde\x18\x0e\x05\xf2o'
    bytes_1 = b'\x89 ~\xebc8p\xa5\xe8\xf3E36\x810\x9f\xc6\xb1\xa1'
    list_0 = [bytes_1, bytes_0]
    var_0 = module_0.find_longest_common_prefix_reduce(list_0)
    assert var_0 == b''
    list_1 = [bytes_0, bytes_0, bytes_0, bytes_0]

def test_case_6():
    bool_0 = True
    str_0 = '67%H+H]R~O0FKk<=p'
    var_0 = module_0.find_longest_common_prefix_reduce(str_0)
    assert var_0 == ''
    list_0 = [bool_0, bool_0, bool_0]

def test_case_7():
    bytes_0 = b'.\xbc\xde\x18\x0e\x05\xf2o'
    list_0 = [bytes_0, bytes_0, bytes_0, bytes_0]
    var_0 = module_0.find_longest_common_prefix_reduce(list_0)
    assert var_0 == b'.\xbc\xde\x18\x0e\x05\xf2o'
    list_1 = [bytes_0, bytes_0, bytes_0, bytes_0]

def test_case_8():
    bool_0 = False

def test_case_9():
    str_0 = '\x0b'
    list_0 = [str_0, str_0, str_0, str_0]
    tuple_0 = (str_0, list_0, str_0, list_0)
    var_0 = module_0.find_longest_common_prefix(tuple_0)
    assert var_0 == '\x0b'
    list_1 = [var_0]
    var_1 = module_0.find_longest_common_prefix_reduce(list_1)
    assert var_1 == '\x0b'
    bytes_0 = b'\xc5CQ2S\xdal\xa18Y\x19'
    list_2 = [bytes_0, bytes_0, bytes_0, bytes_0]
    var_2 = module_0.find_longest_common_prefix_reduce(list_2)
    assert var_2 == b'\xc5CQ2S\xdal\xa18Y\x19'
