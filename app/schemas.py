
from pydantic import BaseModel
from typing import Optional

class ProtocolBase(BaseModel):
    name: str
    description: Optional[str] = None

class ProtocolCreateSchema(ProtocolBase):
    pass

class ProtocolSchema(ProtocolBase):
    id: int
    class Config:
        orm_mode = True

class ObjectOfInterestCreateSchema(BaseModel):
    name: str
    type: str
    visibility: str
    room_id: int
    owner_id: int
    protocol_id: int
    target_uri: Optional[str] = None
    is_active: Optional[bool] = True

class ObjectOfInterestSchema(ObjectOfInterestCreateSchema):
    id: int
    class Config:
        orm_mode = True

class PointOfInterestCreateSchema(BaseModel):
    name: str
    type: str
    visibility: str
    room_id: int
    owner_id: int

class PointOfInterestSchema(PointOfInterestCreateSchema):
    id: int
    class Config:
        orm_mode = True
