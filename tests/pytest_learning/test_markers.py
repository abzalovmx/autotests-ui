import pytest


@pytest.mark.smoke
def test_some_case():
    pass


@pytest.mark.smoke
class TestSuite:
    @pytest.mark.smoke
    def test_some_case(self):
        pass

    @pytest.mark.smoke
    @pytest.mark.regression
    def test_regression_case(self):
        pass


@pytest.mark.regression
class TestUserAuthentication:
    @pytest.mark.smoke
    def test_login(self):
        pass

    @pytest.mark.slow
    def test_password_reset(self):
        pass

    def test_logout(self):
        pass


@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.critical
def test_critical_login():
    pass
