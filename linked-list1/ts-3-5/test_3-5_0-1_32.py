import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from linked_list1 import ListNode

def test_contains_cycle():
    # Test case for a list with no cycle
    node1 = ListNode(1)
    assert node1.contains_cycle() == False

    # Test case for a list with a cycle
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node2
    assert node2.contains_cycle() == True

def test_get_beginning_of_cycle_if_exists():
    # Test case for a list with no cycle
    node1 = ListNode(1)
    assert node1.get_beginning_of_cycle_if_exists() == None

    # Test case for a list with a cycle
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node2
    assert node2.get_beginning_of_cycle_if_exists() == node2

def test_reverse():
    # Test case for reversing a list
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
    # Test case for reversing a list recursively
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node1.next = node2
    node2.next = node3
    reversed_node = node1.reverse_recursive()
    assert reversed_node.val == 3
    assert reversed_node.next.val == 2
    assert reversed_node.next.next.val == 1