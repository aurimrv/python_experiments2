#Pyguin test cases converted from long-comm/MIO/seed_1706/test_longest_common_prefix.py
import pytest
import longest_common_prefix as module_0

def test_case_0():
    str_0 = 'O'
    var_0 = module_0.find_longest_common_prefix(str_0)
    assert var_0 == 'O'

def test_case_1():
    str_0 = 'N'
    bytes_0 = b'V\xfd\x1e[9;\xde\xea\xd3\xff\x92\xa7\x17'
    tuple_0 = (str_0, bytes_0, bytes_0)
    list_0 = [tuple_0, str_0, tuple_0]
    var_0 = module_0.find_longest_common_prefix(list_0)
    assert var_0 == 'N'
    bytes_1 = b'\xff\xb4\xc3\xeb\xfd\xf3'

def test_case_2():
    list_0 = []
    list_1 = [list_0]
    var_0 = module_0.find_longest_common_prefix(list_1)
    assert var_0 == ''

def test_case_3():
    bytes_0 = b'\xff\xb4\xc3\xeb\xfd\xf3'
    list_0 = [bytes_0, bytes_0]

def test_case_4():
    list_0 = []
    var_0 = module_0.find_longest_common_prefix(list_0)
    assert var_0 == ''

def test_case_5():
    bytes_0 = b'\xff\xb4\xc3\xeb\xfd\xf3'

def test_case_6():
    list_0 = []
    var_0 = module_0.find_longest_common_prefix_reduce(list_0)
    assert var_0 == ''

def test_case_7():
    str_0 = '\x0c(Jg^3#Sy{B`<'
    var_0 = module_0.find_longest_common_prefix_reduce(str_0)
    assert var_0 == ''

def test_case_8():
    bytes_0 = b'\x93\xbaz\x7f:\xeeW\xb0\xcb\xf8\xe2B\xce\xf5\x18V'
    list_0 = [bytes_0, bytes_0, bytes_0, bytes_0]
    var_0 = module_0.find_longest_common_prefix_reduce(list_0)
    assert var_0 == b'\x93\xbaz\x7f:\xeeW\xb0\xcb\xf8\xe2B\xce\xf5\x18V'

def test_case_9():
    bytes_0 = b'\xff\xb4\xc3\xeb\xfd\xf3'
