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

    hashmap.insert('key2', 'value2')
    assert hashmap.get('key2') == 'value2'

def test_get(hashmap):
    hashmap.insert('key1', 'value1')
    assert hashmap.get('key1') == 'value1'

    with pytest.raises(KeyError):
        hashmap.get('non_existing_key')

def test_delete(hashmap):
    hashmap.insert('key1', 'value1')
    result = hashmap.delete('key1')
    assert result == ('key1', 'value1')

    with pytest.raises(KeyError):
        hashmap.delete('key1')

def test_custom_hash_functions(hashmap):
    hashmap_custom = HashMap(hash_function=djb2)
    hashmap_custom.insert('key1', 'value1')
    assert hashmap_custom.get('key1') == 'value1'

    hashmap_custom_sdbm = HashMap(hash_function=sdbm)
    hashmap_custom_sdbm.insert('key1', 'value1')
    assert hashmap_custom_sdbm.get('key1') == 'value1'

    hashmap_custom_lose = HashMap(hash_function=lose_lose)
    hashmap_custom_lose.insert('key1', 'value1')
    assert hashmap_custom_lose.get('key1') == 'value1'