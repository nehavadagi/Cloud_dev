import pytest
from httpx import AsyncClient
from main import app

@pytest.mark.asyncio
async def test_get_user_credits():
    async with AsyncClient(app=app, base_url="http://test") as client:
        # First, login to get access token
        login_response = await client.post("/auth/login", data={
            "username": "testuser",
            "password": "testpassword"
        })
        assert login_response.status_code == 200
        token = login_response.json()["access_token"]

        # Make authenticated request
        response = await client.get(
            "/user/credits",
            headers={"Authorization": f"Bearer {token}"}
        )

    assert response.status_code == 200
    assert "credits" in response.json()
