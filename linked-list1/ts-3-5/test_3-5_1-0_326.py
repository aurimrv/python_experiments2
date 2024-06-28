import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from linked_list1 import ListNode

@pytest.fixture
def example_list_with_cycle():
    # Create a linked list with a cycle for testing
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node2
    return node1

def test_contains_cycle_empty_list():
    # Test contains_cycle method on an empty list
    empty_list = ListNode(None)
    assert empty_list.contains_cycle() == False

def test_contains_cycle_no_cycle():
    # Test contains_cycle method on a list with no cycle
    node1 = ListNode(1)
    node2 = ListNode(2)
    node1.next = node2
    assert node1.contains_cycle() == False

def test_contains_cycle_with_cycle(example_list_with_cycle):
    # Test contains_cycle method on a list with a cycle
    assert example_list_with_cycle.contains_cycle() == True

def test_get_beginning_of_cycle_if_exists_no_cycle():
    # Test get_beginning_of_cycle_if_exists method on a list with no cycle
    node1 = ListNode(1)
    node2 = ListNode(2)
    node1.next = node2
    assert node1.get_beginning_of_cycle_if_exists() == None

def test_get_beginning_of_cycle_if_exists_with_cycle(example_list_with_cycle):
    # Test get_beginning_of_cycle_if_exists method on a list with a cycle
    beginning_of_cycle = example_list_with_cycle.get_beginning_of_cycle_if_exists()
    assert beginning_of_cycle.val == 2

def test_reverse():
    # Test reverse method on a list
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node1.next = node2
    node2.next = node3
    reversed_list = node1.reverse()
    assert reversed_list.val == 3
    assert reversed_list.next.val == 2
    assert reversed_list.next.next.val == 1

def test_reverse_recursive():
    # Test reverse_recursive method on a list
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node1.next = node2
    node2.next = node3
    reversed_list = node1.reverse_recursive()
    assert reversed_list.val == 3
    assert reversed_list.next.val == 2
    assert reversed_list.next.next.val == 1