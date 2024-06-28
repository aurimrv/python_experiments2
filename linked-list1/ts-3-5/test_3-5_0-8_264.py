import os
import sys

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from linked_list1 import ListNode

import pytest

@pytest.fixture
def sample_linked_list():
    # Setup a sample linked list for testing
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    return node1

def test_contains_cycle(sample_linked_list):
    # Test when there is no cycle
    assert sample_linked_list.contains_cycle() == False

    # Test when there is a cycle
    sample_linked_list.next.next.next.next = sample_linked_list.next
    assert sample_linked_list.contains_cycle() == True

def test_get_beginning_of_cycle_if_exists(sample_linked_list):
    # Test when there is no cycle
    assert sample_linked_list.get_beginning_of_cycle_if_exists() == None

    # Test when there is a cycle
    sample_linked_list.next.next.next.next = sample_linked_list.next
    assert sample_linked_list.get_beginning_of_cycle_if_exists().val == 2

def test_reverse(sample_linked_list):
    reversed_list = sample_linked_list.reverse()
    assert reversed_list.val == 4
    assert reversed_list.next.val == 3
    assert reversed_list.next.next.val == 2
    assert reversed_list.next.next.next.val == 1

def test_reverse_recursive(sample_linked_list):
    reversed_list = sample_linked_list.reverse_recursive()
    assert reversed_list.val == 4
    assert reversed_list.next.val == 3
    assert reversed_list.next.next.val == 2
    assert reversed_list.next.next.next.val == 1