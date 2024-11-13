#Pyguin test cases converted from complement/DYNAMOSA/seed_1706/test_complement.py
import pytest
import complement as module_0

def test_case_0():
    float_0 = -335.788283
    var_0 = module_0.complement(float_0)
    assert var_0 == pytest.approx(-335.788283, abs=0.01, rel=0.01)

def test_case_1():
    none_type_0 = None
    var_0 = module_0.complement(none_type_0)
    assert var_0 == 1

def test_case_2():
    float_0 = 734.9873
    none_type_0 = None
    var_0 = module_0.complement(none_type_0)
    assert var_0 == 1

def test_case_3():
    none_type_0 = None
    var_0 = module_0.complement(none_type_0)
    assert var_0 == 1
    var_1 = module_0.complement(var_0)
    assert var_1 == 0
    int_0 = 1480
    var_2 = module_0.complement(int_0)
    assert var_2 == 567
    var_3 = module_0.complement(int_0)
    assert var_3 == 567
    var_4 = module_0.complement(var_2)
    assert var_4 == 456

def test_case_4():
    set_0 = set()
    var_0 = module_0.complement(set_0)
    assert var_0 == 1
    bool_0 = True
    none_type_0 = None
    var_1 = module_0.complement(none_type_0)
    assert var_1 == 1
    var_2 = module_0.complement(bool_0)
    assert var_2 == 0
    str_0 = '@d&QXpS z}J\tfS'
