from httpx import Client
from pydantic import BaseModel, EmailStr
from functools import lru_cache
from clients.authentication.authentication_client import get_authentication_client
# Импортируем модель LoginRequestSchema
from clients.authentication.authentication_schema import LoginRequestSchema
from clients.event_hooks import curl_event_hook


# Добавили суффикс Schema вместо Dict
class AuthenticationUserSchema(BaseModel, frozen=True):  # Наследуем от BaseModel вместо TypedDict
    email: EmailStr
    password: str


@lru_cache(maxsize=None)
def get_private_http_client(user: AuthenticationUserSchema) -> Client:
    authentication_client = get_authentication_client()

    # Используем модель LoginRequestSchema
    # Значения теперь извлекаем не по ключу, а через атрибуты
    login_request = LoginRequestSchema(email=user.email, password=user.password)
    login_response = authentication_client.login(login_request)

    return Client(
        timeout=100,
        base_url="http://localhost:8000",
        # Значения теперь извлекаем не по ключу, а через атрибуты
        headers={"Authorization": f"Bearer {login_response.token.access_token}"},
        event_hooks={"request": [curl_event_hook]}
    )
