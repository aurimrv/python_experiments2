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

def test_hashmap_insert(hashmap):
    hashmap.insert('key1', 'value1')
    assert hashmap.get('key1') == 'value1'

def test_hashmap_insert_override(hashmap):
    hashmap.insert('key2', 'value2')
    hashmap.insert('key2', 'new_value2')
    assert hashmap.get('key2') == 'new_value2'

def test_hashmap_get_not_found(hashmap):
    with pytest.raises(KeyError):
        hashmap.get('non_existent_key')

def test_hashmap_delete(hashmap):
    hashmap.insert('key3', 'value3')
    deleted_value = hashmap.delete('key3')
    assert deleted_value == ('key3', 'value3')
    with pytest.raises(KeyError):
        hashmap.get('key3')

def test_hashmap_delete_not_found(hashmap):
    with pytest.raises(KeyError):
        hashmap.delete('non_existent_key')

def test_djb2_hash_function():
    assert djb2('test') == 6385723493

def test_sdbm_hash_function():
    assert sdbm('test') == 32745785343201586

def test_lose_lose_hash_function():
    assert lose_lose('test') == 448