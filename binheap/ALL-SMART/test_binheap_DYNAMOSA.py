#Pyguin test cases converted from binheap/DYNAMOSA/seed_1706/test_binheap.py
import pytest
import binheap as module_0

def test_case_0():
    int_0 = 5326

def test_case_1():
    binheap_0 = module_0.Binheap()
    assert f'{type(binheap_0).__module__}.{type(binheap_0).__qualname__}' == 'binheap.Binheap'
    assert binheap_0.container == [None]
    with pytest.raises(IndexError):
        binheap_0.pop()

def test_case_2():
    int_0 = 2061
    str_0 = '1zI\x0cL&\x0cz'
    binheap_0 = module_0.Binheap(str_0)
    assert f'{type(binheap_0).__module__}.{type(binheap_0).__qualname__}' == 'binheap.Binheap'
    assert binheap_0.container == [None, 'z', 'z', 'I', 'L', '1', '&', '\x0c', '\x0c']

def test_case_3():
    binheap_0 = module_0.Binheap()
    assert f'{type(binheap_0).__module__}.{type(binheap_0).__qualname__}' == 'binheap.Binheap'
    assert binheap_0.container == [None]
    var_0 = binheap_0.push(binheap_0)
    var_1 = binheap_0.display()
    var_2 = binheap_0.pop()
    assert binheap_0.container == [None]
    var_3 = binheap_0.push(var_1)

def test_case_4():
    binheap_0 = module_0.Binheap()
    assert f'{type(binheap_0).__module__}.{type(binheap_0).__qualname__}' == 'binheap.Binheap'
    assert binheap_0.container == [None]
    var_0 = binheap_0.display()
    assert var_0 == ''
    with pytest.raises(IndexError):
        binheap_0.pop()

def test_case_5():
    float_0 = 1426.75
    binheap_0 = module_0.Binheap()
    assert f'{type(binheap_0).__module__}.{type(binheap_0).__qualname__}' == 'binheap.Binheap'
    assert binheap_0.container == [None]
    var_0 = binheap_0.push(float_0)
    var_1 = binheap_0.push(float_0)
    var_2 = binheap_0.display()
    assert var_2 == ' 1426.75 \n1426.75 \n'
    binheap_1 = module_0.Binheap()
    binheap_2 = module_0.Binheap()
    with pytest.raises(IndexError):
        binheap_2.pop()
