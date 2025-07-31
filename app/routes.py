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

@router.get("/buildings", response_model=list[schemas.BuildingSchema])
def get_buildings(db: Session = Depends(get_db)):
    return db.query(models.Building).all()
