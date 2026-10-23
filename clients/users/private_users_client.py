from httpx import Response
from clients.api_client import APIClient
from clients.private_http_builder import get_private_http_client, AuthenticationUserSchema
from clients.users.users_schema import UpdateUserRequestSchema, GetUserResponseSchema
import allure
from tools.routes import APIRoutes


class PrivateUsersClient(APIClient):
    @allure.step("Make GET user me")
    def get_user_me_api(self) -> Response:
        return self.get(f'{APIRoutes.USERS}/me')

    @allure.step("Make GET user by id {user_id}")
    def get_user_api(self, user_id: str) -> Response:
        return self.get(f'{APIRoutes.USERS}/{user_id}')


    def get_user(self, user_id: str) -> GetUserResponseSchema:
        response = self.get_user_api(user_id)
        return GetUserResponseSchema.model_validate_json(response.text)

    @allure.step("Make UPDATE user by {user_id}")
    def update_user_api(self, user_id, request: UpdateUserRequestSchema) -> Response:
        return self.patch(f'{APIRoutes.USERS}/{user_id}', json=request.model_dump(by_alias=True))

    @allure.step("Make DELETE user by {user_id}")
    def delete_user_api(self, user_id: str) -> Response:
        return self.delete(f'{APIRoutes.USERS}/{user_id}')

def get_private_users_client(user: AuthenticationUserSchema) -> PrivateUsersClient:
    return PrivateUsersClient(client=get_private_http_client(user))

