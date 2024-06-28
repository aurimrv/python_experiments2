import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from hash_map import HashMap, djb2, sdbm, lose_lose

def test_hash_map_insert():
    hash_map = HashMap()
    hash_map.insert('key1', 'value1')
    assert hash_map.get('key1') == 'value1'

def test_hash_map_get():
    hash_map = HashMap()
    hash_map.insert('key1', 'value1')
    assert hash_map.get('key1') == 'value1'

def test_hash_map_delete():
    hash_map = HashMap()
    hash_map.insert('key1', 'value1')
    deleted_value = hash_map.delete('key1')
    assert deleted_value == ('key1', 'value1')

def test_djb2_hash_function():
    assert djb2('test') == 6385723493

def test_sdbm_hash_function():
    assert sdbm('test') == 32745785343201586

def test_lose_lose_hash_function():
    assert lose_lose('test') == 448

def test_hash_map_insert_override():
    hash_map = HashMap()
    hash_map.insert('key1', 'value1')
    hash_map.insert('key1', 'value2')
    assert hash_map.get('key1') == 'value2'

def test_hash_map_get_key_not_found():
    hash_map = HashMap()
    with pytest.raises(KeyError):
        hash_map.get('non_existent_key')

def test_hash_map_delete_key_not_found():
    hash_map = HashMap()
    with pytest.raises(KeyError):
        hash_map.delete('non_existent_key')