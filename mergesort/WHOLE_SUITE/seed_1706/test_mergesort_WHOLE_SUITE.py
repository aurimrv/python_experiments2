#Pyguin test cases converted from mergesort/WHOLE_SUITE/seed_1706/test_mergesort.py
import pytest
import mergesort as module_0
import collections as module_1

def test_case_0():
    bool_0 = False

def test_case_1():
    none_type_0 = None

def test_case_2():
    str_0 = 'agZZ '
    var_0 = module_0.mergesort(str_0)
    var_1 = module_0.mergesort(var_0)
    var_2 = module_0.mergesort(var_0)
    set_0 = set()
    var_3 = module_0.mergesort(var_2)
    var_4 = module_0.mergesort(var_2)
    var_5 = module_0.mergesort(var_2)
    dict_0 = {}
    var_6 = module_0.mergesort(var_5)
    var_7 = module_0.mergesort(dict_0)
    var_8 = module_0.mergesort(dict_0)
    var_9 = module_0.mergesort(var_4)
    var_10 = module_0.mergesort(var_0)
    var_11 = module_0.mergesort(var_10)
    var_12 = module_0.mergesort(var_0)
    var_13 = module_0.mergesort(var_0)
    var_14 = module_0.mergesort(str_0)
    var_15 = module_0.mergesort(var_13)
    var_16 = module_0.mergesort(var_14)
    var_17 = module_0.mergesort(var_15)
    var_18 = module_0.mergesort(var_7)
    var_19 = module_0.mergesort(set_0)
    var_20 = module_0.mergesort(var_19)
    var_21 = module_0.mergesort(var_10)
    var_22 = module_0.mergesort(dict_0)
    var_23 = module_0.mergesort(var_8)
    var_24 = module_0.mergesort(var_13)
    var_25 = module_0.mergesort(var_8)
    var_26 = module_0.mergesort(var_0)
    var_27 = module_0.mergesort(set_0)
    var_28 = module_0.mergesort(var_7)
    var_29 = module_0.mergesort(var_18)
    var_30 = module_0.mergesort(var_19)
    var_31 = module_0.mergesort(str_0)
    deque_0 = module_1.deque()
    var_32 = module_0.mergesort(deque_0)

def test_case_3():
    int_0 = 155

def test_case_4():
    bool_0 = False

def test_case_5():
    dict_0 = {}
    deque_0 = module_1.deque(**dict_0)
    var_0 = module_0.mergesort(deque_0)
    assert f'{type(var_0).__module__}.{type(var_0).__qualname__}' == 'collections.deque'
    assert len(var_0) == 0
    var_1 = module_0.mergesort(deque_0)
    var_2 = module_0.mergesort(var_0)
    var_3 = module_0.mergesort(dict_0)
    var_4 = module_0.mergesort(var_1)
    var_5 = module_0.mergesort(var_0)
    str_0 = 'N*\rG3!}k'
    var_6 = module_0.mergesort(str_0)
    var_7 = module_0.mergesort(var_1)
    var_8 = module_0.mergesort(var_5)
    set_0 = {str_0, str_0, str_0}
    var_9 = module_0.mergesort(var_3)
    var_10 = module_0.mergesort(str_0)
    var_11 = module_0.mergesort(set_0)
    var_12 = module_0.mergesort(var_3)
    var_13 = module_0.mergesort(var_11)

def test_case_6():
    deque_0 = module_1.deque()
    var_0 = module_0.mergesort(deque_0)
    assert f'{type(var_0).__module__}.{type(var_0).__qualname__}' == 'collections.deque'
    assert len(var_0) == 0
    var_1 = module_0.mergesort(deque_0)
    var_2 = module_0.mergesort(deque_0)
    var_3 = module_0.mergesort(var_2)
    list_0 = [deque_0, deque_0, deque_0]
    var_4 = module_0.mergesort(var_1)

def test_case_7():
    pass
