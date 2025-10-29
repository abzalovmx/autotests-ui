import pytest


@pytest.mark.parametrize('number', [1, 2, 3, -1])
def test_numbers(number: int):
    assert 1 > 0
    assert 2 > 1
    assert 3 > 0
