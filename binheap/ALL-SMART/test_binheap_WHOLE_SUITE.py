#Pyguin test cases converted from binheap/WHOLE_SUITE/seed_1706/test_binheap.py
import pytest
import binheap as module_0

def test_case_0():
    binheap_0 = module_0.Binheap()
    assert f'{type(binheap_0).__module__}.{type(binheap_0).__qualname__}' == 'binheap.Binheap'
    assert binheap_0.container == [None]
    with pytest.raises(IndexError):
        binheap_0.pop()

def test_case_1():
    str_0 = 'y5!w6L\\x<#:LI'
    binheap_0 = module_0.Binheap(str_0)
    assert f'{type(binheap_0).__module__}.{type(binheap_0).__qualname__}' == 'binheap.Binheap'
    assert binheap_0.container == [None, 'y', 'x', '\\', 'w', ':', 'L', 'L', '5', '<', '#', '6', '!', 'I']
    var_0 = binheap_0.display()
    assert var_0 == '    y \n  x \\ \n w : L L \n5 < # 6 ! I \n'
    var_1 = binheap_0.display()
    assert var_1 == '    y \n  x \\ \n w : L L \n5 < # 6 ! I \n'

def test_case_2():
    binheap_0 = module_0.Binheap()
    assert f'{type(binheap_0).__module__}.{type(binheap_0).__qualname__}' == 'binheap.Binheap'
    assert binheap_0.container == [None]
    var_0 = binheap_0.display()
    assert var_0 == ''
    binheap_1 = module_0.Binheap()
    var_1 = binheap_1.display()
    assert var_1 == ''
    with pytest.raises(IndexError):
        binheap_1.pop()

def test_case_3():
    binheap_0 = module_0.Binheap()
    assert f'{type(binheap_0).__module__}.{type(binheap_0).__qualname__}' == 'binheap.Binheap'
    assert binheap_0.container == [None]
    var_0 = binheap_0.display()
    assert var_0 == ''

def test_case_4():
    complex_0 = -52 - 1606.8j
    binheap_0 = module_0.Binheap()
    assert f'{type(binheap_0).__module__}.{type(binheap_0).__qualname__}' == 'binheap.Binheap'
    assert binheap_0.container == [None]
    var_0 = binheap_0.display()
    assert var_0 == ''

def test_case_5():
    bytes_0 = b'\nk\xc5J9\x9c\xf9\xda\x1aJ'
    binheap_0 = module_0.Binheap(bytes_0)
    assert f'{type(binheap_0).__module__}.{type(binheap_0).__qualname__}' == 'binheap.Binheap'
    assert binheap_0.container == [None, 249, 218, 197, 74, 74, 107, 156, 10, 26, 57]
    binheap_1 = module_0.Binheap()
    assert f'{type(binheap_1).__module__}.{type(binheap_1).__qualname__}' == 'binheap.Binheap'
    assert binheap_1.container == [None]
    with pytest.raises(IndexError):
        binheap_1.pop()

def test_case_6():
    binheap_0 = module_0.Binheap()
    assert f'{type(binheap_0).__module__}.{type(binheap_0).__qualname__}' == 'binheap.Binheap'
    assert binheap_0.container == [None]
    int_0 = -287
    var_0 = binheap_0.push(int_0)
    var_1 = binheap_0.display()
    assert var_1 == '-287 \n'
    binheap_1 = module_0.Binheap()
    with pytest.raises(IndexError):
        binheap_1.pop()
