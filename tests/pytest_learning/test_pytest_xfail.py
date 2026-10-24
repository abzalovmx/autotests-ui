import pytest


@pytest.mark.xfail
def test_with_bug():
    assert False


@pytest.mark.xfail
def test_with_bug2():
    assert True
