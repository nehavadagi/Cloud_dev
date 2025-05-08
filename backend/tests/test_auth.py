import pytest
from httpx import AsyncClient
from sqlalchemy.orm import Session
from main import app
from database.db import SessionLocal
from models.user import User
from utils.hashing import hash_password


# Setup: Create test user before login tests
def create_test_user():
    db: Session = SessionLocal()
    user = db.query(User).filter(User.email == "testuser@example.com").first()
    if not user:
        user = User(
            username="testuser",
            email="testuser@example.com",
            hashed_password=hash_password("testpassword"),
            credits=5
        )
        db.add(user)
        db.commit()
        db.refresh(user)
    db.close()


@pytest.mark.asyncio
async def test_login_success():
    create_test_user()

    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.post(
            "/auth/login",
            data={"username": "testuser@example.com", "password": "testpassword"},
            headers={"Content-Type": "application/x-www-form-urlencoded"},
        )
    assert response.status_code == 200
    assert "access_token" in response.json()


@pytest.mark.asyncio
async def test_login_failure():
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.post(
            "/auth/login",
            data={"username": "wrong@example.com", "password": "wrongpass"},
            headers={"Content-Type": "application/x-www-form-urlencoded"},
        )
    assert response.status_code == 401
    assert response.json()["detail"] == "Invalid credentials"
