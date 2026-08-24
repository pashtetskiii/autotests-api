import httpx

url = "http://127.0.0.1:8000"

post_payload = {
  "email": "user@example.com",
  "password": "string"
}

post_response = httpx.post(f'{url}/api/v1/authentication/login', json=post_payload)
access_token = post_response.json()["token"]["accessToken"]
print(post_response.status_code)
print(access_token)

headers = {"Authorization": f"Bearer {access_token}"}
get_response = httpx.get(f'{url}/api/v1/users/me', headers=headers)

print(get_response.json())
print(get_response.status_code)