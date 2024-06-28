import os
import sys

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from hash_map import HashMap, djb2, sdbm, lose_lose

def test_hash_map_insert():
    h = HashMap()
    
    h.insert('key1', 'value1')
    assert h.get('key1') == 'value1'
    
    h.insert('key2', 'value2')
    assert h.get('key2') == 'value2'

def test_hash_map_get():
    h = HashMap()
    
    h.insert('key1', 'value1')
    h.insert('key2', 'value2')
    
    assert h.get('key1') == 'value1'
    assert h.get('key2') == 'value2'

def test_hash_map_delete():
    h = HashMap()
    
    h.insert('key1', 'value1')
    h.insert('key2', 'value2')
    
    deleted_value = h.delete('key1')
    assert deleted_value == ('key1', 'value1')
    
    try:
        h.get('key1')
    except KeyError:
        assert True

def test_djb2_hash():
    assert djb2('key') == 193496974

def test_sdbm_hash():
    assert sdbm('key') == 460452107327

def test_lose_lose_hash():
    assert lose_lose('key') == 329