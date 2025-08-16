import pytest
from Cezar_code import crypt


def test_encode():
    """ Check encoding """
    assert crypt('encode', 1, 'niekody') == 'ojflpez'
    assert crypt('encode', 3, 'blabla') == 'eodeod'


def test_decode():
    """ Check encoding """
    assert crypt('decode', 6, 'kody') == 'eixs'
    assert crypt('decode', 4, 'blablabla') == 'xhwxhwxhw'


def test_no_input():
    """ Check encoding """
    assert crypt('decode', 0, '') == 'You_did_not_give_any_message'
    assert crypt('encode', 50, '') == 'You_did_not_give_any_message'
