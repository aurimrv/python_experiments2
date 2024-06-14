import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from combinations import combinations_of_word, combinations_of_phone_input

def test_combinations_of_word():
    # Test case for empty string
    assert combinations_of_word('') == []

    # Test case for single character string
    assert combinations_of_word('a') == ['a']

    # Test case for a simple word
    assert combinations_of_word('cat') == ['c', 'ca', 'cat', 'a', 'at', 't']

    # Test case for a longer word
    assert combinations_of_word('hello') == ['h', 'he', 'hel', 'hell', 'hello', 'e', 'el', 'ell', 'ello', 'l', 'll', 'llo', 'l', 'lo', 'o']

def test_combinations_of_phone_input():
    # Test case for single digit input
    assert combinations_of_phone_input('2') == ['a', 'b', 'c']

    # Test case for two-digit input
    assert combinations_of_phone_input('23') == ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']

    # Test case for three-digit input
    assert combinations_of_phone_input('456') == ['gjm', 'gjn', 'gjo', 'gkm', 'gkn', 'gko', 'glm', 'gln', 'glo', 'hjm', 'hjn', 'hjo', 'hkm', 'hkn', 'hko', 'hlm', 'hln', 'hlo', 'ijm', 'ijn', 'ijo', 'ikm', 'ikn', 'iko', 'ilm', 'iln', 'ilo']

    # Test case for input with repeating digits
    assert combinations_of_phone_input('777') == ['ppp', 'ppq', 'ppr', 'pps', 'pqp', 'pqq', 'pqr', 'pqs', 'prp', 'prq', 'prr', 'prs', 'psp', 'psq', 'psr', 'pss', 'qpp', 'qpq', 'qpr', 'qps', 'qqp', 'qqq', 'qqr', 'qqs', 'qrp', 'qrq', 'qrr', 'qrs', 'qsp', 'qsq', 'qsr', 'qss', 'rpp', 'rpq', 'rpr', 'rps', 'rqp', 'rqq', 'rqr', 'rqs', 'rrp', 'rrq', 'rrr', 'rrs', 'rsp', 'rsq', 'rsr', 'rss', 'spp', 'spq', 'spr', 'sps', 'sqp', 'sqq', 'sqr', 'sqs', 'srp', 'srq', 'srr', 'srs', 'ssp', 'ssq', 'ssr', 'sss']
