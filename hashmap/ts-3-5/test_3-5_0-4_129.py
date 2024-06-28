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
    hashmap.insert('key1', 'value1')
    assert hashmap.get('key1') == 'value1'

def test_get_existing_key(hashmap):
    hashmap.insert('key2', 'value2')
    assert hashmap.get('key2') == 'value2'

def test_get_non_existing_key(hashmap):
    with pytest.raises(KeyError):
        hashmap.get('non_existing_key')

def test_delete_existing_key(hashmap):
    hashmap.insert('key3', 'value3')
    deleted_value = hashmap.delete('key3')
    assert deleted_value == ('key3', 'value3')
    with pytest.raises(KeyError):
        hashmap.get('key3')

def test_delete_non_existing_key(hashmap):
    with pytest.raises(KeyError):
        hashmap.delete('non_existing_key')

def test_custom_hash_functions():
    custom_hashmap = HashMap(hash_function=djb2)
    custom_hashmap.insert('key4', 'value4')
    assert custom_hashmap.get('key4') == 'value4'

    custom_hashmap = HashMap(hash_function=sdbm)
    custom_hashmap.insert('key5', 'value5')
    assert custom_hashmap.get('key5') == 'value5'

    custom_hashmap = HashMap(hash_function=lose_lose)
    custom_hashmap.insert('key6', 'value6')
    assert custom_hashmap.get('key6') == 'value6'