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

@pytest.fixture
def hash_functions():
    return [djb2, sdbm, lose_lose]

def test_insert(hashmap):
    # Test inserting a key-value pair
    hashmap.insert('key1', 'value1')
    assert hashmap.get('key1') == 'value1'

    # Test inserting and updating a key-value pair
    hashmap.insert('key2', 'value2')
    hashmap.insert('key2', 'value_new')
    assert hashmap.get('key2') == 'value_new'

def test_get(hashmap):
    # Test getting a value for an existing key
    hashmap.insert('key3', 'value3')
    assert hashmap.get('key3') == 'value3'

    # Test getting a value for a non-existing key raises KeyError
    with pytest.raises(KeyError):
        hashmap.get('non_existing_key')

def test_delete(hashmap):
    # Test deleting a key and getting its value
    hashmap.insert('key4', 'value4')
    deleted_value = hashmap.delete('key4')
    assert deleted_value == ('key4', 'value4')

    # Test deleting a non-existing key raises KeyError
    with pytest.raises(KeyError):
        hashmap.delete('non_existing_key')

def test_hash_functions(hash_functions):
    # Test hash functions return numerical values
    for func in hash_functions:
        hash_value = func('test_key')
        assert isinstance(hash_value, int)

        # Test hash functions return different values for different keys
        other_hash_value = func('other_key')
        assert hash_value != other_hash_value