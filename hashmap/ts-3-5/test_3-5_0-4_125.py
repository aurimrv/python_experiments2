import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from hash_map import HashMap, djb2, sdbm, lose_lose

@pytest.fixture
def empty_hash_map():
    return HashMap()

def test_insert_and_get(empty_hash_map):
    empty_hash_map.insert('key1', 'value1')
    assert empty_hash_map.get('key1') == 'value1'

def test_insert_override(empty_hash_map):
    empty_hash_map.insert('key2', 'value2')
    empty_hash_map.insert('key2', 'new_value2')
    assert empty_hash_map.get('key2') == 'new_value2'

def test_get_key_not_found(empty_hash_map):
    with pytest.raises(KeyError):
        empty_hash_map.get('non_existent_key')

def test_delete(empty_hash_map):
    empty_hash_map.insert('key3', 'value3')
    deleted_value = empty_hash_map.delete('key3')
    with pytest.raises(KeyError):
        empty_hash_map.get('key3')
    assert deleted_value == ('key3', 'value3')

def test_delete_key_not_found(empty_hash_map):
    with pytest.raises(KeyError):
        empty_hash_map.delete('non_existent_key')

def test_djb2_hash_function():
    assert djb2('test') == 6385723493

def test_sdbm_hash_function():
    assert sdbm('test') == 32745785343201586

def test_lose_lose_hash_function():
    assert lose_lose('test') == 448