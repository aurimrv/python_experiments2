#Pyguin test cases converted from deque/MOSA/seed_1706/test_deque.py
import pytest
import deque as module_0

def test_case_0():
    deque_0 = module_0.Deque()
    var_0 = deque_0.peekleft()
    var_1 = deque_0.append(deque_0)
    var_2 = deque_0.peek()
    assert f'{type(var_2).__module__}.{type(var_2).__qualname__}' == 'deque.Deque'
    var_3 = var_2.popleft()
    assert f'{type(var_3).__module__}.{type(var_3).__qualname__}' == 'deque.Deque'
    var_4 = deque_0.size()

def test_case_1():
    deque_0 = module_0.Deque()
    var_0 = deque_0.size()
    var_1 = deque_0.peek()

def test_case_2():
    deque_0 = module_0.Deque()
    var_0 = deque_0.append(deque_0)
    bool_0 = True
    deque_1 = module_0.Deque()
    var_1 = deque_0.peekleft()
    assert f'{type(var_1).__module__}.{type(var_1).__qualname__}' == 'deque.Deque'
    var_2 = deque_1.append(bool_0)

def test_case_3():
    deque_0 = module_0.Deque()
    var_0 = deque_0.peekleft()
    var_1 = deque_0.size()

def test_case_4():
    deque_0 = module_0.Deque()

def test_case_5():
    none_type_0 = None
    deque_0 = module_0.Deque()
    var_0 = deque_0.appendleft(none_type_0)

def test_case_6():
    deque_0 = module_0.Deque()
    deque_1 = module_0.Deque()

def test_case_7():
    deque_0 = module_0.Deque()
    var_0 = deque_0.size()
