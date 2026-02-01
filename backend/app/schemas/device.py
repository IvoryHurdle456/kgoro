from ipaddress import ip_address

from pydantic import BaseModel, Field, field_validator

from backend.app.core.enums import Vendor, DeviceType


class DeviceBase(BaseModel):
    hostname: str = Field(min_length=1, max_length=255)
    mgmt_ip: str
    vendor: Vendor
    device_type: DeviceType
    site: str | None = Field(default=None, max_length=128)
    description: str | None = None

    @field_validator("mgmt_ip")
    @classmethod
    def validate_ip(cls, v: str) -> str:
        ip_address(v)
        return v.strip()


class DeviceCreate(DeviceBase):
    pass


class DeviceUpdate(BaseModel):
    hostname: str | None = Field(default=None, min_length=1, max_length=255)
    mgmt_ip: str | None = None
    vendor: Vendor | None = None
    device_type: DeviceType | None = None
    site: str | None = Field(default=None, max_length=128)
    description: str | None = None

    @field_validator("mgmt_ip")
    @classmethod
    def validate_ip(cls, v: str | None) -> str | None:
        if v is None:
            return None
        ip_address(v)
        return v.strip()


class DeviceOut(DeviceBase):
    id: int

    class Config:
        from_attributes = True
