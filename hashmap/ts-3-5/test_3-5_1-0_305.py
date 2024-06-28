import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from hash_map import HashMap, djb2, sdbm, lose_lose

@pytest.fixture
def hashmap_instance():
    return HashMap()

def test_hashmap_insert(hashmap_instance):
    hashmap_instance.insert("key1", "value1")
    assert hashmap_instance.get("key1") == "value1"

def test_hashmap_get(hashmap_instance):
    hashmap_instance.insert("key2", "value2")
    assert hashmap_instance.get("key2") == "value2"

def test_hashmap_delete(hashmap_instance):
    hashmap_instance.insert("key3", "value3")
    value_deleted = hashmap_instance.delete("key3")
    assert value_deleted == ("key3", "value3")
    with pytest.raises(KeyError):
        hashmap_instance.get("key3")

def test_hash_functions():
    assert djb2("hello") == 210714636441
    assert sdbm("world") == 2203646929940705947314
    assert lose_lose("test") == 448