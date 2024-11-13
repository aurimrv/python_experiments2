#Pyguin test cases converted from linked-list1/DYNAMOSA/seed_1706/test_linked_list1.py
import pytest
import linked_list1 as module_0

def test_case_0():
    set_0 = set()
    list_node_0 = module_0.ListNode(set_0)
    list_node_1 = module_0.ListNode(list_node_0, list_node_0)
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
    var_0 = list_node_0.reverse_recursive()
    assert f'{type(var_0).__module__}.{type(var_0).__qualname__}' == 'linked_list1.ListNode'
    assert var_0.val is None
    assert var_0.next is None
    var_1 = var_0.get_beginning_of_cycle_if_exists()

def test_case_3():
    bool_0 = True
    list_node_0 = module_0.ListNode(bool_0, bool_0)

def test_case_4():
    bool_0 = True
    list_node_0 = module_0.ListNode(bool_0)
    var_0 = list_node_0.reverse()
    assert f'{type(var_0).__module__}.{type(var_0).__qualname__}' == 'linked_list1.ListNode'
    assert var_0.val is True
    assert var_0.next is None
    var_1 = var_0.reverse()
    var_2 = var_1.reverse_recursive()
    assert f'{type(var_2).__module__}.{type(var_2).__qualname__}' == 'linked_list1.ListNode'
    assert var_2.val is True
    assert var_2.next is None
    var_3 = var_2.reverse()

def test_case_5():
    complex_0 = -104.01418079158825 + 635.33j
    list_node_0 = module_0.ListNode(complex_0)
    list_node_1 = module_0.ListNode(list_node_0, list_node_0)
    var_0 = list_node_1.reverse_recursive()
    assert f'{type(list_node_0.next).__module__}.{type(list_node_0.next).__qualname__}' == 'linked_list1.ListNode'
    assert list_node_1.next is None
    assert var_0.val == -104.01418079158825 + 635.33j
    list_node_2 = module_0.ListNode(var_0, list_node_0)

def test_case_6():
    bytes_0 = b'\xcb\x13'
    none_type_0 = None
    list_node_0 = module_0.ListNode(bytes_0, none_type_0)

def test_case_7():
    set_0 = set()
    list_node_0 = module_0.ListNode(set_0)
    list_node_1 = module_0.ListNode(list_node_0, list_node_0)
    var_0 = list_node_1.get_beginning_of_cycle_if_exists()

def test_case_8():
    complex_0 = -104.01418079158825 + 635.33j
    list_node_0 = module_0.ListNode(complex_0)
    list_node_1 = module_0.ListNode(list_node_0, list_node_0)
    list_node_2 = module_0.ListNode(list_node_1, list_node_0)
    var_0 = list_node_2.reverse()
    assert f'{type(list_node_0.next).__module__}.{type(list_node_0.next).__qualname__}' == 'linked_list1.ListNode'
    assert var_0.val == -104.01418079158825 + 635.33j
    assert f'{type(var_0.next).__module__}.{type(var_0.next).__qualname__}' == 'linked_list1.ListNode'
    var_1 = list_node_2.get_beginning_of_cycle_if_exists()

def test_case_9():
    complex_0 = -104.01418079158825 + 635.33j
    list_node_0 = module_0.ListNode(complex_0)
    list_node_1 = module_0.ListNode(list_node_0, list_node_0)
    var_0 = list_node_1.reverse_recursive()
    assert f'{type(list_node_0.next).__module__}.{type(list_node_0.next).__qualname__}' == 'linked_list1.ListNode'
    assert list_node_1.next is None
    assert var_0.val == -104.01418079158825 + 635.33j
    list_node_2 = module_0.ListNode(var_0, list_node_0)
    var_1 = list_node_0.contains_cycle()
    assert var_1 is False
    var_2 = list_node_0.reverse_recursive()
    assert var_0.next is None
    assert f'{type(var_2).__module__}.{type(var_2).__qualname__}' == 'linked_list1.ListNode'
    assert f'{type(var_2.val).__module__}.{type(var_2.val).__qualname__}' == 'linked_list1.ListNode'
    assert f'{type(var_2.next).__module__}.{type(var_2.next).__qualname__}' == 'linked_list1.ListNode'
    var_3 = list_node_2.reverse()
    assert f'{type(list_node_0.next).__module__}.{type(list_node_0.next).__qualname__}' == 'linked_list1.ListNode'
    assert f'{type(var_0.next).__module__}.{type(var_0.next).__qualname__}' == 'linked_list1.ListNode'
    assert var_3.val == -104.01418079158825 + 635.33j
    assert f'{type(var_3.next).__module__}.{type(var_3.next).__qualname__}' == 'linked_list1.ListNode'
    var_4 = list_node_2.get_beginning_of_cycle_if_exists()
    var_5 = list_node_1.contains_cycle()
    assert var_5 is True

