
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from . import models, schemas
from .database import get_db

router = APIRouter()

# Zone Types
@router.post("/zone-types", response_model=schemas.ZoneTypeSchema)
def create_zone_type(zone_type: schemas.ZoneTypeCreateSchema, db: Session = Depends(get_db)):
    db_zone = models.ZoneType(name=zone_type.name)
    db.add(db_zone)
    db.commit()
    db.refresh(db_zone)
    return db_zone

@router.get("/zone-types", response_model=list[schemas.ZoneTypeSchema])
def get_zone_types(db: Session = Depends(get_db)):
    return db.query(models.ZoneType).all()

# Room Types
@router.post("/room-types", response_model=schemas.RoomTypeSchema)
def create_room_type(room_type: schemas.RoomTypeCreateSchema, db: Session = Depends(get_db)):
    db_room = models.RoomType(name=room_type.name)
    db.add(db_room)
    db.commit()
    db.refresh(db_room)
    return db_room

@router.get("/room-types", response_model=list[schemas.RoomTypeSchema])
def get_room_types(db: Session = Depends(get_db)):
    return db.query(models.RoomType).all()
