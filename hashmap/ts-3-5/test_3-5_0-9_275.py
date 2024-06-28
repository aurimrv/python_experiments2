import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from hash_map import HashMap, djb2, sdbm, lose_lose

@pytest.fixture
def hashmap():
    return HashMap(buckets=5, hash_function=djb2)

def test_insert(hashmap):
    hashmap.insert('test_key', 'test_value')
    assert hashmap.get('test_key') == 'test_value'

def test_get_empty_key_raises_keyerror(hashmap):
    with pytest.raises(KeyError):
        hashmap.get('nonexistent_key')

def test_delete(hashmap):
    hashmap.insert('key_to_delete', 'value_to_delete')
    deleted_value = hashmap.delete('key_to_delete')
    assert deleted_value == ('key_to_delete', 'value_to_delete')

def test_delete_nonexistent_key_raises_keyerror(hashmap):
    with pytest.raises(KeyError):
        hashmap.delete('nonexistent_key')

def test_multiple_inserts(hashmap):
    hashmap.insert('key1', 'value1')
    hashmap.insert('key2', 'value2')
    hashmap.insert('key3', 'value3')
    assert hashmap.get('key1') == 'value1'
    assert hashmap.get('key2') == 'value2'
    assert hashmap.get('key3') == 'value3'

def test_override_existing_key(hashmap):
    hashmap.insert('key_to_override', 'initial_value')
    hashmap.insert('key_to_override', 'new_value')
    assert hashmap.get('key_to_override') == 'new_value'

def test_hash_functions():
    assert djb2('test') == 6385723493
    assert sdbm('test') == 32745785343201586
    assert lose_lose('test') == 448