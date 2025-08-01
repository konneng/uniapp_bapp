
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from . import models, schemas
from .database import get_db

router = APIRouter()

@router.post("/protocols", response_model=schemas.ProtocolSchema)
def create_protocol(protocol: schemas.ProtocolCreateSchema, db: Session = Depends(get_db)):
    db_protocol = models.Protocol(**protocol.dict())
    db.add(db_protocol)
    db.commit()
    db.refresh(db_protocol)
    return db_protocol

@router.get("/protocols", response_model=list[schemas.ProtocolSchema])
def get_protocols(db: Session = Depends(get_db)):
    return db.query(models.Protocol).all()
