#Pyguin test cases converted from heapsort/MOSA/seed_1706/test_heapsort.py
import pytest
import heapsort as module_0

def test_case_0():
    bool_0 = False
    list_0 = [bool_0, bool_0]
    var_0 = module_0.heap_sort(list_0)

def test_case_1():
    list_0 = []
    var_0 = module_0.heap_sort(list_0)

def test_case_2():
    bool_0 = True
    list_0 = [bool_0]
    var_0 = module_0.max_heap_sort(list_0)
    var_1 = module_0.max_heap_sort(list_0)

def test_case_3():
    list_0 = []
    var_0 = module_0.max_heap_sort(list_0)

def test_case_4():
    list_0 = []
    var_0 = module_0.custom_heap_sort(list_0)

def test_case_5():
    float_0 = 1790.173978

def test_case_6():
    bool_0 = False
    bytes_0 = b'=\x17\xa0J8\xe2\x8c4f,\xcc'
    list_0 = []
    tuple_0 = (bool_0, bytes_0, list_0)
    list_1 = [tuple_0]
    var_0 = module_0.custom_heap_sort(list_1)
    bytes_1 = b'\x8e\xcb\xaf}\xdcT'
    tuple_1 = (bytes_1, bytes_1, bytes_1)
    list_2 = [tuple_1, bytes_1, tuple_1]

def test_case_7():
    none_type_0 = None

def test_case_8():
    bool_0 = True
