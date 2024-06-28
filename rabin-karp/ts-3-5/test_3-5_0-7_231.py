import os
import sys
module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from rabin_karp_substring_search import rabin_karp_find_substring

def test_rabin_karp_find_substring():
    assert rabin_karp_find_substring('hello', 'ell') == 1
    assert rabin_karp_find_substring('hello', 'lo') == 3
    assert rabin_karp_find_substring('hello', 'hello') == 0
    assert rabin_karp_find_substring('hello', 'world') == -1

def test_rabin_karp_find_substring_different_base():
    assert rabin_karp_find_substring('hello', 'ell', base=10) == 1
    assert rabin_karp_find_substring('hello', 'lo', base=10) == 3
    assert rabin_karp_find_substring('hello', 'hello', base=10) == 0
    assert rabin_karp_find_substring('hello', 'world', base=10) == -1

def test_rabin_karp_find_substring_different_prime_modulus():
    assert rabin_karp_find_substring('hello', 'ell', prime_modulus=11) == 1
    assert rabin_karp_find_substring('hello', 'lo', prime_modulus=11) == 3
    assert rabin_karp_find_substring('hello', 'hello', prime_modulus=11) == 0
    assert rabin_karp_find_substring('hello', 'world', prime_modulus=11) == -1