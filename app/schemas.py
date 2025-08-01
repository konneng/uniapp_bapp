from pydantic import BaseModel
from typing import Optional

class ZoneTypeSchema(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True

class ZoneTypeCreateSchema(BaseModel):
    name: str

class RoomTypeSchema(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True

class RoomTypeCreateSchema(BaseModel):
    name: str

class BuildingSchema(BaseModel):
    id: str
    country_code: str
    province_code: str
    name: str
    address: str
    latitude: Optional[float]
    longitude: Optional[float]
    building_type: str
    group_id: str = "-1"

    class Config:
        orm_mode = True

class ZoneSchema(BaseModel):
    id: int
    building_id: str
    zone_type_id: int

    class Config:
        orm_mode = True

class ZoneCreateSchema(BaseModel):
    building_id: str
    zone_type_id: int

class RoomSchema(BaseModel):
    id: int
    zone_id: int
    room_type_id: int

    class Config:
        orm_mode = True

class RoomCreateSchema(BaseModel):
    zone_id: int
    room_type_id: int

class POISchema(BaseModel):
    id: int
    room_id: int
    name: str
    status: str

    class Config:
        orm_mode = True

class POICreateSchema(BaseModel):
    room_id: int
    name: str
    status: str

class EnvParamSchema(BaseModel):
    id: int
    room_id: int
    temperature: Optional[float]
    humidity: Optional[float]
    co2_ppm: Optional[int]

    class Config:
        orm_mode = True

class EnvParamCreateSchema(BaseModel):
    room_id: int
    temperature: Optional[float]
    humidity: Optional[float]
    co2_ppm: Optional[int]

class DevicePresenceSchema(BaseModel):
    id: int
    room_id: int
    device_id: str
    type: str
    present: bool

    class Config:
        orm_mode = True

class DevicePresenceCreateSchema(BaseModel):
    room_id: int
    device_id: str
    type: str
    present: bool
