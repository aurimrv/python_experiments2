import os
import sys
module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from hash_map import HashMap, djb2, sdbm, lose_lose

import pytest

@pytest.fixture
def map_data():
    map = HashMap()
    map.insert("key1", "value1")
    map.insert("key2", "value2")
    map.insert("key3", "value3")
    return map

def test_hash_map_insert(map_data):
    map_data.insert("new_key", "new_value")
    assert map_data.get("new_key") == "new_value"

def test_hash_map_get(map_data):
    assert map_data.get("key1") == "value1"
    with pytest.raises(KeyError):
        map_data.get("non_existent_key")

def test_hash_map_delete(map_data):
    deleted_value = map_data.delete("key2")
    assert deleted_value == ("key2", "value2")
    with pytest.raises(KeyError):
        map_data.delete("key2")

def test_djb2():
    assert djb2("test") == 6385723493

def test_sdbm():
    assert sdbm("test") == 32745785343201586

def test_lose_lose():
    assert lose_lose("test") == 448