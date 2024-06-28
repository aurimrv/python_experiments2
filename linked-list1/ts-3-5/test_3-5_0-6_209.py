import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from linked_list1 import ListNode

def test_contains_cycle():
    # Test case 1: No cycle in the list
    node1 = ListNode(1)
    assert node1.contains_cycle() == False

    # Test case 2: Cycle exists in the list
    node2 = ListNode(1)
    node2.next = ListNode(2)
    node2.next.next = node2
    assert node2.contains_cycle() == True

def test_get_beginning_of_cycle_if_exists():
    # Test case 1: No cycle in the list
    node1 = ListNode(1)
    assert node1.get_beginning_of_cycle_if_exists() == None

    # Test case 2: Cycle exists in the list
    node2 = ListNode(1)
    node2.next = ListNode(2)
    node2.next.next = node2
    assert node2.get_beginning_of_cycle_if_exists() == node2

def test_reverse():
    # Test case 1: Reversing a single node list
    node1 = ListNode(1)
    reversed_node1 = node1.reverse()
    assert reversed_node1.val == 1
    assert reversed_node1.next == None

    # Test case 2: Reversing a list with multiple nodes
    node2 = ListNode(1)
    node2.next = ListNode(2)
    node2.next.next = ListNode(3)
    reversed_node2 = node2.reverse()
    assert reversed_node2.val == 3
    assert reversed_node2.next.val == 2
    assert reversed_node2.next.next.val == 1

def test_reverse_recursive():
    # Test case 1: Reversing a single node list recursively
    node1 = ListNode(1)
    reversed_node1 = node1.reverse_recursive()
    assert reversed_node1.val == 1
    assert reversed_node1.next == None

    # Test case 2: Reversing a list with multiple nodes recursively
    node2 = ListNode(1)
    node2.next = ListNode(2)
    node2.next.next = ListNode(3)
    reversed_node2 = node2.reverse_recursive()
    assert reversed_node2.val == 3
    assert reversed_node2.next.val == 2
    assert reversed_node2.next.next.val == 1