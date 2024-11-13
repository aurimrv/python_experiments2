#Pyguin test cases converted from convert-base/MOSA/seed_1706/test_convert_base.py
import pytest
import convert_base as module_0

def test_case_0():
    str_0 = 'Fr`#/'
    int_0 = 1922
    var_0 = module_0.convert_base(str_0, int_0)
    assert var_0 == -1

def test_case_1():
    str_0 = "n>Tz*D\x0b'J=kK7"
    var_0 = module_0.convert_digit_to_int(str_0)
    assert var_0 == -1
    var_1 = module_0.convert_digit_to_int(str_0)
    assert var_1 == -1
    bool_0 = False
    var_2 = module_0.convert_base(str_0, bool_0)
    assert var_2 == -1

def test_case_2():
    bool_0 = False

def test_case_3():
    str_0 = "'g\x0coz9"
    bool_0 = True

def test_case_4():
    none_type_0 = None
    int_0 = 3048
    var_0 = module_0.convert_base(none_type_0, int_0)
    assert var_0 == -1
    var_1 = module_0.convert_base(var_0, var_0)
    assert var_1 == -1

def test_case_5():
    str_0 = 'pc\x0b+P1'
    var_0 = module_0.convert_digit_to_int(str_0)
    assert var_0 == -1

def test_case_6():
    str_0 = '5aw:\t2TL'
    bool_0 = False
    var_0 = module_0.convert_base(str_0, bool_0)
    assert var_0 == -1
    str_1 = 'pc\x0b+P1'
    var_1 = module_0.convert_digit_to_int(str_1)
    assert var_1 == -1

def test_case_7():
    bool_0 = False
    str_0 = '\x0cQqKrux}$F.6H*yn0=\t1'
    var_0 = module_0.convert_digit_to_int(str_0)
    assert var_0 == -1
    str_1 = ''
    var_1 = module_0.convert_base(str_1, bool_0)
    assert var_1 == 0

def test_case_8():
    str_0 = '\r-MqS\\2'
    var_0 = module_0.convert_digit_to_int(str_0)
    assert var_0 == -1
    str_1 = '0f'
    bool_0 = False
    var_1 = module_0.convert_base(str_1, bool_0)
    assert var_1 == -1
    var_2 = module_0.convert_digit_to_int(str_0)
    assert var_2 == -1
    var_3 = module_0.convert_digit_to_int(str_0)
    assert var_3 == -1
    str_2 = '<u^|,H"&:l<\r'
    str_3 = "2GILmNk2M!(<'$\\atB"
    var_4 = module_0.convert_digit_to_int(str_3)
    assert var_4 == -1
    var_5 = module_0.convert_base(str_2, var_2)
    assert var_5 == -1
    str_4 = 'VYT;_ks%%e'
    var_6 = module_0.convert_base(str_4, var_3)
    assert var_6 == -1
    var_7 = module_0.convert_digit_to_int(str_0)
    assert var_7 == -1
    int_0 = 12
    var_8 = module_0.convert_base(var_5, int_0)
    assert var_8 == -1

def test_case_9():
    str_0 = '\r-MqS\\2'
    var_0 = module_0.convert_digit_to_int(str_0)
    assert var_0 == -1
    str_1 = '0f'
    bool_0 = False
    var_1 = module_0.convert_base(str_1, bool_0)
    assert var_1 == -1
    str_2 = 'U}BAZ2wt;P#'
    var_2 = module_0.convert_digit_to_int(str_2)
    assert var_2 == -1
    str_3 = '<u^|,H"&:l<\r'
    int_0 = -693
    int_1 = 16
    var_3 = module_0.convert_base(str_1, int_1)
    assert var_3 == 15
    str_4 = 'tlrDvS>f@Qv4,[\tz'
    var_4 = module_0.convert_base(str_4, var_2)
    assert var_4 == -1
    str_5 = '*kjy7{,SovB:1N?J-'
    var_5 = module_0.convert_base(str_5, int_0)
    assert var_5 == -1
    str_6 = 'P\n)G*99>\n8K'
    var_6 = module_0.convert_digit_to_int(str_6)
    assert var_6 == -1
