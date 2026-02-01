from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass

from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


# Import models so Alembic can discover them
from backend.app.models.device import Device  # noqa: E402,F401

# Import Base first
from backend.app.db.base_class import Base  # noqa: F401

# Import all models here so Alembic can discover them
from backend.app.models.device import Device  # noqa: F401,E402