def test_case_10():
    complex_0 = -104.01418079158825 + 635.33j
    list_node_0 = module_0.ListNode(complex_0)
    list_node_1 = module_0.ListNode(complex_0)
    list_node_2 = module_0.ListNode(list_node_0, list_node_0)
    var_0 = list_node_2.reverse_recursive()
    assert f'{type(list_node_0.next).__module__}.{type(list_node_0.next).__qualname__}' == 'linked_list1.ListNode'
    assert list_node_2.next is None
    assert var_0.val == -104.01418079158825 + 635.33j
    list_node_3 = module_0.ListNode(var_0, list_node_0)
    var_1 = list_node_3.reverse()
    assert f'{type(list_node_2.next).__module__}.{type(list_node_2.next).__qualname__}' == 'linked_list1.ListNode'
    assert f'{type(var_1.val).__module__}.{type(var_1.val).__qualname__}' == 'linked_list1.ListNode'
    assert f'{type(var_1.next).__module__}.{type(var_1.next).__qualname__}' == 'linked_list1.ListNode'
    var_2 = list_node_0.contains_cycle()
    assert var_2 is False
    var_3 = list_node_3.get_beginning_of_cycle_if_exists()
    var_4 = list_node_2.contains_cycle()
    assert var_4 is True

def test_case_11():
    complex_0 = -104 + 635.33j
    list_node_0 = module_0.ListNode(complex_0)
    var_0 = list_node_0.reverse_recursive()
    assert f'{type(var_0).__module__}.{type(var_0).__qualname__}' == 'linked_list1.ListNode'
    assert var_0.val == -104 + 635.33j
    assert var_0.next is None
    var_1 = var_0.reverse()
    assert f'{type(var_1).__module__}.{type(var_1).__qualname__}' == 'linked_list1.ListNode'
    assert var_1.val == -104 + 635.33j
    assert var_1.next is None
    list_node_1 = module_0.ListNode(complex_0, var_0)
    list_node_2 = module_0.ListNode(list_node_1, list_node_0)
    var_2 = list_node_2.contains_cycle()
    assert var_2 is False
    var_3 = list_node_0.contains_cycle()
    assert var_3 is False
    var_4 = list_node_1.get_beginning_of_cycle_if_exists()
    var_5 = list_node_0.reverse_recursive()
    var_6 = list_node_1.reverse()
    assert f'{type(list_node_0.next).__module__}.{type(list_node_0.next).__qualname__}' == 'linked_list1.ListNode'
    assert f'{type(var_0.next).__module__}.{type(var_0.next).__qualname__}' == 'linked_list1.ListNode'
    assert f'{type(var_1.next).__module__}.{type(var_1.next).__qualname__}' == 'linked_list1.ListNode'
    assert f'{type(var_5.next).__module__}.{type(var_5.next).__qualname__}' == 'linked_list1.ListNode'
    assert f'{type(var_6.next).__module__}.{type(var_6.next).__qualname__}' == 'linked_list1.ListNode'
    var_7 = list_node_2.reverse()
    assert f'{type(list_node_1.next).__module__}.{type(list_node_1.next).__qualname__}' == 'linked_list1.ListNode'
    assert var_7.val == -104 + 635.33j
    assert f'{type(var_7.next).__module__}.{type(var_7.next).__qualname__}' == 'linked_list1.ListNode'
    var_8 = list_node_2.get_beginning_of_cycle_if_exists()
    var_9 = var_0.contains_cycle()
    assert var_9 is False
    var_10 = list_node_2.contains_cycle()
    list_node_3 = module_0.ListNode(var_0, var_5)
    var_11 = list_node_0.get_beginning_of_cycle_if_exists()
    var_12 = var_5.contains_cycle()
    assert var_12 is False
    var_13 = var_7.contains_cycle()
    assert var_13 is True
    list_node_4 = module_0.ListNode(list_node_0, list_node_1)
    var_14 = list_node_4.get_beginning_of_cycle_if_exists()
    var_15 = list_node_4.reverse()
    assert f'{type(list_node_2.next).__module__}.{type(list_node_2.next).__qualname__}' == 'linked_list1.ListNode'
    assert f'{type(var_15.val).__module__}.{type(var_15.val).__qualname__}' == 'linked_list1.ListNode'
    assert f'{type(var_15.next).__module__}.{type(var_15.next).__qualname__}' == 'linked_list1.ListNode'

def test_case_12():
    complex_0 = -104 + 635.33j
    list_node_0 = module_0.ListNode(complex_0)
    list_node_1 = module_0.ListNode(list_node_0, list_node_0)
    var_0 = list_node_1.reverse_recursive()
    assert f'{type(list_node_0.next).__module__}.{type(list_node_0.next).__qualname__}' == 'linked_list1.ListNode'
    assert list_node_1.next is None
    assert var_0.val == -104 + 635.33j
    list_node_2 = module_0.ListNode(var_0, list_node_0)
    var_1 = list_node_0.contains_cycle()
    assert var_1 is False
    var_2 = var_0.get_beginning_of_cycle_if_exists()
    list_node_3 = module_0.ListNode(complex_0, list_node_2)
    var_3 = list_node_3.contains_cycle()
    assert var_3 is False
    list_node_4 = module_0.ListNode(list_node_1)
