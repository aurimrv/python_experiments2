#Pyguin test cases converted from linked-list1/MIO/seed_1706/test_linked_list1.py
import pytest
import linked_list1 as module_0

def test_case_0():
    bool_0 = True
    list_node_0 = module_0.ListNode(bool_0)
    list_node_1 = module_0.ListNode(bool_0, list_node_0)
    var_0 = list_node_1.contains_cycle()
    assert var_0 is False

def test_case_1():
    float_0 = 301.1743079325407
    list_node_0 = module_0.ListNode(float_0)
    list_node_1 = module_0.ListNode(float_0, list_node_0)
    list_node_2 = module_0.ListNode(float_0, list_node_1)
    var_0 = list_node_2.contains_cycle()
    assert var_0 is True

def test_case_2():
    bool_0 = True
    list_node_0 = module_0.ListNode(bool_0)
    list_node_1 = module_0.ListNode(bool_0, list_node_0)
    list_node_2 = module_0.ListNode(bool_0, list_node_1)
    var_0 = list_node_2.reverse()
    assert f'{type(list_node_0.next).__module__}.{type(list_node_0.next).__qualname__}' == 'linked_list1.ListNode'
    assert f'{type(var_0.next).__module__}.{type(var_0.next).__qualname__}' == 'linked_list1.ListNode'
    var_1 = list_node_1.get_beginning_of_cycle_if_exists()
    var_2 = list_node_0.contains_cycle()
    assert var_2 is True
    var_3 = list_node_2.get_beginning_of_cycle_if_exists()
    var_4 = list_node_0.reverse_recursive()
    assert list_node_0.next is None
    assert f'{type(list_node_2.next).__module__}.{type(list_node_2.next).__qualname__}' == 'linked_list1.ListNode'
    assert var_0.next is None
    assert f'{type(var_4.next).__module__}.{type(var_4.next).__qualname__}' == 'linked_list1.ListNode'

def test_case_3():
    bool_0 = True
    list_node_0 = module_0.ListNode(bool_0)
    var_0 = list_node_0.contains_cycle()
    assert var_0 is False

def test_case_4():
    bool_0 = False
    list_node_0 = module_0.ListNode(bool_0)
    list_node_1 = module_0.ListNode(bool_0, list_node_0)
    var_0 = list_node_1.get_beginning_of_cycle_if_exists()

def test_case_5():
    bool_0 = True
    list_node_0 = module_0.ListNode(bool_0)
    list_node_1 = module_0.ListNode(bool_0, list_node_0)
    list_node_2 = module_0.ListNode(bool_0, list_node_1)

def test_case_6():
    float_0 = -872.5004051658266
    list_node_0 = module_0.ListNode(float_0, float_0)
    list_node_1 = module_0.ListNode(float_0, list_node_0)

def test_case_7():
    bool_0 = True
    list_node_0 = module_0.ListNode(bool_0)
    var_0 = list_node_0.get_beginning_of_cycle_if_exists()

def test_case_8():
    float_0 = 301.1743079325407
    list_node_0 = module_0.ListNode(float_0)
    list_node_1 = module_0.ListNode(float_0, list_node_0)
    list_node_2 = module_0.ListNode(float_0, list_node_1)
    var_0 = list_node_2.reverse()
    assert f'{type(list_node_0.next).__module__}.{type(list_node_0.next).__qualname__}' == 'linked_list1.ListNode'
    assert f'{type(var_0.next).__module__}.{type(var_0.next).__qualname__}' == 'linked_list1.ListNode'

def test_case_9():
    bool_0 = True
    list_node_0 = module_0.ListNode(bool_0)
    list_node_1 = module_0.ListNode(bool_0, list_node_0)
    var_0 = list_node_1.reverse()
    assert f'{type(list_node_0.next).__module__}.{type(list_node_0.next).__qualname__}' == 'linked_list1.ListNode'
    assert f'{type(var_0.next).__module__}.{type(var_0.next).__qualname__}' == 'linked_list1.ListNode'

def test_case_10():
    int_0 = 2053
    list_node_0 = module_0.ListNode(int_0, int_0)

def test_case_11():
    bool_0 = False
    list_node_0 = module_0.ListNode(bool_0)
    var_0 = list_node_0.reverse()
    assert f'{type(var_0).__module__}.{type(var_0).__qualname__}' == 'linked_list1.ListNode'
    assert var_0.val is False
    assert var_0.next is None

def test_case_12():
    int_0 = 2053
    list_node_0 = module_0.ListNode(int_0, int_0)

def test_case_13():
    bool_0 = True
    list_node_0 = module_0.ListNode(bool_0)
    var_0 = list_node_0.reverse_recursive()
    assert f'{type(var_0).__module__}.{type(var_0).__qualname__}' == 'linked_list1.ListNode'
    assert var_0.val is True
    assert var_0.next is None

def test_case_14():
    bool_0 = True
    list_node_0 = module_0.ListNode(bool_0)
