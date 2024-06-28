import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from hash_map import HashMap, djb2, sdbm, lose_lose

@pytest.fixture
def hashmap():
    return HashMap()

@pytest.fixture
def hashmap_custom():
    return HashMap(buckets=10, hash_function=djb2)

def test_insert(hashmap):
    hashmap.insert('a', 1)
    assert hashmap.get('a') == 1

    hashmap.insert('a', 2)
    assert hashmap.get('a') == 2

def test_get(hashmap):
    hashmap.insert('b', 3)
    assert hashmap.get('b') == 3

    with pytest.raises(KeyError):
        hashmap.get('c')

def test_delete(hashmap):
    hashmap.insert('c', 4)
    value = hashmap.delete('c')
    assert value == ('c', 4)
    with pytest.raises(KeyError):
        hashmap.get('c')

def test_custom_hash_function(hashmap_custom):
    hashmap_custom.insert('abc', 123)
    assert hashmap_custom.get('abc') == 123

    hashmap_custom.insert('def', 456)
    assert hashmap_custom.get('def') == 456

    value = hashmap_custom.delete('abc')
    assert value == ('abc', 123)
    with pytest.raises(KeyError):
        hashmap_custom.get('abc')