import pytest
from linked_list1 import ListNode


def test_ll_contains_cycle():
    head = ListNode(3)
    head.next = ListNode(4)
    head.next.next = ListNode(5)
    cycle_start = ListNode(6)
    head.next.next.next = cycle_start
    cycle_start.next = ListNode(7)
    cycle_start.next.next = ListNode(8)
    cycle_start.next.next.next = cycle_start

    assert head.contains_cycle() is True


def test_ll_no_cycle():
    head = ListNode(3)
    head.next = ListNode(4)
    head.next.next = ListNode(5)
    cycle_start = ListNode(6)
    head.next.next.next = cycle_start
    cycle_start.next = ListNode(7)
    cycle_start.next.next = ListNode(8)

    assert head.contains_cycle() is False


def test_ll_cycle_on_single_node():
    assert ListNode(1).contains_cycle() is False


def test_ll_get_cycle_start():
    head = ListNode(3)
    head.next = ListNode(4)
    head.next.next = ListNode(5)
    cycle_start = ListNode(6)
    head.next.next.next = cycle_start
    cycle_start.next = ListNode(7)
    cycle_start.next.next = ListNode(8)
    cycle_start.next.next.next = cycle_start

    assert head.get_beginning_of_cycle_if_exists() == cycle_start


def test_ll_get_cycle_start_no_cycle():
    head = ListNode(3)
    head.next = ListNode(4)
    head.next.next = ListNode(5)
    cycle_start = ListNode(6)
    head.next.next.next = cycle_start
    cycle_start.next = ListNode(7)
    cycle_start.next.next = ListNode(8)

    assert head.get_beginning_of_cycle_if_exists() is None


def test_ll_get_cycle_start_on_single_node():
    assert ListNode(1).get_beginning_of_cycle_if_exists() is None


def test_reverse():
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    assert head.val == 1
    assert head.next.val == 2
    assert head.next.next.val == 3
    head = head.reverse()
    assert head.val == 3
    assert head.next.val == 2
    assert head.next.next.val == 1


def test_reverse_recursive():
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    assert head.val == 1
    assert head.next.val == 2
    assert head.next.next.val == 3
    head = head.reverse_recursive()
    assert head.val == 3
    assert head.next.val == 2
    assert head.next.next.val == 1

