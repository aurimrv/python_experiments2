import os
import sys
module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from hash_map import HashMap, djb2, sdbm, lose_lose

import pytest

@pytest.fixture
def hash_map():
    return HashMap()

def test_insert(hash_map):
    hash_map.insert("key1", "value1")
    assert hash_map.get("key1") == "value1"

def test_get(hash_map):
    hash_map.insert("key2", "value2")
    assert hash_map.get("key2") == "value2"

def test_delete(hash_map):
    hash_map.insert("key3", "value3")
    assert hash_map.delete("key3") == ("key3", "value3")

def test_insert_override(hash_map):
    hash_map.insert("key4", "value4")
    hash_map.insert("key4", "new_value")
    assert hash_map.get("key4") == "new_value"

def test_get_missing_key(hash_map):
    with pytest.raises(KeyError):
        hash_map.get("non_existent_key")

def test_delete_missing_key(hash_map):
    with pytest.raises(KeyError):
        hash_map.delete("non_existent_key")

def test_custom_hash_functions():
    hash_map = HashMap(buckets=256, hash_function=djb2)
    hash_map.insert("key_djb2", "value_djb2")
    assert hash_map.get("key_djb2") == "value_djb2"

    hash_map = HashMap(buckets=256, hash_function=sdbm)
    hash_map.insert("key_sdbm", "value_sdbm")
    assert hash_map.get("key_sdbm") == "value_sdbm"

    hash_map = HashMap(buckets=256, hash_function=lose_lose)
    hash_map.insert("key_lose_lose", "value_lose_lose")
    assert hash_map.get("key_lose_lose") == "value_lose_lose"