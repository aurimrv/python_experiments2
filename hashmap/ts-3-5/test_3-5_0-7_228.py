import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from hash_map import HashMap, djb2, sdbm, lose_lose

def test_insert():
    h = HashMap()
    h.insert('key1', 'value1')
    assert h.get('key1') == 'value1'

def test_insert_override():
    h = HashMap()
    h.insert('key1', 'value1')
    h.insert('key1', 'value2')
    assert h.get('key1') == 'value2'

def test_get():
    h = HashMap()
    h.insert('key1', 'value1')
    assert h.get('key1') == 'value1'

def test_get_key_error():
    h = HashMap()
    with pytest.raises(KeyError):
        h.get('non_existent_key')

def test_delete():
    h = HashMap()
    h.insert('key1', 'value1')
    deleted_value = h.delete('key1')
    assert deleted_value == ('key1', 'value1')

def test_delete_key_error():
    h = HashMap()
    with pytest.raises(KeyError):
        h.delete('non_existent_key')

def test_djb2():
    assert djb2('test') == 6385723493

def test_sdbm():
    assert sdbm('test') == 32745785343201586

def test_lose_lose():
    assert lose_lose('test') == 448