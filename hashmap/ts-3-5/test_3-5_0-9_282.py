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

def test_insert(hashmap):
    key = "test_key"
    value = "test_value"
    hashmap.insert(key, value)
    assert hashmap.get(key) == value

    key2 = "another_key"
    value2 = "another_value"
    hashmap.insert(key2, value2)
    assert hashmap.get(key2) == value2

def test_get(hashmap):
    key = "test_key"
    value = "test_value"
    hashmap.insert(key, value)
    assert hashmap.get(key) == value

    with pytest.raises(KeyError):
        hashmap.get("non_existent_key")

def test_delete(hashmap):
    key = "test_key"
    value = "test_value"
    hashmap.insert(key, value)
    assert hashmap.delete(key) == (key, value)

    with pytest.raises(KeyError):
        hashmap.delete("non_existent_key")