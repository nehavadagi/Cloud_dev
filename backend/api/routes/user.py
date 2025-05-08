from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from database.db import get_db
from utils.tokens import decode_access_token
from models.user import User
from schemas.user import UserOut

router = APIRouter()

def get_current_user(token: str = Depends(decode_access_token), db: Session = Depends(get_db)) -> User:
    email = token.get("sub")
    if not email:
        raise HTTPException(status_code=401, detail="Invalid token")

    user = db.query(User).filter(User.email == email).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    return user

@router.get("/me", response_model=UserOut, tags=["user"])
def get_user_profile(current_user: User = Depends(get_current_user)):
    return current_user

@router.get("/me/credits", tags=["user"])
def get_user_credits(current_user: User = Depends(get_current_user)):
    # Mock logic; assume 'credits' is part of the user model, or customize as needed
    return {"credits": getattr(current_user, "credits", 10)}
