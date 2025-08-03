
from pydantic import BaseModel
from typing import Optional
from datetime import datetime

# -------------------------------
# PROTOCOLS
# -------------------------------
class ProtocolBase(BaseModel):
    name: str
    description: Optional[str] = None

class ProtocolCreateSchema(ProtocolBase):
    pass

class ProtocolSchema(ProtocolBase):
    id: int
    model_config = {"from_attributes": True}


# -------------------------------
# OBJECTS OF INTEREST
# -------------------------------
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
    model_config = {"from_attributes": True}


# -------------------------------
# POINTS OF INTEREST
# -------------------------------
class PointOfInterestCreateSchema(BaseModel):
    name: str
    type: str
    visibility: str
    room_id: int
    owner_id: int

class PointOfInterestSchema(PointOfInterestCreateSchema):
    id: int
    model_config = {"from_attributes": True}


# -------------------------------
# BUILDINGS
# -------------------------------
class BuildingCreateSchema(BaseModel):
    id: str
    country: str
    province: str
    name: str
    address: str
    latitude: float
    longitude: float
    building_type: str
    group_id: str

class BuildingSchema(BuildingCreateSchema):
    model_config = {"from_attributes": True}


# -------------------------------
# ZONES
# -------------------------------
class ZoneCreateSchema(BaseModel):
    id: str
    name: str
    building_id: str

class ZoneSchema(ZoneCreateSchema):
    model_config = {"from_attributes": True}


# -------------------------------
# ROOMS
# -------------------------------
class RoomCreateSchema(BaseModel):
    name: str
    zone_id: int

class RoomSchema(RoomCreateSchema):
    id: int
    model_config = {"from_attributes": True}


# -------------------------------
# ENVIRONMENTAL PARAMETERS
# -------------------------------
class EnvironmentalParameterCreateSchema(BaseModel):
    room_id: int
    temperature: float
    humidity: float
    air_quality: Optional[str] = None
    timestamp: Optional[datetime] = None

class EnvironmentalParameterSchema(EnvironmentalParameterCreateSchema):
    id: int
    model_config = {"from_attributes": True}


# -------------------------------
# DEVICE PRESENCE
# -------------------------------
class DevicePresenceCreateSchema(BaseModel):
    room_id: int
    device_id: str
    present: bool
    timestamp: Optional[datetime] = None

class DevicePresenceSchema(DevicePresenceCreateSchema):
    id: int
    model_config = {"from_attributes": True}


# -------------------------------
# ZONE TYPE
# -------------------------------
class ZoneTypeCreateSchema(BaseModel):
    name: str

class ZoneTypeSchema(ZoneTypeCreateSchema):
    id: int
    model_config = {"from_attributes": True}


# -------------------------------
# ROOM TYPE
# -------------------------------
class RoomTypeCreateSchema(BaseModel):
    name: str

class RoomTypeSchema(RoomTypeCreateSchema):
    id: int
    model_config = {"from_attributes": True}

# -------------------------------
#  USER 
# -------------------------------
class UserStatusSchema(BaseModel):
    id: int
    name: str
    description: Optional[str] = None

    model_config = {"from_attributes": True}
    
class UserCreateSchema(BaseModel):
    username: str
    email: Optional[str]
    phone: Optional[str]
    full_name: Optional[str]
    hashed_password: Optional[str]
    status_id: int
    accepted_terms: Optional[bool] = False

class UserSchema(UserCreateSchema):
    id: int
    signup_date: datetime

    model_config = {"from_attributes": True}
