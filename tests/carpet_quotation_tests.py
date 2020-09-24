import pytest

import carpet_quotation


def test_int_discount():
    actual = carpet_quotation.apply_discount(100, 10)
    assert actual == 90


def test_float_discount():
    actual = carpet_quotation.apply_discount(100.0, 10.0)
    assert actual == 90.0


def test_rejects():
    with pytest.raises(TypeError):
        carpet_quotation.apply_discount("qwe", "zxc")
