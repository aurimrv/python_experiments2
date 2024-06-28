import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from hash_map import HashMap, djb2, sdbm, lose_lose

@pytest.fixture
def empty_hashmap():
    return HashMap()

def test_hashmap_insert_and_get(empty_hashmap):
    empty_hashmap.insert('test_key', 'test_value')
    assert empty_hashmap.get('test_key') == 'test_value'

def test_hashmap_override_value(empty_hashmap):
    empty_hashmap.insert('key', 'value1')
    empty_hashmap.insert('key', 'value2')
    assert empty_hashmap.get('key') == 'value2'

def test_hashmap_delete_key(empty_hashmap):
    empty_hashmap.insert('key1', 'value1')
    empty_hashmap.insert('key2', 'value2')
    deleted_value = empty_hashmap.delete('key1')
    assert deleted_value[0] == 'key1'

def test_hashmap_delete_key_not_found(empty_hashmap):
    with pytest.raises(KeyError):
        empty_hashmap.delete('non_existent_key')

def test_hashmap_custom_hash_functions(empty_hashmap):
    empty_hashmap.hash_function = djb2
    empty_hashmap.insert('custom_key', 'djb2')
    assert empty_hashmap.get('custom_key') == 'djb2'

    empty_hashmap.hash_function = sdbm
    empty_hashmap.insert('custom_key', 'sdbm')
    assert empty_hashmap.get('custom_key') == 'sdbm'

    empty_hashmap.hash_function = lose_lose
    empty_hashmap.insert('custom_key', 'lose_lose')
    assert empty_hashmap.get('custom_key') == 'lose_lose'