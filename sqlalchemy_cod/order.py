from database import Base, SessionLocal
from sqlalchemy import Column, Integer, String, func, Text, DateTime


class ProductionOrder(Base):
    __tablename__ = 'ProductionOrder'
    Id = Column(Integer, primary_key=True)
    OrderNum = Column(String)
    StatusTypeId = Column(Integer)
    DtOrder = Column(DateTime)
    Name = Column(Text)
    IntegrationId = Column(Text)
    CustomerName = Column(Text)
    DtFactFrom = Column(DateTime)
    DtFactTo = Column(DateTime)
    DtForecastFrom = Column(DateTime)
    DtForecastTo = Column(DateTime)
    DtOrderShipment = Column(DateTime)
    DtPlanFrom = Column(DateTime)
    DtPlanTo = Column(DateTime)
    Priority = Column(Integer)
    CurrentStatusId = Column(Integer)
    Description = Column(Text)
    RowAddDate = Column(DateTime)
    RowAddUser = Column(Text)
    RowUpdateDate = Column(DateTime)
    RowUpdateUser = Column(Text)
    DtFromFact = Column(DateTime)
    DtFromPlan = Column(DateTime)
    DtToFact = Column(DateTime)
    DtToPlan = Column(DateTime)
