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
    hashmap.insert('test_key', 'test_value')
    assert hashmap.get('test_key') == 'test_value'

def test_get(hashmap):
    hashmap.insert('test_key', 'test_value')
    assert hashmap.get('test_key') == 'test_value'
    with pytest.raises(KeyError):
        hashmap.get('non_existing_key')

def test_delete(hashmap):
    hashmap.insert('test_key', 'test_value')
    assert hashmap.delete('test_key') == ('test_key', 'test_value')
    with pytest.raises(KeyError):
        hashmap.delete('test_key')

def test_custom_hash_functions(hashmap):
    hashmap_djb2 = HashMap(hash_function=djb2)
    hashmap_sdbm = HashMap(hash_function=sdbm)
    hashmap_lose_lose = HashMap(hash_function=lose_lose)

    hashmap_djb2.insert('test_key', 'test_value')
    hashmap_sdbm.insert('test_key', 'test_value')
    hashmap_lose_lose.insert('test_key', 'test_value')

    assert hashmap_djb2.get('test_key') == 'test_value'
    assert hashmap_sdbm.get('test_key') == 'test_value'
    assert hashmap_lose_lose.get('test_key') == 'test_value'

    hashmap_djb2.delete('test_key')
    hashmap_sdbm.delete('test_key')
    hashmap_lose_lose.delete('test_key')

    with pytest.raises(KeyError):
        hashmap_djb2.get('test_key')
    with pytest.raises(KeyError):
        hashmap_sdbm.get('test_key')
    with pytest.raises(KeyError):
        hashmap_lose_lose.get('test_key')