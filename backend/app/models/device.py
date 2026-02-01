from sqlalchemy import DateTime, String, Text, func
from sqlalchemy.orm import Mapped, mapped_column

from backend.app.db.base_class import Base



class Device(Base):
    __tablename__ = "devices"

    id: Mapped[int] = mapped_column(primary_key=True)
    hostname: Mapped[str] = mapped_column(String(255), index=True)
    mgmt_ip: Mapped[str] = mapped_column(String(45), unique=True, index=True)  # IPv4/IPv6 string
    vendor: Mapped[str] = mapped_column(String(64), index=True)
    device_type: Mapped[str] = mapped_column(String(64), index=True)  # router/switch/firewall/ap/pbx/phone/etc
    site: Mapped[str | None] = mapped_column(String(128), nullable=True, index=True)
    description: Mapped[str | None] = mapped_column(Text, nullable=True)

    created_at: Mapped[DateTime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    updated_at: Mapped[DateTime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
    )
