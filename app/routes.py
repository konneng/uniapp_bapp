from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from . import database, models, schemas

router = APIRouter()

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

# GET /buildings
@router.get("/buildings", response_model=list[schemas.BuildingSchema])
def get_buildings(db: Session = Depends(get_db)):
    return db.query(models.Building).all()

# POST /buildings
@router.post("/buildings", response_model=schemas.BuildingSchema)
def create_building(building: schemas.BuildingSchema, db: Session = Depends(get_db)):
    db_building = models.Building(**building.dict())
    db.add(db_building)
    db.commit()
    db.refresh(db_building)
    return db_building

# GET /zones
@router.get("/zones", response_model=list[schemas.ZoneSchema])
def get_zones(db: Session = Depends(get_db)):
    return db.query(models.Zone).all()

# POST /zones
@router.post("/zones", response_model=schemas.ZoneSchema)
def create_zone(zone: schemas.ZoneCreateSchema, db: Session = Depends(get_db)):
    db_zone = models.Zone(**zone.dict())
    db.add(db_zone)
    db.commit()
    db.refresh(db_zone)
    return db_zone

# GET /rooms
@router.get("/rooms", response_model=list[schemas.RoomSchema])
def get_rooms(db: Session = Depends(get_db)):
    return db.query(models.Room).all()

# POST /rooms
@router.post("/rooms", response_model=schemas.RoomSchema)
def create_room(room: schemas.RoomCreateSchema, db: Session = Depends(get_db)):
    db_room = models.Room(**room.dict())
    db.add(db_room)
    db.commit()
    db.refresh(db_room)
    return db_room
