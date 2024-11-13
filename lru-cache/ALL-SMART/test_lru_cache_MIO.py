#Pyguin test cases converted from lru-cache/MIO/seed_1706/test_lru_cache.py
import pytest
import lru_cache as module_0

def test_case_0():
    int_0 = -1209
    with pytest.raises(ValueError):
        module_0.LruCache(int_0)

def test_case_1():
    int_0 = 2234
    lru_cache_0 = module_0.LruCache(int_0)
    assert f'{type(lru_cache_0).__module__}.{type(lru_cache_0).__qualname__}' == 'lru_cache.LruCache'
    assert f'{type(lru_cache_0.head).__module__}.{type(lru_cache_0.head).__qualname__}' == 'lru_cache.ListNode'
    assert f'{type(lru_cache_0.tail).__module__}.{type(lru_cache_0.tail).__qualname__}' == 'lru_cache.ListNode'
    assert lru_cache_0.lookup_map == {}
    assert lru_cache_0.capacity == 2234
    assert module_0.LruCache.terminal_value == 0

def test_case_2():
    none_type_0 = None
    none_type_1 = None
    int_0 = 2
    lru_cache_0 = module_0.LruCache(int_0)
    assert f'{type(lru_cache_0).__module__}.{type(lru_cache_0).__qualname__}' == 'lru_cache.LruCache'
    assert f'{type(lru_cache_0.head).__module__}.{type(lru_cache_0.head).__qualname__}' == 'lru_cache.ListNode'
    assert f'{type(lru_cache_0.tail).__module__}.{type(lru_cache_0.tail).__qualname__}' == 'lru_cache.ListNode'
    assert lru_cache_0.lookup_map == {}
    assert lru_cache_0.capacity == 2
    assert module_0.LruCache.terminal_value == 0
    var_0 = lru_cache_0.put(none_type_0, none_type_1)
    assert len(lru_cache_0.lookup_map) == 1
    var_1 = lru_cache_0.put(int_0, var_0)
    assert len(lru_cache_0.lookup_map) == 2
    var_2 = lru_cache_0.get(none_type_0)
    var_3 = lru_cache_0.put(none_type_1, none_type_1)
    var_4 = lru_cache_0.put(lru_cache_0, none_type_0)
    list_node_0 = module_0.ListNode(var_4, lru_cache_0)

def test_case_3():
    int_0 = 2234
    lru_cache_0 = module_0.LruCache(int_0)
    assert f'{type(lru_cache_0).__module__}.{type(lru_cache_0).__qualname__}' == 'lru_cache.LruCache'
    assert f'{type(lru_cache_0.head).__module__}.{type(lru_cache_0.head).__qualname__}' == 'lru_cache.ListNode'
    assert f'{type(lru_cache_0.tail).__module__}.{type(lru_cache_0.tail).__qualname__}' == 'lru_cache.ListNode'
    assert lru_cache_0.lookup_map == {}
    assert lru_cache_0.capacity == 2234
    assert module_0.LruCache.terminal_value == 0
    var_0 = lru_cache_0.put(lru_cache_0, lru_cache_0)
    assert len(lru_cache_0.lookup_map) == 1

def test_case_4():
    none_type_0 = None
    int_0 = 87
    lru_cache_0 = module_0.LruCache(int_0)
    assert f'{type(lru_cache_0).__module__}.{type(lru_cache_0).__qualname__}' == 'lru_cache.LruCache'
    assert f'{type(lru_cache_0.head).__module__}.{type(lru_cache_0.head).__qualname__}' == 'lru_cache.ListNode'
    assert f'{type(lru_cache_0.tail).__module__}.{type(lru_cache_0.tail).__qualname__}' == 'lru_cache.ListNode'
    assert lru_cache_0.lookup_map == {}
    assert lru_cache_0.capacity == 87
    assert module_0.LruCache.terminal_value == 0
    var_0 = lru_cache_0.put(int_0, none_type_0)
    assert len(lru_cache_0.lookup_map) == 1
    var_1 = lru_cache_0.put(int_0, none_type_0)

def test_case_5():
    none_type_0 = None
    int_0 = 126
    lru_cache_0 = module_0.LruCache(int_0)
    assert f'{type(lru_cache_0).__module__}.{type(lru_cache_0).__qualname__}' == 'lru_cache.LruCache'
    assert f'{type(lru_cache_0.head).__module__}.{type(lru_cache_0.head).__qualname__}' == 'lru_cache.ListNode'
    assert f'{type(lru_cache_0.tail).__module__}.{type(lru_cache_0.tail).__qualname__}' == 'lru_cache.ListNode'
    assert lru_cache_0.lookup_map == {}
    assert lru_cache_0.capacity == 126
    assert module_0.LruCache.terminal_value == 0
    var_0 = lru_cache_0.put(none_type_0, none_type_0)
    assert len(lru_cache_0.lookup_map) == 1
    lru_cache_1 = module_0.LruCache(int_0)
    var_1 = lru_cache_0.get(none_type_0)

def test_case_6():
    none_type_0 = None
    int_0 = 2
    lru_cache_0 = module_0.LruCache(int_0)
    assert f'{type(lru_cache_0).__module__}.{type(lru_cache_0).__qualname__}' == 'lru_cache.LruCache'
    assert f'{type(lru_cache_0.head).__module__}.{type(lru_cache_0.head).__qualname__}' == 'lru_cache.ListNode'
    assert f'{type(lru_cache_0.tail).__module__}.{type(lru_cache_0.tail).__qualname__}' == 'lru_cache.ListNode'
    assert lru_cache_0.lookup_map == {}
    assert lru_cache_0.capacity == 2
    assert module_0.LruCache.terminal_value == 0
    var_0 = lru_cache_0.get(lru_cache_0)
    assert var_0 == -1
    var_1 = lru_cache_0.put(lru_cache_0, none_type_0)
    assert len(lru_cache_0.lookup_map) == 1
    with pytest.raises(ValueError):
        module_0.LruCache(var_0)
