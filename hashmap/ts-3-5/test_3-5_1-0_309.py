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
        return HashMap(buckets=256)

    @pytest.mark.parametrize("test_input, expected", [
        (("key1", "value1"), None),
        (("key2", "value2"), None),
        (("key3", "value3"), None),
    ])
    def test_insert(self, hashmap, test_input, expected):
        key, value = test_input
        hashmap.insert(key, value)
        assert hashmap.get(key) == value

    @pytest.mark.parametrize("test_input, expected", [
        ("key1", "value1"),
        ("key2", "value2"),
        ("key3", "value3"),
    ])
    def test_get(self, hashmap, test_input, expected):
        hashmap.insert(test_input, expected)
        assert hashmap.get(test_input) == expected

    @pytest.mark.parametrize("test_input, expected", [
        ("key1", "value1"),
        ("key2", "value2"),
        ("key3", "value3"),
    ])
    def test_delete(self, hashmap, test_input, expected):
        hashmap.insert(test_input, expected)
        assert hashmap.delete(test_input) == (test_input, expected)

    @pytest.mark.parametrize("test_key, test_hash_function, expected_hash", [
        ("key", djb2, 193496974),
        ("key", sdbm, 460452107327),
        ("key", lose_lose, 329),
    ])
    def test_hash_functions(self, test_key, test_hash_function, expected_hash):
        assert test_hash_function(test_key) == expected_hash