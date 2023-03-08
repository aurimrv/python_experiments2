import pytest
from edit_distance import calculate_edit_distance

def test_edit_distance():
    assert calculate_edit_distance('hello', 'teio') == ['Substitute h', 'Insert l', 'Substitute l']

def test_deletion_required():
    assert calculate_edit_distance('two', 'one two') == ['Delete o', 'Delete n', 'Delete e', 'Delete  ']

