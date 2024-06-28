import os
import sys
module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from hash_map import HashMap, djb2, sdbm, lose_lose

import pytest

@pytest.fixture
def empty_map():
    return HashMap()

@pytest.fixture
def filled_map():
    h = HashMap()
    h.insert('a', 1)
    h.insert('b', 2)
    return h

def test_insert(empty_map):
    empty_map.insert('test_key', 'test_value')
    assert empty_map.get('test_key') == 'test_value'
    assert len(empty_map.buckets[empty_map.hash_function('test_key') % len(empty_map.buckets)]) == 1

def test_get(filled_map):
    assert filled_map.get('a') == 1
    assert filled_map.get('b') == 2

def test_delete(filled_map):
    assert filled_map.delete('b') == ('b', 2)
    with pytest.raises(KeyError):
        filled_map.get('b')

def test_djb2():
    assert djb2('test_key') != djb2('another_key')
    assert djb2('test_key') == djb2('test_key')

def test_sdbm():
    assert sdbm('test_key') != sdbm('another_key')
    assert sdbm('test_key') == sdbm('test_key')

def test_lose_lose():
    assert lose_lose('test_key') != lose_lose('another_key')
    assert lose_lose('test_key') == lose_lose('test_key')