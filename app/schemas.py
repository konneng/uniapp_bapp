
from pydantic import BaseModel
from typing import Optional

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

    model_config = {
        "from_attributes": True
    }

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

    model_config = {
        "from_attributes": True
    }

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

    model_config = {
        "from_attributes": True
    }

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
    model_config = {
        "from_attributes": True
    }
# -------------------------------
# ZONES
# -------------------------------
class ZoneCreateSchema(BaseModel):
    id: str
    name: str
    building_id: str

class ZoneSchema(ZoneCreateSchema):
    model_config = {
        "from_attributes": True
    }

# -------------------------------
# ROOMS
# -------------------------------
class RoomCreateSchema(BaseModel):
    id: str
    name: str
    zone_id: str

class RoomSchema(RoomCreateSchema):
    model_config = {
        "from_attributes": True
    }
# -------------------------------
# ENVIRONMENTAL PARAMETERS
# -------------------------------
class EnvironmentalParameterCreateSchema(BaseModel):
    room_id: int
    temperature: float
    humidity: float
    air_quality: Optional[str] = None
    timestamp: Optional[str] = None  # puoi usare datetime se preferisci

class EnvironmentalParameterSchema(EnvironmentalParameterCreateSchema):
    id: int

    model_config = {
        "from_attributes": True
    }
# -------------------------------
# DEVICE PRESENCE
# -------------------------------
class DevicePresenceCreateSchema(BaseModel):
    room_id: int
    device_id: str  # es: MAC address, UUID BLE, etc.
    present: bool
    timestamp: Optional[str] = None  # o datetime

class DevicePresenceSchema(DevicePresenceCreateSchema):
    id: int

    model_config = {
        "from_attributes": True
    }
# -------------------------------
# ZONE TYPE
# -------------------------------
class ZoneTypeCreateSchema(BaseModel):
    name: str

class ZoneTypeSchema(ZoneTypeCreateSchema):
    id: int

    model_config = {
        "from_attributes": True
    }
# -------------------------------
# ROOM TYPE
# -------------------------------
class RoomTypeCreateSchema(BaseModel):
    name: str

class RoomTypeSchema(RoomTypeCreateSchema):
    id: int

    model_config = {
        "from_attributes": True
    }
