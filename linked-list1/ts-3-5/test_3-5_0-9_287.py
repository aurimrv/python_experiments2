import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from linked_list1 import ListNode

# Test cases for ListNode class methods

def test_contains_cycle_empty_list():
    node = ListNode(1)
    assert node.contains_cycle() == False

def test_contains_cycle_no_cycle():
    node1 = ListNode(1)
    node2 = ListNode(2)
    node1.next = node2
    assert node1.contains_cycle() == False

def test_contains_cycle_with_cycle():
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node1.next = node2
    node2.next = node3
    node3.next = node1
    assert node1.contains_cycle() == True

def test_get_beginning_of_cycle_empty_list():
    node = ListNode(1)
    assert node.get_beginning_of_cycle_if_exists() == None

def test_get_beginning_of_cycle_no_cycle():
    node1 = ListNode(1)
    node2 = ListNode(2)
    node1.next = node2
    assert node1.get_beginning_of_cycle_if_exists() == None

def test_get_beginning_of_cycle_with_cycle():
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node1.next = node2
    node2.next = node3
    node3.next = node1
    result = node1.get_beginning_of_cycle_if_exists()
    assert result.val == 1

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
    assert reversed_node.next.next.next == None

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
    assert reversed_node.next.next.next == None