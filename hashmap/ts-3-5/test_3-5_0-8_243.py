import os
import sys

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from hash_map import HashMap, djb2, sdbm, lose_lose

import pytest

@pytest.fixture
def hashmap():
    return HashMap()

def test_insert(hashmap):
    hashmap.insert("key1", 1)
    assert hashmap.get("key1") == 1

    hashmap.insert("key2", 2)
    assert hashmap.get("key2") == 2

def test_get(hashmap):
    hashmap.insert("key1", 1)
    hashmap.insert("key2", 2)

    assert hashmap.get("key1") == 1
    assert hashmap.get("key2") == 2

def test_delete(hashmap):
    hashmap.insert("key1", 1)
    hashmap.insert("key2", 2)

    assert hashmap.delete("key1") == ("key1", 1)
    with pytest.raises(KeyError):
        hashmap.get("key1")

def test_hash_functions():
    assert djb2("key1") == djb2("key1")
    assert sdbm("key1") == sdbm("key1")
    assert lose_lose("key1") == lose_lose("key1")