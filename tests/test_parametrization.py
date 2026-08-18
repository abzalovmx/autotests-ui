import pytest
from _pytest.fixtures import SubRequest


@pytest.mark.parametrize('number', [1, 2, 3, -1])
def test_numbers(number: int):
    assert number > 0


@pytest.mark.parametrize('number, expected', [(1,1), (2, 4), (3, 9)])
def test_several_numbers(number: int, expected: int):
    assert number ** 2 == expected

@pytest.mark.parametrize('os', ['macos', 'linux', 'windows', 'debian'])
@pytest.mark.parametrize('browser', ['chrome', 'firefox', 'webkit'])
def test_multiplication_of_numbers(os: str, browser: str):
    assert len(os + browser) > 0


@pytest.fixture(params=['chrome', 'firefox', 'webkit'])
def browser(request: SubRequest):
    return request.param


def test_open_browser(browser: str):
    print(f'Running test on browser: {browser}')


@pytest.mark.parametrize('user', ['Alice', 'Zara'])
class TestOperations:
    @pytest.mark.parametrize('account', ['Credit card', 'Debit card'])
    def test_user_with_operations(self, user: str, account: str):
        pass


    def test_user_without_operations(self, user: str):
        pass


users = {
    '+998994564': 'User with money on bank account',
    '+998654654': 'User without money on bank account',
    '+998745678': 'User with operations on bank account'
}


@pytest.mark.parametrize(
    'phone_number',
    users.keys(),
    ids=lambda phone_number: f'{phone_number}: {users[phone_number]}'
)
def test_identifiers(phone_number: str):
    pass
