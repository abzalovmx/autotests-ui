import pytest


@pytest.mark.skip(reason="Skip test")
def test_feature_in_development():
    pass


@pytest.mark.skip(reason="Skip test")
class TestSuiteSkip:
    def test_feature_in_development(self):
        pass

    def test_feature_in_development_2(self):
        pass
