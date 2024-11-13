#Pyguin test cases converted from deque/MIO/seed_1706/test_deque.py
import pytest
import deque as module_0

def test_case_0():
    bytes_0 = b'\xec}k>dX!\x16\xc8F,d\x06'
    deque_0 = module_0.Deque()
    deque_1 = module_0.Deque(bytes_0)
    var_0 = deque_1.peek()
    assert var_0 == 6

def test_case_1():
    deque_0 = module_0.Deque()
    var_0 = deque_0.size()
    var_1 = deque_0.peek()

def test_case_2():
    float_0 = 200.0
    bytes_0 = b'\xc3\x11o\xdb\xd0'
    deque_0 = module_0.Deque()
    var_0 = deque_0.appendleft(deque_0)
    var_1 = deque_0.peekleft()
    assert f'{type(var_1).__module__}.{type(var_1).__qualname__}' == 'deque.Deque'
    var_2 = deque_0.size()
    var_3 = deque_0.append(bytes_0)

def test_case_3():
    deque_0 = module_0.Deque()
    var_0 = deque_0.peekleft()

def test_case_4():
    deque_0 = module_0.Deque()

def test_case_5():
    deque_0 = module_0.Deque()
    var_0 = deque_0.append(deque_0)
    var_1 = deque_0.size()

def test_case_6():
    deque_0 = module_0.Deque()
    var_0 = deque_0.peekleft()

def test_case_7():
    deque_0 = module_0.Deque()
    var_0 = deque_0.size()
