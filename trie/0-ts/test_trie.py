import pytest
from trie import Trie


def test_trie():
    trie = Trie(['hello','hel','headway','tree','second','true'])

    assert Trie.eof in trie.head['h']['e']['l']
    assert Trie.eof in trie.head['t']['r']['e']['e']
    assert Trie.eof in trie.head['h']['e']['l']['l']['o']


def test_add():
    trie = Trie(['1',])

    with pytest.raises(KeyError):
        trie.head['2']

    trie.add('2')

    assert Trie.eof in trie.head['2']

