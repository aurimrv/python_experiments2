#Pyguin test cases converted from edit-distance/DYNAMOSA/seed_1706/test_edit_distance.py
import pytest
import edit_distance as module_0
import builtins as module_1

def test_case_0():
    str_0 = '\\O#q*4>m?3'
    var_0 = module_0.calculate_edit_distance(str_0, str_0)

def test_case_1():
    str_0 = ''
    var_0 = module_0.calculate_edit_distance(str_0, str_0)

def test_case_2():
    bool_0 = True

def test_case_3():
    str_0 = '4w*X9_'
    str_1 = ')4w*X9_'
    var_0 = module_0.calculate_edit_distance(str_0, str_1)

def test_case_4():
    str_0 = '4w*X9_'
    str_1 = '\x0b"C.\''
    var_0 = module_0.calculate_edit_distance(str_0, str_1)
