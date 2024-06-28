import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from linked_list1 import ListNode

def test_contains_cycle():
    # Test case where there is a cycle in the linked list
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node1.next = node2
    node2.next = node3
    node3.next = node1  # creating a cycle

    assert node1.contains_cycle() == True

    # Test case where there is no cycle in the linked list
    node4 = ListNode(4)
    node5 = ListNode(5)
    node4.next = node5

    assert node4.contains_cycle() == False

def test_get_beginning_of_cycle_if_exists():
    # Test case where there is a cycle in the linked list
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node1.next = node2
    node2.next = node3
    node3.next = node1  # creating a cycle

    assert node1.get_beginning_of_cycle_if_exists() == node1

    # Test case where there is no cycle in the linked list
    node4 = ListNode(4)
    node5 = ListNode(5)
    node4.next = node5

    assert node4.get_beginning_of_cycle_if_exists() == None

def test_reverse():
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
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node1.next = node2
    node2.next = node3

    reversed_node = node1.reverse_recursive()

    assert reversed_node.val == 3
    assert reversed_node.next.val == 2
    assert reversed_node.next.next.val == 1