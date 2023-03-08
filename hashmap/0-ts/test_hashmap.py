import pytest
from hash_map import HashMap, djb2, sdbm, lose_lose


def test_insert():
    hash_map = HashMap()

    hash_map.insert('hello', 'world')

    assert hash_map.get('hello') == 'world'


def test_get():
    hash_map = HashMap()

    hash_map.insert(3, 'three')
    hash_map.insert('99', 99)

    assert hash_map.get(3) == 'three'
    assert hash_map.get('99') == 99


def test_collisions():
    hash_map = HashMap()

    for i in range(257):
        hash_map.insert(i, str(i))

    for i in range(257):
        assert hash_map.get(i) == str(i)


def test_overwrite():
    hash_map = HashMap()

    hash_map.insert(1, '1')

    assert hash_map.get(1) == '1'

    hash_map.insert(1, '2')

    assert hash_map.get(1) == '2'


def test_not_found():
    hash_map = HashMap()

    with pytest.raises(KeyError):
        hash_map.get(1)


def test_delete():
    hash_map = HashMap()

    hash_map.insert(1, '1')

    assert hash_map.get(1) == '1'

    assert hash_map.delete(1) == (1, '1')

    with pytest.raises(KeyError):
        hash_map.get(1)

    with pytest.raises(KeyError):
        hash_map.delete(1)


def test_djb2():
    assert djb2('hello') == 210714636441

    hash_map = HashMap(hash_function=djb2)

    hash_map.insert('hello', 'world')

    assert hash_map.get('hello') == 'world'
    assert hash_map.buckets[djb2('hello') % len(hash_map.buckets)] == [('hello', 'world')]


def test_sdbm():
    assert sdbm('hello') == 1925877435333486942514

    hash_map = HashMap(hash_function=sdbm)

    hash_map.insert('hello', 'world')

    assert hash_map.get('hello') == 'world'
    assert hash_map.buckets[sdbm('hello') % len(hash_map.buckets)] == [('hello', 'world')]


def test_lose_lose():
    assert lose_lose('hello') == 532

    hash_map = HashMap(hash_function=lose_lose)

    hash_map.insert('hello', 'world')

    assert hash_map.get('hello') == 'world'
    assert hash_map.buckets[lose_lose('hello') % len(hash_map.buckets)] == [('hello', 'world')]
