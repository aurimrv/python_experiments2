#Pyguin test cases converted from heapsort/WHOLE_SUITE/seed_1706/test_heapsort.py
import pytest
import heapsort as module_0

def test_case_0():
    bool_0 = False

def test_case_1():
    str_0 = '\tJK@q`aSTySi]'
    list_0 = [str_0, str_0, str_0, str_0]
    var_0 = module_0.heap_sort(list_0)
    var_1 = module_0.custom_heap_sort(var_0)
    var_2 = module_0.max_heap_sort(var_0)

def test_case_2():
    str_0 = 'Ok]Dj}5VG;(Xfv'

def test_case_3():
    bytes_0 = b'{\xef\xbf;\x8c'

def test_case_4():
    none_type_0 = None

def test_case_5():
    bool_0 = True
    list_0 = [bool_0, bool_0]
    var_0 = module_0.custom_heap_sort(list_0)
    var_1 = module_0.custom_heap_sort(var_0)
    var_2 = module_0.max_heap_sort(var_0)
    list_1 = []
    var_3 = module_0.max_heap_sort(list_1)
    var_4 = module_0.heap_sort(var_3)

def test_case_6():
    int_0 = 2105
    list_0 = [int_0]
    var_0 = module_0.heap_sort(list_0)

def test_case_7():
    str_0 = 'mnZKQky\rzp-_;w~'
    str_1 = 'max'
    list_0 = [str_0, str_0, str_1]
    var_0 = module_0.custom_heap_sort(list_0)
    var_1 = module_0.max_heap_sort(list_0)
    var_2 = module_0.max_heap_sort(list_0)
    var_3 = module_0.custom_heap_sort(list_0, str_1)
