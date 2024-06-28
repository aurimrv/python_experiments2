import os
import sys
module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)
from linked_list1 import ListNode

import pytest

@pytest.fixture
def create_linked_list():
    # Fixture to create a linked list for testing purposes
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    return node1

def test_contains_cycle_false():
    # Test contains_cycle() for a linked list without a cycle
    node = ListNode(1)
    assert not node.contains_cycle()

def test_contains_cycle_true():
    # Test contains_cycle() for a linked list with a cycle
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node2
    assert node1.contains_cycle()

def test_get_beginning_of_cycle_if_exists_none():
    # Test get_beginning_of_cycle_if_exists() for a linked list without a cycle
    node = ListNode(1)
    assert node.get_beginning_of_cycle_if_exists() == None

def test_get_beginning_of_cycle_if_exists_exists():
    # Test get_beginning_of_cycle_if_exists() for a linked list with a cycle
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node2
    assert node1.get_beginning_of_cycle_if_exists().val == 2

def test_reverse():
    # Test the reverse() method for a linked list
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node1.next = node2
    node2.next = node3
    new_head = node1.reverse()
    assert new_head.val == 3
    assert new_head.next.val == 2
    assert new_head.next.next.val == 1

def test_reverse_recursive():
    # Test the reverse_recursive() method for a linked list
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node1.next = node2
    node2.next = node3
    new_head = node1.reverse_recursive()
    assert new_head.val == 3
    assert new_head.next.val == 2
    assert new_head.next.next.val == 1