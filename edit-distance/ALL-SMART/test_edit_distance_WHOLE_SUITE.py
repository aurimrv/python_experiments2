#Pyguin test cases converted from edit-distance/WHOLE_SUITE/seed_1706/test_edit_distance.py
import pytest
import edit_distance as module_0
import builtins as module_1

def test_case_0():
    none_type_0 = None
    none_type_1 = None

def test_case_1():
    bool_0 = True

def test_case_2():
    bool_0 = True

def test_case_3():
    str_0 = 'Gl`!ZRgDw " xVxW6,'
    str_1 = 'Gl`!ZRgDw  xV0\\tW6,0'
    var_0 = module_0.calculate_edit_distance(str_1, str_0)
    bool_0 = False

def test_case_4():
    int_0 = 7

def test_case_5():
    str_0 = ';d.8*z21R'
    bool_0 = False
    bytes_0 = b'\x81C(\xaf\xbd\x8d\x92\xeae\xf9\xf5d|S\xc7.\xa43%'
    tuple_0 = (bool_0, bool_0, bytes_0, str_0)
    list_0 = [str_0, str_0, tuple_0, bool_0]
    str_1 = "G\nnUY'1ZLIU:u;q"
    str_2 = '_}Qn>Tz'
    bytes_1 = b'\xa0)\\\x0f\xb7\x7f\xcbm\xc5\xef\x87'
    dict_0 = {str_0: list_0, str_1: str_1, str_1: tuple_0, str_2: bytes_1}

def test_case_6():
    str_0 = '1rgC'
    var_0 = module_0.calculate_edit_distance(str_0, str_0)

def test_case_7():
    pass

def test_case_8():
    object_0 = module_1.object()
    bytes_0 = b'\x85\xa1\x81\xd6\xc8\xc2\x15\x1ft'
    bytes_1 = b'\xb4\x04\x81\xb5\x891O\x85\xd6\x8d\x99DN)U'

def test_case_9():
    bool_0 = False

def test_case_10():
    str_0 = ''
    var_0 = module_0.calculate_edit_distance(str_0, str_0)
