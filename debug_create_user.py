"""
Диагностика: почему create_user_response.json() падает с JSONDecodeError.
Запусти:  python debug_create_user.py
и пришли мне весь вывод.
"""
import os
import httpx

print("httpx version:", httpx.__version__)
print("proxy env:", {
    k: v for k, v in os.environ.items()
    if k.upper() in ("HTTP_PROXY", "HTTPS_PROXY", "ALL_PROXY", "NO_PROXY")
})

from faker_example import fake
from clients.users.public_users_client import get_public_users_client, CreateUserRequestDict

request = CreateUserRequestDict(
    email=fake.email(),
    password="string",
    lastName="string",
    firstName="string",
    middleName="string",
)
print("request:", request)

response = get_public_users_client().create_user_api(request)

print("=" * 60)
print("request url :", response.request.url)
print("status      :", response.status_code)
print("reason      :", response.reason_phrase)
print("history     :", response.history)
print("headers     :", dict(response.headers))
print("len(content):", len(response.content))
print("text repr   :", repr(response.text[:1000]))
print("=" * 60)
