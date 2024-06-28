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

def test_hashmap_insert(hashmap):
    hashmap.insert(1, 'one')
    assert hashmap.get(1) == 'one'

    hashmap.insert(1, 'updated')
    assert hashmap.get(1) == 'updated'

    hashmap.insert(2, 'two')
    assert hashmap.get(2) == 'two'

def test_hashmap_get(hashmap):
    hashmap.insert('a', 'apple')
    hashmap.insert('b', 'banana')

    assert hashmap.get('a') == 'apple'
    assert hashmap.get('b') == 'banana'

def test_hashmap_delete(hashmap):
    hashmap.insert('key1', 'value1')
    hashmap.insert('key2', 'value2')

    assert hashmap.delete('key1') == ('key1', 'value1')
    with pytest.raises(KeyError):
        hashmap.get('key1')

def test_djb2():
    assert djb2('hashing') == 229468090697575
    assert djb2('test') == 6385723493

def test_sdbm():
    assert sdbm('hashing') == 8287486388061793431311623892916
    assert sdbm('test') == 32745785343201586

def test_lose_lose():
    assert lose_lose('hashing') == 738
    assert lose_lose('test') == 448