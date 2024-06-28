import os
import sys

# Add project directory to path for correct imports
module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from lru_cache import ListNode, LruCache

# Test cases for ListNode class
def test_list_node_init():
    node = ListNode(1, "value")
    assert node.key == 1
    assert node.val == "value"
    assert node.next is None
    assert node.prev is None

# Test cases for LruCache class
def test_lru_cache_init():
    cache = LruCache(3)
    assert cache.capacity == 3
    assert cache.head.key == LruCache.terminal_value
    assert cache.tail.val == LruCache.terminal_value
    assert len(cache.lookup_map) == 0

def test_lru_cache_put_get():
    cache = LruCache(2)
    cache.put(1, "val1")
    cache.put(2, "val2")
    
    assert cache.get(1) == "val1"  # Check if values are correctly added
    assert cache.get(2) == "val2"

    cache.put(3, "val3")  # Adding a new value should remove the least recently used value
    
    assert cache.get(3) == "val3"  # Check if correct value is retrieved after adding more than capacity

def test_lru_cache_put_same_key():
    cache = LruCache(2)
    cache.put(1, "val1")
    cache.put(1, "val2")  # Putting with same key should update the value
    
    assert cache.get(1) == "val2"  # Check if value is correctly updated

def test_lru_cache_get_non_existing_key():
    cache = LruCache(2)
    cache.put(1, "val1")
    
    assert cache.get(2) == -1  # Getting a non-existing key should return -1

def test_lru_cache_capacity_exception():
    try:
        cache = LruCache(0)  # Capacity less than 1 should raise ValueError
    except ValueError as e:
        assert str(e) == "Capacity must be >= 1"

    try:
        cache = LruCache(-1)  # Capacity less than 1 should raise ValueError
    except ValueError as e:
        assert str(e) == "Capacity must be >= 1"