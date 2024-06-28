import os
import sys

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from hash_map import HashMap, djb2, sdbm, lose_lose

import pytest

class TestHashMap:
    @pytest.fixture
    def hashmap(self):
        return HashMap(buckets=5, hash_function=djb2)
    
    def test_insert(self, hashmap):
        hashmap.insert('test_key', 'test_value')
        assert hashmap.get('test_key') == 'test_value'
    
    def test_insert_override(self, hashmap):
        hashmap.insert('test_key', 'test_value')
        hashmap.insert('test_key', 'new_value')
        assert hashmap.get('test_key') == 'new_value'
    
    def test_get_existing_key(self, hashmap):
        hashmap.insert('test_key', 'test_value')
        assert hashmap.get('test_key') == 'test_value'
    
    def test_get_non_existing_key(self, hashmap):
        with pytest.raises(KeyError):
            hashmap.get('non_existing_key')
    
    def test_delete_existing_key(self, hashmap):
        hashmap.insert('test_key', 'test_value')
        deleted_value = hashmap.delete('test_key')
        with pytest.raises(KeyError):
            hashmap.get('test_key')
    
    def test_delete_non_existing_key(self, hashmap):
        with pytest.raises(KeyError):
            hashmap.delete('non_existing_key')