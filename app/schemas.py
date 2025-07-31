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
