from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from . import models, schemas
from .database import get_db

router = APIRouter()

# --- BUILDINGS ---
@router.post("/buildings", response_model=schemas.BuildingSchema)
def create_building(building: schemas.BuildingSchema, db: Session = Depends(get_db)):
    db_building = models.Building(**building.dict())
    db.add(db_building)
    db.commit()
    db.refresh(db_building)
    return db_building  # ✅ restituisci l’oggetto SQLAlchemy aggiornato

@router.get("/buildings", response_model=list[schemas.BuildingSchema])
def get_buildings(db: Session = Depends(get_db)):
    print("📥 [GET /buildings] Richiesta ricevuta")
    try:
        buildings = db.query(models.Building).all()
        print(f"📤 [GET /buildings] Edifici trovati: {len(buildings)}")
        return buildings
    except Exception as e:
        print(f"❌ Errore nella query /buildings: {e}")
        raise

# --- ZONES ---
@router.post("/zones", response_model=schemas.ZoneSchema)
def create_zone(zone: schemas.ZoneCreateSchema, db: Session = Depends(get_db)):
    db_zone = models.Zone(**zone.dict())
    db.add(db_zone)
    db.commit()
    db.refresh(db_zone)
    return db_zone

@router.get("/zones", response_model=list[schemas.ZoneSchema])
def get_zones(db: Session = Depends(get_db)):
    return db.query(models.Zone).all()

# --- ROOMS ---
@router.post("/rooms", response_model=schemas.RoomSchema)
def create_room(room: schemas.RoomCreateSchema, db: Session = Depends(get_db)):
    db_room = models.Room(**room.dict())
    db.add(db_room)
    db.commit()
    db.refresh(db_room)
    return db_room

@router.get("/rooms", response_model=list[schemas.RoomSchema])
def get_rooms(db: Session = Depends(get_db)):
    return db.query(models.Room).all()

# --- POINTS OF INTEREST ---
@router.post("/points-of-interest", response_model=schemas.PointOfInterestSchema)
def create_poi(poi: schemas.PointOfInterestCreateSchema, db: Session = Depends(get_db)):
    db_poi = models.PointOfInterest(**poi.dict())
    db.add(db_poi)
    db.commit()
    db.refresh(db_poi)
    return db_poi

@router.get("/points-of-interest", response_model=list[schemas.PointOfInterestSchema])
def get_pois(db: Session = Depends(get_db)):
    return db.query(models.PointOfInterest).all()

# --- ENVIRONMENTAL PARAMETERS ---
@router.post("/environmental-parameters", response_model=schemas.EnvironmentalParameterSchema)
def create_env_param(param: schemas.EnvironmentalParameterCreateSchema, db: Session = Depends(get_db)):
    db_param = models.EnvironmentalParameter(**param.dict())
    db.add(db_param)
    db.commit()
    db.refresh(db_param)
    return db_param

@router.get("/environmental-parameters", response_model=list[schemas.EnvironmentalParameterSchema])
def get_env_params(db: Session = Depends(get_db)):
    return db.query(models.EnvironmentalParameter).all()

# --- DEVICE PRESENCE ---
@router.post("/device-presence", response_model=schemas.DevicePresenceSchema)
def create_device_presence(data: schemas.DevicePresenceCreateSchema, db: Session = Depends(get_db)):
    db_device = models.DevicePresence(**data.dict())
    db.add(db_device)
    db.commit()
    db.refresh(db_device)
    return db_device

@router.get("/device-presence", response_model=list[schemas.DevicePresenceSchema])
def get_device_presence(db: Session = Depends(get_db)):
    return db.query(models.DevicePresence).all()

# --- ZONE TYPES ---
@router.post("/zone-types", response_model=schemas.ZoneTypeSchema)
def create_zone_type(zone_type: schemas.ZoneTypeCreateSchema, db: Session = Depends(get_db)):
    db_zone_type = models.ZoneType(name=zone_type.name)
    db.add(db_zone_type)
    db.commit()
    db.refresh(db_zone_type)
    return db_zone_type

@router.get("/zone-types", response_model=list[schemas.ZoneTypeSchema])
def get_zone_types(db: Session = Depends(get_db)):
    return db.query(models.ZoneType).all()

# --- ROOM TYPES ---
@router.post("/room-types", response_model=schemas.RoomTypeSchema)
def create_room_type(room_type: schemas.RoomTypeCreateSchema, db: Session = Depends(get_db)):
    db_room_type = models.RoomType(name=room_type.name)
    db.add(db_room_type)
    db.commit()
    db.refresh(db_room_type)
    return db_room_type

@router.get("/room-types", response_model=list[schemas.RoomTypeSchema])
def get_room_types(db: Session = Depends(get_db)):
    return db.query(models.RoomType).all()

# --- OBJECTS OF INTEREST ---
@router.post("/objects-of-interest", response_model=schemas.ObjectOfInterestSchema)
def create_ooi(ooi: schemas.ObjectOfInterestCreateSchema, db: Session = Depends(get_db)):
    db_ooi = models.ObjectOfInterest(**ooi.dict())
    db.add(db_ooi)
    db.commit()
    db.refresh(db_ooi)
    return db_ooi

@router.get("/objects-of-interest", response_model=list[schemas.ObjectOfInterestSchema])
def get_ooi(db: Session = Depends(get_db)):
    return db.query(models.ObjectOfInterest).all()

# --- USERS ---
@router.post("/users", response_model=schemas.UserSchema)
def create_user(user: schemas.UserCreateSchema, db: Session = Depends(get_db)):
    db_user = models.User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

@router.get("/users", response_model=list[schemas.UserSchema])
def get_users(db: Session = Depends(get_db)):
    return db.query(models.User).all()
