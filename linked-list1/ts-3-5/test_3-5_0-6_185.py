import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from linked_list1 import ListNode

def test_contains_cycle():
    # Test case 1: No cycle in the linked list
    node1 = ListNode(1)
    assert node1.contains_cycle() == False

    # Test case 2: Cycle exists in the linked list
    node1.next = ListNode(2)
    node1.next.next = node1
    assert node1.contains_cycle() == True

def test_get_beginning_of_cycle_if_exists():
    # Test case 1: No cycle in the linked list
    node1 = ListNode(1)
    assert node1.get_beginning_of_cycle_if_exists() == None

    # Test case 2: Cycle exists in the linked list
    node1.next = ListNode(2)
    node1.next.next = node1
    assert node1.get_beginning_of_cycle_if_exists() == node1

def test_reverse():
    # Test case 1: Reverse a linked list with multiple nodes
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node1.next = node2
    node2.next = node3
    reversed_node = node1.reverse()
    assert reversed_node.val == 3
    assert reversed_node.next.val == 2
    assert reversed_node.next.next.val == 1

def test_reverse_recursive():
    # Test case 1: Reverse a linked list with multiple nodes using recursion
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node1.next = node2
    node2.next = node3
    reversed_node = node1.reverse_recursive()
    assert reversed_node.val == 3
    assert reversed_node.next.val == 2
    assert reversed_node.next.next.val == 1