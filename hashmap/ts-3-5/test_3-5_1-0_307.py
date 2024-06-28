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
        return HashMap()

    def test_insert(self, hashmap):
        hashmap.insert('key1', 'value1')
        assert hashmap.get('key1') == 'value1'

    def test_insert_override(self, hashmap):
        hashmap.insert('key1', 'value1')
        hashmap.insert('key1', 'value2')
        assert hashmap.get('key1') == 'value2'

    def test_get_existing_key(self, hashmap):
        hashmap.insert('key1', 'value1')
        assert hashmap.get('key1') == 'value1'

    def test_get_non_existing_key(self, hashmap):
        with pytest.raises(KeyError):
            hashmap.get('key2')

    def test_delete_existing_key(self, hashmap):
        hashmap.insert('key1', 'value1')
        assert hashmap.delete('key1') == ('key1', 'value1')
    
    def test_delete_non_existing_key(self, hashmap):
        with pytest.raises(KeyError):
            hashmap.delete('key2')

class TestHashFunctions:

    def test_djb2(self):
        assert djb2('test') == 6385723493
        assert djb2('hash') != 290186750

    def test_sdbm(self):
        assert sdbm('test') == 32745785343201586
        assert sdbm('hash') != 281783555

    def test_lose_lose(self):
        assert lose_lose('test') == 448
        assert lose_lose('hash') != 448