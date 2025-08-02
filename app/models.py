
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Text, Float, DateTime
from sqlalchemy.orm import relationship
from .database import Base
from datetime import datetime

# -------------------------------
# PROTOCOLS
# -------------------------------
class Protocol(Base):
    __tablename__ = "protocols"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)
    description = Column(Text)

    # Relationship (facoltativa)
    objects = relationship("ObjectOfInterest", back_populates="protocol")

# -------------------------------
# OBJECTS OF INTEREST (OOI)
# -------------------------------
class ObjectOfInterest(Base):
    __tablename__ = "objects_of_interest"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    type = Column(String, nullable=False)  # OOR or OOV
    visibility = Column(String, nullable=False)  # PUBBLICO, PRIVATO, GRUPPI
    room_id = Column(Integer, ForeignKey("rooms.id"))
    owner_id = Column(Integer, ForeignKey("users.id"))
    protocol_id = Column(Integer, ForeignKey("protocols.id"))
    target_uri = Column(Text)
    is_active = Column(Boolean, default=True)

    # Relationship (facoltativa)
    protocol = relationship("Protocol", back_populates="objects")

# -------------------------------
# POINTS OF INTEREST (POI / POV)
# -------------------------------
class PointOfInterest(Base):
    __tablename__ = "points_of_interest"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    type = Column(String, nullable=False)  # POI or POV
    visibility = Column(String, nullable=False)  # PUBBLICO, PRIVATO, GRUPPI
    room_id = Column(Integer, ForeignKey("rooms.id"))
    owner_id = Column(Integer, ForeignKey("users.id"))

# -------------------------------
# BUILDINGS (se non già presente)
# -------------------------------
class Building(Base):
    __tablename__ = "buildings"
    id = Column(String, primary_key=True, index=True)  # es: BUI_IT_MI000000001
    country = Column(String, nullable=False)
    province = Column(String, nullable=False)
    name = Column(String, nullable=False)
    address = Column(String, nullable=False)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    building_type = Column(String, nullable=False)  # es: RESIDENZIALE, PUBBLICO, ...
    group_id = Column(String, nullable=False, default="SB")  # SB = Single Building. edificio non in gruppo

# -------------------------------
# DEVICES (se non già presente)
# -------------------------------
class DevicePresence(Base):
    __tablename__ = "device_presence"
    id = Column(Integer, primary_key=True, index=True)
    room_id = Column(Integer, ForeignKey("rooms.id"), nullable=False)
    device_id = Column(String, nullable=False)
    present = Column(Boolean, nullable=False)
    timestamp = Column(String)  # oppure DateTime

# -------------------------------
# ROOMS (se non già presente)
# -------------------------------
class RoomType(Base):
    __tablename__ = "room_types"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False, unique=True)

class Room(Base):
    __tablename__ = "rooms"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    zone_id = Column(Integer, ForeignKey("zones.id"), nullable=False)
    room_type_id = Column(Integer, ForeignKey("room_types.id"), nullable=True)

    zone = relationship("Zone")
    room_type = relationship("RoomType")

# -------------------------------
# ZONES (se non già presente)
# -------------------------------
class Zone(Base):
    __tablename__ = "zones"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    building_id = Column(String, ForeignKey("buildings.id"), nullable=False)

# -------------------------------
# USERS (se non già presente)
# -------------------------------
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=True)
    hashed_password = Column(String, nullable=True)
    full_name = Column(String, nullable=True)
    is_active = Column(Boolean, default=True)

# -------------------------------
# ENVIRONMENTAL PARAMETERS
# -------------------------------
class EnvironmentalParameter(Base):
    __tablename__ = "environmental_parameters"

    id = Column(Integer, primary_key=True, index=True)
    room_id = Column(Integer, ForeignKey("rooms.id"), nullable=False)
    temperature = Column(Float, nullable=False)
    humidity = Column(Float, nullable=False)
    air_quality = Column(String, nullable=True)
    timestamp = Column(DateTime, default=datetime.utcnow)
