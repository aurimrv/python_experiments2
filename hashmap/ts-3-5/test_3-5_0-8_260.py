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

def test_get_non_existing_key_raises_KeyError(hashmap):
    with pytest.raises(KeyError):
        hashmap.get('non_existing_key')

def test_update_existing_key(hashmap):
    hashmap.insert('key3', 'value3')
    hashmap.insert('key3', 'new_value3')
    assert hashmap.get('key3') == 'new_value3'

def test_delete_existing_key(hashmap):
    hashmap.insert('key4', 'value4')
    assert hashmap.delete('key4') == ('key4', 'value4')
    with pytest.raises(KeyError):
        hashmap.get('key4')

def test_delete_non_existing_key_raises_KeyError(hashmap):
    with pytest.raises(KeyError):
        hashmap.delete('non_existing_key')

def test_djb2_hash_function():
    assert djb2('abc') == 193485963

def test_sdbm_hash_function():
    assert sdbm('def') == 430329505701

def test_lose_lose_hash_function():
    assert lose_lose('ghi') == 312