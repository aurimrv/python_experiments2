import os
import sys
module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from hash_map import HashMap, djb2, sdbm, lose_lose

import pytest

@pytest.fixture
def empty_hashmap():
    return HashMap()

@pytest.fixture
def hashmap_with_data():
    hm = HashMap()
    hm.insert('key1', 'value1')
    hm.insert('key2', 'value2')
    return hm

def test_insert(empty_hashmap):
    empty_hashmap.insert('key1', 'value1')
    assert empty_hashmap.get('key1') == 'value1'

    empty_hashmap.insert('key2', 'value2')
    assert empty_hashmap.get('key2') == 'value2'

def test_get(hashmap_with_data):
    assert hashmap_with_data.get('key1') == 'value1'
    assert hashmap_with_data.get('key2') == 'value2'
    with pytest.raises(KeyError):
        hashmap_with_data.get('key3')

def test_delete(hashmap_with_data):
    deleted_value = hashmap_with_data.delete('key1')
    assert deleted_value == ('key1', 'value1')
    with pytest.raises(KeyError):
        hashmap_with_data.get('key1')

def test_djb2():
    assert djb2('test') == 6385723493
    assert djb2('hello') == 210714636441

def test_sdbm():
    assert sdbm('test') == 32745785343201586
    assert sdbm('hello') == 1925877435333486942514

def test_lose_lose():
    assert lose_lose('test') == 448
    assert lose_lose('hello') == 532