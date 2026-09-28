import pytest

@pytest.fixture(autouse=True)
def send_analytics_data():
    print("[Autouse] отправляем данные в сервис аналитики")

@pytest.fixture(scope="session")
def settings():
    print("[Session] инициализируем настройки автотестов")


@pytest.fixture(scope="class")
def user():
    print("[Class] создаем данные пользователя один раз раз на тестовый класс")


@pytest.fixture(scope='function')
def users_client(settings):
    print("[Function] Созданем апи клиент на каждый автотест")



class TestUserFlow:
    def test_user_and_login(self, settings, user, users_client):
        ...

    def test_user_can_create_course(self, settings, user, users_client):
        ...

class TestAccountFlow:
    def test_user_account(self, settings, user, users_client):
        ...

@pytest.fixture(scope="function")
def user_data() -> dict:
    print("Создаем пользователя до теста (setup)")
    yield {"username": "test_user", "email": "test@example.com"}
    print("Удаляем пользователя после теста (teardown)")


def test_user_email(user_data: dict):
    print(user_data)
    assert user_data["email"] == "test@example.com"


def test_username(user_data: dict):
    print(user_data)
    assert user_data["username"] == "test_user"