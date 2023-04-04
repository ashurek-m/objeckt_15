from database import Base, SessionLocal
from sqlalchemy import Column, Integer, String, func


class AssemblyUnit(Base):
    __tablename__ = 'AssemblyUnit'
    Id = Column(Integer, primary_key=True)

