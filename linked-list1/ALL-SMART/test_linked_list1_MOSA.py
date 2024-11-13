#Pyguin test cases converted from linked-list1/MOSA/seed_1706/test_linked_list1.py
import pytest
import linked_list1 as module_0
import builtins as module_1

def test_case_0():
    none_type_0 = None
    list_node_0 = module_0.ListNode(none_type_0)
    list_node_1 = module_0.ListNode(none_type_0, list_node_0)
    var_0 = list_node_1.contains_cycle()
    assert var_0 is False

def test_case_1():
    none_type_0 = None
    list_node_0 = module_0.ListNode(none_type_0)
    var_0 = list_node_0.contains_cycle()
    assert var_0 is False

def test_case_2():
    none_type_0 = None
    list_node_0 = module_0.ListNode(none_type_0)
    var_0 = list_node_0.get_beginning_of_cycle_if_exists()
    list_node_1 = module_0.ListNode(var_0, list_node_0)
    var_1 = list_node_1.get_beginning_of_cycle_if_exists()

def test_case_3():
    none_type_0 = None
    list_node_0 = module_0.ListNode(none_type_0, none_type_0)
    var_0 = list_node_0.reverse()
    assert f'{type(var_0).__module__}.{type(var_0).__qualname__}' == 'linked_list1.ListNode'
    assert var_0.val is None
    assert var_0.next is None
    var_1 = var_0.reverse_recursive()
    assert f'{type(var_1).__module__}.{type(var_1).__qualname__}' == 'linked_list1.ListNode'
    assert var_1.val is None
    assert var_1.next is None
    list_node_1 = module_0.ListNode(var_1)
    list_node_2 = module_0.ListNode(var_1, list_node_1)
    var_2 = list_node_2.contains_cycle()
    assert var_2 is False
    var_3 = list_node_2.get_beginning_of_cycle_if_exists()
    var_4 = list_node_2.reverse()
    assert f'{type(list_node_1.next).__module__}.{type(list_node_1.next).__qualname__}' == 'linked_list1.ListNode'
    assert f'{type(var_4.next).__module__}.{type(var_4.next).__qualname__}' == 'linked_list1.ListNode'
    var_5 = var_4.reverse_recursive()
    assert f'{type(list_node_2.next).__module__}.{type(list_node_2.next).__qualname__}' == 'linked_list1.ListNode'
    assert f'{type(var_5.next).__module__}.{type(var_5.next).__qualname__}' == 'linked_list1.ListNode'
    var_6 = var_1.get_beginning_of_cycle_if_exists()

def test_case_4():
    none_type_0 = None
    list_node_0 = module_0.ListNode(none_type_0)
    list_node_1 = module_0.ListNode(none_type_0, list_node_0)
    var_0 = list_node_1.contains_cycle()
    assert var_0 is False
    var_1 = list_node_0.reverse()
    assert f'{type(var_1).__module__}.{type(var_1).__qualname__}' == 'linked_list1.ListNode'
    assert var_1.val is None
    assert var_1.next is None

def test_case_5():
    none_type_0 = None
    list_node_0 = module_0.ListNode(none_type_0)
    var_0 = list_node_0.get_beginning_of_cycle_if_exists()
    list_node_1 = module_0.ListNode(var_0, list_node_0)
    var_1 = list_node_1.contains_cycle()
    assert var_1 is False
    var_2 = list_node_1.reverse_recursive()
    assert f'{type(list_node_0.next).__module__}.{type(list_node_0.next).__qualname__}' == 'linked_list1.ListNode'
    assert list_node_1.next is None

def test_case_6():
    none_type_0 = None
    list_node_0 = module_0.ListNode(none_type_0)
    list_node_1 = module_0.ListNode(none_type_0, list_node_0)
    var_0 = list_node_0.reverse_recursive()
    assert f'{type(var_0).__module__}.{type(var_0).__qualname__}' == 'linked_list1.ListNode'
    assert var_0.val is None
    assert var_0.next is None
    var_1 = list_node_1.contains_cycle()
    assert var_1 is False

def test_case_7():
    bytes_0 = b'\xcb\x13'
    none_type_0 = None
    list_node_0 = module_0.ListNode(bytes_0, none_type_0)

def test_case_8():
    none_type_0 = None
    list_node_0 = module_0.ListNode(none_type_0)
    list_node_1 = module_0.ListNode(none_type_0, list_node_0)
    var_0 = list_node_1.get_beginning_of_cycle_if_exists()

def test_case_9():
    complex_0 = 2787.69 - 2181.5008j
    list_node_0 = module_0.ListNode(complex_0)
    list_node_1 = module_0.ListNode(list_node_0, list_node_0)
    var_0 = list_node_0.reverse()
    assert f'{type(var_0).__module__}.{type(var_0).__qualname__}' == 'linked_list1.ListNode'
    assert var_0.val == 2787.69 - 2181.5008j
    assert var_0.next is None
    var_1 = list_node_1.reverse_recursive()
    assert f'{type(list_node_0.next).__module__}.{type(list_node_0.next).__qualname__}' == 'linked_list1.ListNode'
    assert list_node_1.next is None
    assert f'{type(var_0.next).__module__}.{type(var_0.next).__qualname__}' == 'linked_list1.ListNode'
    assert var_1.val == 2787.69 - 2181.5008j
    list_node_2 = module_0.ListNode(list_node_0, var_0)
    list_node_3 = module_0.ListNode(complex_0)
    var_2 = list_node_2.contains_cycle()
    assert var_2 is True
    var_3 = var_1.get_beginning_of_cycle_if_exists()

