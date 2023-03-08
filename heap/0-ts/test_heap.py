import pytest
from heap import Heap

def build_basic_heap():
    heap = Heap()

    heap.insert(23)
    heap.insert(12)
    heap.insert(7)
    heap.insert(5)
    heap.insert(34)
    heap.insert(88)
    heap.insert(2)

    return heap

def test_basic_creation():
    heap = build_basic_heap()

    assert heap.heap_list == [0,2,7,5,23,34,88, 12]

def test_delete_min():
    heap = build_basic_heap()

    assert heap.delete_min() == 2

    assert heap.heap_list == [0,5,7,12,23,34,88]

    heap = Heap()

    assert heap.delete_min() == None

    heap.insert(4)

    assert heap.delete_min() == 4

def test_find_min():

    heap = build_basic_heap()

    assert heap.min() == 2

    assert Heap().min() == None

def test_build():

    built = Heap()

    built.build([23,12,7,5,34,88,2])

    assert built.heap_list == [0,2,5,7,12,34,88,23]

def test_find_min_outside_bounds():

    heap = build_basic_heap()

    assert heap.find_min_child_index(len(heap.heap_list)) == None

