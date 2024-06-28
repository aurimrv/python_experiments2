import os
import sys
module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from linked_list1 import ListNode

def test_contains_cycle():
    # Test case 1: Empty list should not contain a cycle
    head = ListNode(None)
    assert not head.contains_cycle()

    # Test case 2: List with one node should not contain a cycle
    head = ListNode(5)
    assert not head.contains_cycle()

    # Test case 3: List with cycle should return True
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = head
    assert head.contains_cycle()

def test_get_beginning_of_cycle_if_exists():
    # Test case 1: Empty list should not contain a cycle
    head = ListNode(None)
    assert not head.get_beginning_of_cycle_if_exists()

    # Test case 2: List with one node should not contain a cycle
    head = ListNode(5)
    assert not head.get_beginning_of_cycle_if_exists()

    # Test case 3: List with cycle should return the beginning of the cycle node
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = head
    assert head.get_beginning_of_cycle_if_exists() == head

def test_reverse():
    # Test case 1: Empty list should reverse to itself
    head = ListNode(None)
    assert head.reverse() == head

    # Test case 2: List with multiple nodes should reverse correctly
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    reversed_head = head.reverse()
    assert reversed_head.val == 3
    assert reversed_head.next.val == 2
    assert reversed_head.next.next.val == 1

def test_reverse_recursive():
    # Test case 1: Empty list should reverse to itself
    head = ListNode(None)
    assert head.reverse_recursive() == head

    # Test case 2: List with multiple nodes should reverse correctly
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    reversed_head = head.reverse_recursive()
    assert reversed_head.val == 3
    assert reversed_head.next.val == 2
    assert reversed_head.next.next.val == 1