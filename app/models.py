
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Text, Float
from sqlalchemy.orm import relationship
from .database import Base

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
