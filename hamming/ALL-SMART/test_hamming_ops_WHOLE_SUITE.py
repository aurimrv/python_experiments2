#Pyguin test cases converted from hamming/WHOLE_SUITE/seed_1706/test_hamming_ops.py
import pytest
import hamming_ops as module_0

def test_case_0():
    none_type_0 = None
    var_0 = module_0.hamming_weight(none_type_0)
    assert var_0 == 0
    int_0 = -2371

def test_case_1():
    bool_0 = False
    var_0 = module_0.hamming_weight(bool_0)
    assert var_0 == 0
    bool_1 = False
    var_1 = module_0.hamming_distance(var_0, bool_1)
    assert var_1 == 0
    var_2 = module_0.hamming_weight(var_1)
    assert var_2 == 0
    var_3 = module_0.hamming_distance(var_0, bool_0)
    assert var_3 == 0
    int_0 = 3359
    var_4 = module_0.hamming_distance(int_0, var_0)
    assert var_4 == 8
    var_5 = module_0.hamming_weight(int_0)
    assert var_5 == 8
    var_6 = module_0.hamming_weight(var_0)
    assert var_6 == 0
    var_7 = module_0.hamming_weight(var_1)
    assert var_7 == 0
    var_8 = module_0.hamming_weight(int_0)
    assert var_8 == 8
    var_9 = module_0.hamming_weight(var_8)
    assert var_9 == 1
    var_10 = module_0.hamming_distance(bool_1, int_0)
    assert var_10 == 8

def test_case_2():
    complex_0 = -2984.92216 + 1289j

def test_case_3():
    bool_0 = False
    var_0 = module_0.hamming_weight(bool_0)
    assert var_0 == 0
    bool_1 = False
    var_1 = module_0.hamming_weight(bool_1)
    assert var_1 == 0
    var_2 = module_0.hamming_weight(var_1)
    assert var_2 == 0
    int_0 = -859

def test_case_4():
    int_0 = -540
    bool_0 = False
    var_0 = module_0.hamming_weight(bool_0)
    assert var_0 == 0

def test_case_5():
    int_0 = 7
    float_0 = 3404.0
    dict_0 = {float_0: int_0}
    bool_0 = False
    bool_1 = False
    var_0 = module_0.hamming_weight(bool_1)
    assert var_0 == 0

def test_case_6():
    float_0 = -1048.48

def test_case_7():
    bool_0 = True
    bool_1 = True
    var_0 = module_0.hamming_weight(bool_1)
    assert var_0 == 1
    var_1 = module_0.hamming_distance(bool_0, bool_0)
    assert var_1 == 0
    var_2 = module_0.hamming_distance(bool_0, bool_0)
    assert var_2 == 0
    bool_2 = False
    var_3 = module_0.hamming_weight(bool_2)
    assert var_3 == 0
    var_4 = module_0.hamming_weight(var_2)
    assert var_4 == 0
    int_0 = -1720
    var_5 = module_0.hamming_distance(int_0, int_0)
    assert var_5 == 0
