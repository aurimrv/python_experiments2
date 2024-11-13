#Pyguin test cases converted from heap/DYNAMOSA/seed_1706/test_heap.py
import pytest
import heap as module_0
import builtins as module_1

def test_case_0():
    bool_0 = False
    int_0 = -4832
    heap_0 = module_0.Heap()
    assert heap_0.heap_list == [0]
    var_0 = heap_0.insert(int_0)
    assert heap_0.heap_list == [0, -4832]

def test_case_1():
    heap_0 = module_0.Heap()
    assert heap_0.heap_list == [0]
    heap_1 = module_0.Heap()
    assert heap_1.heap_list == [0]
    var_0 = heap_1.min()

def test_case_2():
    heap_0 = module_0.Heap()
    assert heap_0.heap_list == [0]
    heap_1 = module_0.Heap()
    assert heap_1.heap_list == [0]
    var_0 = heap_1.delete_min()

def test_case_3():
    list_0 = []
    heap_0 = module_0.Heap()
    assert heap_0.heap_list == [0]
    var_0 = heap_0.build(list_0)

def test_case_4():
    heap_0 = module_0.Heap()
    assert heap_0.heap_list == [0]

def test_case_5():
    heap_0 = module_0.Heap()
    assert heap_0.heap_list == [0]
    heap_1 = module_0.Heap()
    assert heap_1.heap_list == [0]
    var_0 = heap_0.size()
    assert var_0 == 0

def test_case_6():
    heap_0 = module_0.Heap()
    assert heap_0.heap_list == [0]
    list_0 = []
    list_1 = [heap_0, list_0]

def test_case_7():
    bool_0 = True
    heap_0 = module_0.Heap()
    assert heap_0.heap_list == [0]
    var_0 = heap_0.insert(bool_0)
    assert heap_0.heap_list == [0, True]
    var_1 = heap_0.min()
    assert var_1 is True
    var_2 = heap_0.insert(var_1)
    assert heap_0.heap_list == [0, True, True]

def test_case_8():
    heap_0 = module_0.Heap()
    assert heap_0.heap_list == [0]
    var_0 = heap_0.insert(heap_0)
    var_1 = heap_0.size()
    assert var_1 == 1
    heap_1 = module_0.Heap()
    assert heap_1.heap_list == [0]
    var_2 = heap_0.delete_min()
    assert heap_0.heap_list == [0]
    assert f'{type(var_2).__module__}.{type(var_2).__qualname__}' == 'heap.Heap'
    assert var_2.heap_list == [0]

def test_case_9():
    bool_0 = True
    int_0 = -3047
    heap_0 = module_0.Heap()
    assert heap_0.heap_list == [0]
    int_1 = 631
    var_0 = heap_0.insert(int_1)
    assert heap_0.heap_list == [0, 631]
    var_1 = heap_0.insert(int_1)
    assert heap_0.heap_list == [0, 631, 631]
    var_2 = heap_0.sift(bool_0)

def test_case_10():
    heap_0 = module_0.Heap()
    assert heap_0.heap_list == [0]
    int_0 = 631
    var_0 = heap_0.insert(int_0)
    assert heap_0.heap_list == [0, 631]
    var_1 = heap_0.insert(int_0)
    assert heap_0.heap_list == [0, 631, 631]

def test_case_11():
    heap_0 = module_0.Heap()
    assert heap_0.heap_list == [0]
    var_0 = heap_0.insert(heap_0)
    var_1 = heap_0.size()
    assert var_1 == 1
    var_2 = heap_0.delete_min()
    assert heap_0.heap_list == [0]
    assert f'{type(var_2).__module__}.{type(var_2).__qualname__}' == 'heap.Heap'
    assert var_2.heap_list == [0]
    bool_0 = True
    var_3 = var_2.sift(bool_0)
    var_4 = var_2.min()
    var_5 = heap_0.find_min_child_index(bool_0)

def test_case_12():
    bool_0 = True
    int_0 = 2
    heap_0 = module_0.Heap()
    assert heap_0.heap_list == [0]
    int_1 = 631
    var_0 = heap_0.insert(int_1)
    assert heap_0.heap_list == [0, 631]
    var_1 = heap_0.insert(int_1)
    assert heap_0.heap_list == [0, 631, 631]
    var_2 = heap_0.sift(bool_0)
    var_3 = heap_0.find_min_child_index(int_0)

def test_case_13():
    bool_0 = True
    heap_0 = module_0.Heap()
    assert heap_0.heap_list == [0]
    int_0 = 631
    var_0 = heap_0.insert(int_0)
    assert heap_0.heap_list == [0, 631]
    var_1 = heap_0.insert(int_0)
    assert heap_0.heap_list == [0, 631, 631]
    var_2 = heap_0.sift(bool_0)

def test_case_14():
    bool_0 = False
    heap_0 = module_0.Heap()
    assert heap_0.heap_list == [0]
    var_0 = heap_0.insert(bool_0)
    assert heap_0.heap_list == [0, False]
    int_0 = 631
    var_1 = heap_0.insert(int_0)
    assert heap_0.heap_list == [0, False, 631]
    var_2 = heap_0.insert(int_0)
    assert heap_0.heap_list == [0, False, 631, 631]
    var_3 = heap_0.sift(bool_0)

def test_case_15():
    bool_0 = True
    int_0 = 2
    heap_0 = module_0.Heap()
    assert heap_0.heap_list == [0]
    int_1 = 631
    var_0 = heap_0.insert(int_0)
    assert heap_0.heap_list == [0, 2]
    int_2 = -1271
    var_1 = heap_0.insert(int_2)
    assert heap_0.heap_list == [0, -1271, 2]
    var_2 = module_1.object()
    var_3 = heap_0.insert(int_1)
    assert heap_0.heap_list == [0, -1271, 2, 631]
    var_4 = heap_0.sift(bool_0)
    var_5 = heap_0.find_min_child_index(int_0)

def test_case_16():
    bool_0 = False
    list_0 = [bool_0, bool_0, bool_0, bool_0]
    bool_1 = True
    list_1 = [bool_1, bool_1, bool_1, bool_1]
    heap_0 = module_0.Heap()
    assert heap_0.heap_list == [0]
    var_0 = heap_0.build(list_1)
    assert heap_0.heap_list == [0, True, True, True, True]

def test_case_17():
    bool_0 = False
    list_0 = [bool_0, bool_0, bool_0]
    heap_0 = module_0.Heap()
    assert heap_0.heap_list == [0]
    var_0 = heap_0.build(list_0)
    assert heap_0.heap_list == [0, False, False, False]

def test_case_18():
    bool_0 = True
    int_0 = 2
    heap_0 = module_0.Heap()
    assert heap_0.heap_list == [0]
    int_1 = 631
    var_0 = heap_0.insert(int_0)
    assert heap_0.heap_list == [0, 2]
    int_2 = 511
    var_1 = heap_0.insert(int_2)
    assert heap_0.heap_list == [0, 2, 511]
    var_2 = heap_0.delete_min()
    assert var_2 == 2
    assert heap_0.heap_list == [0, 511]
    var_3 = heap_0.insert(int_1)
    assert heap_0.heap_list == [0, 511, 631]
    var_4 = heap_0.sift(bool_0)
    var_5 = heap_0.find_min_child_index(int_0)
