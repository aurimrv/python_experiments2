import sys
import os

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from hash_map import HashMap, djb2, sdbm, lose_lose

import pytest

@pytest.fixture
def hashmap():
    return HashMap()

def test_insert(hashmap):
    hashmap.insert('key1', 'value1')
    assert hashmap.get('key1') == 'value1'

def test_get(hashmap):
    hashmap.insert('key1', 'value1')
    hashmap.insert('key2', 'value2')
    
    assert hashmap.get('key1') == 'value1'
    assert hashmap.get('key2') == 'value2'
    with pytest.raises(KeyError):
        hashmap.get('non_existent_key')

def test_delete(hashmap):
    hashmap.insert('key1', 'value1')
    result = hashmap.delete('key1')
    
    assert result == ('key1', 'value1')
    with pytest.raises(KeyError):
        hashmap.delete('non_existent_key')

def test_hash_functions():
    assert djb2('test') == djb2('test')
    assert djb2('test') != djb2('Test')
    
    assert sdbm('test') == sdbm('test')
    assert sdbm('test') != sdbm('Test')
    
    assert lose_lose('test') == lose_lose('test')
    assert lose_lose('test') != lose_lose('Test')