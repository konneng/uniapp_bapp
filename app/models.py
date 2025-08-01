from sqlalchemy import Column, String, Float, Integer, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from .database import Base

class Building(Base):
    __tablename__ = "buildings"
    id = Column(String, primary_key=True, index=True)
    country_code = Column(String)
    province_code = Column(String)
    name = Column(String)
    address = Column(String)
    latitude = Column(Float)
    longitude = Column(Float)
    building_type = Column(String)
    group_id = Column(String, default="-1")
    zones = relationship("Zone", back_populates="building")

class ZoneType(Base):
    __tablename__ = "zone_types"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)

class RoomType(Base):
    __tablename__ = "room_types"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)

class Zone(Base):
    __tablename__ = "zones"
    id = Column(Integer, primary_key=True, index=True)
    building_id = Column(String, ForeignKey("buildings.id"))
    zone_type_id = Column(Integer, ForeignKey("zone_types.id"))

    building = relationship("Building", back_populates="zones")
    zone_type = relationship("ZoneType")
    rooms = relationship("Room", back_populates="zone")

class Room(Base):
    __tablename__ = "rooms"
    id = Column(Integer, primary_key=True, index=True)
    zone_id = Column(Integer, ForeignKey("zones.id"))
    room_type_id = Column(Integer, ForeignKey("room_types.id"))

    zone = relationship("Zone", back_populates="rooms")
    room_type = relationship("RoomType")

class PointOfInterest(Base):
    __tablename__ = "points_of_interest"
    id = Column(Integer, primary_key=True, index=True)
    room_id = Column(Integer, ForeignKey("rooms.id"))
    name = Column(String)
    status = Column(String)

class EnvironmentalParameter(Base):
    __tablename__ = "environmental_parameters"
    id = Column(Integer, primary_key=True, index=True)
    room_id = Column(Integer, ForeignKey("rooms.id"))
    temperature = Column(Float)
    humidity = Column(Float)
    co2_ppm = Column(Integer)

class DevicePresence(Base):
    __tablename__ = "device_presence"
    id = Column(Integer, primary_key=True, index=True)
    room_id = Column(Integer, ForeignKey("rooms.id"))
    device_id = Column(String)
    type = Column(String)
    present = Column(Boolean)
