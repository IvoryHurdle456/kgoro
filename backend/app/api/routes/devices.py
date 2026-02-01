from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from backend.app.api.deps import get_db
from backend.app.models.device import Device
from backend.app.schemas.device import DeviceCreate, DeviceOut, DeviceUpdate

router = APIRouter(prefix="/devices", tags=["devices"])


@router.post("", response_model=DeviceOut, status_code=status.HTTP_201_CREATED)
def create_device(payload: DeviceCreate, db: Session = Depends(get_db)):
    device = Device(**payload.model_dump())
    db.add(device)
    try:
        db.commit()
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Device with this mgmt_ip already exists.",
        )
    db.refresh(device)
    return device


@router.get("", response_model=list[DeviceOut])
def list_devices(db: Session = Depends(get_db), limit: int = 100, offset: int = 0):
    limit = min(max(limit, 1), 500)
    offset = max(offset, 0)
    return db.query(Device).order_by(Device.id.desc()).offset(offset).limit(limit).all()


@router.get("/{device_id}", response_model=DeviceOut)
def get_device(device_id: int, db: Session = Depends(get_db)):
    device = db.get(Device, device_id)
    if not device:
        raise HTTPException(status_code=404, detail="Device not found.")
    return device


@router.patch("/{device_id}", response_model=DeviceOut)
def update_device(device_id: int, payload: DeviceUpdate, db: Session = Depends(get_db)):
    device = db.get(Device, device_id)
    if not device:
        raise HTTPException(status_code=404, detail="Device not found.")

    data = payload.model_dump(exclude_unset=True)
    for k, v in data.items():
        setattr(device, k, v)

    try:
        db.commit()
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Update violates a uniqueness constraint (likely mgmt_ip).",
        )
    db.refresh(device)
    return device


@router.delete("/{device_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_device(device_id: int, db: Session = Depends(get_db)):
    device = db.get(Device, device_id)
    if not device:
        raise HTTPException(status_code=404, detail="Device not found.")
    db.delete(device)
    db.commit()
