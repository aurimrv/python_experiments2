import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from hash_map import HashMap, djb2, sdbm, lose_lose

@pytest.fixture
def initialize_hash_map():
    hash_map = HashMap()
    return hash_map

def test_insert_and_get(initialize_hash_map):
    hm = initialize_hash_map
    
    hm.insert('a', 1)
    assert hm.get('a') == 1

    hm.insert('b', 5)
    assert hm.get('b') == 5

def test_insert_override(initialize_hash_map):
    hm = initialize_hash_map
    
    hm.insert('test', 10)
    assert hm.get('test') == 10

    hm.insert('test', 20)
    assert hm.get('test') == 20

def test_get_nonexistent_key(initialize_hash_map):
    hm = initialize_hash_map
    with pytest.raises(KeyError):
        hm.get('nonexistent-key')

def test_delete_key(initialize_hash_map):
    hm = initialize_hash_map
    
    hm.insert('key1', 15)
    assert hm.get('key1') == 15

    deleted_key = hm.delete('key1')
    with pytest.raises(KeyError):
        hm.get('key1')
    assert deleted_key == ('key1', 15)

def test_delete_nonexistent_key(initialize_hash_map):
    hm = initialize_hash_map
    with pytest.raises(KeyError):
        hm.delete('nonexistent-key')

def test_djb2_hash_function():
    assert djb2('hello') == 210714636441

def test_sdbm_hash_function():
    assert sdbm('world') == 2203646929940705947314

def test_lose_lose_hash_function():
    assert lose_lose('hashing') == 738