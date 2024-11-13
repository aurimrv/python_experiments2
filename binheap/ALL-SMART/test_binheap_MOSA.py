#Pyguin test cases converted from binheap/MOSA/seed_1706/test_binheap.py
import pytest
import binheap as module_0

def test_case_0():
    dict_0 = {}
    float_0 = 1912.019
    tuple_0 = (dict_0, float_0)
    tuple_1 = (dict_0, float_0, tuple_0)

def test_case_1():
    int_0 = 5326

def test_case_2():
    binheap_0 = module_0.Binheap()
    assert f'{type(binheap_0).__module__}.{type(binheap_0).__qualname__}' == 'binheap.Binheap'
    assert binheap_0.container == [None]
    with pytest.raises(IndexError):
        binheap_0.pop()

def test_case_3():
    binheap_0 = module_0.Binheap()
    assert f'{type(binheap_0).__module__}.{type(binheap_0).__qualname__}' == 'binheap.Binheap'
    assert binheap_0.container == [None]
    var_0 = binheap_0.push(binheap_0)
    var_1 = binheap_0.display()

def test_case_4():
    binheap_0 = module_0.Binheap()
    assert f'{type(binheap_0).__module__}.{type(binheap_0).__qualname__}' == 'binheap.Binheap'
    assert binheap_0.container == [None]
    var_0 = binheap_0.display()
    assert var_0 == ''

def test_case_5():
    str_0 = 'dk26:Z0f>x'
    binheap_0 = module_0.Binheap()
    assert f'{type(binheap_0).__module__}.{type(binheap_0).__qualname__}' == 'binheap.Binheap'
    assert binheap_0.container == [None]
    var_0 = binheap_0.push(str_0)
    none_type_0 = None
    var_1 = binheap_0.pop()
    assert binheap_0.container == [None]
    binheap_1 = module_0.Binheap(none_type_0)
    binheap_2 = module_0.Binheap(str_0)
    assert f'{type(binheap_2).__module__}.{type(binheap_2).__qualname__}' == 'binheap.Binheap'
    assert binheap_2.container == [None, 'x', 'k', 'Z', 'd', 'f', '2', '0', '6', '>', ':']
    var_2 = binheap_0.push(binheap_1)

def test_case_6():
    float_0 = 1426.75
    binheap_0 = module_0.Binheap()
    assert f'{type(binheap_0).__module__}.{type(binheap_0).__qualname__}' == 'binheap.Binheap'
    assert binheap_0.container == [None]
    var_0 = binheap_0.push(float_0)
    var_1 = binheap_0.push(float_0)
    var_2 = binheap_0.display()
    assert var_2 == ' 1426.75 \n1426.75 \n'
    binheap_1 = module_0.Binheap()
