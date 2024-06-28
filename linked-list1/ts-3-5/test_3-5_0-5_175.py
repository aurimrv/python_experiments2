import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from linked_list1 import ListNode

def test_contains_cycle():
    # Test case 1: No cycle in the linked list
    head = ListNode(1)
    assert head.contains_cycle() == False

    # Test case 2: Cycle exists in the linked list
    head.next = ListNode(2)
    head.next.next = head
    assert head.contains_cycle() == True

def test_get_beginning_of_cycle_if_exists():
    # Test case 1: No cycle in the linked list
    head = ListNode(1)
    assert head.get_beginning_of_cycle_if_exists() == None

    # Test case 2: Cycle exists in the linked list
    head.next = ListNode(2)
    head.next.next = head
    assert head.get_beginning_of_cycle_if_exists() == head

def test_reverse():
    # Test case 1: Reverse a linked list with multiple nodes
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    reversed_head = head.reverse()
    assert reversed_head.val == 3
    assert reversed_head.next.val == 2
    assert reversed_head.next.next.val == 1

def test_reverse_recursive():
    # Test case 1: Reverse a linked list with multiple nodes using recursion
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    reversed_head = head.reverse_recursive()
    assert reversed_head.val == 3
    assert reversed_head.next.val == 2
    assert reversed_head.next.next.val == 1