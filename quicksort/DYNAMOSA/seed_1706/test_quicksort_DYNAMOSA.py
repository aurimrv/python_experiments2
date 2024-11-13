#Pyguin test cases converted from quicksort/DYNAMOSA/seed_1706/test_quicksort.py
import pytest
import quicksort as module_0

def test_case_0():
    tuple_0 = ()
    list_0 = [tuple_0, tuple_0, tuple_0]
    var_0 = module_0.quicksort(list_0)
    var_1 = module_0.quicksort(tuple_0)

def test_case_1():
    int_0 = 2085
    list_0 = [int_0]
    var_0 = module_0.quicksort(list_0)
    var_1 = module_0.quicksort(list_0)
    float_0 = -566.53
    list_1 = [int_0, float_0, float_0]
    var_2 = module_0.quicksort(list_1)
    float_1 = -3212.2364
    var_3 = module_0.quicksort(list_0)
