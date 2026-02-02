from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from backend.app.api.deps import get_db
from backend.app.core.security import create_access_token, verify_password, hash_password
from backend.app.models.user import User
from backend.app.schemas.auth import LoginIn, Token

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/login", response_model=Token)
def login(payload: LoginIn, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.username == payload.username).first()
    if not user or not verify_password(payload.password, user.hashed_password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
    token = create_access_token(sub=user.username, role=user.role)
    return Token(access_token=token)

@router.post("/bootstrap-admin", status_code=201)
def bootstrap_admin(username: str, password: str, db: Session = Depends(get_db)):
    # one-time helper for dev. Remove/lock later.
    existing = db.query(User).filter(User.username == username).first()
    if existing:
        raise HTTPException(409, "User exists")
    u = User(username=username, hashed_password=hash_password(password), role="admin", is_active=True)
    db.add(u)
    db.commit()
    return {"created": username}
