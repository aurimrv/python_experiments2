#Pyguin test cases converted from complement/MIO/seed_1706/test_complement.py
import pytest
import complement as module_0
import builtins as module_1

def test_case_0():
    bool_0 = False
    var_0 = module_0.complement(bool_0)
    assert var_0 == 1
    var_1 = module_0.complement(var_0)
    assert var_1 == 0

def test_case_1():
    int_0 = -561
    var_0 = module_0.complement(int_0)
    assert var_0 == -561

def test_case_2():
    int_0 = 879
    var_0 = module_0.complement(int_0)
    assert var_0 == 144
    dict_0 = {}
    none_type_0 = None
    var_1 = module_0.complement(none_type_0)
    assert var_1 == 1
    var_2 = module_0.complement(dict_0)
    assert var_2 == 1
    var_3 = module_0.complement(dict_0)
    assert var_3 == 1
    var_4 = module_0.complement(dict_0)
    assert var_4 == 1
    object_0 = module_1.object()

def test_case_3():
    str_0 = 'rKd%>0:7(*K\\\nAZP<'

def test_case_4():
    none_type_0 = None
    var_0 = module_0.complement(none_type_0)
    assert var_0 == 1
