#Pyguin test cases converted from heap/MIO/seed_1706/test_heap.py
import pytest
import heap as module_0

def test_case_0():
    heap_0 = module_0.Heap()
    assert heap_0.heap_list == [0]
    int_0 = -2384
    int_1 = 7679
    var_0 = heap_0.insert(int_1)
    assert heap_0.heap_list == [0, 7679]
    var_1 = heap_0.insert(int_0)
    assert heap_0.heap_list == [0, -2384, 7679]
    var_2 = heap_0.delete_min()
    assert var_2 == -2384
    assert heap_0.heap_list == [0, 7679]

def test_case_1():
    heap_0 = module_0.Heap()
    assert heap_0.heap_list == [0]
    int_0 = 1572
    list_0 = [int_0]
    var_0 = heap_0.build(list_0)
    assert heap_0.heap_list == [0, 1572]
    var_1 = heap_0.insert(int_0)
    assert heap_0.heap_list == [0, 1572, 1572]

def test_case_2():
    heap_0 = module_0.Heap()
    assert heap_0.heap_list == [0]
    float_0 = -887.7357516000512
    list_0 = [float_0, float_0, float_0]
    bool_0 = False
    heap_1 = module_0.Heap()
    assert heap_1.heap_list == [0]
    var_0 = heap_1.build(list_0)
    assert len(heap_1.heap_list) == 4
    var_1 = heap_1.insert(bool_0)

def test_case_3():
    float_0 = 559.41324
    heap_0 = module_0.Heap()
    assert heap_0.heap_list == [0]

def test_case_4():
    heap_0 = module_0.Heap()
    assert heap_0.heap_list == [0]
    var_0 = heap_0.insert(heap_0)

def test_case_5():
    float_0 = -881.3117066116605
    list_0 = [float_0]
    bool_0 = False
    heap_0 = module_0.Heap()
    assert heap_0.heap_list == [0]
    var_0 = heap_0.build(list_0)
    assert len(heap_0.heap_list) == 2
    var_1 = heap_0.sift(bool_0)

def test_case_6():
    float_0 = -869.603350366817
    list_0 = [float_0, float_0, float_0, float_0, float_0, float_0, float_0]
    heap_0 = module_0.Heap()
    assert heap_0.heap_list == [0]
    var_0 = heap_0.build(list_0)
    assert len(heap_0.heap_list) == 8

def test_case_7():
    bool_0 = True
    heap_0 = module_0.Heap()
    assert heap_0.heap_list == [0]
    var_0 = heap_0.sift(bool_0)

def test_case_8():
    float_0 = 3460.0
    list_0 = [float_0, float_0, float_0, float_0]
    heap_0 = module_0.Heap()
    assert heap_0.heap_list == [0]
    var_0 = heap_0.build(list_0)
    assert len(heap_0.heap_list) == 5

def test_case_9():
    bool_0 = False
    heap_0 = module_0.Heap()
    assert heap_0.heap_list == [0]
    int_0 = -2566
    list_0 = [int_0, int_0, bool_0]
    var_0 = heap_0.build(list_0)
    assert heap_0.heap_list == [0, -2566, -2566, False]
    var_1 = heap_0.min()
    assert var_1 == -2566
    var_2 = heap_0.insert(var_1)
    assert heap_0.heap_list == [0, -2566, -2566, False, -2566]

def test_case_10():
    int_0 = 6
    heap_0 = module_0.Heap()
    assert heap_0.heap_list == [0]
    var_0 = heap_0.find_min_child_index(int_0)

def test_case_11():
    heap_0 = module_0.Heap()
    assert heap_0.heap_list == [0]
    var_0 = heap_0.insert(heap_0)
    var_1 = heap_0.min()
    assert f'{type(var_1).__module__}.{type(var_1).__qualname__}' == 'heap.Heap'
    assert f'{type(var_1.heap_list).__module__}.{type(var_1.heap_list).__qualname__}' == 'builtins.list'
    assert len(var_1.heap_list) == 2

def test_case_12():
    heap_0 = module_0.Heap()
    assert heap_0.heap_list == [0]
    var_0 = heap_0.min()

def test_case_13():
    heap_0 = module_0.Heap()
    assert heap_0.heap_list == [0]
    int_0 = -2384
    var_0 = heap_0.insert(int_0)
    assert heap_0.heap_list == [0, -2384]
    var_1 = heap_0.delete_min()
    assert var_1 == -2384
    assert heap_0.heap_list == [0]

def test_case_14():
    float_0 = 3460.0
    list_0 = [float_0, float_0]
    heap_0 = module_0.Heap()
    assert heap_0.heap_list == [0]
    var_0 = heap_0.build(list_0)
    assert len(heap_0.heap_list) == 3
    var_1 = heap_0.delete_min()
    assert var_1 == pytest.approx(3460.0, abs=0.01, rel=0.01)
    assert len(heap_0.heap_list) == 2

def test_case_15():
    heap_0 = module_0.Heap()
    assert heap_0.heap_list == [0]
    var_0 = heap_0.delete_min()

def test_case_16():
    heap_0 = module_0.Heap()
    assert heap_0.heap_list == [0]
    list_0 = []
    var_0 = heap_0.build(list_0)

def test_case_17():
    heap_0 = module_0.Heap()
    assert heap_0.heap_list == [0]

def test_case_18():
    heap_0 = module_0.Heap()
    assert heap_0.heap_list == [0]
    var_0 = heap_0.size()
    assert var_0 == 0