def test_case_10():
    none_type_0 = None
    list_node_0 = module_0.ListNode(none_type_0, none_type_0)
    list_node_1 = module_0.ListNode(list_node_0, list_node_0)
    list_node_2 = module_0.ListNode(list_node_0, list_node_1)

def test_case_11():
    bool_0 = False
    list_node_0 = module_0.ListNode(bool_0, bool_0)
    var_0 = list_node_0.contains_cycle()
    assert var_0 is False
    list_node_1 = module_0.ListNode(list_node_0, list_node_0)

def test_case_12():
    none_type_0 = None
    list_node_0 = module_0.ListNode(none_type_0, none_type_0)
    list_node_1 = module_0.ListNode(list_node_0, list_node_0)
    var_0 = list_node_0.reverse()
    assert f'{type(var_0).__module__}.{type(var_0).__qualname__}' == 'linked_list1.ListNode'
    assert var_0.val is None
    assert var_0.next is None
    var_1 = var_0.reverse()
    list_node_2 = module_0.ListNode(list_node_1, list_node_1)
    var_2 = module_1.object()
    list_node_3 = module_0.ListNode(var_2, list_node_1)
    var_3 = list_node_2.reverse()
    assert f'{type(list_node_0.next).__module__}.{type(list_node_0.next).__qualname__}' == 'linked_list1.ListNode'
    assert f'{type(var_0.next).__module__}.{type(var_0.next).__qualname__}' == 'linked_list1.ListNode'
    assert f'{type(var_1.next).__module__}.{type(var_1.next).__qualname__}' == 'linked_list1.ListNode'
    assert var_3.val is None
    assert f'{type(var_3.next).__module__}.{type(var_3.next).__qualname__}' == 'linked_list1.ListNode'
    var_4 = var_3.contains_cycle()
    assert var_4 is True

def test_case_13():
    none_type_0 = None
    list_node_0 = module_0.ListNode(none_type_0, none_type_0)
    list_node_1 = module_0.ListNode(list_node_0, list_node_0)
    var_0 = list_node_0.reverse_recursive()
    assert f'{type(var_0).__module__}.{type(var_0).__qualname__}' == 'linked_list1.ListNode'
    assert var_0.val is None
    assert var_0.next is None
    var_1 = var_0.reverse()
    assert f'{type(var_1).__module__}.{type(var_1).__qualname__}' == 'linked_list1.ListNode'
    assert var_1.val is None
    assert var_1.next is None
    var_2 = var_1.reverse()
    var_3 = var_1.get_beginning_of_cycle_if_exists()
    list_node_2 = module_0.ListNode(var_3, list_node_1)
    var_4 = list_node_2.contains_cycle()
    assert var_4 is True
    list_node_3 = module_0.ListNode(var_0, list_node_1)
    var_5 = list_node_3.contains_cycle()
    assert var_5 is True
    var_6 = module_0.ListNode(list_node_3, list_node_3)
    var_7 = var_6.contains_cycle()
    assert var_7 is False

def test_case_14():
    none_type_0 = None
    list_node_0 = module_0.ListNode(none_type_0, none_type_0)
    list_node_1 = module_0.ListNode(list_node_0, list_node_0)
    var_0 = list_node_0.reverse_recursive()
    assert f'{type(var_0).__module__}.{type(var_0).__qualname__}' == 'linked_list1.ListNode'
    assert var_0.val is None
    assert var_0.next is None
    var_1 = var_0.reverse()
    assert f'{type(var_1).__module__}.{type(var_1).__qualname__}' == 'linked_list1.ListNode'
    assert var_1.val is None
    assert var_1.next is None
    var_2 = var_1.reverse()
    var_3 = var_1.get_beginning_of_cycle_if_exists()
    list_node_2 = module_0.ListNode(var_3, list_node_1)
    var_4 = list_node_2.contains_cycle()
    assert var_4 is True
    list_node_3 = module_0.ListNode(var_0, list_node_1)
    var_5 = var_1.contains_cycle()
    assert var_5 is False
    list_node_4 = module_0.ListNode(var_5)
    var_6 = list_node_0.contains_cycle()
    var_7 = list_node_4.contains_cycle()
    var_8 = list_node_3.contains_cycle()
    assert var_8 is True
    var_9 = var_2.get_beginning_of_cycle_if_exists()
    var_10 = list_node_3.contains_cycle()
    assert var_10 is True
    var_11 = list_node_2.contains_cycle()
    assert var_11 is True
    list_node_5 = module_0.ListNode(var_4, var_2)
    assert list_node_5.val is True
    var_12 = list_node_5.reverse()
    assert f'{type(list_node_0.next).__module__}.{type(list_node_0.next).__qualname__}' == 'linked_list1.ListNode'
    assert f'{type(var_0.next).__module__}.{type(var_0.next).__qualname__}' == 'linked_list1.ListNode'
    assert f'{type(var_1.next).__module__}.{type(var_1.next).__qualname__}' == 'linked_list1.ListNode'
    assert f'{type(var_2.next).__module__}.{type(var_2.next).__qualname__}' == 'linked_list1.ListNode'
    assert var_12.val is None
    assert f'{type(var_12.next).__module__}.{type(var_12.next).__qualname__}' == 'linked_list1.ListNode'
    var_13 = list_node_2.get_beginning_of_cycle_if_exists()
