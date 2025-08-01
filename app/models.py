
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Text
from sqlalchemy.orm import relationship
from .database import Base

class Protocol(Base):
    __tablename__ = "protocols"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)
    description = Column(Text)

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

class PointOfInterest(Base):
    __tablename__ = "points_of_interest"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    type = Column(String, nullable=False)  # POI or POV
    visibility = Column(String, nullable=False)  # PUBBLICO, PRIVATO, GRUPPI
    room_id = Column(Integer, ForeignKey("rooms.id"))
    owner_id = Column(Integer, ForeignKey("users.id"))
