import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from linked_list1 import ListNode

def test_contains_cycle():
    # Test case 1: Testing a cycle with 3 nodes
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node1.next = node2
    node2.next = node3
    node3.next = node1
    assert node1.contains_cycle() == True

    # Test case 2: Testing a list with no cycle
    node4 = ListNode(4)
    node5 = ListNode(5)
    node4.next = node5
    assert node4.contains_cycle() == False

def test_get_beginning_of_cycle_if_exists():
    # Test case 1: Testing a cycle with 4 nodes
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node2
    assert node1.get_beginning_of_cycle_if_exists().val == 2

    # Test case 2: Testing no cycle in the list
    node5 = ListNode(5)
    node6 = ListNode(6)
    node5.next = node6
    assert node5.get_beginning_of_cycle_if_exists() == None

def test_reverse():
    # Test case 1: Testing reversal of a list with 3 nodes
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node1.next = node2
    node2.next = node3
    reversed_list = node1.reverse()
    assert reversed_list.val == 3
    assert reversed_list.next.val == 2
    assert reversed_list.next.next.val == 1

    # Test case 2: Testing reversal of a list with 1 node
    node4 = ListNode(4)
    reversed_list = node4.reverse()
    assert reversed_list.val == 4

def test_reverse_recursive():
    # Test case 1: Testing recursive reversal of a list with 4 nodes
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    reversed_list = node1.reverse_recursive()
    assert reversed_list.val == 4
    assert reversed_list.next.val == 3
    assert reversed_list.next.next.val == 2
    assert reversed_list.next.next.next.val == 1

    # Test case 2: Testing recursive reversal of a list with 1 node
    node5 = ListNode(5)
    reversed_list = node5.reverse_recursive()
    assert reversed_list.val == 5