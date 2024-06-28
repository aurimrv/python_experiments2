import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from linked_list1 import ListNode

class TestListNode:

    def test_contains_cycle_one_node_no_cycle(self):
        node = ListNode(1)
        assert node.contains_cycle() == False

    def test_contains_cycle_cycle_exists(self):
        head = ListNode(1)
        node1 = ListNode(2)
        node2 = ListNode(3)
        node3 = ListNode(4)
        head.next = node1
        node1.next = node2
        node2.next = node3
        node3.next = head
        assert head.contains_cycle() == True

    def test_get_beginning_of_cycle_if_exists_no_cycle(self):
        node = ListNode(1)
        assert node.get_beginning_of_cycle_if_exists() == None

    def test_get_beginning_of_cycle_if_exists_cycle_exists(self):
        head = ListNode(1)
        node1 = ListNode(2)
        node2 = ListNode(3)
        node3 = ListNode(4)
        head.next = node1
        node1.next = node2
        node2.next = node3
        node3.next = head
        assert head.get_beginning_of_cycle_if_exists() == head

    def test_reverse_single_node(self):
        node = ListNode(1)
        new_head = node.reverse()
        assert new_head.val == 1
        assert new_head.next == None

    def test_reverse_multiple_nodes(self):
        head = ListNode(1)
        node1 = ListNode(2)
        node2 = ListNode(3)
        head.next = node1
        node1.next = node2
        new_head = head.reverse()
        assert new_head.val == 3
        assert new_head.next.val == 2
        assert new_head.next.next.val == 1
        assert new_head.next.next.next == None

    def test_reverse_recursive_single_node(self):
        node = ListNode(1)
        new_head = node.reverse_recursive()
        assert new_head.val == 1
        assert new_head.next == None

    def test_reverse_recursive_multiple_nodes(self):
        head = ListNode(1)
        node1 = ListNode(2)
        node2 = ListNode(3)
        head.next = node1
        node1.next = node2
        new_head = head.reverse_recursive()
        assert new_head.val == 3
        assert new_head.next.val == 2
        assert new_head.next.next.val == 1
        assert new_head.next.next.next == None