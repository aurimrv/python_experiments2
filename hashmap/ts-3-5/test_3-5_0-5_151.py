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

def test_hashmap_insert(hashmap):
    hashmap.insert('test_key', 'test_value')
    assert hashmap.get('test_key') == 'test_value'

def test_hashmap_insert_override(hashmap):
    hashmap.insert('test_key', 'initial_value')
    hashmap.insert('test_key', 'updated_value')
    assert hashmap.get('test_key') == 'updated_value'

def test_hashmap_get(hashmap):
    hashmap.insert('test_key', 'test_value')
    assert hashmap.get('test_key') == 'test_value'

def test_hashmap_get_key_error(hashmap):
    with pytest.raises(KeyError):
        hashmap.get('non_existent_key')

def test_hashmap_delete(hashmap):
    hashmap.insert('test_key', 'test_value')
    deleted_value = hashmap.delete('test_key')
    assert deleted_value == ('test_key', 'test_value')
    with pytest.raises(KeyError):
        hashmap.get('test_key')

def test_hashmap_delete_key_error(hashmap):
    with pytest.raises(KeyError):
        hashmap.delete('non_existent_key')

def test_djb2_hash_function():
    assert djb2('test_key') == 7572963594076045

def test_sdbm_hash_function():
    assert sdbm('test_key') == 606379187146086983188292032049998418

def test_lose_lose_hash_function():
    assert lose_lose('test_key') == 872