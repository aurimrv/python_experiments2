#Pyguin test cases converted from fibonacci/WHOLE_SUITE/seed_1706/test_fibonacci.py
import pytest
import fibonacci as module_0

def test_case_0():
    bool_0 = True
    var_0 = module_0.fibonacci_recursive(bool_0)
    assert var_0 is True
    var_1 = module_0.fibonacci_dp(var_0)
    assert var_1 == 1
    var_2 = module_0.fibonacci_dp(bool_0)
    assert var_2 == 1
    bool_1 = False
    var_3 = module_0.fibonacci_dp(bool_1)
    assert var_3 == 0
    var_4 = module_0.fibonacci_recursive(bool_1)
    assert var_4 == 0
    var_5 = module_0.fibonacci_recursive(bool_1)
    assert var_5 == 0
    var_6 = module_0.fibonacci_recursive(bool_1)
    assert var_6 == 0
    var_7 = module_0.fibonacci_recursive(var_6)
    assert var_7 == 0

def test_case_1():
    bool_0 = False
    var_0 = module_0.fibonacci_dp(bool_0)
    assert var_0 == 0
    var_1 = module_0.fibonacci_recursive(bool_0)
    assert var_1 == 0

def test_case_2():
    float_0 = -99.91
    var_0 = module_0.fibonacci_recursive(float_0)
    assert var_0 == 0
    var_1 = module_0.fibonacci_recursive(float_0)
    assert var_1 == 0
    bytes_0 = b'\xf6\xecC@\x9c\xd6\x80JbM \xc6%dl\xd3M-\xa4'

def test_case_3():
    str_0 = '9aqboW*[$*!-UZ9='

def test_case_4():
    int_0 = 619
    bool_0 = False
    var_0 = module_0.fibonacci_dp(bool_0)
    assert var_0 == 0
    bool_1 = False
    var_1 = module_0.fibonacci_dp(bool_1)
    assert var_1 == 0
    int_1 = -972
    var_2 = module_0.fibonacci_recursive(int_1)
    assert var_2 == 0
    var_3 = module_0.fibonacci_recursive(var_2)
    assert var_3 == 0
    var_4 = module_0.fibonacci_dp(int_0)
    assert var_4 == 1032438788598817315437189032298124708705297018004363191791263255924514005104084376841381572199036650610593743671014987440620684581
    bool_2 = True
    var_5 = module_0.fibonacci_dp(bool_2)
    assert var_5 == 1
    bool_3 = True
    var_6 = module_0.fibonacci_dp(bool_3)
    assert var_6 == 1

def test_case_5():
    pass
