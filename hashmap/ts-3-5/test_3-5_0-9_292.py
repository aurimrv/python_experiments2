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
    # Test inserting a new key
    hashmap.insert('test_key', 'test_value')
    assert hashmap.get('test_key') == 'test_value'
    
    # Test inserting a key that already exists, value should be overridden
    hashmap.insert('test_key', 'new_test_value')
    assert hashmap.get('test_key') == 'new_test_value'

def test_get(hashmap):
    # Test getting a value for a key that exists
    hashmap.insert('existing_key', 'existing_value')
    assert hashmap.get('existing_key') == 'existing_value'
    
    # Test getting a value for a key that does not exist, should raise KeyError
    with pytest.raises(KeyError):
        hashmap.get('non_existing_key')

def test_delete(hashmap):
    # Test deleting a key that exists
    hashmap.insert('key_to_delete', 'value_to_delete')
    deleted_value = hashmap.delete('key_to_delete')
    assert deleted_value == ('key_to_delete', 'value_to_delete')
    
    # Test deleting a key that does not exist, should raise KeyError
    with pytest.raises(KeyError):
        hashmap.delete('non_existing_key')

def test_djb2():
    hashed_value = djb2('test_key')
    assert isinstance(hashed_value, int)

def test_sdbm():
    hashed_value = sdbm('test_key')
    assert isinstance(hashed_value, int)

def test_lose_lose():
    hashed_value = lose_lose('test_key')
    assert isinstance(hashed_value, int)