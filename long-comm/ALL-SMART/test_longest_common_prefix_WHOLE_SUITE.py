#Pyguin test cases converted from long-comm/WHOLE_SUITE/seed_1706/test_longest_common_prefix.py
import pytest
import longest_common_prefix as module_0
import trie as module_1

def test_case_0():
    int_0 = -1419
    bool_0 = True
    dict_0 = {int_0: int_0, int_0: bool_0}
    var_0 = module_0.find_longest_common_prefix_reduce(dict_0)
    assert var_0 == -1419
    str_0 = ')v=z{U-B1'
    list_0 = [str_0, str_0, str_0]
    var_1 = module_0.find_longest_common_prefix_reduce(list_0)
    assert var_1 == ')v=z{U-B1'
    var_2 = module_0.find_longest_common_prefix(list_0)
    assert var_2 == ')v=z{U-B1'
    tuple_0 = (list_0,)

def test_case_1():
    none_type_0 = None
    var_0 = module_0.find_longest_common_prefix_reduce(none_type_0)
    assert var_0 == ''

def test_case_2():
    list_0 = []
    var_0 = module_0.find_longest_common_prefix_reduce(list_0)
    assert var_0 == ''

def test_case_3():
    str_0 = '"^LCJ(6Y~N '
    float_0 = -597.0018002832842
    var_0 = module_0.find_longest_common_prefix_reduce(str_0)
    assert var_0 == ''
    var_1 = module_0.find_longest_common_prefix_reduce(str_0)
    assert var_1 == ''
    var_2 = module_0.find_longest_common_prefix_reduce(str_0)
    assert var_2 == ''
    list_0 = [float_0, float_0, float_0]

def test_case_4():
    bytes_0 = b'\x7fa)b\xfcP\x8c\x13&\xb7\x02'
    str_0 = 's3]JKV'
    set_0 = {bytes_0, str_0, str_0, str_0}
    tuple_0 = (str_0, set_0)
    var_0 = module_0.find_longest_common_prefix(tuple_0)
    assert var_0 == ''

def test_case_5():
    bool_0 = False
    var_0 = module_0.find_longest_common_prefix_reduce(bool_0)
    assert var_0 == ''
    list_0 = [var_0]
    var_1 = module_0.find_longest_common_prefix(list_0)
    assert var_1 == ''
    list_1 = [bool_0]
    var_2 = module_0.find_longest_common_prefix_reduce(list_1)
    var_3 = module_0.find_longest_common_prefix_reduce(list_1)
    list_2 = []
    var_4 = module_0.find_longest_common_prefix_reduce(list_2)
    assert var_4 == ''
    var_5 = module_0.find_longest_common_prefix(list_2)
    assert var_5 == ''
    none_type_0 = None
    var_6 = module_0.find_longest_common_prefix_reduce(none_type_0)
    assert var_6 == ''
    var_7 = module_0.find_longest_common_prefix(list_2)
    bytes_0 = b'\xa0\xeen\xb5'

def test_case_6():
    bool_0 = True
    list_0 = []
    var_0 = module_0.find_longest_common_prefix_reduce(list_0)
    assert var_0 == ''
    bool_1 = False
    list_1 = [bool_0, bool_0, bool_1, bool_1]

def test_case_7():
    bool_0 = False

def test_case_8():
    bytes_0 = b'r\xfd\xd3\x12\xfcCs\xe4%\x1a\xe3\xc0\xe6r\xff\x97x\xb6w'

def test_case_9():
    none_type_0 = None
    list_0 = [none_type_0, none_type_0]

def test_case_10():
    float_0 = -2818.838
    none_type_0 = None
    var_0 = module_0.find_longest_common_prefix_reduce(none_type_0)
    assert var_0 == ''
    tuple_0 = (float_0, var_0)
    tuple_1 = (float_0, tuple_0)
    list_0 = [tuple_1, tuple_0]
