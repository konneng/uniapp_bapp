from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey, CheckConstraint, TIMESTAMP
from sqlalchemy.orm import relationship
from .database import Base

class Building(Base):
    __tablename__ = 'buildings'

    id = Column(String, primary_key=True)
    country_code = Column(String(2), nullable=False)
    province_code = Column(String(2), nullable=False)
    name = Column(String, nullable=False)
    address = Column(String, nullable=False)
    latitude = Column(Float)
    longitude = Column(Float)
    building_type = Column(String, CheckConstraint(
        "building_type IN ('RESIDENZIALE','COMMERCIALE','BUSINESS','PUBBLICA AMMINISTRAZIONE','PUBBLICO','MISTO')"
    ))

    zones = relationship("Zone", back_populates="building")


class Zone(Base):
    __tablename__ = 'zones'

    id = Column(Integer, primary_key=True)
    building_id = Column(String, ForeignKey("buildings.id", ondelete="CASCADE"))
    name = Column(String, nullable=False)

    building = relationship("Building", back_populates="zones")
    rooms = relationship("Room", back_populates="zone")


class Room(Base):
    __tablename__ = 'rooms'

    id = Column(Integer, primary_key=True)
    zone_id = Column(Integer, ForeignKey("zones.id", ondelete="CASCADE"))
    name = Column(String, nullable=False)

    zone = relationship("Zone", back_populates="rooms")
