import pytest
from _pytest.fixtures import SubRequest


@pytest.mark.parametrize("number", [1, 2, 3, -1])
def test_numbers(number: int):
    assert number > 0

@pytest.mark.parametrize("number, expected", [(1, 1),
                                              (2, 4),
                                              (3, 9)])
def test_several_numbers(number: int, expected: int):
    assert number ** 2 == expected

'''
может пригодится для тестирования прав доступа к опеределенному эндпоинту
'''

@pytest.mark.parametrize("os", ["macos", "linux", "windows", "debian"])
@pytest.mark.parametrize("host", [
    "https://dev/company.com",
    "https://stable/company.com",
    "https://prod/company.com",
])
def test_multiplacation_of_numbers(os: str, host: str):
    assert len(os + host) > 0

@pytest.fixture(params=[
    "https://dev/company.com",
    "https://stable/company.com",
    "https://prod/company.com",
])
def host(request: SubRequest) -> str:
    return request.param

def test_host(host: str):
    print(f"Running test: {host}")


@pytest.mark.parametrize("user", ["Alice", "Zara"])
class TestOperations:
    def test_user_with_operations(self, user: str):
        print(f"User with operations: {user}")

    def test_user_without_operations(self, user: str):
        print(f"User without operations: {user}")

users = {
    "+70000011": "user with money on bank account",
    "+70000022": "user with money on bank account",
    "+70000023": "user with money on bank account"
}


@pytest.mark.parametrize(
    "phone_number",
     users.keys(),
     ids=lambda phone_number: f"{phone_number}: {users[phone_number]}"
)
def test_identifiers_operation(phone_number: str):
    pass