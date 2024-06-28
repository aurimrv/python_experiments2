import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from hash_map import HashMap, djb2, sdbm, lose_lose

def test_hashmap_insert():
    hashmap = HashMap()
    hashmap.insert(1, 'a')
    assert hashmap.get(1) == 'a'

    hashmap.insert(1, 'b')
    assert hashmap.get(1) == 'b'

def test_hashmap_get():
    hashmap = HashMap()
    hashmap.insert(1, 'a')
    assert hashmap.get(1) == 'a'

    with pytest.raises(KeyError):
        hashmap.get(2)

def test_hashmap_delete():
    hashmap = HashMap()
    hashmap.insert(1, 'a')
    assert hashmap.delete(1) == (1, 'a')

    with pytest.raises(KeyError):
        hashmap.delete(2)

def test_djb2_hash_function():
    assert djb2('hello') == 210714636441

    # Test with empty string
    assert djb2('') == 5381

def test_sdbm_hash_function():
    assert sdbm('hello') == 1925877435333486942514

    # Test with empty string
    assert sdbm('') == 0

def test_lose_lose_hash_function():
    assert lose_lose('hello') == 532

    # Test with empty string
    assert lose_lose('') == 0