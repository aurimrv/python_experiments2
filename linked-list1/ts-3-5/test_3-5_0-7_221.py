import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from linked_list1 import ListNode

def test_contains_cycle():
    # Test case 1: Empty list should not contain a cycle
    head = ListNode(1)
    assert not head.contains_cycle()

    # Test case 2: List with a cycle should return True
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node1.next = node2
    node2.next = node3
    node3.next = node1
    assert node1.contains_cycle()

def test_get_beginning_of_cycle_if_exists():
    # Test case 1: Empty list should not have a cycle
    head = ListNode(1)
    assert head.get_beginning_of_cycle_if_exists() is None

    # Test case 2: List with a cycle, find the beginning node
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node1.next = node2
    node2.next = node3
    node3.next = node1
    assert node1.get_beginning_of_cycle_if_exists() == node1

def test_reverse():
    # Test case 1: Reverse a list with one node
    head = ListNode(1)
    assert head.reverse().val == 1

    # Test case 2: Reverse a list with multiple nodes
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node1.next = node2
    node2.next = node3
    reversed_head = node1.reverse()
    assert reversed_head.val == 3
    assert reversed_head.next.val == 2
    assert reversed_head.next.next.val == 1

def test_reverse_recursive():
    # Test case 1: Reverse a list with one node recursively
    head = ListNode(1)
    assert head.reverse_recursive().val == 1

    # Test case 2: Reverse a list with multiple nodes recursively
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node1.next = node2
    node2.next = node3
    reversed_head = node1.reverse_recursive()
    assert reversed_head.val == 3
    assert reversed_head.next.val == 2
    assert reversed_head.next.next.val == 1