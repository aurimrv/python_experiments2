#Pyguin test cases converted from heapsort/MIO/seed_1706/test_heapsort.py
import pytest
import heapsort as module_0

def test_case_0():
    bytes_0 = b'7\x9f}\xae\xa1M\x88\xd0\x81\x89\xed\xb7\x08\x96\x1a\x1d\xf1\xab'
    list_0 = [bytes_0, bytes_0]
    var_0 = module_0.heap_sort(list_0)

def test_case_1():
    list_0 = []
    var_0 = module_0.heap_sort(list_0)

def test_case_2():
    bytes_0 = b'\xa0s'
    var_0 = module_0.max_heap_sort(bytes_0)

def test_case_3():
    list_0 = []
    var_0 = module_0.custom_heap_sort(list_0, list_0)

def test_case_4():
    float_0 = -3092.7

def test_case_5():
    float_0 = 429.01
    list_0 = [float_0, float_0, float_0, float_0, float_0]
    var_0 = module_0.custom_heap_sort(list_0)

def test_case_6():
    bool_0 = False

def test_case_7():
    bool_0 = False
