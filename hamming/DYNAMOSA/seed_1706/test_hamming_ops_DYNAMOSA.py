#Pyguin test cases converted from hamming/DYNAMOSA/seed_1706/test_hamming_ops.py
import pytest
import hamming_ops as module_0

def test_case_0():
    int_0 = 1022
    var_0 = module_0.hamming_weight(int_0)
    assert var_0 == 9

def test_case_1():
    int_0 = 1926
    var_0 = module_0.hamming_weight(int_0)
    assert var_0 == 6
    bool_0 = False
    var_1 = module_0.hamming_weight(bool_0)
    assert var_1 == 0

def test_case_2():
    int_0 = -3158
    bool_0 = False
