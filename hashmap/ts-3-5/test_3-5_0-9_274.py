import os
import sys
module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from hash_map import HashMap, djb2, sdbm, lose_lose

def test_insert():
    h = HashMap(buckets=2, hash_function=djb2)
    
    h.insert('key1', 'value1')
    assert h.get('key1') == 'value1'
    
    h.insert('key1', 'value2')
    assert h.get('key1') == 'value2'
    
def test_get():
    h = HashMap(buckets=2, hash_function=djb2)
    
    h.insert('key1', 'value1')
    assert h.get('key1') == 'value1'
    
    h.insert('key2', 'value2')
    assert h.get('key2') == 'value2'
    
def test_delete():
    h = HashMap(buckets=2, hash_function=djb2)
    
    h.insert('key1', 'value1')
    deleted = h.delete('key1')
    assert deleted == ('key1', 'value1')
    
    try:
        h.get('key1')
    except KeyError:
        assert True
    
def test_djb2_hash_function():
    assert djb2('ABC') == 193450027
    assert djb2('XYZ') == 193475856  # Collision with ABC

def test_sdbm_hash_function():
    assert sdbm('ABC') == 279714201666
    assert sdbm('XYZ') == 378689972889

def test_lose_lose_hash_function():
    assert lose_lose('ABC') == 198
    assert lose_lose('XYZ') == 267  # Collision with ABC