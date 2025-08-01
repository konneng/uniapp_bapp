from pydantic import BaseModel
from typing import Optional

class BuildingSchema(BaseModel):
    id: str
    country_code: str
    province_code: str
    name: str
    address: str
    latitude: Optional[float]
    longitude: Optional[float]
    building_type: str

    class Config:
        orm_mode = True

class ZoneSchema(BaseModel):
    id: int
    building_id: str
    name: str

    class Config:
        orm_mode = True

class ZoneCreateSchema(BaseModel):
    building_id: str
    name: str

class RoomSchema(BaseModel):
    id: int
    zone_id: int
    name: str

    class Config:
        orm_mode = True

class RoomCreateSchema(BaseModel):
    zone_id: int
    name: str
