from clients.api_client import APIClient
from clients.public_http_builder import get_public_http_client  # Импортируем builder
from httpx import Response
from typing import TypedDict
from clients.authentication.authentication_schema import LoginRequestSchema, RefreshRequestSchema,LoginResponseSchema


class AuthenticationClient(APIClient):
    def login_api(self, request: LoginRequestSchema) -> Response:
        return self.post('/api/v1/authentication/login',
                         json=request.model_dump(by_alias=True))

    def refresh_api(self, request: RefreshRequestSchema) -> Response:
        return self.post('/api/v1/authentication/refresh',
                         json=request.model_dump(by_alias=True))

    def login(self, request: LoginRequestSchema) -> LoginResponseSchema:
        response = self.login_api(request)
        return LoginResponseSchema.model_validate_json(response.text) #если придёт null мы узнаем это из за .text

# Добавляем builder для AuthenticationClient
def get_authentication_client() -> AuthenticationClient:
    """
    Функция создаёт экземпляр AuthenticationClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию AuthenticationClient.
    """
    return AuthenticationClient(client=get_public_http_client())