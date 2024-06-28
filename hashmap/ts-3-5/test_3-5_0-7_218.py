import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from hash_map import HashMap, djb2, sdbm, lose_lose

@pytest.fixture
def hashmap():
    return HashMap(buckets=256, hash_function=djb2)

def test_insert(hashmap):
    # Test inserting a key-value pair
    hashmap.insert('test_key', 'test_value')
    assert hashmap.get('test_key') == 'test_value'

    # Test inserting a key that already exists to override the value
    hashmap.insert('test_key', 'new_value')
    assert hashmap.get('test_key') == 'new_value'

def test_get(hashmap):
    # Test getting a value for an existing key
    hashmap.insert('existing_key', 'existing_value')
    assert hashmap.get('existing_key') == 'existing_value'

    # Test getting a value for a key that does not exist
    with pytest.raises(KeyError):
        hashmap.get('non_existing_key')

def test_delete(hashmap):
    # Test deleting a key and getting its value
    hashmap.insert('key_to_delete', 'value_to_delete')
    deleted_value = hashmap.delete('key_to_delete')
    assert deleted_value == ('key_to_delete', 'value_to_delete')

    # Test deleting a key that does not exist
    with pytest.raises(KeyError):
        hashmap.delete('non_existing_key')