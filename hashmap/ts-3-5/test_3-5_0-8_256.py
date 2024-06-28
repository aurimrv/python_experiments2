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
    hashmap.insert('test_key', 'test_value')
    assert hashmap.get('test_key') == 'test_value'

def test_get_existing_key(hashmap):
    hashmap.insert('existing_key', 'existing_value')
    assert hashmap.get('existing_key') == 'existing_value'

def test_get_non_existing_key(hashmap):
    with pytest.raises(KeyError):
        hashmap.get('non_existing_key')

def test_delete_existing_key(hashmap):
    hashmap.insert('key_to_delete', 'value_to_delete')
    deleted_value = hashmap.delete('key_to_delete')
    assert deleted_value == ('key_to_delete', 'value_to_delete')
    with pytest.raises(KeyError):
        hashmap.get('key_to_delete')

def test_delete_non_existing_key(hashmap):
    with pytest.raises(KeyError):
        hashmap.delete('non_existing_key')

def test_hash_functions():
    assert djb2('test_key') == djb2('test_key')
    assert sdbm('test_key') == sdbm('test_key')
    assert lose_lose('test_key') == lose_lose('test_key')