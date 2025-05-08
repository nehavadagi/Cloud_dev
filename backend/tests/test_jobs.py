import pytest
from httpx import AsyncClient
from main import app

@pytest.mark.asyncio
async def test_submit_job_success():
    async with AsyncClient(app=app, base_url="http://test") as client:
        # Login first
        login_response = await client.post("/auth/login", data={"username": "testuser", "password": "testpassword"})
        assert login_response.status_code == 200
        token = login_response.json()["access_token"]

        # Submit job with token
        response = await client.post(
            "/jobs/submit",
            json={"task_type": "summarize", "input_data": "Test data"},
            headers={"Authorization": f"Bearer {token}"}
        )
        assert response.status_code == 200
        assert "job_id" in response.json()


@pytest.mark.asyncio
async def test_submit_job_insufficient_credits():
    async with AsyncClient(app=app, base_url="http://test") as client:
        # Login first
        login_response = await client.post("/auth/login", data={"username": "testuser", "password": "testpassword"})
        assert login_response.status_code == 200
        token = login_response.json()["access_token"]

        # Simulate 0 credits (this assumes your backend respects current credit state)
        # You may need a fixture or route to reset credits to 0 for this test

        response = await client.post(
            "/jobs/submit",
            json={"task_type": "summarize", "input_data": "Test data"},
            headers={"Authorization": f"Bearer {token}"}
        )
        assert response.status_code == 403
        assert response.json()["detail"] == "Insufficient credits"
