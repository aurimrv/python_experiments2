import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from linked_list1 import ListNode

def test_contains_cycle():
    node1 = ListNode(1)
    assert not node1.contains_cycle()

    node2 = ListNode(1)
    node3 = ListNode(2)
    node4 = ListNode(3)
    node5 = ListNode(4)
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node2
    assert node2.contains_cycle()

def test_get_beginning_of_cycle_if_exists():
    node1 = ListNode(1)
    node2 = ListNode(2)
    node1.next = node2
    assert node1.get_beginning_of_cycle_if_exists() is None

    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)
    node6 = ListNode(6)
    node3.next = node4
    node4.next = node5
    node5.next = node6
    node6.next = node4
    assert node3.get_beginning_of_cycle_if_exists() == node4

def test_reverse():
    node1 = ListNode(1)
    node_res = node1.reverse()
    assert node_res.val == 1 and not node_res.next

    node2 = ListNode(1)
    node3 = ListNode(2)
    node4 = ListNode(3)
    node2.next = node3
    node3.next = node4
    new_head = node2.reverse()
    assert new_head.val == 3 and new_head.next.val == 2 and new_head.next.next.val == 1

def test_reverse_recursive():
    node1 = ListNode(1)
    node_res = node1.reverse_recursive()
    assert node_res.val == 1 and not node_res.next

    node2 = ListNode(1)
    node3 = ListNode(2)
    node4 = ListNode(3)
    node2.next = node3
    node3.next = node4
    new_head = node2.reverse_recursive()
    assert new_head.val == 3 and new_head.next.val == 2 and new_head.next.next.val == 1