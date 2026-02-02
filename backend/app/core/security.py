from datetime import datetime, timedelta, timezone

from jose import jwt
from passlib.context import CryptContext

from backend.app.core.config import settings

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(password: str, hashed: str) -> bool:
    return pwd_context.verify(password, hashed)

def create_access_token(sub: str, role: str) -> str:
    expire_minutes = int(getattr(settings, "ACCESS_TOKEN_EXPIRE_MINUTES", 60))
    exp = datetime.now(timezone.utc) + timedelta(minutes=expire_minutes)
    payload = {"sub": sub, "role": role, "exp": exp}
    return jwt.encode(payload, settings.JWT_SECRET, algorithm=settings.JWT_ALG)
